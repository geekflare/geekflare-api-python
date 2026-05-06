# TimingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **float** | Time spent in DNS lookup (ms) | 
**connect** | **float** | Time to establish TCP connection (ms) | 
**tls** | **float** | Time to complete TLS handshake (ms) | 
**send** | **float** | Time to send request (ms) | 
**wait** | **float** | Server processing time (ms) | 
**ttfb** | **float** | Time to First Byte - calculated as dns+connect+tls+send+wait (ms) | 
**download** | **float** | Time to download response body (ms) | 
**total** | **float** | Total load time (ms) | 
**redirect_duration** | **float** | Time spent in redirects before reaching final URL (ms) | 

## Example

```python
from geekflare_api.models.timings_dto import TimingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimingsDto from a JSON string
timings_dto_instance = TimingsDto.from_json(json)
# print the JSON string representation of the object
print(TimingsDto.to_json())

# convert the object into a dict
timings_dto_dict = timings_dto_instance.to_dict()
# create an instance of TimingsDto from a dict
timings_dto_from_dict = TimingsDto.from_dict(timings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


