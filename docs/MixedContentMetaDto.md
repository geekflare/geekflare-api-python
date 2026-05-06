# MixedContentMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested URL | 
**proxy_country** | **str** | Country used for proxy | [optional] 
**follow_redirect** | **bool** | Indicates if redirects should be followed | [optional] 
**redirected_url** | **str** | Final URL after redirection (if any) | [optional] 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 

## Example

```python
from geekflare_api.models.mixed_content_meta_dto import MixedContentMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of MixedContentMetaDto from a JSON string
mixed_content_meta_dto_instance = MixedContentMetaDto.from_json(json)
# print the JSON string representation of the object
print(MixedContentMetaDto.to_json())

# convert the object into a dict
mixed_content_meta_dto_dict = mixed_content_meta_dto_instance.to_dict()
# create an instance of MixedContentMetaDto from a dict
mixed_content_meta_dto_from_dict = MixedContentMetaDto.from_dict(mixed_content_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


