# RedirectCheckMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The original URL checked | 
**proxy_country** | **object** | Proxy country used (if any) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Test details object | 

## Example

```python
from geekflare_api.models.redirect_check_meta_dto import RedirectCheckMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectCheckMetaDto from a JSON string
redirect_check_meta_dto_instance = RedirectCheckMetaDto.from_json(json)
# print the JSON string representation of the object
print(RedirectCheckMetaDto.to_json())

# convert the object into a dict
redirect_check_meta_dto_dict = redirect_check_meta_dto_instance.to_dict()
# create an instance of RedirectCheckMetaDto from a dict
redirect_check_meta_dto_from_dict = RedirectCheckMetaDto.from_dict(redirect_check_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


