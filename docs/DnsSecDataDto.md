# DnsSecDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates if DNSSEC is enabled for the domain | 
**dnskey** | **List[str]** | List of DNSKEY records if DNSSEC is enabled | [optional] 
**rrsig** | **List[str]** | List of RRSIG records if DNSSEC is enabled | [optional] 

## Example

```python
from geekflare_api.models.dns_sec_data_dto import DnsSecDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecDataDto from a JSON string
dns_sec_data_dto_instance = DnsSecDataDto.from_json(json)
# print the JSON string representation of the object
print(DnsSecDataDto.to_json())

# convert the object into a dict
dns_sec_data_dto_dict = dns_sec_data_dto_instance.to_dict()
# create an instance of DnsSecDataDto from a dict
dns_sec_data_dto_from_dict = DnsSecDataDto.from_dict(dns_sec_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


