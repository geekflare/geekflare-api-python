# LoadTime200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Overall summary of reachability across all tested locations | 
**meta** | [**LoadTimeMultiLocationMetaDto**](LoadTimeMultiLocationMetaDto.md) | Metadata about the multi-location test | 
**data** | [**LoadTimeDataDto**](LoadTimeDataDto.md) | Comprehensive site load time metrics | 
**summary** | [**LoadTimeMultiLocationResponseDtoSummary**](LoadTimeMultiLocationResponseDtoSummary.md) |  | 
**locations** | [**List[LoadTimeLocationResultDto]**](LoadTimeLocationResultDto.md) | Per-location test results, including the default US server test | 

## Example

```python
from geekflare_api.models.load_time200_response import LoadTime200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTime200Response from a JSON string
load_time200_response_instance = LoadTime200Response.from_json(json)
# print the JSON string representation of the object
print(LoadTime200Response.to_json())

# convert the object into a dict
load_time200_response_dict = load_time200_response_instance.to_dict()
# create an instance of LoadTime200Response from a dict
load_time200_response_from_dict = LoadTime200Response.from_dict(load_time200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


