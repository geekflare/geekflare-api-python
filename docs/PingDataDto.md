# PingDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **float** | Number of ping requests sent | 
**loss** | **float** | Packet loss percentage | 
**latency** | **float** | Average latency in milliseconds | 
**min** | **float** | Minimum round-trip time (RTT) in milliseconds | 
**max** | **float** | Maximum round-trip time (RTT) in milliseconds | 
**avg** | **float** | Average round-trip time (RTT) in milliseconds | 
**std_dev** | **float** | Standard deviation of RTT in milliseconds | 
**ip** | **str** | Resolved IP address of the tested domain | 

## Example

```python
from geekflare_api.models.ping_data_dto import PingDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of PingDataDto from a JSON string
ping_data_dto_instance = PingDataDto.from_json(json)
# print the JSON string representation of the object
print(PingDataDto.to_json())

# convert the object into a dict
ping_data_dto_dict = ping_data_dto_instance.to_dict()
# create an instance of PingDataDto from a dict
ping_data_dto_from_dict = PingDataDto.from_dict(ping_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


