# Search200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**SearchMetaDto**](SearchMetaDto.md) |  | 
**data** | **object** |  | 

## Example

```python
from geekflare_api.models.search200_response import Search200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Search200Response from a JSON string
search200_response_instance = Search200Response.from_json(json)
# print the JSON string representation of the object
print(Search200Response.to_json())

# convert the object into a dict
search200_response_dict = search200_response_instance.to_dict()
# create an instance of Search200Response from a dict
search200_response_from_dict = Search200Response.from_dict(search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


