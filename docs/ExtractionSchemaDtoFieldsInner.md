# ExtractionSchemaDtoFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title/key of the extracted field | 
**value** | **object** | Static value to assign to this field | 
**name** | **str** | Field name in the extracted JSON | 
**selector** | **str** | Selector or XPath to extract value | 
**type** | **str** | Type of data to extract | 
**attribute** | **str** | If type&#x3D;attr, specify attribute name | [optional] 
**fields** | [**List[SelectorExtractionFieldDto]**](SelectorExtractionFieldDto.md) | Nested fields | [optional] 

## Example

```python
from geekflare_api.models.extraction_schema_dto_fields_inner import ExtractionSchemaDtoFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionSchemaDtoFieldsInner from a JSON string
extraction_schema_dto_fields_inner_instance = ExtractionSchemaDtoFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ExtractionSchemaDtoFieldsInner.to_json())

# convert the object into a dict
extraction_schema_dto_fields_inner_dict = extraction_schema_dto_fields_inner_instance.to_dict()
# create an instance of ExtractionSchemaDtoFieldsInner from a dict
extraction_schema_dto_fields_inner_from_dict = ExtractionSchemaDtoFieldsInner.from_dict(extraction_schema_dto_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


