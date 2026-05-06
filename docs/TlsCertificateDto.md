# TlsCertificateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common name (CN) on the certificate | 
**subject_alt_name** | **str** | Subject Alternative Names (SAN) | 
**issuer** | [**TlsCertificateIssuerDto**](TlsCertificateIssuerDto.md) | Issuer details | 
**expiry** | **str** | Certificate expiry date | 

## Example

```python
from geekflare_api.models.tls_certificate_dto import TlsCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsCertificateDto from a JSON string
tls_certificate_dto_instance = TlsCertificateDto.from_json(json)
# print the JSON string representation of the object
print(TlsCertificateDto.to_json())

# convert the object into a dict
tls_certificate_dto_dict = tls_certificate_dto_instance.to_dict()
# create an instance of TlsCertificateDto from a dict
tls_certificate_dto_from_dict = TlsCertificateDto.from_dict(tls_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


