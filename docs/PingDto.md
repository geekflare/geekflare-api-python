# PingDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 

## Example

```python
from geekflare_api.models.ping_dto import PingDto

# TODO update the JSON string below
json = "{}"
# create an instance of PingDto from a JSON string
ping_dto_instance = PingDto.from_json(json)
# print the JSON string representation of the object
print(PingDto.to_json())

# convert the object into a dict
ping_dto_dict = ping_dto_instance.to_dict()
# create an instance of PingDto from a dict
ping_dto_from_dict = PingDto.from_dict(ping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


