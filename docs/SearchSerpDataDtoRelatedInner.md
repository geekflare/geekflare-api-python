# SearchSerpDataDtoRelatedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**rank** | **float** | Position within this section | [optional] 
**global_rank** | **float** | Position across the whole results page | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_related_inner import SearchSerpDataDtoRelatedInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoRelatedInner from a JSON string
search_serp_data_dto_related_inner_instance = SearchSerpDataDtoRelatedInner.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoRelatedInner.to_json())

# convert the object into a dict
search_serp_data_dto_related_inner_dict = search_serp_data_dto_related_inner_instance.to_dict()
# create an instance of SearchSerpDataDtoRelatedInner from a dict
search_serp_data_dto_related_inner_from_dict = SearchSerpDataDtoRelatedInner.from_dict(search_serp_data_dto_related_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


