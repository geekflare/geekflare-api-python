# TestMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique test identifier | 

## Example

```python
from geekflare_api.models.test_meta_dto import TestMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of TestMetaDto from a JSON string
test_meta_dto_instance = TestMetaDto.from_json(json)
# print the JSON string representation of the object
print(TestMetaDto.to_json())

# convert the object into a dict
test_meta_dto_dict = test_meta_dto_instance.to_dict()
# create an instance of TestMetaDto from a dict
test_meta_dto_from_dict = TestMetaDto.from_dict(test_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


