# SearchResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) |  | 
**data** | [**List[SearchResultItemDto]**](SearchResultItemDto.md) |  | 

## Example

```python
from geekflare_api.models.search_response_dto import SearchResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseDto from a JSON string
search_response_dto_instance = SearchResponseDto.from_json(json)
# print the JSON string representation of the object
print(SearchResponseDto.to_json())

# convert the object into a dict
search_response_dto_dict = search_response_dto_instance.to_dict()
# create an instance of SearchResponseDto from a dict
search_response_dto_from_dict = SearchResponseDto.from_dict(search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


