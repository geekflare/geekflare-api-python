# BrandSocialProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from geekflare_api.models.brand_social_profile_dto import BrandSocialProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandSocialProfileDto from a JSON string
brand_social_profile_dto_instance = BrandSocialProfileDto.from_json(json)
# print the JSON string representation of the object
print(BrandSocialProfileDto.to_json())

# convert the object into a dict
brand_social_profile_dto_dict = brand_social_profile_dto_instance.to_dict()
# create an instance of BrandSocialProfileDto from a dict
brand_social_profile_dto_from_dict = BrandSocialProfileDto.from_dict(brand_social_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


