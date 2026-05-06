# ExtractionSchemaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name/Label for this extraction schema | 
**base_selector** | **str** | Base selector for scoping extraction (css/xpath only) | [optional] 
**fields** | [**List[ExtractionSchemaDtoFieldsInner]**](ExtractionSchemaDtoFieldsInner.md) | List of fields to extract | 

## Example

```python
from geekflare_api.models.extraction_schema_dto import ExtractionSchemaDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionSchemaDto from a JSON string
extraction_schema_dto_instance = ExtractionSchemaDto.from_json(json)
# print the JSON string representation of the object
print(ExtractionSchemaDto.to_json())

# convert the object into a dict
extraction_schema_dto_dict = extraction_schema_dto_instance.to_dict()
# create an instance of ExtractionSchemaDto from a dict
extraction_schema_dto_from_dict = ExtractionSchemaDto.from_dict(extraction_schema_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


