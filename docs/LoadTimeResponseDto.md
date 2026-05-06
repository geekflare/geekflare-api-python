# LoadTimeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Overall message about site reachability | [optional] 
**meta** | [**LoadTimeMetaDto**](LoadTimeMetaDto.md) | Metadata about the load time test | 
**data** | [**LoadTimeDataDto**](LoadTimeDataDto.md) | Comprehensive site load time metrics | 

## Example

```python
from geekflare_api.models.load_time_response_dto import LoadTimeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoadTimeResponseDto from a JSON string
load_time_response_dto_instance = LoadTimeResponseDto.from_json(json)
# print the JSON string representation of the object
print(LoadTimeResponseDto.to_json())

# convert the object into a dict
load_time_response_dto_dict = load_time_response_dto_instance.to_dict()
# create an instance of LoadTimeResponseDto from a dict
load_time_response_dto_from_dict = LoadTimeResponseDto.from_dict(load_time_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


