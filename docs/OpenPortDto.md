# OpenPortDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL, hostname, IPv4, or IPv6 address to be checked | 
**top_ports** | **float** | Scan only the top N ports (optional) | [optional] 
**port_ranges** | **str** | Custom port ranges to scan, e.g., \&quot;80,443,1000-1010\&quot; | [optional] 
**detect_services** | **bool** | When true, also runs service/version detection (nmap -sV) on the ports found open. Slower than the base scan since it probes each open port individually — best-effort: if it fails, the port list is still returned without service info. | [optional] [default to False]

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


