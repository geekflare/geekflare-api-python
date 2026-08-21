# WebScrapeDtoAiPrompt

Ask AI to extract or analyze the scraped page. Always runs against the Markdown of the page regardless of the format field. Adds +6 credits on top of the base scraping cost.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | AI extraction mode | 
**query** | **str** | Open-ended question about the page | 
**var_schema** | **object** | JSON Schema-like object describing fields to extract | 
**item_schema** | **object** | JSON Schema-like object describing each item to extract from a listing/category page | 
**max_items** | **float** | Maximum number of items to extract | [optional] [default to 20]
**style** | **str** | Summary style | [optional] [default to 'paragraph']
**focus** | **str** | Only summarize the parts of the content relevant to this focus area | [optional] 
**max_length** | **float** | Sentence count (paragraph/tldr) or bullet count (bullets) | [optional] [default to 5]
**aspects** | **List[str]** | Aspects to score individually (aspect-based sentiment). If omitted, only overall sentiment is returned. | [optional] 
**max_keywords** | **float** | Maximum number of keywords to return | [optional] [default to 10]
**include_entities** | **bool** | Also extract named entities (organizations, people, dates, laws, locations) | [optional] [default to False]

## Example

```python
from geekflare_api.models.web_scrape_dto_ai_prompt import WebScrapeDtoAiPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of WebScrapeDtoAiPrompt from a JSON string
web_scrape_dto_ai_prompt_instance = WebScrapeDtoAiPrompt.from_json(json)
# print the JSON string representation of the object
print(WebScrapeDtoAiPrompt.to_json())

# convert the object into a dict
web_scrape_dto_ai_prompt_dict = web_scrape_dto_ai_prompt_instance.to_dict()
# create an instance of WebScrapeDtoAiPrompt from a dict
web_scrape_dto_ai_prompt_from_dict = WebScrapeDtoAiPrompt.from_dict(web_scrape_dto_ai_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


