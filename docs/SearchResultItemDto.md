# SearchResultItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Result title | 
**url** | **str** | Canonical URL | 
**snippet** | **str** | Clean snippet (ads/HTML removed) | 
**var_date** | **str** | Published date (if available) | [optional] 
**position** | **float** | Rank position | 
**content** | **object** | Scraped cleaned HTML content from the result URL | [optional] 
**thumbnail** | **object** | Thumbnail image URL (if available) | [optional] 

## Example

```python
from geekflare_api.models.search_result_item_dto import SearchResultItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultItemDto from a JSON string
search_result_item_dto_instance = SearchResultItemDto.from_json(json)
# print the JSON string representation of the object
print(SearchResultItemDto.to_json())

# convert the object into a dict
search_result_item_dto_dict = search_result_item_dto_instance.to_dict()
# create an instance of SearchResultItemDto from a dict
search_result_item_dto_from_dict = SearchResultItemDto.from_dict(search_result_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


