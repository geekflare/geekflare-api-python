# GroundedAnswerResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) |  | 
**data** | [**GroundedAnswerDataDto**](GroundedAnswerDataDto.md) |  | 

## Example

```python
from geekflare_api.models.grounded_answer_response_dto import GroundedAnswerResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroundedAnswerResponseDto from a JSON string
grounded_answer_response_dto_instance = GroundedAnswerResponseDto.from_json(json)
# print the JSON string representation of the object
print(GroundedAnswerResponseDto.to_json())

# convert the object into a dict
grounded_answer_response_dto_dict = grounded_answer_response_dto_instance.to_dict()
# create an instance of GroundedAnswerResponseDto from a dict
grounded_answer_response_dto_from_dict = GroundedAnswerResponseDto.from_dict(grounded_answer_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


