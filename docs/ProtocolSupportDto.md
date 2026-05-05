# ProtocolSupportDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http10** | **bool** | Whether HTTP/1.0 is supported | 
**http11** | **bool** | Whether HTTP/1.1 is supported | 
**http2** | **bool** | Whether HTTP/2 is supported | 
**http3** | **bool** | Whether HTTP/3 is supported | 
**http3_supported_version** | **List[str]** | HTTP/3 supported versions if available | [optional] 

## Example

```python
from geekflare_api.models.protocol_support_dto import ProtocolSupportDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolSupportDto from a JSON string
protocol_support_dto_instance = ProtocolSupportDto.from_json(json)
# print the JSON string representation of the object
print(ProtocolSupportDto.to_json())

# convert the object into a dict
protocol_support_dto_dict = protocol_support_dto_instance.to_dict()
# create an instance of ProtocolSupportDto from a dict
protocol_support_dto_from_dict = ProtocolSupportDto.from_dict(protocol_support_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


