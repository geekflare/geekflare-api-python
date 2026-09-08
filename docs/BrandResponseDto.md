# BrandResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**BrandMetaDto**](BrandMetaDto.md) | Metadata about the request | 
**data** | [**BrandDataDto**](BrandDataDto.md) | Brand data payload | 

## Example

```python
from geekflare_api.models.brand_response_dto import BrandResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandResponseDto from a JSON string
brand_response_dto_instance = BrandResponseDto.from_json(json)
# print the JSON string representation of the object
print(BrandResponseDto.to_json())

# convert the object into a dict
brand_response_dto_dict = brand_response_dto_instance.to_dict()
# create an instance of BrandResponseDto from a dict
brand_response_dto_from_dict = BrandResponseDto.from_dict(brand_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


