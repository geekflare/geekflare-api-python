# GroundedSourceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**url** | **str** |  | 
**position** | **float** |  | 

## Example

```python
from geekflare_api.models.grounded_source_dto import GroundedSourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroundedSourceDto from a JSON string
grounded_source_dto_instance = GroundedSourceDto.from_json(json)
# print the JSON string representation of the object
print(GroundedSourceDto.to_json())

# convert the object into a dict
grounded_source_dto_dict = grounded_source_dto_instance.to_dict()
# create an instance of GroundedSourceDto from a dict
grounded_source_dto_from_dict = GroundedSourceDto.from_dict(grounded_source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


