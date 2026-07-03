# ScreenshotResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**ScreenshotMetaDto**](ScreenshotMetaDto.md) | Metadata about the request | 
**data** | **str** | URL of the captured screenshot | 
**inline** | [**ScreenshotInlineDto**](ScreenshotInlineDto.md) | Inline Base64 image data. Present only when the request included &#x60;inline: true&#x60;. | [optional] 

## Example

```python
from geekflare_api.models.screenshot_response_dto import ScreenshotResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotResponseDto from a JSON string
screenshot_response_dto_instance = ScreenshotResponseDto.from_json(json)
# print the JSON string representation of the object
print(ScreenshotResponseDto.to_json())

# convert the object into a dict
screenshot_response_dto_dict = screenshot_response_dto_instance.to_dict()
# create an instance of ScreenshotResponseDto from a dict
screenshot_response_dto_from_dict = ScreenshotResponseDto.from_dict(screenshot_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


