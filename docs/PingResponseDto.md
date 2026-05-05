# PingResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**PingMetaDto**](PingMetaDto.md) | Metadata about the Ping test execution | 
**data** | [**PingDataDto**](PingDataDto.md) | Ping result statistics | 

## Example

```python
from geekflare_api.models.ping_response_dto import PingResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PingResponseDto from a JSON string
ping_response_dto_instance = PingResponseDto.from_json(json)
# print the JSON string representation of the object
print(PingResponseDto.to_json())

# convert the object into a dict
ping_response_dto_dict = ping_response_dto_instance.to_dict()
# create an instance of PingResponseDto from a dict
ping_response_dto_from_dict = PingResponseDto.from_dict(ping_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


