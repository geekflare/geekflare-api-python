# TlsScanDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 

## Example

```python
from geekflare_api.models.tls_scan_dto import TlsScanDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsScanDto from a JSON string
tls_scan_dto_instance = TlsScanDto.from_json(json)
# print the JSON string representation of the object
print(TlsScanDto.to_json())

# convert the object into a dict
tls_scan_dto_dict = tls_scan_dto_instance.to_dict()
# create an instance of TlsScanDto from a dict
tls_scan_dto_from_dict = TlsScanDto.from_dict(tls_scan_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


