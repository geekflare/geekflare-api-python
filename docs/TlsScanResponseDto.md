# TlsScanResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**TlsScanMetaDto**](TlsScanMetaDto.md) | Metadata about the TLS scan request | 
**data** | [**TlsScanDataDto**](TlsScanDataDto.md) | TLS scan result data | 

## Example

```python
from geekflare_api.models.tls_scan_response_dto import TlsScanResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TlsScanResponseDto from a JSON string
tls_scan_response_dto_instance = TlsScanResponseDto.from_json(json)
# print the JSON string representation of the object
print(TlsScanResponseDto.to_json())

# convert the object into a dict
tls_scan_response_dto_dict = tls_scan_response_dto_instance.to_dict()
# create an instance of TlsScanResponseDto from a dict
tls_scan_response_dto_from_dict = TlsScanResponseDto.from_dict(tls_scan_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


