# BrandDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**name** | **str** |  | [optional] 
**tagline** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**slogan** | **str** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] [default to False]
**favicon** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**logos** | [**List[BrandLogoDto]**](BrandLogoDto.md) |  | [optional] 
**colors** | [**BrandColorsDto**](BrandColorsDto.md) |  | [optional] 
**color_scheme** | **str** |  | [optional] 
**fonts** | [**List[BrandFontDto]**](BrandFontDto.md) |  | [optional] 
**font_sizes** | [**BrandTypographyDto**](BrandTypographyDto.md) |  | [optional] 
**components** | [**BrandComponentsDto**](BrandComponentsDto.md) |  | [optional] 
**spacing** | [**BrandSpacingDto**](BrandSpacingDto.md) |  | [optional] 
**social_profiles** | [**List[BrandSocialProfileDto]**](BrandSocialProfileDto.md) |  | [optional] 
**links** | [**BrandLinksDto**](BrandLinksDto.md) |  | [optional] 
**company** | [**BrandCompanyDto**](BrandCompanyDto.md) |  | [optional] 
**page_meta** | [**BrandPageMetaDto**](BrandPageMetaDto.md) |  | [optional] 

## Example

```python
from geekflare_api.models.brand_data_dto import BrandDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandDataDto from a JSON string
brand_data_dto_instance = BrandDataDto.from_json(json)
# print the JSON string representation of the object
print(BrandDataDto.to_json())

# convert the object into a dict
brand_data_dto_dict = brand_data_dto_instance.to_dict()
# create an instance of BrandDataDto from a dict
brand_data_dto_from_dict = BrandDataDto.from_dict(brand_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


