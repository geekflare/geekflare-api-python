# MtrDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hop** | **float** | Hop number in the traceroute path | 
**host** | **str** | Host IP or domain name at this hop | 
**asn** | **str** | Autonomous System Number (ASN) for the host | 
**loss** | **float** | Packet loss percentage at this hop | 
**sent** | **float** | Number of packets sent to this hop | 
**last** | **float** | Last recorded round-trip time (RTT) in milliseconds | 
**avg** | **float** | Average RTT across packets | 
**best** | **float** | Best (lowest) RTT observed | 
**worst** | **float** | Worst (highest) RTT observed | 
**std_dev** | **float** | Standard deviation of RTT measurements | 

## Example

```python
from geekflare_api.models.mtr_data_dto import MtrDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of MtrDataDto from a JSON string
mtr_data_dto_instance = MtrDataDto.from_json(json)
# print the JSON string representation of the object
print(MtrDataDto.to_json())

# convert the object into a dict
mtr_data_dto_dict = mtr_data_dto_instance.to_dict()
# create an instance of MtrDataDto from a dict
mtr_data_dto_from_dict = MtrDataDto.from_dict(mtr_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


