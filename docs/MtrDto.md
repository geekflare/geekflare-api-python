# MtrDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]

## Example

```python
from geekflare_api.models.mtr_dto import MtrDto

# TODO update the JSON string below
json = "{}"
# create an instance of MtrDto from a JSON string
mtr_dto_instance = MtrDto.from_json(json)
# print the JSON string representation of the object
print(MtrDto.to_json())

# convert the object into a dict
mtr_dto_dict = mtr_dto_instance.to_dict()
# create an instance of MtrDto from a dict
mtr_dto_from_dict = MtrDto.from_dict(mtr_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


