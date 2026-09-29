"""
Playwright template for JS-rendered pages.

Only use when static fetch doesn't contain the data (SPAs, infinite scroll, etc).
Playwright is ~10× slower than httpx — prefer httpx when possible.

Install: pip install playwright && playwright install chromium
"""

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass, asdict
from pathlib import Path

from playwright.async_api import async_playwright, Page, TimeoutError as PWTimeout

SEED = "https://example.com"
OUT = Path("data.jsonl")
CONCURRENCY = 3   # keep low — each context = a tab


@dataclass
class Record:
    url: str
    title: str


async def extract(page: Page, url: str) -> Record | None:
    await page.goto(url, wait_until="domcontentloaded", timeout=30_000)
    # Wait for the specific element you need, not networkidle (unreliable on SPAs)
    try:
        await page.wait_for_selector("h1", timeout=10_000)
    except PWTimeout:
        return None

    # Prefer evaluating JS to extract structured data over scraping DOM strings
    data = await page.evaluate(
        """() => {
          const jsonLd = document.querySelector('script[type="application/ld+json"]');
          if (jsonLd) { try { return JSON.parse(jsonLd.textContent); } catch {} }
          return { title: document.title };
        }"""
    )
    return Record(url=url, title=data.get("title") or data.get("name") or "")


async def handle_infinite_scroll(page: Page, max_scrolls: int = 20) -> None:
    """Scroll until no new content loads or max reached."""
    prev_height = 0
    for _ in range(max_scrolls):
        curr = await page.evaluate("document.body.scrollHeight")
        if curr == prev_height:
            break
        prev_height = curr
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.5)


async def worker(context, queue: asyncio.Queue[str], out_file) -> None:
    page = await context.new_page()
    while True:
        url = await queue.get()
        try:
            try:
                rec = await extract(page, url)
                if rec:
                    out_file.write(json.dumps(asdict(rec)) + "\n")
                    out_file.flush()
            except Exception as e:
                print(f"  ! {url}: {e.__class__.__name__}: {e}")
        finally:
            queue.task_done()
    await page.close()


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="research-crawler/1.0 (+contact@example.com)",
            viewport={"width": 1280, "height": 900},
        )
        # Block noisy assets for speed
        await context.route("**/*.{png,jpg,jpeg,svg,gif,woff,woff2,css}", lambda r: r.abort())

        queue: asyncio.Queue[str] = asyncio.Queue()
        for url in [SEED]:
            await queue.put(url)

        with OUT.open("a", encoding="utf-8") as f:
            workers = [
                asyncio.create_task(worker(context, queue, f))
                for _ in range(CONCURRENCY)
            ]
            await queue.join()
            for w in workers:
                w.cancel()

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
