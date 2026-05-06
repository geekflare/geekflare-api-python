# DnsMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL that was scraped | 
**types** | **str** | List of DNS record types to query. If omitted, all supported types will be returned. | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.dns_meta_dto import DnsMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of DnsMetaDto from a JSON string
dns_meta_dto_instance = DnsMetaDto.from_json(json)
# print the JSON string representation of the object
print(DnsMetaDto.to_json())

# convert the object into a dict
dns_meta_dto_dict = dns_meta_dto_instance.to_dict()
# create an instance of DnsMetaDto from a dict
dns_meta_dto_from_dict = DnsMetaDto.from_dict(dns_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


