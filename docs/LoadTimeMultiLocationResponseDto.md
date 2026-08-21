# LoadTimeMultiLocationResponseDto

Returned instead of LoadTimeResponseDto when `targetCountries` is set on the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Overall summary of reachability across all tested locations | 
**meta** | [**LoadTimeMultiLocationMetaDto**](LoadTimeMultiLocationMetaDto.md) | Metadata about the multi-location test | 
**summary** | [**LoadTimeMultiLocationResponseDtoSummary**](LoadTimeMultiLocationResponseDtoSummary.md) |  | 
**locations** | [**List[LoadTimeLocationResultDto]**](LoadTimeLocationResultDto.md) | Per-location test results, including the default US server test | 

## Example

```python
from geekflare_api.models.load_time_multi_location_response_dto import LoadTimeMultiLocationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeMultiLocationResponseDto from a JSON string
load_time_multi_location_response_dto_instance = LoadTimeMultiLocationResponseDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeMultiLocationResponseDto.to_json())

# convert the object into a dict
load_time_multi_location_response_dto_dict = load_time_multi_location_response_dto_instance.to_dict()
# create an instance of LoadTimeMultiLocationResponseDto from a dict
load_time_multi_location_response_dto_from_dict = LoadTimeMultiLocationResponseDto.from_dict(load_time_multi_location_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


