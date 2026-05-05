import geekflare_api
from geekflare_api.api.api_tool_api import ApiToolApi
from geekflare_api.models import (
    BrokenLinkDto,
    DnsRecordDto,
    DnsSecDto,
    LighthouseDto,
    LoadTimeDto,
    MetaScrapeDto,
    MixedContentDto,
    MtrDto,
    OpenPortDto,
    PingDto,
    RedirectCheckDto,
    ScreenshotDto,
    SearchRequestDto,
    SiteStatusDto,
    TlsScanDto,
    Url2PdfDto,
    WebScrapeDto,
)


class GeekflareClient:
    def __init__(self, api_key: str, base_url: str = "https://api.geekflare.com"):
        configuration = geekflare_api.Configuration(host=base_url)
        configuration.api_key["x-api-key"] = api_key
        configuration.api_key_prefix["x-api-key"] = ""
        self._client = geekflare_api.ApiClient(configuration)
        self._api = ApiToolApi(self._client)

    def meta_scrape(self, body: MetaScrapeDto):
        return self._api.meta_scrape(body)

    def web_scrape(self, body: WebScrapeDto):
        return self._api.web_scrape(body)

    def dns_record(self, body: DnsRecordDto):
        return self._api.dns_record(body)

    def screenshot(self, body: ScreenshotDto):
        return self._api.screenshot(body)

    def site_status(self, body: SiteStatusDto):
        return self._api.site_status(body)

    def redirect_check(self, body: RedirectCheckDto):
        return self._api.redirect_check(body)

    def broken_link(self, body: BrokenLinkDto):
        return self._api.broken_link(body)

    def url2_pdf(self, body: Url2PdfDto):
        return self._api.url2_pdf(body)

    def open_ports(self, body: OpenPortDto):
        return self._api.open_ports(body)

    def tls_scan(self, body: TlsScanDto):
        return self._api.tls_scan(body)

    def load_time(self, body: LoadTimeDto):
        return self._api.load_time(body)

    def mixed_content(self, body: MixedContentDto):
        return self._api.mixed_content(body)

    def dns_sec(self, body: DnsSecDto):
        return self._api.dns_sec(body)

    def mtr(self, body: MtrDto):
        return self._api.mtr(body)

    def ping(self, body: PingDto):
        return self._api.ping(body)

    def lighthouse(self, body: LighthouseDto):
        return self._api.lighthouse(body)

    def search(self, body: SearchRequestDto):
        return self._api.search(body)

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()