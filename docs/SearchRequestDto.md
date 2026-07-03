# SearchRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search query | 
**limit** | **float** | Number of results | [optional] [default to 10]
**time** | **str** | Time filter (h, d, w, m, y or h2, d7, etc.) | [optional] [default to 'any']
**location** | **str** | Country code (ISO alpha-2) | [optional] [default to 'us']
**source** | **str** | Search source | [optional] [default to 'web']
**category** | **str** | Category filter | [optional] [default to 'general']
**include_domains** | **List[str]** | Include only these domains | [optional] 
**exclude_domains** | **List[str]** | Exclude these domains | [optional] 
**format** | **str** | Output format | [optional] [default to 'json']
**scrape** | **bool** | scrape and extract content from SERP result URLs | [optional] [default to False]
**scrape_limit** | **float** | Number of URLs to scrape (requires scrape: true) | [optional] [default to 3]
**grounded_answer** | **bool** | Use AI to synthesize a grounded answer from search results. | [optional] [default to False]

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


