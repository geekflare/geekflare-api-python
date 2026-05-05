# ServiceHealthResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Top-level message summarizing the overall health check | 
**services** | [**List[ServiceStatus]**](ServiceStatus.md) | Status of individual internal services | 

## Example

```python
from geekflare_api.models.service_health_response_dto import ServiceHealthResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceHealthResponseDto from a JSON string
service_health_response_dto_instance = ServiceHealthResponseDto.from_json(json)
# print the JSON string representation of the object
print(ServiceHealthResponseDto.to_json())

# convert the object into a dict
service_health_response_dto_dict = service_health_response_dto_instance.to_dict()
# create an instance of ServiceHealthResponseDto from a dict
service_health_response_dto_from_dict = ServiceHealthResponseDto.from_dict(service_health_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


