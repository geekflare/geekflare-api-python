# TlsVulnerabilitiesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poodle** | **object** | POODLE (SSLv3 padding oracle) exposure and TLS_FALLBACK_SCSV support | 
**drown** | **object** | DROWN exposure, simplified to SSLv2 support (full check requires cross-server key reuse analysis) | 
**freak** | **object** | FREAK — whether the server accepts EXPORT-grade RSA cipher suites | 
**logjam** | **object** | LOGJAM — whether the server negotiates a DHE group under 1024 bits | 
**sweet32** | **object** | SWEET32 — whether the server negotiates 3DES/64-bit block ciphers | 
**rc4** | **object** | Whether the server accepts RC4 cipher suites | 
**null_cipher** | **object** | Whether the server accepts NULL-encryption cipher suites | 
**anonymous_cipher** | **object** | Whether the server accepts anonymous (unauthenticated) cipher suites | 
**crime** | **object** | CRIME — whether the server accepts TLS-level (DEFLATE) compression | 

## Example

```python
from geekflare_api.models.tls_vulnerabilities_dto import TlsVulnerabilitiesDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsVulnerabilitiesDto from a JSON string
tls_vulnerabilities_dto_instance = TlsVulnerabilitiesDto.from_json(json)
# print the JSON string representation of the object
print(TlsVulnerabilitiesDto.to_json())

# convert the object into a dict
tls_vulnerabilities_dto_dict = tls_vulnerabilities_dto_instance.to_dict()
# create an instance of TlsVulnerabilitiesDto from a dict
tls_vulnerabilities_dto_from_dict = TlsVulnerabilitiesDto.from_dict(tls_vulnerabilities_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


