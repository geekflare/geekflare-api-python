# BrokenLinkResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** | Timestamp of the request in milliseconds | 
**api_status** | **str** | API status message | 
**api_code** | **float** | API status code | 
**message** | **str** | Human-readable message about the broken link scan result | 
**meta** | [**BrokenLinkMetaDto**](BrokenLinkMetaDto.md) | Metadata about the broken link request | 
**summary** | [**BrokenLinkSummaryDto**](BrokenLinkSummaryDto.md) | Summary of link check results categorized by status | 
**data** | **List[str]** | List of links found on the page and their HTTP status | 

## Example

```python
from geekflare_api.models.broken_link_response_dto import BrokenLinkResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenLinkResponseDto from a JSON string
broken_link_response_dto_instance = BrokenLinkResponseDto.from_json(json)
# print the JSON string representation of the object
print(BrokenLinkResponseDto.to_json())

# convert the object into a dict
broken_link_response_dto_dict = broken_link_response_dto_instance.to_dict()
# create an instance of BrokenLinkResponseDto from a dict
broken_link_response_dto_from_dict = BrokenLinkResponseDto.from_dict(broken_link_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


