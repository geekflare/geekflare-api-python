# SearchSerpDataDtoPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[SearchSerpDataDtoPaginationPagesInner]**](SearchSerpDataDtoPaginationPagesInner.md) |  | [optional] 
**current_page** | **float** |  | [optional] 
**next_page** | **float** |  | [optional] 
**next_page_start** | **float** |  | [optional] 
**next_page_link** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_pagination import SearchSerpDataDtoPagination

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoPagination from a JSON string
search_serp_data_dto_pagination_instance = SearchSerpDataDtoPagination.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoPagination.to_json())

# convert the object into a dict
search_serp_data_dto_pagination_dict = search_serp_data_dto_pagination_instance.to_dict()
# create an instance of SearchSerpDataDtoPagination from a dict
search_serp_data_dto_pagination_from_dict = SearchSerpDataDtoPagination.from_dict(search_serp_data_dto_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


