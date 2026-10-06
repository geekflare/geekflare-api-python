# SearchSerpDataDtoGeneral

Details about the search that was run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_engine** | **str** |  | [optional] 
**query** | **str** | Query as searched | [optional] 
**detected_query** | **str** |  | [optional] 
**results_cnt** | **float** | Approximate total results reported by Google | [optional] 
**search_time** | **float** | Search time in seconds | [optional] 
**language** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**location** | **str** | Location the search was targeted to | [optional] 
**gl** | **str** |  | [optional] 
**mobile** | **bool** |  | [optional] 
**basic_view** | **bool** |  | [optional] 
**search_type** | **str** |  | [optional] 
**page_title** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_general import SearchSerpDataDtoGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoGeneral from a JSON string
search_serp_data_dto_general_instance = SearchSerpDataDtoGeneral.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoGeneral.to_json())

# convert the object into a dict
search_serp_data_dto_general_dict = search_serp_data_dto_general_instance.to_dict()
# create an instance of SearchSerpDataDtoGeneral from a dict
search_serp_data_dto_general_from_dict = SearchSerpDataDtoGeneral.from_dict(search_serp_data_dto_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


