# MtrResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**MtrMetaDto**](MtrMetaDto.md) | Metadata about the MTR test execution | 
**data** | [**List[MtrDataDto]**](MtrDataDto.md) | Array of hop details observed in the MTR trace route | 

## Example

```python
from geekflare_api.models.mtr_response_dto import MtrResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MtrResponseDto from a JSON string
mtr_response_dto_instance = MtrResponseDto.from_json(json)
# print the JSON string representation of the object
print(MtrResponseDto.to_json())

# convert the object into a dict
mtr_response_dto_dict = mtr_response_dto_instance.to_dict()
# create an instance of MtrResponseDto from a dict
mtr_response_dto_from_dict = MtrResponseDto.from_dict(mtr_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


