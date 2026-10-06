# SearchSerpDataDtoOrganicInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**display_link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**snippet_highlighted_words** | **List[str]** | Portions of the snippet Google highlights | [optional] 
**extensions** | [**List[SearchSerpDataDtoOrganicInnerExtensionsInner]**](SearchSerpDataDtoOrganicInnerExtensionsInner.md) | Extra info shown with the result, such as a date | [optional] 
**icon** | **str** | Site icon as a data URI | [optional] 
**rank** | **float** | Position within this section | [optional] 
**global_rank** | **float** | Position across the whole results page | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_organic_inner import SearchSerpDataDtoOrganicInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoOrganicInner from a JSON string
search_serp_data_dto_organic_inner_instance = SearchSerpDataDtoOrganicInner.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoOrganicInner.to_json())

# convert the object into a dict
search_serp_data_dto_organic_inner_dict = search_serp_data_dto_organic_inner_instance.to_dict()
# create an instance of SearchSerpDataDtoOrganicInner from a dict
search_serp_data_dto_organic_inner_from_dict = SearchSerpDataDtoOrganicInner.from_dict(search_serp_data_dto_organic_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


