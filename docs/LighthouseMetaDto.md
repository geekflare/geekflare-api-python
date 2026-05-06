# LighthouseMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type used | 
**follow_redirect** | **bool** | Whether redirects were followed | 
**redirected_url** | **str** | Final URL after redirection (if any) | 
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.lighthouse_meta_dto import LighthouseMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of LighthouseMetaDto from a JSON string
lighthouse_meta_dto_instance = LighthouseMetaDto.from_json(json)
# print the JSON string representation of the object
print(LighthouseMetaDto.to_json())

# convert the object into a dict
lighthouse_meta_dto_dict = lighthouse_meta_dto_instance.to_dict()
# create an instance of LighthouseMetaDto from a dict
lighthouse_meta_dto_from_dict = LighthouseMetaDto.from_dict(lighthouse_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


