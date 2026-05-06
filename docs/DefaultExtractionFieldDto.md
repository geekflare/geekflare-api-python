# DefaultExtractionFieldDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title/key of the extracted field | 
**value** | **object** | Static value to assign to this field | 

## Example

```python
from geekflare_api.models.default_extraction_field_dto import DefaultExtractionFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultExtractionFieldDto from a JSON string
default_extraction_field_dto_instance = DefaultExtractionFieldDto.from_json(json)
# print the JSON string representation of the object
print(DefaultExtractionFieldDto.to_json())

# convert the object into a dict
default_extraction_field_dto_dict = default_extraction_field_dto_instance.to_dict()
# create an instance of DefaultExtractionFieldDto from a dict
default_extraction_field_dto_from_dict = DefaultExtractionFieldDto.from_dict(default_extraction_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


