# MetaScrapeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**device** | **str** | Device type to emulate. Defaults to desktop. | [optional] [default to 'desktop']
**block_ads** | **bool** | Whether to block ads | [optional] [default to True]
**render_js** | **bool** | Whether to render JavaScript | [optional] [default to True]
**proxy_country** | **str** | Proxy country code to route the request | [optional] 
**format** | **str** | Format of the scraped result. Defaults to html. | [optional] [default to 'json']
**file_output** | **bool** | Whether to get response in file format | [optional] [default to False]

## Example

```python
from geekflare_api.models.meta_scrape_dto import MetaScrapeDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetaScrapeDto from a JSON string
meta_scrape_dto_instance = MetaScrapeDto.from_json(json)
# print the JSON string representation of the object
print(MetaScrapeDto.to_json())

# convert the object into a dict
meta_scrape_dto_dict = meta_scrape_dto_instance.to_dict()
# create an instance of MetaScrapeDto from a dict
meta_scrape_dto_from_dict = MetaScrapeDto.from_dict(meta_scrape_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


