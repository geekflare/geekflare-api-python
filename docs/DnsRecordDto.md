# DnsRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**types** | **List[str]** | List of DNS record types to query. If omitted, all supported types will be returned. | [optional] 

## Example

```python
from geekflare_api.models.dns_record_dto import DnsRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordDto from a JSON string
dns_record_dto_instance = DnsRecordDto.from_json(json)
# print the JSON string representation of the object
print(DnsRecordDto.to_json())

# convert the object into a dict
dns_record_dto_dict = dns_record_dto_instance.to_dict()
# create an instance of DnsRecordDto from a dict
dns_record_dto_from_dict = DnsRecordDto.from_dict(dns_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


