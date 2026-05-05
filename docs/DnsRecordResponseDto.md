# DnsRecordResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**DnsMetaDto**](DnsMetaDto.md) | Metadata about the request. | 
**data** | **object** | DNS records grouped by type. | 

## Example

```python
from geekflare_api.models.dns_record_response_dto import DnsRecordResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordResponseDto from a JSON string
dns_record_response_dto_instance = DnsRecordResponseDto.from_json(json)
# print the JSON string representation of the object
print(DnsRecordResponseDto.to_json())

# convert the object into a dict
dns_record_response_dto_dict = dns_record_response_dto_instance.to_dict()
# create an instance of DnsRecordResponseDto from a dict
dns_record_response_dto_from_dict = DnsRecordResponseDto.from_dict(dns_record_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


