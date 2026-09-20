---
name: web-research
description: Required toolkit for internet search, current-web research, source discovery, news/image/video discovery, or multi-source investigation. Load before beginning web discovery. Do not load merely to fetch or summarize a specific user-provided URL.
---

# Web Research Toolkit

Use this toolkit for web discovery and internet investigation. For a specific URL supplied by the user, use the appropriate fetch tool directly.

Call `load_firecrawl_tools` before using Firecrawl. The available tools support complementary approaches:

- Use `firecrawl_search` to discover web, news, image, or video sources.
- Use `firecrawl_scrape` to extract page content. It can also provide structured extraction, screenshots, media, and browser actions when the task benefits from those capabilities.
- Use `web_fetch` to inspect an individual page with readable content extraction.
- Use `batch_web_fetch` to inspect several pages concurrently.

Choose page-extraction tools according to the task and page rather than treating one as the universal default. Both `firecrawl_scrape` and `web_fetch` are suitable for ordinary page extraction. If one produces incomplete or unsuitable results, try the other. Use both when a second representation would improve coverage or confidence.

Research may include refining queries around evidence gaps, preferring primary sources, corroborating material claims with independent sources, and investigating disagreements. Continue only as far as the task and available evidence require.

Follow the loaded Firecrawl tool definitions for detailed options, costs, privacy, and safety guidance.

# Proxy

Proxy available at `192.168.31.1:18080`. Try to use in case of network related issues.
