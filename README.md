# geekflare-api

Official Python SDK for the [Geekflare](https://geekflare.com/api/).

- API version: 1.0.0
- Package version: 0.3.2

## Requirements.

Python 3.10+

## Installation & Usage

### pip install

```bash
pip install geekflare-api
```

## Quick Start

```python
from geekflare_api.client import GeekflareClient
from geekflare_api.models import WebScrapeDto

with GeekflareClient(api_key="your-api-key") as client:
    result = client.web_scrape(WebScrapeDto(url="https://toscrape.com/"))
    print(result)
```

## Available Methods

| Method                        | Description                                               |
| ----------------------------- | --------------------------------------------------------- |
| `client.meta_scrape(body)`    | Scrape meta tags from a URL                               |
| `client.web_scrape(body)`     | Scrape web page content                                   |
| `client.brand(body)`          | Get structured brand and company information for a domain |
| `client.dns_record(body)`     | Look up DNS records                                       |
| `client.screenshot(body)`     | Take a screenshot of a URL                                |
| `client.site_status(body)`    | Check if a site is up or down                             |
| `client.redirect_check(body)` | Check redirect chain of a URL                             |
| `client.broken_link(body)`    | Find broken links on a page                               |
| `client.url2_pdf(body)`       | Convert a URL to PDF                                      |
| `client.open_ports(body)`     | Scan open ports on a host                                 |
| `client.tls_scan(body)`       | Scan TLS/SSL configuration                                |
| `client.load_time(body)`      | Test page load time                                       |
| `client.mixed_content(body)`  | Check for mixed content issues                            |
| `client.dns_sec(body)`        | Check DNSSEC configuration                                |
| `client.mtr(body)`            | Perform MTR network test                                  |
| `client.ping(body)`           | Ping a host                                               |
| `client.lighthouse(body)`     | Run Lighthouse audit                                      |
| `client.search(body)`         | Perform a web search                                      |

## Error Handling

```python

import geekflare_api
from geekflare_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.geekflare.com
# See configuration.py for a list of all supported configuration parameters.
configuration = geekflare_api.Configuration(
    host = "https://api.geekflare.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'


# Enter a context with an instance of the API client
with geekflare_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geekflare_api.ApiToolApi(api_client)
    broken_link_dto = geekflare_api.BrokenLinkDto() # BrokenLinkDto |

    try:
        # Check if a webpage contains broken links
        api_response = api_instance.broken_link(broken_link_dto)
        print("The response of ApiToolApi->broken_link:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiToolApi->broken_link: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.geekflare.com*

| Class        | Method                                                  | HTTP request            | Description                                         |
| ------------ | ------------------------------------------------------- | ----------------------- | --------------------------------------------------- |
| _ApiToolApi_ | [**brand**](docs/ApiToolApi.md#brand)                   | **POST** /brand         | Get brand data for a domain                         |
| _ApiToolApi_ | [**broken_link**](docs/ApiToolApi.md#broken_link)       | **POST** /brokenlink    | Check if a webpage contains broken links            |
| _ApiToolApi_ | [**dns_record**](docs/ApiToolApi.md#dns_record)         | **POST** /dnsrecord     | Retrieve DNS records for a given domain             |
| _ApiToolApi_ | [**dns_sec**](docs/ApiToolApi.md#dns_sec)               | **POST** /dnssec        | Check if DNSSEC is enabled for a domain             |
| _ApiToolApi_ | [**lighthouse**](docs/ApiToolApi.md#lighthouse)         | **POST** /lighthouse    | Run Lighthouse audit on a website                   |
| _ApiToolApi_ | [**load_time**](docs/ApiToolApi.md#load_time)           | **POST** /loadtime      | Measure the page load time for a given URL          |
| _ApiToolApi_ | [**meta_scrape**](docs/ApiToolApi.md#meta_scrape)       | **POST** /metascraping  | Scrape a webpage meta with custom options           |
| _ApiToolApi_ | [**mixed_content**](docs/ApiToolApi.md#mixed_content)   | **POST** /mixedcontent  | Check for mixed content on a site                   |
| _ApiToolApi_ | [**mtr**](docs/ApiToolApi.md#mtr)                       | **POST** /mtr           | Perform MTR (My Traceroute) network diagnostic test |
| _ApiToolApi_ | [**open_ports**](docs/ApiToolApi.md#open_ports)         | **POST** /openport      | Scan a website for open ports                       |
| _ApiToolApi_ | [**ping**](docs/ApiToolApi.md#ping)                     | **POST** /ping          | Perform ICMP Ping test on a given URL or IP         |
| _ApiToolApi_ | [**redirect_check**](docs/ApiToolApi.md#redirect_check) | **POST** /redirectcheck | Check the redirection chain of a given URL          |
| _ApiToolApi_ | [**screenshot**](docs/ApiToolApi.md#screenshot)         | **POST** /screenshot    | Capture a full-page screenshot of a website         |
| _ApiToolApi_ | [**search**](docs/ApiToolApi.md#search)                 | **POST** /search        | Search API for AI Agents &amp; LLMs                 |
| _ApiToolApi_ | [**site_status**](docs/ApiToolApi.md#site_status)       | **POST** /up            | Check if a site is up or down                       |
| _ApiToolApi_ | [**tls_scan**](docs/ApiToolApi.md#tls_scan)             | **POST** /tlsscan       | Perform TLS scan for a given domain                 |
| _ApiToolApi_ | [**url2_pdf**](docs/ApiToolApi.md#url2_pdf)             | **POST** /url2pdf       | Capture a full-page Url2Pdf of a website            |
| _ApiToolApi_ | [**web_scrape**](docs/ApiToolApi.md#web_scrape)         | **POST** /webscraping   | Scrape a webpage with custom options                |

## Documentation For Models

- [BaseErrorResponseDto](docs/BaseErrorResponseDto.md)
- [BrandButtonStyleDto](docs/BrandButtonStyleDto.md)
- [BrandColorEntryDto](docs/BrandColorEntryDto.md)
- [BrandColorsDto](docs/BrandColorsDto.md)
- [BrandCompanyDto](docs/BrandCompanyDto.md)
- [BrandComponentsDto](docs/BrandComponentsDto.md)
- [BrandDataDto](docs/BrandDataDto.md)
- [BrandDto](docs/BrandDto.md)
- [BrandFontDto](docs/BrandFontDto.md)
- [BrandLinksDto](docs/BrandLinksDto.md)
- [BrandLocationDto](docs/BrandLocationDto.md)
- [BrandLogoDto](docs/BrandLogoDto.md)
- [BrandMetaDto](docs/BrandMetaDto.md)
- [BrandPageMetaDto](docs/BrandPageMetaDto.md)
- [BrandResponseDto](docs/BrandResponseDto.md)
- [BrandSocialProfileDto](docs/BrandSocialProfileDto.md)
- [BrandSpacingDto](docs/BrandSpacingDto.md)
- [BrandTypographyDto](docs/BrandTypographyDto.md)
- [BrokenLinkDto](docs/BrokenLinkDto.md)
- [BrokenLinkMetaDto](docs/BrokenLinkMetaDto.md)
- [BrokenLinkResponseDto](docs/BrokenLinkResponseDto.md)
- [BrokenLinkSummaryDto](docs/BrokenLinkSummaryDto.md)
- [DefaultExtractionFieldDto](docs/DefaultExtractionFieldDto.md)
- [DetectedServiceDto](docs/DetectedServiceDto.md)
- [DnsMetaDto](docs/DnsMetaDto.md)
- [DnsRecordDto](docs/DnsRecordDto.md)
- [DnsRecordResponseDto](docs/DnsRecordResponseDto.md)
- [DnsSecDataDto](docs/DnsSecDataDto.md)
- [DnsSecDto](docs/DnsSecDto.md)
- [DnsSecMetaDto](docs/DnsSecMetaDto.md)
- [DnsSecResponseDto](docs/DnsSecResponseDto.md)
- [ExtractionSchemaDto](docs/ExtractionSchemaDto.md)
- [ExtractionSchemaDtoFieldsInner](docs/ExtractionSchemaDtoFieldsInner.md)
- [GroundedAnswerDataDto](docs/GroundedAnswerDataDto.md)
- [GroundedAnswerResponseDto](docs/GroundedAnswerResponseDto.md)
- [GroundedSourceDto](docs/GroundedSourceDto.md)
- [HealthResponseDto](docs/HealthResponseDto.md)
- [ImageSearchResponseDto](docs/ImageSearchResponseDto.md)
- [ImageSearchResultItemDto](docs/ImageSearchResultItemDto.md)
- [KeywordsAiPromptDto](docs/KeywordsAiPromptDto.md)
- [LighthouseDto](docs/LighthouseDto.md)
- [LighthouseMetaDto](docs/LighthouseMetaDto.md)
- [LighthouseResponseDto](docs/LighthouseResponseDto.md)
- [ListingAiPromptDto](docs/ListingAiPromptDto.md)
- [LoadTime200Response](docs/LoadTime200Response.md)
- [LoadTimeDataDto](docs/LoadTimeDataDto.md)
- [LoadTimeDto](docs/LoadTimeDto.md)
- [LoadTimeLocationResultDto](docs/LoadTimeLocationResultDto.md)
- [LoadTimeMetaDto](docs/LoadTimeMetaDto.md)
- [LoadTimeMultiLocationMetaDto](docs/LoadTimeMultiLocationMetaDto.md)
- [LoadTimeMultiLocationResponseDto](docs/LoadTimeMultiLocationResponseDto.md)
- [LoadTimeMultiLocationResponseDtoSummary](docs/LoadTimeMultiLocationResponseDtoSummary.md)
- [LoadTimeResponseDto](docs/LoadTimeResponseDto.md)
- [MarginDto](docs/MarginDto.md)
- [MetaScrapeDto](docs/MetaScrapeDto.md)
- [MetaScrapeMetaDto](docs/MetaScrapeMetaDto.md)
- [MetaScrapeResponseDto](docs/MetaScrapeResponseDto.md)
- [MetaScrapeResponseDtoData](docs/MetaScrapeResponseDtoData.md)
- [MixedContentDataDto](docs/MixedContentDataDto.md)
- [MixedContentDto](docs/MixedContentDto.md)
- [MixedContentMetaDto](docs/MixedContentMetaDto.md)
- [MixedContentResponseDto](docs/MixedContentResponseDto.md)
- [MixedContentResponseDtoData](docs/MixedContentResponseDtoData.md)
- [MtrDataDto](docs/MtrDataDto.md)
- [MtrDto](docs/MtrDto.md)
- [MtrMetaDto](docs/MtrMetaDto.md)
- [MtrResponseDto](docs/MtrResponseDto.md)
- [NetworkDto](docs/NetworkDto.md)
- [OpenPortDto](docs/OpenPortDto.md)
- [OpenPortMetaDto](docs/OpenPortMetaDto.md)
- [OpenPortResponseDto](docs/OpenPortResponseDto.md)
- [PingDataDto](docs/PingDataDto.md)
- [PingDto](docs/PingDto.md)
- [PingMetaDto](docs/PingMetaDto.md)
- [PingResponseDto](docs/PingResponseDto.md)
- [PortServiceDetectionResultDto](docs/PortServiceDetectionResultDto.md)
- [PromptAiPromptDto](docs/PromptAiPromptDto.md)
- [ProtocolSupportDto](docs/ProtocolSupportDto.md)
- [RedirectCheckDto](docs/RedirectCheckDto.md)
- [RedirectCheckMetaDto](docs/RedirectCheckMetaDto.md)
- [RedirectCheckResponseDto](docs/RedirectCheckResponseDto.md)
- [RedirectHopDto](docs/RedirectHopDto.md)
- [SchemaAiPromptDto](docs/SchemaAiPromptDto.md)
- [ScreenshotDto](docs/ScreenshotDto.md)
- [ScreenshotInlineDto](docs/ScreenshotInlineDto.md)
- [ScreenshotMetaDto](docs/ScreenshotMetaDto.md)
- [ScreenshotResponseDto](docs/ScreenshotResponseDto.md)
- [Search200Response](docs/Search200Response.md)
- [SearchHtmlResponseDto](docs/SearchHtmlResponseDto.md)
- [SearchMarkdownResponseDto](docs/SearchMarkdownResponseDto.md)
- [SearchMetaDto](docs/SearchMetaDto.md)
- [SearchRequestDto](docs/SearchRequestDto.md)
- [SearchResponseDto](docs/SearchResponseDto.md)
- [SearchResultItemDto](docs/SearchResultItemDto.md)
- [SelectorExtractionFieldDto](docs/SelectorExtractionFieldDto.md)
- [SentimentAiPromptDto](docs/SentimentAiPromptDto.md)
- [ServiceHealthResponseDto](docs/ServiceHealthResponseDto.md)
- [ServiceStatus](docs/ServiceStatus.md)
- [SiteStatusDto](docs/SiteStatusDto.md)
- [SiteStatusMetaDto](docs/SiteStatusMetaDto.md)
- [SiteStatusResponseDto](docs/SiteStatusResponseDto.md)
- [SummaryAiPromptDto](docs/SummaryAiPromptDto.md)
- [TestMetaDto](docs/TestMetaDto.md)
- [TimingsDto](docs/TimingsDto.md)
- [TlsAdvisoryDto](docs/TlsAdvisoryDto.md)
- [TlsCertificateChainDto](docs/TlsCertificateChainDto.md)
- [TlsCertificateChainEntryDto](docs/TlsCertificateChainEntryDto.md)
- [TlsCertificateDto](docs/TlsCertificateDto.md)
- [TlsCertificateIssuerDto](docs/TlsCertificateIssuerDto.md)
- [TlsForwardSecrecyDto](docs/TlsForwardSecrecyDto.md)
- [TlsProtocolsDto](docs/TlsProtocolsDto.md)
- [TlsScanDataDto](docs/TlsScanDataDto.md)
- [TlsScanDto](docs/TlsScanDto.md)
- [TlsScanMetaDto](docs/TlsScanMetaDto.md)
- [TlsScanResponseDto](docs/TlsScanResponseDto.md)
- [TlsVulnerabilitiesDto](docs/TlsVulnerabilitiesDto.md)
- [Url2PdfDto](docs/Url2PdfDto.md)
- [Url2PdfMetaDto](docs/Url2PdfMetaDto.md)
- [Url2PdfResponseDto](docs/Url2PdfResponseDto.md)
- [WebScrapeDto](docs/WebScrapeDto.md)
- [WebScrapeDtoAiPrompt](docs/WebScrapeDtoAiPrompt.md)
- [WebScrapeDtoProxyMode](docs/WebScrapeDtoProxyMode.md)
- [WebScrapeMetaDto](docs/WebScrapeMetaDto.md)
- [WebScrapeResponseDto](docs/WebScrapeResponseDto.md)
- [WebScrapeResponseDtoData](docs/WebScrapeResponseDtoData.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="x-api-key"></a>

### x-api-key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

<a id="bearer-token"></a>

### bearer-token

- **Type**: Bearer authentication (JWT)

<a id="gf_auth_session"></a>

### gf_auth_session

- **Type**: API key
- **API key parameter name**: gf_auth_session
- **Location**:

## Links

- [API Documentation](https://docs.geekflare.com/api/intro)
- [Geekflare API](https://dash.geekflare.com)
- [Report Issues](https://github.com/geekflare/geekflare-api-python/issues)

## License

MIT

mcp-name: com.geekflare/mcp
