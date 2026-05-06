# MixedContentDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]

## Example

```python
from geekflare_api.models.mixed_content_dto import MixedContentDto

# TODO update the JSON string below
json = "{}"
# create an instance of MixedContentDto from a JSON string
mixed_content_dto_instance = MixedContentDto.from_json(json)
# print the JSON string representation of the object
print(MixedContentDto.to_json())

# convert the object into a dict
mixed_content_dto_dict = mixed_content_dto_instance.to_dict()
# create an instance of MixedContentDto from a dict
mixed_content_dto_from_dict = MixedContentDto.from_dict(mixed_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


