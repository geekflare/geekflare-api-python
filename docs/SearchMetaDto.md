# SearchMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Original query | 
**limit** | **float** | Number of results requested | [optional] 
**count** | **float** | Number of results returned | 
**source** | **List[str]** | Search source used | 
**location** | **str** | Country used for ranking | 
**city** | **str** | City used for localized results, if one was requested | [optional] 
**time** | **str** | Time filter applied | 
**category** | **str** | Category filter applied | [optional] 
**include_domains** | **List[str]** | Domains results were restricted to, if any | [optional] 
**exclude_domains** | **List[str]** | Domains excluded from results, if any | [optional] 
**format** | **str** | Output format requested | [optional] 
**scrape** | **bool** | Whether URL scraping was enabled | 
**scrape_limit** | **float** | Number of URLs scraped | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test metadata | 

## Example

```python
from geekflare_api.models.search_meta_dto import SearchMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of SearchMetaDto from a JSON string
search_meta_dto_instance = SearchMetaDto.from_json(json)
# print the JSON string representation of the object
print(SearchMetaDto.to_json())

# convert the object into a dict
search_meta_dto_dict = search_meta_dto_instance.to_dict()
# create an instance of SearchMetaDto from a dict
search_meta_dto_from_dict = SearchMetaDto.from_dict(search_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


