# NetworkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The actual HTTP protocol used (e.g. h2, h3, http/1.1, http/1.0) | 
**remote_ip** | **str** | Remote IP address of the server | [optional] 
**bytes_read** | **float** | Total bytes read from the response | 

## Example

```python
from geekflare_api.models.network_dto import NetworkDto

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDto from a JSON string
network_dto_instance = NetworkDto.from_json(json)
# print the JSON string representation of the object
print(NetworkDto.to_json())

# convert the object into a dict
network_dto_dict = network_dto_instance.to_dict()
# create an instance of NetworkDto from a dict
network_dto_from_dict = NetworkDto.from_dict(network_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


