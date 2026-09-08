# BrandMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that was queried | 
**mode** | **str** | Mode requested | 
**cached** | **bool** | Whether this response was served from cache | 
**last_updated** | **str** | When the underlying data was last fetched/updated | 
**data_age** | **str** | Human-readable age of the cached data | 
**refresh_requested** | **bool** | Whether a forced refresh was requested | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.brand_meta_dto import BrandMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandMetaDto from a JSON string
brand_meta_dto_instance = BrandMetaDto.from_json(json)
# print the JSON string representation of the object
print(BrandMetaDto.to_json())

# convert the object into a dict
brand_meta_dto_dict = brand_meta_dto_instance.to_dict()
# create an instance of BrandMetaDto from a dict
brand_meta_dto_from_dict = BrandMetaDto.from_dict(brand_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


