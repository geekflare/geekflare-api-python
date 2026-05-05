# Url2PdfMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL | 
**device** | **str** | Device type used | 
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**format** | **str** | Paper format | 
**orientation** | **str** | Orientation | 
**margin** | [**MarginDto**](MarginDto.md) | Margins in mm | [optional] 
**scale** | **float** | Rendering scale | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details | 

## Example

```python
from geekflare_api.models.url2_pdf_meta_dto import Url2PdfMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of Url2PdfMetaDto from a JSON string
url2_pdf_meta_dto_instance = Url2PdfMetaDto.from_json(json)
# print the JSON string representation of the object
print(Url2PdfMetaDto.to_json())

# convert the object into a dict
url2_pdf_meta_dto_dict = url2_pdf_meta_dto_instance.to_dict()
# create an instance of Url2PdfMetaDto from a dict
url2_pdf_meta_dto_from_dict = Url2PdfMetaDto.from_dict(url2_pdf_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


