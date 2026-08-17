---
name: web-research
description: Required workflow for internet search, current-web research, source discovery, news/image/video discovery, or multi-source investigation. Load before beginning web discovery. Do not load merely to fetch or summarize a specific user-provided URL.
---

# Web Research

Use this workflow for web discovery and internet investigation. Do not use it merely to fetch or summarize a specific URL supplied by the user.

## Discovery workflow

1. Call `load_firecrawl_tools` before using Firecrawl.
2. For the initial discovery pass, search with both `firecrawl_search` and Degoog for complementary coverage.
3. Merge and deduplicate the results, then identify promising and preferably primary sources.
4. Inspect one selected source with `web_fetch`, or inspect several independent sources concurrently with `batch_web_fetch`.
5. Refine queries from the findings. On later passes, use whichever search source best addresses the remaining evidence gap; repeating every query through both is unnecessary.
6. Cross-check material claims and source disagreements, and continue until the available evidence is sufficient for the task.
7. If Firecrawl or Degoog fails, continue with the other rather than abandoning the investigation.

Use `firecrawl_scrape` instead of ordinary fetching only when a page needs Firecrawl-specific extraction, screenshots, media, browser actions, structured output, or handling that `web_fetch` cannot provide. Follow the loaded Firecrawl tool definitions for detailed options, costs, privacy, and safety guidance.

## Degoog

Request Degoog through `web_fetch` using this endpoint:

```text
http://192.168.31.1:4444/api/search?q=<encoded-query>&type=<type>&page=<page-number>&lang=<language>
```

Percent-encode query and parameter values. The endpoint returns JSON search results.

Supported parameters:

- `q` — required search query
- `type` — `web` (default), `images`, `videos`, or `news`
- `page` — result page from `1` through `10`
- `time` — `any`, `hour`, `day`, `week`, `month`, `year`, or `custom`
- `dateFrom`, `dateTo` — required with `time=custom`, formatted as `YYYY MM DD`
- `lang` — ISO 639-1 language code
