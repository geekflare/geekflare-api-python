# PromptAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**query** | **str** | Open-ended question about the page | 

## Example

```python
from geekflare_api.models.prompt_ai_prompt_dto import PromptAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of PromptAiPromptDto from a JSON string
prompt_ai_prompt_dto_instance = PromptAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(PromptAiPromptDto.to_json())

# convert the object into a dict
prompt_ai_prompt_dto_dict = prompt_ai_prompt_dto_instance.to_dict()
# create an instance of PromptAiPromptDto from a dict
prompt_ai_prompt_dto_from_dict = PromptAiPromptDto.from_dict(prompt_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


