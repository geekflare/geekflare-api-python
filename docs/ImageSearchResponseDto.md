# ImageSearchResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) |  | 
**data** | [**List[ImageSearchResultItemDto]**](ImageSearchResultItemDto.md) |  | 

## Example

```python
from geekflare_api.models.image_search_response_dto import ImageSearchResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSearchResponseDto from a JSON string
image_search_response_dto_instance = ImageSearchResponseDto.from_json(json)
# print the JSON string representation of the object
print(ImageSearchResponseDto.to_json())

# convert the object into a dict
image_search_response_dto_dict = image_search_response_dto_instance.to_dict()
# create an instance of ImageSearchResponseDto from a dict
image_search_response_dto_from_dict = ImageSearchResponseDto.from_dict(image_search_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


