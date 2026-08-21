# SchemaAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**var_schema** | **object** | JSON Schema-like object describing fields to extract | 

## Example

```python
from geekflare_api.models.schema_ai_prompt_dto import SchemaAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAiPromptDto from a JSON string
schema_ai_prompt_dto_instance = SchemaAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(SchemaAiPromptDto.to_json())

# convert the object into a dict
schema_ai_prompt_dto_dict = schema_ai_prompt_dto_instance.to_dict()
# create an instance of SchemaAiPromptDto from a dict
schema_ai_prompt_dto_from_dict = SchemaAiPromptDto.from_dict(schema_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


