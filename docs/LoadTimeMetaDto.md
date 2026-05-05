# LoadTimeMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested URL | 
**proxy_country** | **str** | Proxy country used for the test | [optional] 
**follow_redirect** | **bool** | Indicates if redirects were followed during the test | [optional] 
**redirected_url** | **str** | Final URL after redirection (if any) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 

## Example

```python
from geekflare_api.models.load_time_meta_dto import LoadTimeMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeMetaDto from a JSON string
load_time_meta_dto_instance = LoadTimeMetaDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeMetaDto.to_json())

# convert the object into a dict
load_time_meta_dto_dict = load_time_meta_dto_instance.to_dict()
# create an instance of LoadTimeMetaDto from a dict
load_time_meta_dto_from_dict = LoadTimeMetaDto.from_dict(load_time_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


