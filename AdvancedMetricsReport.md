# AdvancedMetricsReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_source** | **str** | The metric source for the advanced metrics report. The value can be lmql, or otlp. Default is lmql. | [optional] 
**date_range** | **str** | Overrides the LMQL query time range with a specified time period. | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns displayed in the report | [optional] 
**query** | **str** | The LMQL query for the advanced metrics report | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

