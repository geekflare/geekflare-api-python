# BrandSpacingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_unit** | **float** | Heuristic: mode of observed small padding/margin values, not a guaranteed design token | [optional] 
**border_radius** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_spacing_dto import BrandSpacingDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSpacingDto from a JSON string
brand_spacing_dto_instance = BrandSpacingDto.from_json(json)
# print the JSON string representation of the object
print(BrandSpacingDto.to_json())

# convert the object into a dict
brand_spacing_dto_dict = brand_spacing_dto_instance.to_dict()
# create an instance of BrandSpacingDto from a dict
brand_spacing_dto_from_dict = BrandSpacingDto.from_dict(brand_spacing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


