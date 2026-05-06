# WebScrapeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type to emulate. Defaults to desktop. | [optional] [default to 'desktop']
**block_ads** | **bool** | Whether to block ads | [optional] [default to True]
**render_js** | **bool** | Whether to render JavaScript | [optional] [default to True]
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**format** | **List[str]** | Format(s) of the scraped result. Comma-separated or array. Defaults to html. | [optional] [default to [html-llm]]
**file_output** | **bool** | Whether to get response in file format | [optional] [default to False]
**stealth** | **bool** | Enable stealth mode to bypass basic bot detection (removes webdriver signals, patches navigator properties) | [optional] [default to False]
**wait_time** | **float** | Seconds to wait after page load before capturing content. Helps bypass lazy-loaded content and bot checks. | [optional] [default to 0]
**extraction_mode** | **str** | Extraction mode (only used if format&#x3D;json) | [optional] [default to 'default']
**extraction_schema** | [**ExtractionSchemaDto**](ExtractionSchemaDto.md) | Extraction schema (optional in default mode, required in css/xpath) | [optional] 

## Example

```python
from geekflare_api.models.web_scrape_dto import WebScrapeDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebScrapeDto from a JSON string
web_scrape_dto_instance = WebScrapeDto.from_json(json)
# print the JSON string representation of the object
print(WebScrapeDto.to_json())

# convert the object into a dict
web_scrape_dto_dict = web_scrape_dto_instance.to_dict()
# create an instance of WebScrapeDto from a dict
web_scrape_dto_from_dict = WebScrapeDto.from_dict(web_scrape_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


