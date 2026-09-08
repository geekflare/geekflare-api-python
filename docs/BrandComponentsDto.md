# BrandComponentsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_primary** | [**BrandButtonStyleDto**](BrandButtonStyleDto.md) |  | [optional] 
**button_secondary** | [**BrandButtonStyleDto**](BrandButtonStyleDto.md) |  | [optional] 
**input** | [**BrandButtonStyleDto**](BrandButtonStyleDto.md) |  | [optional] 

## Example

```python
from geekflare_api.models.brand_components_dto import BrandComponentsDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandComponentsDto from a JSON string
brand_components_dto_instance = BrandComponentsDto.from_json(json)
# print the JSON string representation of the object
print(BrandComponentsDto.to_json())

# convert the object into a dict
brand_components_dto_dict = brand_components_dto_instance.to_dict()
# create an instance of BrandComponentsDto from a dict
brand_components_dto_from_dict = BrandComponentsDto.from_dict(brand_components_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


