# LighthouseResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**LighthouseMetaDto**](LighthouseMetaDto.md) | Metadata about the request | 
**data** | **str** | URL to the Lighthouse report | 

## Example

```python
from geekflare_api.models.lighthouse_response_dto import LighthouseResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LighthouseResponseDto from a JSON string
lighthouse_response_dto_instance = LighthouseResponseDto.from_json(json)
# print the JSON string representation of the object
print(LighthouseResponseDto.to_json())

# convert the object into a dict
lighthouse_response_dto_dict = lighthouse_response_dto_instance.to_dict()
# create an instance of LighthouseResponseDto from a dict
lighthouse_response_dto_from_dict = LighthouseResponseDto.from_dict(lighthouse_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


