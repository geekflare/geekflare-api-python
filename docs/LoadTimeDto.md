# LoadTimeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**follow_redirect** | **bool** | Whether to follow redirects when checking site status | [optional] [default to False]
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**target_countries** | **List[str]** | Test the URL from up to 3 additional locations via proxy, alongside the default US server test. Each entry is an ISO alpha-2 country code. When set, the response includes a per-location reachability breakdown instead of a single result. | [optional] 

## Example

```python
from geekflare_api.models.load_time_dto import LoadTimeDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeDto from a JSON string
load_time_dto_instance = LoadTimeDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeDto.to_json())

# convert the object into a dict
load_time_dto_dict = load_time_dto_instance.to_dict()
# create an instance of LoadTimeDto from a dict
load_time_dto_from_dict = LoadTimeDto.from_dict(load_time_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


