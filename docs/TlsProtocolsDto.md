# TlsProtocolsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls10** | **bool** | Whether TLS 1.0 is supported | 
**tls11** | **bool** | Whether TLS 1.1 is supported | 
**tls12** | **bool** | Whether TLS 1.2 is supported | 
**tls13** | **bool** | Whether TLS 1.3 is supported | 

## Example

```python
from geekflare_api.models.tls_protocols_dto import TlsProtocolsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsProtocolsDto from a JSON string
tls_protocols_dto_instance = TlsProtocolsDto.from_json(json)
# print the JSON string representation of the object
print(TlsProtocolsDto.to_json())

# convert the object into a dict
tls_protocols_dto_dict = tls_protocols_dto_instance.to_dict()
# create an instance of TlsProtocolsDto from a dict
tls_protocols_dto_from_dict = TlsProtocolsDto.from_dict(tls_protocols_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


