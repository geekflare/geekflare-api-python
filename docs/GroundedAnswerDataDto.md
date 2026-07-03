# GroundedAnswerDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | AI-synthesized answer with inline citations | 
**sources** | [**List[GroundedSourceDto]**](GroundedSourceDto.md) | Sources cited in the answer | 

## Example

```python
from geekflare_api.models.grounded_answer_data_dto import GroundedAnswerDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroundedAnswerDataDto from a JSON string
grounded_answer_data_dto_instance = GroundedAnswerDataDto.from_json(json)
# print the JSON string representation of the object
print(GroundedAnswerDataDto.to_json())

# convert the object into a dict
grounded_answer_data_dto_dict = grounded_answer_data_dto_instance.to_dict()
# create an instance of GroundedAnswerDataDto from a dict
grounded_answer_data_dto_from_dict = GroundedAnswerDataDto.from_dict(grounded_answer_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


