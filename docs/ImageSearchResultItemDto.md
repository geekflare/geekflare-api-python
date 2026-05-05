# ImageSearchResultItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**image_url** | **str** |  | 
**source_url** | **str** |  | 
**width** | **float** |  | 
**height** | **float** |  | 

## Example

```python
from geekflare_api.models.image_search_result_item_dto import ImageSearchResultItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSearchResultItemDto from a JSON string
image_search_result_item_dto_instance = ImageSearchResultItemDto.from_json(json)
# print the JSON string representation of the object
print(ImageSearchResultItemDto.to_json())

# convert the object into a dict
image_search_result_item_dto_dict = image_search_result_item_dto_instance.to_dict()
# create an instance of ImageSearchResultItemDto from a dict
image_search_result_item_dto_from_dict = ImageSearchResultItemDto.from_dict(image_search_result_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


