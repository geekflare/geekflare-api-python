# DnsSecMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested domain name | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 

## Example

```python
from geekflare_api.models.dns_sec_meta_dto import DnsSecMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecMetaDto from a JSON string
dns_sec_meta_dto_instance = DnsSecMetaDto.from_json(json)
# print the JSON string representation of the object
print(DnsSecMetaDto.to_json())

# convert the object into a dict
dns_sec_meta_dto_dict = dns_sec_meta_dto_instance.to_dict()
# create an instance of DnsSecMetaDto from a dict
dns_sec_meta_dto_from_dict = DnsSecMetaDto.from_dict(dns_sec_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


