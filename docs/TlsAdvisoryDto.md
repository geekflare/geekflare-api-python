# TlsAdvisoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breach** | **object** | BREACH is an HTTP-layer attack, not a TLS property — this is advisory only, not a vulnerability verdict | 
**secure_renegotiation** | **object** | Secure renegotiation (RFC 5746) support signal — absence does not necessarily mean vulnerable | 
**ocsp_stapling** | **object** | Whether the server stapled an OCSP response during the handshake | 

## Example

```python
from geekflare_api.models.tls_advisory_dto import TlsAdvisoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsAdvisoryDto from a JSON string
tls_advisory_dto_instance = TlsAdvisoryDto.from_json(json)
# print the JSON string representation of the object
print(TlsAdvisoryDto.to_json())

# convert the object into a dict
tls_advisory_dto_dict = tls_advisory_dto_instance.to_dict()
# create an instance of TlsAdvisoryDto from a dict
tls_advisory_dto_from_dict = TlsAdvisoryDto.from_dict(tls_advisory_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


