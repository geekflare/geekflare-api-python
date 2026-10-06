# SearchRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search query | 
**limit** | **float** | Number of results | [optional] [default to 10]
**time** | **str** | Time filter (h, d, w, m, y or h2, d7, etc.) | [optional] [default to 'any']
**location** | **str** | Country code (ISO alpha-2). Can be combined with &#x60;city&#x60; for city-level targeting; when &#x60;city&#x60; is set, it takes priority. | [optional] [default to 'us']
**device** | **str** | Device to emulate when searching. Defaults to desktop. | [optional] [default to 'desktop']
**source** | **str** | Search source. SERP mode accepts one source per request. | [optional] [default to 'web']
**category** | **str** | Category filter. Ignored in SERP mode. | [optional] [default to 'general']
**include_domains** | **List[str]** | Include only these domains | [optional] 
**exclude_domains** | **List[str]** | Exclude these domains | [optional] 
**format** | **str** | Output format. Ignored in SERP mode. | [optional] [default to 'json']
**scrape** | **bool** | scrape and extract content from SERP result URLs. Ignored in SERP mode. | [optional] [default to False]
**scrape_limit** | **float** | Number of URLs to scrape (requires scrape: true). Ignored in SERP mode. | [optional] [default to 3]
**grounded_answer** | **bool** | Use AI to synthesize a grounded answer from search results. Ignored in SERP mode. | [optional] [default to False]
**serp** | **bool** | Return the full Google search results page (SERP) including organic results, AI Overviews, related searches, People Also Ask, pagination, and more. Supported in this mode: &#x60;query&#x60;, &#x60;location&#x60;, &#x60;city&#x60;, &#x60;device&#x60;, &#x60;limit&#x60;, &#x60;source&#x60; (one value), &#x60;time&#x60;, &#x60;includeDomains&#x60;, and &#x60;excludeDomains&#x60;. It returns the first page of results. | [optional] [default to False]
**city** | **str** | City to target for localized results, using the name exactly as listed in the supported cities file, e.g. &#x60;London,England,United Kingdom&#x60;. Works with standard search and with &#x60;serp: true&#x60;. When set, it takes priority over &#x60;location&#x60;. Supported cities: https://cdn.geekflare.com/api-assets/geotargets-2026-08-12.json | [optional] 

## Example

```python
from geekflare_api.models.search_request_dto import SearchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestDto from a JSON string
search_request_dto_instance = SearchRequestDto.from_json(json)
# print the JSON string representation of the object
print(SearchRequestDto.to_json())

# convert the object into a dict
search_request_dto_dict = search_request_dto_instance.to_dict()
# create an instance of SearchRequestDto from a dict
search_request_dto_from_dict = SearchRequestDto.from_dict(search_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


