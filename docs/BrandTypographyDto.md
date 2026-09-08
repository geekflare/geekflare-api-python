# BrandTypographyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h1** | **str** |  | [optional] 
**h2** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_typography_dto import BrandTypographyDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandTypographyDto from a JSON string
brand_typography_dto_instance = BrandTypographyDto.from_json(json)
# print the JSON string representation of the object
print(BrandTypographyDto.to_json())

# convert the object into a dict
brand_typography_dto_dict = brand_typography_dto_instance.to_dict()
# create an instance of BrandTypographyDto from a dict
brand_typography_dto_from_dict = BrandTypographyDto.from_dict(brand_typography_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


