# MtrMetaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The tested URL or IP address | 
**proxy_country** | **str** | Country used for proxy | [optional] 
**follow_redirect** | **bool** | Indicates if redirects should be followed | [optional] 
**redirected_url** | **str** | Final URL after redirection (if any) | 
**test** | [**TestMetaDto**](TestMetaDto.md) | Metadata about the test execution | 

## Example

```python
from geekflare_api.models.mtr_meta_dto import MtrMetaDto

# TODO update the JSON string below
json = "{}"
# create an instance of MtrMetaDto from a JSON string
mtr_meta_dto_instance = MtrMetaDto.from_json(json)
# print the JSON string representation of the object
print(MtrMetaDto.to_json())

# convert the object into a dict
mtr_meta_dto_dict = mtr_meta_dto_instance.to_dict()
# create an instance of MtrMetaDto from a dict
mtr_meta_dto_from_dict = MtrMetaDto.from_dict(mtr_meta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


