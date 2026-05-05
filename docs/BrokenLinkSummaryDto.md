# BrokenLinkSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total number of links checked | 
**successful** | **float** | Number of successful links (2xx status codes) | 
**redirects** | **float** | Number of redirect links (3xx status codes) | 
**broken** | **float** | Number of broken links (4xx status codes and DNS/network failures) | 
**server_error** | **float** | Number of server errors (5xx status codes) | 

## Example

```python
from geekflare_api.models.broken_link_summary_dto import BrokenLinkSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrokenLinkSummaryDto from a JSON string
broken_link_summary_dto_instance = BrokenLinkSummaryDto.from_json(json)
# print the JSON string representation of the object
print(BrokenLinkSummaryDto.to_json())

# convert the object into a dict
broken_link_summary_dto_dict = broken_link_summary_dto_instance.to_dict()
# create an instance of BrokenLinkSummaryDto from a dict
broken_link_summary_dto_from_dict = BrokenLinkSummaryDto.from_dict(broken_link_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


