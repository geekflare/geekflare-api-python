# SentimentAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**aspects** | **List[str]** | Aspects to score individually (aspect-based sentiment). If omitted, only overall sentiment is returned. | [optional] 

## Example

```python
from geekflare_api.models.sentiment_ai_prompt_dto import SentimentAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of SentimentAiPromptDto from a JSON string
sentiment_ai_prompt_dto_instance = SentimentAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(SentimentAiPromptDto.to_json())

# convert the object into a dict
sentiment_ai_prompt_dto_dict = sentiment_ai_prompt_dto_instance.to_dict()
# create an instance of SentimentAiPromptDto from a dict
sentiment_ai_prompt_dto_from_dict = SentimentAiPromptDto.from_dict(sentiment_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


