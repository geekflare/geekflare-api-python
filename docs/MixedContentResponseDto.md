# MixedContentResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Indicates whether mixed content found or not. It can either be \&quot;Mixed content(s) found.\&quot; or \&quot;No mixed content found.\&quot; | 
**meta** | [**MixedContentMetaDto**](MixedContentMetaDto.md) | Metadata about the mixed content test | 
**data** | [**MixedContentResponseDtoData**](MixedContentResponseDtoData.md) |  | 

## Example

```python
from geekflare_api.models.mixed_content_response_dto import MixedContentResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MixedContentResponseDto from a JSON string
mixed_content_response_dto_instance = MixedContentResponseDto.from_json(json)
# print the JSON string representation of the object
print(MixedContentResponseDto.to_json())

# convert the object into a dict
mixed_content_response_dto_dict = mixed_content_response_dto_instance.to_dict()
# create an instance of MixedContentResponseDto from a dict
mixed_content_response_dto_from_dict = MixedContentResponseDto.from_dict(mixed_content_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


