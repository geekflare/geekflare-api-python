# TlsCertificateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common name (CN) on the certificate | 
**subject_alt_name** | **str** | Subject Alternative Names (SAN) | 
**issuer** | [**TlsCertificateIssuerDto**](TlsCertificateIssuerDto.md) | Issuer details | 
**expiry** | **str** | Certificate expiry date | 
**valid_from** | **str** | Certificate valid-from date | 
**is_expired** | **bool** | Whether the certificate has expired | 
**is_not_yet_valid** | **bool** | Whether the certificate is not yet valid | 
**hostname_matches** | **bool** | Whether the requested hostname matches the certificate (CN/SAN) | 
**self_signed** | **bool** | Whether the leaf certificate is self-signed | 
**key_bits** | **object** | Public key size in bits, null if not an RSA key | 
**weak_key** | **object** | Whether the key size is considered weak (RSA &lt; 2048 bits), null if not applicable | 
**weak_signature_algorithm** | **object** | Whether the certificate uses a weak signature algorithm (SHA-1/MD5); heuristic OID scan, null if undeterminable | 
**chain** | [**TlsCertificateChainDto**](TlsCertificateChainDto.md) | Certificate chain analysis | 
**forward_secrecy** | [**TlsForwardSecrecyDto**](TlsForwardSecrecyDto.md) | Forward secrecy signal from the negotiated handshake | 
**trusted** | **bool** | Whether the chain validates against Node/OpenSSL&#39;s built-in trust store | 
**authorization_error** | **object** | Node TLS authorization error code/message if not trusted, null otherwise | 

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


