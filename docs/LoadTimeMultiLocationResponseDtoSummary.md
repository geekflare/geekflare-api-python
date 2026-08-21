# LoadTimeMultiLocationResponseDtoSummary

Locations grouped by reachability outcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reachable** | **List[str]** | Locations from which the site was reachable | [optional] 

## Example

```python
from geekflare_api.models.load_time_multi_location_response_dto_summary import LoadTimeMultiLocationResponseDtoSummary

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeMultiLocationResponseDtoSummary from a JSON string
load_time_multi_location_response_dto_summary_instance = LoadTimeMultiLocationResponseDtoSummary.from_json(json)
# print the JSON string representation of the object
print(LoadTimeMultiLocationResponseDtoSummary.to_json())

# convert the object into a dict
load_time_multi_location_response_dto_summary_dict = load_time_multi_location_response_dto_summary_instance.to_dict()
# create an instance of LoadTimeMultiLocationResponseDtoSummary from a dict
load_time_multi_location_response_dto_summary_from_dict = LoadTimeMultiLocationResponseDtoSummary.from_dict(load_time_multi_location_response_dto_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


