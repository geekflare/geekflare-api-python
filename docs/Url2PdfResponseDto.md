# Url2PdfResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**Url2PdfMetaDto**](Url2PdfMetaDto.md) | Metadata about the request | 
**data** | **str** | Generated PDF URL | 

## Example

```python
from geekflare_api.models.url2_pdf_response_dto import Url2PdfResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of Url2PdfResponseDto from a JSON string
url2_pdf_response_dto_instance = Url2PdfResponseDto.from_json(json)
# print the JSON string representation of the object
print(Url2PdfResponseDto.to_json())

# convert the object into a dict
url2_pdf_response_dto_dict = url2_pdf_response_dto_instance.to_dict()
# create an instance of Url2PdfResponseDto from a dict
url2_pdf_response_dto_from_dict = Url2PdfResponseDto.from_dict(url2_pdf_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


