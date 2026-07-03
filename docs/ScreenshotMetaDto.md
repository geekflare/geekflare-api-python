# ScreenshotMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL that was captured | 
**type** | **str** | File type of screenshot | 
**device** | **str** | Device type used | 
**full_page** | **bool** | Whether full-page screenshot was taken | 
**block_ads** | **bool** | Whether ads were blocked | 
**hide_cookie** | **bool** | Whether cookie popups were hidden | 
**skip_captcha** | **bool** | Whether captcha was bypassed | 
**add_timestamp** | **bool** | Whether timestamp watermark was added | 
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**page_height** | **float** | Height of the page | [optional] 
**viewport_width** | **float** | Width of the viewport | [optional] 
**viewport_height** | **float** | Height of the viewport | [optional] 
**theme** | **str** | Theme used | [optional] 
**remove_background** | **bool** | Whether background was removed | [optional] 
**highlight_links** | **bool** | Whether links were highlighted | [optional] 
**delay** | **float** | Delay before screenshot | [optional] 
**disable_animations** | **bool** | Whether animations were disabled | [optional] 
**quality** | **float** | Image quality (JPEG/WEBP) | [optional] 
**scale_factor** | **float** | Device scale factor | [optional] 
**capture_beyond_viewport** | **bool** | Capture beyond viewport | [optional] 
**selector** | **str** | CSS selector that was targeted, if provided | [optional] 
**fallback_to_full_page** | **bool** | Whether fallback to full-page was enabled | [optional] 
**inline** | **bool** | Whether inline base64 output was requested | [optional] 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details | 

## Example

```python
from geekflare_api.models.screenshot_meta_dto import ScreenshotMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotMetaDto from a JSON string
screenshot_meta_dto_instance = ScreenshotMetaDto.from_json(json)
# print the JSON string representation of the object
print(ScreenshotMetaDto.to_json())

# convert the object into a dict
screenshot_meta_dto_dict = screenshot_meta_dto_instance.to_dict()
# create an instance of ScreenshotMetaDto from a dict
screenshot_meta_dto_from_dict = ScreenshotMetaDto.from_dict(screenshot_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


