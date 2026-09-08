# BrandColorsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** |  | [optional] 
**secondary** | **str** |  | [optional] 
**background** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**accent** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**palette** | [**List[BrandColorEntryDto]**](BrandColorEntryDto.md) |  | 

## Example

```python
from geekflare_api.models.brand_colors_dto import BrandColorsDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandColorsDto from a JSON string
brand_colors_dto_instance = BrandColorsDto.from_json(json)
# print the JSON string representation of the object
print(BrandColorsDto.to_json())

# convert the object into a dict
brand_colors_dto_dict = brand_colors_dto_instance.to_dict()
# create an instance of BrandColorsDto from a dict
brand_colors_dto_from_dict = BrandColorsDto.from_dict(brand_colors_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


