# TlsCertificateChainEntryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common name of this certificate in the chain | 
**issuer_common_name** | **str** | Common name of this certificate&#39;s issuer | 
**fingerprint** | **str** | SHA-1 fingerprint of this certificate | 

## Example

```python
from geekflare_api.models.tls_certificate_chain_entry_dto import TlsCertificateChainEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsCertificateChainEntryDto from a JSON string
tls_certificate_chain_entry_dto_instance = TlsCertificateChainEntryDto.from_json(json)
# print the JSON string representation of the object
print(TlsCertificateChainEntryDto.to_json())

# convert the object into a dict
tls_certificate_chain_entry_dto_dict = tls_certificate_chain_entry_dto_instance.to_dict()
# create an instance of TlsCertificateChainEntryDto from a dict
tls_certificate_chain_entry_dto_from_dict = TlsCertificateChainEntryDto.from_dict(tls_certificate_chain_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


