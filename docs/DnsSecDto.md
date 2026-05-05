# DnsSecDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 

## Example

```python
from geekflare_api.models.dns_sec_dto import DnsSecDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecDto from a JSON string
dns_sec_dto_instance = DnsSecDto.from_json(json)
# print the JSON string representation of the object
print(DnsSecDto.to_json())

# convert the object into a dict
dns_sec_dto_dict = dns_sec_dto_instance.to_dict()
# create an instance of DnsSecDto from a dict
dns_sec_dto_from_dict = DnsSecDto.from_dict(dns_sec_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


