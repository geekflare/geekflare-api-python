# WebScrapeDtoProxyMode

Controls when a proxy is used. `false` doesn't use a proxy (default), `auto` tries without a proxy first and retries through one if the site blocks the request, `true` always uses a proxy. `proxyMode` is optional — to route through a proxy in a specific country, you can set `proxyCountry` on its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from geekflare_api.models.web_scrape_dto_proxy_mode import WebScrapeDtoProxyMode

# TODO update the JSON string below
json = "{}"
# create an instance of WebScrapeDtoProxyMode from a JSON string
web_scrape_dto_proxy_mode_instance = WebScrapeDtoProxyMode.from_json(json)
# print the JSON string representation of the object
print(WebScrapeDtoProxyMode.to_json())

# convert the object into a dict
web_scrape_dto_proxy_mode_dict = web_scrape_dto_proxy_mode_instance.to_dict()
# create an instance of WebScrapeDtoProxyMode from a dict
web_scrape_dto_proxy_mode_from_dict = WebScrapeDtoProxyMode.from_dict(web_scrape_dto_proxy_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


