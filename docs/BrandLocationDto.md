# BrandLocationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **object** |  | [optional] 
**state** | **object** |  | [optional] 
**country** | **object** |  | [optional] 
**country_code** | **object** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_location_dto import BrandLocationDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandLocationDto from a JSON string
brand_location_dto_instance = BrandLocationDto.from_json(json)
# print the JSON string representation of the object
print(BrandLocationDto.to_json())

# convert the object into a dict
brand_location_dto_dict = brand_location_dto_instance.to_dict()
# create an instance of BrandLocationDto from a dict
brand_location_dto_from_dict = BrandLocationDto.from_dict(brand_location_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


