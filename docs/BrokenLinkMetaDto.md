# BrokenLinkMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL checked for broken links | 
**proxy_country** | **str** | Proxy country used for this request | 
**follow_redirect** | **bool** | Whether redirection was followed | 
**redirected_url** | **str** | Final URL after redirection (if any) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.broken_link_meta_dto import BrokenLinkMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenLinkMetaDto from a JSON string
broken_link_meta_dto_instance = BrokenLinkMetaDto.from_json(json)
# print the JSON string representation of the object
print(BrokenLinkMetaDto.to_json())

# convert the object into a dict
broken_link_meta_dto_dict = broken_link_meta_dto_instance.to_dict()
# create an instance of BrokenLinkMetaDto from a dict
broken_link_meta_dto_from_dict = BrokenLinkMetaDto.from_dict(broken_link_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


