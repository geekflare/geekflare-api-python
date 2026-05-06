# DnsSecResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**DnsSecMetaDto**](DnsSecMetaDto.md) | Metadata about the DNSSEC test | 
**data** | [**DnsSecDataDto**](DnsSecDataDto.md) | DNSSEC test result data | 

## Example

```python
from geekflare_api.models.dns_sec_response_dto import DnsSecResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecResponseDto from a JSON string
dns_sec_response_dto_instance = DnsSecResponseDto.from_json(json)
# print the JSON string representation of the object
print(DnsSecResponseDto.to_json())

# convert the object into a dict
dns_sec_response_dto_dict = dns_sec_response_dto_instance.to_dict()
# create an instance of DnsSecResponseDto from a dict
dns_sec_response_dto_from_dict = DnsSecResponseDto.from_dict(dns_sec_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


