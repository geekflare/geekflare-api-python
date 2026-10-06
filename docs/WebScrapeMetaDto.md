# WebScrapeMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL that was scraped | 
**device** | **str** | Device type used | 
**format** | **List[str]** | Output format(s) of the result | 
**file_output** | **bool** | Whether to get response in file format | 
**block_ads** | **bool** | Whether ads were blocked | 
**render_js** | **bool** | Whether JavaScript was rendered for this request (resolved automatically unless explicitly set) | 
**stealth** | **bool** | Whether stealth mode was enabled | 
**proxy_mode** | **str** | Proxy mode requested for this request, echoed as a string (\&quot;false\&quot;, \&quot;auto\&quot;, or \&quot;true\&quot;) | 
**proxy_used** | **bool** | Whether a proxy was actually used for this request. When proxyMode is &#x60;auto&#x60;, this depends on whether the site blocked the initial request. | 
**wait_time** | **float** | Seconds to wait after page load before capturing content. Helps bypass lazy-loaded content and bot checks. | [default to 0]
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**extraction_mode** | **str** | Extraction mode used for this request. When an extraction mode is requested, the result is returned as JSON. | 
**template** | **str** | Extraction template used, if extractionMode was &#x60;template&#x60; | [optional] 
**extraction_schema** | [**ExtractionSchemaDto**](ExtractionSchemaDto.md) | Extraction schema (optional in default mode, required in css/xpath) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 
**ai_prompt_type** | **str** | The aiPrompt.type used for this request, if any | [optional] 

## Example

```python
from geekflare_api.models.web_scrape_meta_dto import WebScrapeMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebScrapeMetaDto from a JSON string
web_scrape_meta_dto_instance = WebScrapeMetaDto.from_json(json)
# print the JSON string representation of the object
print(WebScrapeMetaDto.to_json())

# convert the object into a dict
web_scrape_meta_dto_dict = web_scrape_meta_dto_instance.to_dict()
# create an instance of WebScrapeMetaDto from a dict
web_scrape_meta_dto_from_dict = WebScrapeMetaDto.from_dict(web_scrape_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


