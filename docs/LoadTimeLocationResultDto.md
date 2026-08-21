# LoadTimeLocationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | ISO alpha-2 country code for this test location | 
**country_name** | **str** | Full country name for this test location | 
**status** | **str** | Whether the site was reachable from this location | 
**data** | **Dict[str, object]** | Load time metrics for this location, same structure as the single-location &#x60;data&#x60; object | 

## Example

```python
from geekflare_api.models.load_time_location_result_dto import LoadTimeLocationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeLocationResultDto from a JSON string
load_time_location_result_dto_instance = LoadTimeLocationResultDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeLocationResultDto.to_json())

# convert the object into a dict
load_time_location_result_dto_dict = load_time_location_result_dto_instance.to_dict()
# create an instance of LoadTimeLocationResultDto from a dict
load_time_location_result_dto_from_dict = LoadTimeLocationResultDto.from_dict(load_time_location_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


