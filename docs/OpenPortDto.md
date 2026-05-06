# OpenPortDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to be checked | 
**top_ports** | **float** | Scan only the top N ports (optional) | [optional] 
**port_ranges** | **str** | Custom port ranges to scan, e.g., \&quot;80,443,1000-1010\&quot; | [optional] 

## Example

```python
from geekflare_api.models.open_port_dto import OpenPortDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPortDto from a JSON string
open_port_dto_instance = OpenPortDto.from_json(json)
# print the JSON string representation of the object
print(OpenPortDto.to_json())

# convert the object into a dict
open_port_dto_dict = open_port_dto_instance.to_dict()
# create an instance of OpenPortDto from a dict
open_port_dto_from_dict = OpenPortDto.from_dict(open_port_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


