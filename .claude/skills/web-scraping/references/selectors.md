# Selectors cheatsheet

## CSS — always try first, faster than XPath

| Goal                          | Selector                                      |
| ----------------------------- | --------------------------------------------- |
| By tag                        | `article`                                     |
| By class                      | `.product-card`                               |
| By id                         | `#main`                                       |
| By attribute                  | `a[href^="/products/"]`                       |
| Attribute contains            | `div[class*="price"]`                         |
| Nth child                     | `li:nth-child(2)`                             |
| Descendant                    | `div.card h2`                                 |
| Direct child                  | `div.card > h2`                               |
| Next sibling                  | `h2 + p`                                      |
| Multiple classes              | `.btn.primary`                                |
| Has-text (Playwright only)    | `button:has-text("Submit")`                   |

## Structured data first — most stable

Check these **before** writing any CSS selector. Sites rewrite visual HTML; they rarely rewrite structured data.

1. **JSON-LD**: `<script type="application/ld+json">…</script>` — SEO schemas, usually contain `name`, `price`, `image`, `description`.
2. **OpenGraph**: `<meta property="og:*">` — title, image, type.
3. **Microdata**: `itemprop="price"` attributes.
4. **RSS/Atom feeds** at `/feed` / `/rss` — clean paginated entries.
5. **`sitemap.xml`** — canonical URL list with `lastmod`.

```python
# JSON-LD extraction (selectolax)
for node in doc.css('script[type="application/ld+json"]'):
    try:
        data = json.loads(node.text())
    except json.JSONDecodeError:
        continue
    # data may be a list or a dict with @graph
```

## When CSS fails: XPath

XPath shines for "the element whose text matches X" and "parent of Y":

| Goal                     | XPath                                           |
| ------------------------ | ----------------------------------------------- |
| Text equals              | `//button[text()="Load More"]`                  |
| Text contains            | `//span[contains(text(), "$")]`                 |
| Parent of                | `//img[@alt="hero"]/..`                         |
| Following sibling        | `//h3/following-sibling::p[1]`                  |
| By attribute value       | `//div[@data-id="42"]`                          |

## Finding selectors in DevTools

1. Right-click element → **Inspect**.
2. In Elements panel, right-click the node → **Copy → Copy selector** (minimal unique CSS path).
3. Test in Console: `document.querySelectorAll('your-selector').length`.

## Paginations you'll actually see

| Kind                    | How to enumerate                                             |
| ----------------------- | ------------------------------------------------------------ |
| `?page=N`               | Loop N=1…∞ until empty result. Check for a total-count.      |
| Offset/limit            | `?offset=0&limit=50`, walk offsets.                          |
| Cursor                  | Response returns `next_cursor`; pass it back.                |
| Link header             | Parse `Link: <…>; rel="next"` from response headers.         |
| Numbered page links     | Read `.pagination a[href]` once, queue them all.             |
| Infinite scroll         | Playwright + scroll-until-stable (see starter_playwright).    |
| Load-more button        | Playwright clicks button until it disappears.                |
