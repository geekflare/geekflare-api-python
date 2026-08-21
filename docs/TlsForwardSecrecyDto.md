# TlsForwardSecrecyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negotiated_cipher** | **object** | Cipher suite negotiated on the primary handshake | 
**ephemeral_key_type** | **object** | Ephemeral key exchange type (e.g. ECDH, DH), null if the cipher does not provide forward secrecy | 
**ephemeral_key_size** | **object** | Ephemeral key size in bits | 

## Example

```python
from geekflare_api.models.tls_forward_secrecy_dto import TlsForwardSecrecyDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsForwardSecrecyDto from a JSON string
tls_forward_secrecy_dto_instance = TlsForwardSecrecyDto.from_json(json)
# print the JSON string representation of the object
print(TlsForwardSecrecyDto.to_json())

# convert the object into a dict
tls_forward_secrecy_dto_dict = tls_forward_secrecy_dto_instance.to_dict()
# create an instance of TlsForwardSecrecyDto from a dict
tls_forward_secrecy_dto_from_dict = TlsForwardSecrecyDto.from_dict(tls_forward_secrecy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


