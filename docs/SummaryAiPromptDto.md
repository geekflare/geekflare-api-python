# SummaryAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**style** | **str** | Summary style | [optional] [default to 'paragraph']
**focus** | **str** | Only summarize the parts of the content relevant to this focus area | [optional] 
**max_length** | **float** | Sentence count (paragraph/tldr) or bullet count (bullets) | [optional] [default to 5]

## Example

```python
from geekflare_api.models.summary_ai_prompt_dto import SummaryAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryAiPromptDto from a JSON string
summary_ai_prompt_dto_instance = SummaryAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(SummaryAiPromptDto.to_json())

# convert the object into a dict
summary_ai_prompt_dto_dict = summary_ai_prompt_dto_instance.to_dict()
# create an instance of SummaryAiPromptDto from a dict
summary_ai_prompt_dto_from_dict = SummaryAiPromptDto.from_dict(summary_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


