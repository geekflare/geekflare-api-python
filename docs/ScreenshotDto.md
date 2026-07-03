# ScreenshotDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type to emulate. Defaults to desktop. | [optional] [default to 'desktop']
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**type** | **str** | File type of screenshot. Defaults to png. | [optional] [default to 'png']
**full_page** | **bool** | Take full-page screenshot | [optional] [default to False]
**block_ads** | **bool** | Block ads on the page | [optional] [default to True]
**hide_cookie** | **bool** | Hide cookie popups | [optional] [default to True]
**skip_captcha** | **bool** | Try to bypass captcha | [optional] [default to True]
**add_timestamp** | **bool** | Add timestamp watermark | [optional] [default to False]
**page_height** | **float** | Height of the page (for partial screenshot) | [optional] 
**viewport_width** | **float** | Width of the viewport | [optional] 
**viewport_height** | **float** | Height of the viewport | [optional] 
**theme** | **str** | Theme to use for rendering | [optional] [default to 'auto']
**remove_background** | **bool** | Remove background from screenshot | [optional] 
**highlight_links** | **bool** | Highlight links on the page | [optional] 
**delay** | **float** | Delay before taking screenshot (in seconds) | [optional] 
**disable_animations** | **bool** | Disable animations on the page | [optional] 
**quality** | **float** | Image quality (for JPEG/WEBP) | [optional] 
**scale_factor** | **float** | Device scale factor | [optional] 
**capture_beyond_viewport** | **bool** | Capture beyond viewport if possible | [optional] 
**selector** | **str** | CSS selector to capture only a specific element on the page. Supports class (.), ID (#), and attribute selectors. | [optional] 
**fallback_to_full_page** | **bool** | If true and the selector is not found, falls back to a full-page screenshot instead of returning an error. Default: false. | [optional] [default to False]
**inline** | **bool** | If true, includes a Base64-encoded image and data URI in the response. Useful for AI agents and LLMs that cannot fetch URLs. Default: false. | [optional] [default to False]

## Example

```python
from geekflare_api.models.screenshot_dto import ScreenshotDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotDto from a JSON string
screenshot_dto_instance = ScreenshotDto.from_json(json)
# print the JSON string representation of the object
print(ScreenshotDto.to_json())

# convert the object into a dict
screenshot_dto_dict = screenshot_dto_instance.to_dict()
# create an instance of ScreenshotDto from a dict
screenshot_dto_from_dict = ScreenshotDto.from_dict(screenshot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


