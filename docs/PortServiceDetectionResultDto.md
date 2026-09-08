# PortServiceDetectionResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **float** | Port number | 
**state** | **str** | Port state as reported by nmap | 
**service** | [**DetectedServiceDto**](DetectedServiceDto.md) | Detected service details | 

## Example

```python
from geekflare_api.models.port_service_detection_result_dto import PortServiceDetectionResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of PortServiceDetectionResultDto from a JSON string
port_service_detection_result_dto_instance = PortServiceDetectionResultDto.from_json(json)
# print the JSON string representation of the object
print(PortServiceDetectionResultDto.to_json())

# convert the object into a dict
port_service_detection_result_dto_dict = port_service_detection_result_dto_instance.to_dict()
# create an instance of PortServiceDetectionResultDto from a dict
port_service_detection_result_dto_from_dict = PortServiceDetectionResultDto.from_dict(port_service_detection_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


