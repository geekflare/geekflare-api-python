# SelectorExtractionFieldDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name in the extracted JSON | 
**selector** | **str** | Selector or XPath to extract value | 
**type** | **str** | Type of data to extract | 
**attribute** | **str** | If type&#x3D;attr, specify attribute name | [optional] 
**fields** | [**List[SelectorExtractionFieldDto]**](SelectorExtractionFieldDto.md) | Nested fields | [optional] 

## Example

```python
from geekflare_api.models.selector_extraction_field_dto import SelectorExtractionFieldDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectorExtractionFieldDto from a JSON string
selector_extraction_field_dto_instance = SelectorExtractionFieldDto.from_json(json)
# print the JSON string representation of the object
print(SelectorExtractionFieldDto.to_json())

# convert the object into a dict
selector_extraction_field_dto_dict = selector_extraction_field_dto_instance.to_dict()
# create an instance of SelectorExtractionFieldDto from a dict
selector_extraction_field_dto_from_dict = SelectorExtractionFieldDto.from_dict(selector_extraction_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


