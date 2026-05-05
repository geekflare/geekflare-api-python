# SiteStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]

## Example

```python
from geekflare_api.models.site_status_dto import SiteStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of SiteStatusDto from a JSON string
site_status_dto_instance = SiteStatusDto.from_json(json)
# print the JSON string representation of the object
print(SiteStatusDto.to_json())

# convert the object into a dict
site_status_dto_dict = site_status_dto_instance.to_dict()
# create an instance of SiteStatusDto from a dict
site_status_dto_from_dict = SiteStatusDto.from_dict(site_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


