# SearchSerpDataDtoPeopleAlsoAskInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | [optional] 
**question_link** | **str** |  | [optional] 
**question_type** | **str** |  | [optional] 
**rank** | **float** | Position within this section | [optional] 
**global_rank** | **float** | Position across the whole results page | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_people_also_ask_inner import SearchSerpDataDtoPeopleAlsoAskInner

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoPeopleAlsoAskInner from a JSON string
search_serp_data_dto_people_also_ask_inner_instance = SearchSerpDataDtoPeopleAlsoAskInner.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoPeopleAlsoAskInner.to_json())

# convert the object into a dict
search_serp_data_dto_people_also_ask_inner_dict = search_serp_data_dto_people_also_ask_inner_instance.to_dict()
# create an instance of SearchSerpDataDtoPeopleAlsoAskInner from a dict
search_serp_data_dto_people_also_ask_inner_from_dict = SearchSerpDataDtoPeopleAlsoAskInner.from_dict(search_serp_data_dto_people_also_ask_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


