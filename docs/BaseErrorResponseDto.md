# BaseErrorResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Error message | 
**details** | **str** | Detailed error information | [optional] 

## Example

```python
from geekflare_api.models.base_error_response_dto import BaseErrorResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseErrorResponseDto from a JSON string
base_error_response_dto_instance = BaseErrorResponseDto.from_json(json)
# print the JSON string representation of the object
print(BaseErrorResponseDto.to_json())

# convert the object into a dict
base_error_response_dto_dict = base_error_response_dto_instance.to_dict()
# create an instance of BaseErrorResponseDto from a dict
base_error_response_dto_from_dict = BaseErrorResponseDto.from_dict(base_error_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


