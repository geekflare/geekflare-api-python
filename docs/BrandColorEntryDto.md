# BrandColorEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hex** | **str** |  | 
**usage** | **str** |  | 

## Example

```python
from geekflare_api.models.brand_color_entry_dto import BrandColorEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandColorEntryDto from a JSON string
brand_color_entry_dto_instance = BrandColorEntryDto.from_json(json)
# print the JSON string representation of the object
print(BrandColorEntryDto.to_json())

# convert the object into a dict
brand_color_entry_dto_dict = brand_color_entry_dto_instance.to_dict()
# create an instance of BrandColorEntryDto from a dict
brand_color_entry_dto_from_dict = BrandColorEntryDto.from_dict(brand_color_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


