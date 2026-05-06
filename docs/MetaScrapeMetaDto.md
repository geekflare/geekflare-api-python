# MetaScrapeMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The target URL that was scraped | 
**device** | **str** | Device type used | 
**format** | **str** | Output format of the result | 
**file_output** | **bool** | Whether to get response in file format | 
**block_ads** | **bool** | Whether ads were blocked | 
**render_js** | **bool** | Whether JavaScript was rendered | 
**proxy_country** | **str** | Proxy country used, if any | [optional] 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.meta_scrape_meta_dto import MetaScrapeMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetaScrapeMetaDto from a JSON string
meta_scrape_meta_dto_instance = MetaScrapeMetaDto.from_json(json)
# print the JSON string representation of the object
print(MetaScrapeMetaDto.to_json())

# convert the object into a dict
meta_scrape_meta_dto_dict = meta_scrape_meta_dto_instance.to_dict()
# create an instance of MetaScrapeMetaDto from a dict
meta_scrape_meta_dto_from_dict = MetaScrapeMetaDto.from_dict(meta_scrape_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


