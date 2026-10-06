# SearchSerpDataDto

Full Google SERP. Which sections are present depends on what Google returns for the query. With `source` set to `news` or `images`, results are returned under `news` or `images` instead of `organic`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general** | [**SearchSerpDataDtoGeneral**](SearchSerpDataDtoGeneral.md) |  | [optional] 
**input** | [**SearchSerpDataDtoInput**](SearchSerpDataDtoInput.md) |  | [optional] 
**navigation** | [**List[SearchSerpDataDtoNavigationInner]**](SearchSerpDataDtoNavigationInner.md) | Search vertical tabs shown on the page (Images, News, Videos, Maps, etc.) | [optional] 
**organic** | [**List[SearchSerpDataDtoOrganicInner]**](SearchSerpDataDtoOrganicInner.md) | Organic (non-ad) results | [optional] 
**news** | **List[object]** | News results. Returned instead of &#x60;organic&#x60; when &#x60;source&#x60; is &#x60;news&#x60;. | [optional] 
**images** | **List[object]** | Image results. Returned instead of &#x60;organic&#x60; when &#x60;source&#x60; is &#x60;images&#x60;. | [optional] 
**pagination** | [**SearchSerpDataDtoPagination**](SearchSerpDataDtoPagination.md) |  | [optional] 
**related** | [**List[SearchSerpDataDtoRelatedInner]**](SearchSerpDataDtoRelatedInner.md) | Related searches | [optional] 
**ai_overview** | [**SearchSerpDataDtoAiOverview**](SearchSerpDataDtoAiOverview.md) |  | [optional] 
**people_also_ask** | [**List[SearchSerpDataDtoPeopleAlsoAskInner]**](SearchSerpDataDtoPeopleAlsoAskInner.md) | People Also Ask questions | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto import SearchSerpDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDto from a JSON string
search_serp_data_dto_instance = SearchSerpDataDto.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDto.to_json())

# convert the object into a dict
search_serp_data_dto_dict = search_serp_data_dto_instance.to_dict()
# create an instance of SearchSerpDataDto from a dict
search_serp_data_dto_from_dict = SearchSerpDataDto.from_dict(search_serp_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


