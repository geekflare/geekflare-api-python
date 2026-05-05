# TlsScanMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL checked for TLS support | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test metadata object | 

## Example

```python
from geekflare_api.models.tls_scan_meta_dto import TlsScanMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsScanMetaDto from a JSON string
tls_scan_meta_dto_instance = TlsScanMetaDto.from_json(json)
# print the JSON string representation of the object
print(TlsScanMetaDto.to_json())

# convert the object into a dict
tls_scan_meta_dto_dict = tls_scan_meta_dto_instance.to_dict()
# create an instance of TlsScanMetaDto from a dict
tls_scan_meta_dto_from_dict = TlsScanMetaDto.from_dict(tls_scan_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


