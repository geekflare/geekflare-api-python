# ListingAiPromptDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**item_schema** | **object** | JSON Schema-like object describing each item to extract from a listing/category page | 
**max_items** | **float** | Maximum number of items to extract | [optional] [default to 20]

## Example

```python
from geekflare_api.models.listing_ai_prompt_dto import ListingAiPromptDto

# TODO update the JSON string below
json = "{}"
# create an instance of ListingAiPromptDto from a JSON string
listing_ai_prompt_dto_instance = ListingAiPromptDto.from_json(json)
# print the JSON string representation of the object
print(ListingAiPromptDto.to_json())

# convert the object into a dict
listing_ai_prompt_dto_dict = listing_ai_prompt_dto_instance.to_dict()
# create an instance of ListingAiPromptDto from a dict
listing_ai_prompt_dto_from_dict = ListingAiPromptDto.from_dict(listing_ai_prompt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


