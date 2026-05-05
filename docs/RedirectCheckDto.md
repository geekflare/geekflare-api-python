# RedirectCheckDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Target URL | 
**proxy_country** | **str** | Proxy country code to route the request | [optional] 

## Example

```python
from geekflare_api.models.redirect_check_dto import RedirectCheckDto

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectCheckDto from a JSON string
redirect_check_dto_instance = RedirectCheckDto.from_json(json)
# print the JSON string representation of the object
print(RedirectCheckDto.to_json())

# convert the object into a dict
redirect_check_dto_dict = redirect_check_dto_instance.to_dict()
# create an instance of RedirectCheckDto from a dict
redirect_check_dto_from_dict = RedirectCheckDto.from_dict(redirect_check_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


