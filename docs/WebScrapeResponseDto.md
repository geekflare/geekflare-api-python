# WebScrapeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**WebScrapeMetaDto**](WebScrapeMetaDto.md) | Metadata about the request | 
**data** | [**MetaScrapeResponseDtoData**](MetaScrapeResponseDtoData.md) |  | 

## Example

```python
from geekflare_api.models.web_scrape_response_dto import WebScrapeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebScrapeResponseDto from a JSON string
web_scrape_response_dto_instance = WebScrapeResponseDto.from_json(json)
# print the JSON string representation of the object
print(WebScrapeResponseDto.to_json())

# convert the object into a dict
web_scrape_response_dto_dict = web_scrape_response_dto_instance.to_dict()
# create an instance of WebScrapeResponseDto from a dict
web_scrape_response_dto_from_dict = WebScrapeResponseDto.from_dict(web_scrape_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


