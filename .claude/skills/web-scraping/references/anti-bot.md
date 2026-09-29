# Anti-bot systems

This document explains **how detection works** and where the line is between "good scraping hygiene" and "evasion that's legally risky."

## The three kinds of blocks you'll hit

1. **Rate / volume** — 429, 503, or a CAPTCHA page after N req/min.
   - **Fix:** slow down, add jitter, rotate IPs if you're allowed to.
   - **Not sketchy.** Every crawler has to do this.

2. **Header / fingerprint** — site blocks requests missing `User-Agent`, `Accept-Language`, cookies, or with a TLS fingerprint that doesn't look like a real browser.
   - **Fix:** set a descriptive UA identifying your crawler. Include `Accept-*` headers.
   - **Sketchy zone:** lying about being Chrome, `curl-cffi` to mimic browser TLS. Works, but if the site ToS forbids scraping, you're building an evidence trail.

3. **Anti-bot services** — Cloudflare, Akamai, PerimeterX, DataDome. These run JS challenges, check canvas/WebGL fingerprints, mouse entropy.
   - **Fix:** you probably shouldn't be there. If the site deploys commercial anti-bot, they're telling you "no."
   - **If the user insists:** Playwright with `playwright-extra` + `stealth` plugin *may* work. But this is the line where polite scraping becomes adversarial — tell the user before proceeding.

## Rules of thumb

- **Never** scrape through a login you don't own.
- **Never** bypass a paywall.
- **Never** submit fake CAPTCHAs or use captcha-solving services.
- **Always** stop at the first CAPTCHA and tell the user. Don't try to route around it.
- If the user asks you to evade detection aggressively (residential proxies, browser fingerprint spoofing, CAPTCHA farms), ask once whether they have permission from the site owner and note that this path may violate ToS / CFAA.

## Respectful defaults

```python
headers = {
    "User-Agent": "my-crawler/1.0 (+contact@example.com; purpose=research)",
    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}
# 1 req/sec per host, exponential backoff on 429
# honor Crawl-delay from robots.txt
# stop on repeated 403s — don't probe harder
```

## If you see these signals, stop and escalate

- Cloudflare "Checking your browser…" page (blue gradient, ray ID)
- `cf-mitigated: challenge` response header
- Bursts of 403s with empty body
- DataDome or PerimeterX JS snippets in the initial HTML

Surface these to the user. Don't quietly add more evasion layers.
