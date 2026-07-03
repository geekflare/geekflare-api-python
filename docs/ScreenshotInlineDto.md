# ScreenshotInlineDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** | Raw Base64-encoded image string | 
**data_uri** | **str** | Data URI — ready to embed in an &lt;img&gt; tag or pass directly to an LLM | 

## Example

```python
from geekflare_api.models.screenshot_inline_dto import ScreenshotInlineDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotInlineDto from a JSON string
screenshot_inline_dto_instance = ScreenshotInlineDto.from_json(json)
# print the JSON string representation of the object
print(ScreenshotInlineDto.to_json())

# convert the object into a dict
screenshot_inline_dto_dict = screenshot_inline_dto_instance.to_dict()
# create an instance of ScreenshotInlineDto from a dict
screenshot_inline_dto_from_dict = ScreenshotInlineDto.from_dict(screenshot_inline_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


