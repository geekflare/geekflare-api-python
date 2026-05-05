# Url2PdfDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type to emulate. Defaults to desktop. | [optional] [default to 'desktop']
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**format** | **str** | Paper format | [optional] [default to 'a4']
**orientation** | **str** | Orientation | [optional] [default to 'portrait']
**margin** | [**MarginDto**](MarginDto.md) | Margins in mm | [optional] 
**scale** | **float** | Rendering scale between 0–2 | [optional] [default to 1]
**hide_cookie** | **bool** | Hide cookie popups | [optional] [default to False]
**skip_captcha** | **bool** | Try to skip captcha | [optional] [default to False]
**add_timestamp** | **bool** | Add timestamp watermark | [optional] [default to False]

## Example

```python
from geekflare_api.models.url2_pdf_dto import Url2PdfDto

# TODO update the JSON string below
json = "{}"
# create an instance of Url2PdfDto from a JSON string
url2_pdf_dto_instance = Url2PdfDto.from_json(json)
# print the JSON string representation of the object
print(Url2PdfDto.to_json())

# convert the object into a dict
url2_pdf_dto_dict = url2_pdf_dto_instance.to_dict()
# create an instance of Url2PdfDto from a dict
url2_pdf_dto_from_dict = Url2PdfDto.from_dict(url2_pdf_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


