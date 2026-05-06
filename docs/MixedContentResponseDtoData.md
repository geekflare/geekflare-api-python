# MixedContentResponseDtoData

Contains either an array of all resources (when no mixed content) or an object with insecure/secure arrays (when mixed content found)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure** | **List[str]** | List of insecure (HTTP) resources found on the page | 
**secure** | **List[str]** | List of secure (HTTPS) resources found on the page | 

## Example

```python
from geekflare_api.models.mixed_content_response_dto_data import MixedContentResponseDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of MixedContentResponseDtoData from a JSON string
mixed_content_response_dto_data_instance = MixedContentResponseDtoData.from_json(json)
# print the JSON string representation of the object
print(MixedContentResponseDtoData.to_json())

# convert the object into a dict
mixed_content_response_dto_data_dict = mixed_content_response_dto_data_instance.to_dict()
# create an instance of MixedContentResponseDtoData from a dict
mixed_content_response_dto_data_from_dict = MixedContentResponseDtoData.from_dict(mixed_content_response_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


