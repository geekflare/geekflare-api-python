# TlsCertificateIssuerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Issuer country | 
**organization** | **str** | Issuer organization | 
**common_name** | **str** | Issuer common name | 

## Example

```python
from geekflare_api.models.tls_certificate_issuer_dto import TlsCertificateIssuerDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsCertificateIssuerDto from a JSON string
tls_certificate_issuer_dto_instance = TlsCertificateIssuerDto.from_json(json)
# print the JSON string representation of the object
print(TlsCertificateIssuerDto.to_json())

# convert the object into a dict
tls_certificate_issuer_dto_dict = tls_certificate_issuer_dto_instance.to_dict()
# create an instance of TlsCertificateIssuerDto from a dict
tls_certificate_issuer_dto_from_dict = TlsCertificateIssuerDto.from_dict(tls_certificate_issuer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


