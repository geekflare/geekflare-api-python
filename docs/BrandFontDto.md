# BrandFontDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** |  | 
**usage** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from geekflare_api.models.brand_font_dto import BrandFontDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandFontDto from a JSON string
brand_font_dto_instance = BrandFontDto.from_json(json)
# print the JSON string representation of the object
print(BrandFontDto.to_json())

# convert the object into a dict
brand_font_dto_dict = brand_font_dto_instance.to_dict()
# create an instance of BrandFontDto from a dict
brand_font_dto_from_dict = BrandFontDto.from_dict(brand_font_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


