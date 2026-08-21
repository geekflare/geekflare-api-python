# KeywordsAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**max_keywords** | **float** | Maximum number of keywords to return | [optional] [default to 10]
**include_entities** | **bool** | Also extract named entities (organizations, people, dates, laws, locations) | [optional] [default to False]

## Example

```python
from geekflare_api.models.keywords_ai_prompt_dto import KeywordsAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsAiPromptDto from a JSON string
keywords_ai_prompt_dto_instance = KeywordsAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(KeywordsAiPromptDto.to_json())

# convert the object into a dict
keywords_ai_prompt_dto_dict = keywords_ai_prompt_dto_instance.to_dict()
# create an instance of KeywordsAiPromptDto from a dict
keywords_ai_prompt_dto_from_dict = KeywordsAiPromptDto.from_dict(keywords_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


