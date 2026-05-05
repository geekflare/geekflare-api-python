# OpenPortMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The scanned URL | 
**top_ports** | **float** | Top ports scanned (if any) | [optional] 
**port_ranges** | **str** | Custom port ranges scanned (if any) | [optional] 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.open_port_meta_dto import OpenPortMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPortMetaDto from a JSON string
open_port_meta_dto_instance = OpenPortMetaDto.from_json(json)
# print the JSON string representation of the object
print(OpenPortMetaDto.to_json())

# convert the object into a dict
open_port_meta_dto_dict = open_port_meta_dto_instance.to_dict()
# create an instance of OpenPortMetaDto from a dict
open_port_meta_dto_from_dict = OpenPortMetaDto.from_dict(open_port_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


