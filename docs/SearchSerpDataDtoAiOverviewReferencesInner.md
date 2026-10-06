# SearchSerpDataDtoAiOverviewReferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**url** | **str** | Source URL. Can be null when Google doesn&#39;t expose one | [optional] 
**source** | **str** |  | [optional] 
**snippet** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_ai_overview_references_inner import SearchSerpDataDtoAiOverviewReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoAiOverviewReferencesInner from a JSON string
search_serp_data_dto_ai_overview_references_inner_instance = SearchSerpDataDtoAiOverviewReferencesInner.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoAiOverviewReferencesInner.to_json())

# convert the object into a dict
search_serp_data_dto_ai_overview_references_inner_dict = search_serp_data_dto_ai_overview_references_inner_instance.to_dict()
# create an instance of SearchSerpDataDtoAiOverviewReferencesInner from a dict
search_serp_data_dto_ai_overview_references_inner_from_dict = SearchSerpDataDtoAiOverviewReferencesInner.from_dict(search_serp_data_dto_ai_overview_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


