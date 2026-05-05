# OpenPortResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**OpenPortMetaDto**](OpenPortMetaDto.md) | Metadata about the request | 
**data** | **List[float]** | List of open ports found | 

## Example

```python
from geekflare_api.models.open_port_response_dto import OpenPortResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPortResponseDto from a JSON string
open_port_response_dto_instance = OpenPortResponseDto.from_json(json)
# print the JSON string representation of the object
print(OpenPortResponseDto.to_json())

# convert the object into a dict
open_port_response_dto_dict = open_port_response_dto_instance.to_dict()
# create an instance of OpenPortResponseDto from a dict
open_port_response_dto_from_dict = OpenPortResponseDto.from_dict(open_port_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


