# SearchSerpDataDtoAiOverview

AI Overview that Google shows for the query. Only present when Google returns one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | AI Overview as plain text | [optional] 
**html** | **str** | AI Overview as the raw HTML Google rendered | [optional] 
**references** | [**List[SearchSerpDataDtoAiOverviewReferencesInner]**](SearchSerpDataDtoAiOverviewReferencesInner.md) | Sources cited by the AI Overview | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_ai_overview import SearchSerpDataDtoAiOverview

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoAiOverview from a JSON string
search_serp_data_dto_ai_overview_instance = SearchSerpDataDtoAiOverview.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoAiOverview.to_json())

# convert the object into a dict
search_serp_data_dto_ai_overview_dict = search_serp_data_dto_ai_overview_instance.to_dict()
# create an instance of SearchSerpDataDtoAiOverview from a dict
search_serp_data_dto_ai_overview_from_dict = SearchSerpDataDtoAiOverview.from_dict(search_serp_data_dto_ai_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


