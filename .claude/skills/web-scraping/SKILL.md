---
name: web-scraping
description: Scrape structured data from websites at scale. Use when the user asks to extract data from web pages, crawl a site, collect records across many URLs, harvest API responses, or ingest content from third-party sources. Covers static HTML, JS-rendered pages (Playwright), pagination, rate limiting, robots.txt, and persistence to JSON/CSV/SQLite/Postgres.
license: MIT
---

# Web Scraping

Extract structured data from websites reliably and respectfully.

## Decision tree

Before writing any scraper, pick the right approach:

```
Does the site have a public API or sitemap.xml?
├─ YES → use that. Scraping HTML is a last resort.
└─ NO → inspect the network tab:
    ├─ Data comes from a JSON endpoint you can hit directly?
    │   → call that endpoint with fetch/httpx. Fastest, cleanest.
    ├─ Data is in the initial HTML?
    │   → static scrape with requests + selectolax/cheerio/BeautifulSoup.
    └─ Data is rendered by JS after load?
        → Playwright (headless browser).
```

**Prefer network-tab reverse-engineering over DOM scraping** whenever possible. A JSON API call is 100× more reliable than parsing HTML that changes every sprint. Open DevTools → Network → XHR and look for the real data source.

## Legal & ethical guardrails

1. **Check `robots.txt` first**: `curl https://example.com/robots.txt`. Respect `Disallow` and `Crawl-delay`.
2. **Read the Terms of Service.** Many sites prohibit scraping; inform the user if you spot such a clause so they can make an informed call.
3. **Identify yourself**: set a descriptive `User-Agent` — never spoof a real browser to bypass detection unless the user explicitly authorizes it.
4. **Rate-limit yourself**: default to 1 request/sec per host, back off on 429/503.
5. **Cache aggressively**: save raw HTML to disk on first fetch so re-runs don't re-hammer the site.
6. **Never scrape auth-gated content the user doesn't own access to.**

## Default stack

Unless the user specifies otherwise:
- **Language**: Python 3 (richest scraping ecosystem) or Node (if the project is already JS)
- **Static HTTP**: `httpx` (Python) or `undici` (Node) — both support HTTP/2 and connection pooling
- **HTML parsing**: `selectolax` (Python — CSS selectors, 10× faster than BS4) or `cheerio` (Node)
- **Headless**: `playwright` for both. Stealth mode only if needed.
- **Concurrency**: `asyncio.gather` with a `Semaphore(5)` — not threads
- **Storage**: SQLite for mid-size jobs (`sqlite3` stdlib), Postgres for large, JSONL for streaming dumps
- **Retry**: exponential backoff, jitter, max 5 attempts — use `tenacity` (Py) or write a small helper

## Scaffolding workflow

When asked to scrape something, follow this sequence:

1. **Recon** — fetch one page, inspect its structure, find the real data source (HTML structure or JSON endpoint). Use `curl -sL -A "Mozilla/5.0 …" <url> | head -200` or open it in a headless browser with devtools logging.
2. **Prototype** — write a single-URL extractor that returns a typed dict/dataclass for one record. Run it, confirm fields.
3. **Paginate / enumerate** — figure out how to walk all pages (sitemap? page query param? cursor? infinite scroll?).
4. **Parallelize** — wrap in an async crawler with bounded concurrency, rate limit, retry, and caching.
5. **Persist** — stream results to storage as you go (don't hold in memory).
6. **Dedupe & resume** — key every record by a stable id, skip already-seen ones so the job is resumable.
7. **Monitor** — log every N records and every error. Summarize counts at end.

See `scripts/starter_httpx.py` and `scripts/starter_playwright.py` for ready-to-adapt templates.

## Common pitfalls

- **HTML selectors break weekly.** Prefer microdata/JSON-LD (`<script type="application/ld+json">`) — sites rarely restructure those.
- **`requests` blocks in async code**. Use `httpx.AsyncClient`, not `requests`.
- **Playwright is slow** (~500ms/page). Don't use it if a static fetch works.
- **Cloudflare / PerimeterX blocks** — if you hit one, stop and tell the user. Fighting bot-detection is a legal gray zone.
- **Memory balloons on big crawls** — stream to disk, don't accumulate in a list.
- **One crash kills the whole job** — wrap each URL in try/except; log and continue.

## Data quality checks

After a scrape, always:
- Count nulls per field — a sudden spike means the selector broke
- Sample 5 random records and eyeball them
- Compare totals to a known source (search result count on the site itself)

## References

- `scripts/starter_httpx.py` — async static scraper template
- `scripts/starter_playwright.py` — headless browser template
- `references/selectors.md` — CSS selector patterns & XPath cheatsheet
- `references/anti-bot.md` — how detection works; what's safe vs. legally risky
