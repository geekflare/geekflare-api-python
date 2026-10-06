# SearchSerpDataDtoInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_url** | **str** | Google search URL used | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from geekflare_api.models.search_serp_data_dto_input import SearchSerpDataDtoInput

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSerpDataDtoInput from a JSON string
search_serp_data_dto_input_instance = SearchSerpDataDtoInput.from_json(json)
# print the JSON string representation of the object
print(SearchSerpDataDtoInput.to_json())

# convert the object into a dict
search_serp_data_dto_input_dict = search_serp_data_dto_input_instance.to_dict()
# create an instance of SearchSerpDataDtoInput from a dict
search_serp_data_dto_input_from_dict = SearchSerpDataDtoInput.from_dict(search_serp_data_dto_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


