# BrandDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**refresh** | **bool** | Force on-demand fetch and refresh the cache, bypassing any existing cached data | [optional] [default to False]
**mode** | **str** | Depth of brand data to return. Enriched includes LLM-synthesized company intelligence. | [optional] [default to 'standard']

## Example

```python
from geekflare_api.models.brand_dto import BrandDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandDto from a JSON string
brand_dto_instance = BrandDto.from_json(json)
# print the JSON string representation of the object
print(BrandDto.to_json())

# convert the object into a dict
brand_dto_dict = brand_dto_instance.to_dict()
# create an instance of BrandDto from a dict
brand_dto_from_dict = BrandDto.from_dict(brand_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


