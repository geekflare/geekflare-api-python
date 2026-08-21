# LoadTimeMultiLocationMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested URL | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 
**target_countries** | **List[str]** | The full list of locations tested: the default US server plus every requested targetCountries entry | 
**follow_redirect** | **bool** | Indicates if redirects were followed during the test | [optional] 

## Example

```python
from geekflare_api.models.load_time_multi_location_meta_dto import LoadTimeMultiLocationMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeMultiLocationMetaDto from a JSON string
load_time_multi_location_meta_dto_instance = LoadTimeMultiLocationMetaDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeMultiLocationMetaDto.to_json())

# convert the object into a dict
load_time_multi_location_meta_dto_dict = load_time_multi_location_meta_dto_instance.to_dict()
# create an instance of LoadTimeMultiLocationMetaDto from a dict
load_time_multi_location_meta_dto_from_dict = LoadTimeMultiLocationMetaDto.from_dict(load_time_multi_location_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


