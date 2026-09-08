# BrandButtonStyleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**border_color** | **str** |  | [optional] 
**border_radius** | **str** |  | [optional] 
**shadow** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_button_style_dto import BrandButtonStyleDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandButtonStyleDto from a JSON string
brand_button_style_dto_instance = BrandButtonStyleDto.from_json(json)
# print the JSON string representation of the object
print(BrandButtonStyleDto.to_json())

# convert the object into a dict
brand_button_style_dto_dict = brand_button_style_dto_instance.to_dict()
# create an instance of BrandButtonStyleDto from a dict
brand_button_style_dto_from_dict = BrandButtonStyleDto.from_dict(brand_button_style_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


