# MarginDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** | Top margin in mm | [optional] 
**bottom** | **float** | Bottom margin in mm | [optional] 
**right** | **float** | Right margin in mm | [optional] 
**left** | **float** | Left margin in mm | [optional] 

## Example

```python
from geekflare_api.models.margin_dto import MarginDto

# TODO update the JSON string below
json = "{}"
# create an instance of MarginDto from a JSON string
margin_dto_instance = MarginDto.from_json(json)
# print the JSON string representation of the object
print(MarginDto.to_json())

# convert the object into a dict
margin_dto_dict = margin_dto_instance.to_dict()
# create an instance of MarginDto from a dict
margin_dto_from_dict = MarginDto.from_dict(margin_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


