# BrandCompanyDto

LLM-synthesized company intelligence. Only present when mode is `enriched`. Coverage depends on public information available for the domain — not every field is populated for every site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**founded_year** | **float** | Year the company was founded | [optional] 
**employees_range** | **str** | Approximate employee headcount range | [optional] 
**revenue_range** | **str** | Approximate annual revenue range | [optional] 
**kind** | **str** |  | [optional] 
**industry** | **str** | Primary industry or category the company operates in | [optional] 
**location** | [**BrandLocationDto**](BrandLocationDto.md) |  | [optional] 
**stock_ticker** | **str** | Stock ticker symbol, present when kind is PUBLICLY_TRADED | [optional] 
**summary** | **str** |  | [optional] 
**target_audience** | **str** |  | [optional] 
**target_audience_segments** | **List[str]** |  | [optional] 
**brand_voice** | **List[str]** |  | [optional] 
**use_cases** | **List[str]** |  | [optional] 

## Example

```python
from geekflare_api.models.brand_company_dto import BrandCompanyDto

# TODO update the JSON string below
json = "{}"
# create an instance of BrandCompanyDto from a JSON string
brand_company_dto_instance = BrandCompanyDto.from_json(json)
# print the JSON string representation of the object
print(BrandCompanyDto.to_json())

# convert the object into a dict
brand_company_dto_dict = brand_company_dto_instance.to_dict()
# create an instance of BrandCompanyDto from a dict
brand_company_dto_from_dict = BrandCompanyDto.from_dict(brand_company_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


