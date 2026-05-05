# SiteStatusResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Indicates the current status of the site. It can either be \&quot;Site is up\&quot; or \&quot;Unable to reach the URL.\&quot; | 
**meta** | [**SiteStatusMetaDto**](SiteStatusMetaDto.md) | Metadata about the site status check. | 
**data** | **object** | HTTP status information from the site check. | 

## Example

```python
from geekflare_api.models.site_status_response_dto import SiteStatusResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SiteStatusResponseDto from a JSON string
site_status_response_dto_instance = SiteStatusResponseDto.from_json(json)
# print the JSON string representation of the object
print(SiteStatusResponseDto.to_json())

# convert the object into a dict
site_status_response_dto_dict = site_status_response_dto_instance.to_dict()
# create an instance of SiteStatusResponseDto from a dict
site_status_response_dto_from_dict = SiteStatusResponseDto.from_dict(site_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


