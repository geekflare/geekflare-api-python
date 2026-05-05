# LighthouseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type to emulate. Defaults to desktop. | [optional] [default to 'desktop']
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**parameters** | **List[str]** | Extra Lighthouse CLI parameters | [optional] 

## Example

```python
from geekflare_api.models.lighthouse_dto import LighthouseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LighthouseDto from a JSON string
lighthouse_dto_instance = LighthouseDto.from_json(json)
# print the JSON string representation of the object
print(LighthouseDto.to_json())

# convert the object into a dict
lighthouse_dto_dict = lighthouse_dto_instance.to_dict()
# create an instance of LighthouseDto from a dict
lighthouse_dto_from_dict = LighthouseDto.from_dict(lighthouse_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


