# MetaScrapeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**MetaScrapeMetaDto**](MetaScrapeMetaDto.md) | Metadata about the request | 
**data** | [**MetaScrapeResponseDtoData**](MetaScrapeResponseDtoData.md) |  | 

## Example

```python
from geekflare_api.models.meta_scrape_response_dto import MetaScrapeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetaScrapeResponseDto from a JSON string
meta_scrape_response_dto_instance = MetaScrapeResponseDto.from_json(json)
# print the JSON string representation of the object
print(MetaScrapeResponseDto.to_json())

# convert the object into a dict
meta_scrape_response_dto_dict = meta_scrape_response_dto_instance.to_dict()
# create an instance of MetaScrapeResponseDto from a dict
meta_scrape_response_dto_from_dict = MetaScrapeResponseDto.from_dict(meta_scrape_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


