# SearchHtmlResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) |  | 
**data** | **object** |  | 

## Example

```python
from geekflare_api.models.search_html_response_dto import SearchHtmlResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchHtmlResponseDto from a JSON string
search_html_response_dto_instance = SearchHtmlResponseDto.from_json(json)
# print the JSON string representation of the object
print(SearchHtmlResponseDto.to_json())

# convert the object into a dict
search_html_response_dto_dict = search_html_response_dto_instance.to_dict()
# create an instance of SearchHtmlResponseDto from a dict
search_html_response_dto_from_dict = SearchHtmlResponseDto.from_dict(search_html_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


