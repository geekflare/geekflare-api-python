# DetectedServiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Service name (e.g. \&quot;ssh\&quot;, \&quot;http\&quot;) | [optional] 
**product** | **object** | Product name (e.g. \&quot;OpenSSH\&quot;) | [optional] 
**version** | **object** | Product version string | [optional] 
**extra_info** | **object** | Additional context nmap reports alongside the match | [optional] 
**os_type** | **object** | Inferred OS family, if determinable | [optional] 

## Example

```python
from geekflare_api.models.detected_service_dto import DetectedServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of DetectedServiceDto from a JSON string
detected_service_dto_instance = DetectedServiceDto.from_json(json)
# print the JSON string representation of the object
print(DetectedServiceDto.to_json())

# convert the object into a dict
detected_service_dto_dict = detected_service_dto_instance.to_dict()
# create an instance of DetectedServiceDto from a dict
detected_service_dto_from_dict = DetectedServiceDto.from_dict(detected_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


