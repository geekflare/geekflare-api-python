# SearchSerpResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) | Metadata about the search | 
**data** | [**SearchSerpDataDto**](SearchSerpDataDto.md) | Google SERP data (returned when &#x60;serp&#x60; is &#x60;true&#x60;) | 

## Example

```python
from geekflare_api.models.search_serp_response_dto import SearchSerpResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpResponseDto from a JSON string
search_serp_response_dto_instance = SearchSerpResponseDto.from_json(json)
# print the JSON string representation of the object
print(SearchSerpResponseDto.to_json())

# convert the object into a dict
search_serp_response_dto_dict = search_serp_response_dto_instance.to_dict()
# create an instance of SearchSerpResponseDto from a dict
search_serp_response_dto_from_dict = SearchSerpResponseDto.from_dict(search_serp_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


