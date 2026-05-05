# RedirectCheckResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**meta** | [**RedirectCheckMetaDto**](RedirectCheckMetaDto.md) | Metadata about the redirection check. | 
**data** | [**List[RedirectHopDto]**](RedirectHopDto.md) | List of redirection hops with status and headers. | 

## Example

```python
from geekflare_api.models.redirect_check_response_dto import RedirectCheckResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectCheckResponseDto from a JSON string
redirect_check_response_dto_instance = RedirectCheckResponseDto.from_json(json)
# print the JSON string representation of the object
print(RedirectCheckResponseDto.to_json())

# convert the object into a dict
redirect_check_response_dto_dict = redirect_check_response_dto_instance.to_dict()
# create an instance of RedirectCheckResponseDto from a dict
redirect_check_response_dto_from_dict = RedirectCheckResponseDto.from_dict(redirect_check_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


