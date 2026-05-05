# MixedContentDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure** | **List[str]** | List of insecure (HTTP) resources found on the page | 
**secure** | **List[str]** | List of secure (HTTPS) resources found on the page | 

## Example

```python
from geekflare_api.models.mixed_content_data_dto import MixedContentDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of MixedContentDataDto from a JSON string
mixed_content_data_dto_instance = MixedContentDataDto.from_json(json)
# print the JSON string representation of the object
print(MixedContentDataDto.to_json())

# convert the object into a dict
mixed_content_data_dto_dict = mixed_content_data_dto_instance.to_dict()
# create an instance of MixedContentDataDto from a dict
mixed_content_data_dto_from_dict = MixedContentDataDto.from_dict(mixed_content_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


