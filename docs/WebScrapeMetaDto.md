# WebScrapeMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL that was scraped | 
**device** | **str** | Device type used | 
**format** | **List[str]** | Output format(s) of the result | 
**file_output** | **bool** | Whether to get response in file format | 
**block_ads** | **bool** | Whether ads were blocked | 
**render_js** | **bool** | Whether JavaScript was rendered | 
**stealth** | **bool** | Whether stealth mode was enabled | 
**wait_time** | **float** | Seconds to wait after page load before capturing content. Helps bypass lazy-loaded content and bot checks. | [default to 0]
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**extraction_mode** | **str** | Extraction mode (only used if format&#x3D;json) | 
**extraction_schema** | [**ExtractionSchemaDto**](ExtractionSchemaDto.md) | Extraction schema (optional in default mode, required in css/xpath) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

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


