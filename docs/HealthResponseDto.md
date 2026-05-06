# HealthResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Metadata about the request | 

## Example

```python
from geekflare_api.models.health_response_dto import HealthResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of HealthResponseDto from a JSON string
health_response_dto_instance = HealthResponseDto.from_json(json)
# print the JSON string representation of the object
print(HealthResponseDto.to_json())

# convert the object into a dict
health_response_dto_dict = health_response_dto_instance.to_dict()
# create an instance of HealthResponseDto from a dict
health_response_dto_from_dict = HealthResponseDto.from_dict(health_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


