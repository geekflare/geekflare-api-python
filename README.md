# geekflare-api

Official Python SDK for the [Geekflare API](https://geekflare.com/api/).

## Installation

```bash
pip install geekflare-api
```

## Quick Start

```python
from geekflare_api.client import GeekflareClient
from geekflare_api.models import WebScrapeDto

with GeekflareClient(api_key="your-api-key") as client:
    result = client.web_scrape(WebScrapeDto(url="https://google.com"))
    print(result)
```

## Available Methods

| Method                        | Description                    |
| ----------------------------- | ------------------------------ |
| `client.meta_scrape(body)`    | Scrape meta tags from a URL    |
| `client.web_scrape(body)`     | Scrape web page content        |
| `client.dns_record(body)`     | Look up DNS records            |
| `client.screenshot(body)`     | Take a screenshot of a URL     |
| `client.site_status(body)`    | Check if a site is up or down  |
| `client.redirect_check(body)` | Check redirect chain of a URL  |
| `client.broken_link(body)`    | Find broken links on a page    |
| `client.url2_pdf(body)`       | Convert a URL to PDF           |
| `client.open_ports(body)`     | Scan open ports on a host      |
| `client.tls_scan(body)`       | Scan TLS/SSL configuration     |
| `client.load_time(body)`      | Test page load time            |
| `client.mixed_content(body)`  | Check for mixed content issues |
| `client.dns_sec(body)`        | Check DNSSEC configuration     |
| `client.mtr(body)`            | Perform MTR network test       |
| `client.ping(body)`           | Ping a host                    |
| `client.lighthouse(body)`     | Run Lighthouse audit           |
| `client.search(body)`         | Perform a web search           |

## Error Handling

```python
from geekflare_api.exceptions import ApiException

try:
    result = client.web_scrape(WebScrapeDto(url="https://google.com"))
except ApiException as e:
    print(f"API error {e.status}: {e.reason}")
```

## Links

- [API Documentation](https://docs.geekflare.com/api/intro)
- [Geekflare API](https://dash.geekflare.com)
- [Report Issues](https://github.com/geekflare/geekflare-api-python/issues)

## License

MIT
