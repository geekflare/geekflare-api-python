# BrokenLinkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]

## Example

```python
from geekflare_api.models.broken_link_dto import BrokenLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenLinkDto from a JSON string
broken_link_dto_instance = BrokenLinkDto.from_json(json)
# print the JSON string representation of the object
print(BrokenLinkDto.to_json())

# convert the object into a dict
broken_link_dto_dict = broken_link_dto_instance.to_dict()
# create an instance of BrokenLinkDto from a dict
broken_link_dto_from_dict = BrokenLinkDto.from_dict(broken_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


