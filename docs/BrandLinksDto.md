# BrandLinksDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blog** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**signup** | **str** |  | [optional] 
**careers** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**privacy** | **str** |  | [optional] 
**terms** | **str** |  | [optional] 
**pricing** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_links_dto import BrandLinksDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandLinksDto from a JSON string
brand_links_dto_instance = BrandLinksDto.from_json(json)
# print the JSON string representation of the object
print(BrandLinksDto.to_json())

# convert the object into a dict
brand_links_dto_dict = brand_links_dto_instance.to_dict()
# create an instance of BrandLinksDto from a dict
brand_links_dto_from_dict = BrandLinksDto.from_dict(brand_links_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


