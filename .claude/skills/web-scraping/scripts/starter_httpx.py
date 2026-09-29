"""
Async static-HTML scraper template.

Usage: adapt SEED, parse(), and enumerate() for your target site.
Run: python starter_httpx.py
"""

from __future__ import annotations

import asyncio
import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import AsyncIterator

import httpx
from selectolax.parser import HTMLParser
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

SEED = "https://example.com"
OUT = Path("data.jsonl")
CACHE_DIR = Path(".cache_html")
CONCURRENCY = 5
REQ_PER_SEC = 2
USER_AGENT = "research-crawler/1.0 (+contact@example.com)"


@dataclass
class Record:
    url: str
    title: str
    # add fields here


class RateLimiter:
    """Token bucket — wait so we never exceed `rate` requests per second."""

    def __init__(self, rate: float):
        self.interval = 1 / rate
        self._last = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        async with self._lock:
            now = asyncio.get_event_loop().time()
            wait = self._last + self.interval - now
            if wait > 0:
                await asyncio.sleep(wait + random.uniform(0, 0.1))
            self._last = asyncio.get_event_loop().time()


@retry(stop=stop_after_attempt(5), wait=wait_exponential_jitter(initial=1, max=30))
async def fetch(client: httpx.AsyncClient, url: str, limiter: RateLimiter) -> str:
    cache = CACHE_DIR / (url.replace("/", "_")[:200] + ".html")
    if cache.exists():
        return cache.read_text(encoding="utf-8")
    await limiter.acquire()
    r = await client.get(url, timeout=30)
    if r.status_code in (429, 503):
        raise httpx.HTTPStatusError("rate limited", request=r.request, response=r)
    r.raise_for_status()
    CACHE_DIR.mkdir(exist_ok=True)
    cache.write_text(r.text, encoding="utf-8")
    return r.text


def parse(html: str, url: str) -> Record | None:
    """Adapt selectors per site. Prefer JSON-LD over fragile CSS selectors."""
    doc = HTMLParser(html)
    title = (doc.css_first("title").text() if doc.css_first("title") else "").strip()
    if not title:
        return None
    return Record(url=url, title=title)


async def enumerate_urls(
    client: httpx.AsyncClient, limiter: RateLimiter
) -> AsyncIterator[str]:
    """Yield every URL to scrape. Override with sitemap.xml parsing / pagination."""
    yield SEED


async def worker(
    client: httpx.AsyncClient,
    queue: asyncio.Queue[str],
    limiter: RateLimiter,
    seen: set[str],
    out_file,
) -> None:
    while True:
        url = await queue.get()
        try:
            if url in seen:
                continue
            seen.add(url)
            try:
                html = await fetch(client, url, limiter)
                rec = parse(html, url)
                if rec:
                    out_file.write(json.dumps(asdict(rec)) + "\n")
                    out_file.flush()
            except Exception as e:
                print(f"  ! {url}: {e.__class__.__name__}: {e}")
        finally:
            queue.task_done()


async def main() -> None:
    limiter = RateLimiter(REQ_PER_SEC)
    headers = {"User-Agent": USER_AGENT}
    seen: set[str] = set()

    async with httpx.AsyncClient(headers=headers, http2=True, follow_redirects=True) as client:
        queue: asyncio.Queue[str] = asyncio.Queue()
        async for url in enumerate_urls(client, limiter):
            await queue.put(url)

        with OUT.open("a", encoding="utf-8") as f:
            workers = [
                asyncio.create_task(worker(client, queue, limiter, seen, f))
                for _ in range(CONCURRENCY)
            ]
            await queue.join()
            for w in workers:
                w.cancel()

    print(f"✓ wrote {OUT} ({len(seen)} urls visited)")


if __name__ == "__main__":
    asyncio.run(main())
