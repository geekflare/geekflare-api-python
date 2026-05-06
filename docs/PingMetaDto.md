# PingMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested URL or IP address | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 

## Example

```python
from geekflare_api.models.ping_meta_dto import PingMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of PingMetaDto from a JSON string
ping_meta_dto_instance = PingMetaDto.from_json(json)
# print the JSON string representation of the object
print(PingMetaDto.to_json())

# convert the object into a dict
ping_meta_dto_dict = ping_meta_dto_instance.to_dict()
# create an instance of PingMetaDto from a dict
ping_meta_dto_from_dict = PingMetaDto.from_dict(ping_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


