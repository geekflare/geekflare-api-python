# LoadTimeDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **float** | Time spent in DNS lookup (ms) | 
**connect** | **float** | Time to establish TCP connection (ms) | 
**tls** | **float** | Time to complete TLS handshake (ms) | 
**send** | **float** | Time to send request (ms) | 
**wait** | **float** | Time waiting for response (ms) | 
**total** | **float** | Total load time (ms) | 
**status_code** | **float** | HTTP status code of the response | 
**reason_phrase** | **str** | HTTP reason phrase | 
**timings** | [**TimingsDto**](TimingsDto.md) | Detailed timing breakdown | 
**network** | [**NetworkDto**](NetworkDto.md) | Network information | 
**headers** | **object** | Response headers as key-value pairs | 
**protocol_support** | [**ProtocolSupportDto**](ProtocolSupportDto.md) | HTTP protocol support information | 

## Example

```python
from geekflare_api.models.load_time_data_dto import LoadTimeDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeDataDto from a JSON string
load_time_data_dto_instance = LoadTimeDataDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeDataDto.to_json())

# convert the object into a dict
load_time_data_dto_dict = load_time_data_dto_instance.to_dict()
# create an instance of LoadTimeDataDto from a dict
load_time_data_dto_from_dict = LoadTimeDataDto.from_dict(load_time_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


