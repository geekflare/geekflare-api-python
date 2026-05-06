# TlsScanDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocols** | [**TlsProtocolsDto**](TlsProtocolsDto.md) | Protocols supported | 
**certificate** | [**TlsCertificateDto**](TlsCertificateDto.md) | Certificate details | 

## Example

```python
from geekflare_api.models.tls_scan_data_dto import TlsScanDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsScanDataDto from a JSON string
tls_scan_data_dto_instance = TlsScanDataDto.from_json(json)
# print the JSON string representation of the object
print(TlsScanDataDto.to_json())

# convert the object into a dict
tls_scan_data_dto_dict = tls_scan_data_dto_instance.to_dict()
# create an instance of TlsScanDataDto from a dict
tls_scan_data_dto_from_dict = TlsScanDataDto.from_dict(tls_scan_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


