# TlsCertificateChainDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Number of certificates in the chain as presented by the server | 
**complete** | **bool** | Whether the chain terminates in a self-signed root (i.e. is not missing an intermediate) | 
**certificates** | [**List[TlsCertificateChainEntryDto]**](TlsCertificateChainEntryDto.md) | Ordered list of certificates from leaf to root | 

## Example

```python
from geekflare_api.models.tls_certificate_chain_dto import TlsCertificateChainDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsCertificateChainDto from a JSON string
tls_certificate_chain_dto_instance = TlsCertificateChainDto.from_json(json)
# print the JSON string representation of the object
print(TlsCertificateChainDto.to_json())

# convert the object into a dict
tls_certificate_chain_dto_dict = tls_certificate_chain_dto_instance.to_dict()
# create an instance of TlsCertificateChainDto from a dict
tls_certificate_chain_dto_from_dict = TlsCertificateChainDto.from_dict(tls_certificate_chain_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


