# SearchMarkdownResponseDto


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
from geekflare_api.models.search_markdown_response_dto import SearchMarkdownResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMarkdownResponseDto from a JSON string
search_markdown_response_dto_instance = SearchMarkdownResponseDto.from_json(json)
# print the JSON string representation of the object
print(SearchMarkdownResponseDto.to_json())

# convert the object into a dict
search_markdown_response_dto_dict = search_markdown_response_dto_instance.to_dict()
# create an instance of SearchMarkdownResponseDto from a dict
search_markdown_response_dto_from_dict = SearchMarkdownResponseDto.from_dict(search_markdown_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


