# BrandLogoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**theme** | **str** |  | [optional] 
**url** | **str** |  | 
**format** | **str** |  | 

## Example

```python
from geekflare_api.models.brand_logo_dto import BrandLogoDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandLogoDto from a JSON string
brand_logo_dto_instance = BrandLogoDto.from_json(json)
# print the JSON string representation of the object
print(BrandLogoDto.to_json())

# convert the object into a dict
brand_logo_dto_dict = brand_logo_dto_instance.to_dict()
# create an instance of BrandLogoDto from a dict
brand_logo_dto_from_dict = BrandLogoDto.from_dict(brand_logo_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


