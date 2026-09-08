# BrandPageMetaDto

Meta tags scraped from the page head. Which tags are present depends on what the site itself publishes — not every site sets every Open Graph or Twitter Card tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**theme_color** | **str** |  | [optional] 
**canonical_url** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**og_url** | **str** |  | [optional] 
**og_type** | **str** |  | [optional] 
**og_title** | **str** |  | [optional] 
**og_description** | **str** |  | [optional] 
**og_image** | **str** |  | [optional] 
**og_image_type** | **str** |  | [optional] 
**og_image_width** | **str** |  | [optional] 
**og_image_height** | **str** |  | [optional] 
**og_site_name** | **str** |  | [optional] 
**og_locale** | **str** |  | [optional] 
**twitter_card** | **str** |  | [optional] 
**twitter_site** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_page_meta_dto import BrandPageMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandPageMetaDto from a JSON string
brand_page_meta_dto_instance = BrandPageMetaDto.from_json(json)
# print the JSON string representation of the object
print(BrandPageMetaDto.to_json())

# convert the object into a dict
brand_page_meta_dto_dict = brand_page_meta_dto_instance.to_dict()
# create an instance of BrandPageMetaDto from a dict
brand_page_meta_dto_from_dict = BrandPageMetaDto.from_dict(brand_page_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


