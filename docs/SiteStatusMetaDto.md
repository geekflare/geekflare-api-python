# SiteStatusMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL checked | 
**follow_redirect** | **bool** | Whether redirects were followed | 
**redirected_url** | **object** | Final redirected URL (if applicable) | [optional] 
**proxy_country** | **str** | Proxy country used (if any) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.site_status_meta_dto import SiteStatusMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of SiteStatusMetaDto from a JSON string
site_status_meta_dto_instance = SiteStatusMetaDto.from_json(json)
# print the JSON string representation of the object
print(SiteStatusMetaDto.to_json())

# convert the object into a dict
site_status_meta_dto_dict = site_status_meta_dto_instance.to_dict()
# create an instance of SiteStatusMetaDto from a dict
site_status_meta_dto_from_dict = SiteStatusMetaDto.from_dict(site_status_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


