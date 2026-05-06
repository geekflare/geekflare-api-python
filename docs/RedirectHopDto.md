# RedirectHopDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL at this hop | 
**status** | **float** | HTTP status code at this hop | 
**headers** | **List[str]** | Response headers | 

## Example

```python
from geekflare_api.models.redirect_hop_dto import RedirectHopDto

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectHopDto from a JSON string
redirect_hop_dto_instance = RedirectHopDto.from_json(json)
# print the JSON string representation of the object
print(RedirectHopDto.to_json())

# convert the object into a dict
redirect_hop_dto_dict = redirect_hop_dto_instance.to_dict()
# create an instance of RedirectHopDto from a dict
redirect_hop_dto_from_dict = RedirectHopDto.from_dict(redirect_hop_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


