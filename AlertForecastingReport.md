# AlertForecastingReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sorted_by** | **int** | The sort option for the alert forecast report | [optional] 
**confidence_level** | **int** | The confidence level when do forecasting | 
**hosts_val_type** | **str** | The type of the resource selection. Acceptable values are: host, group | 
**date_range** | **str** | The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**hosts_val** | **str** | The group or device name selected for the report | [optional] 
**top10_only** | **bool** | true | false false: CPU metrics will be displayed for all selected devices or groups true: CPU metrics will only be displayed for the top ten device or groups | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns displayed in the report | [optional] 
**metrics** | [**list[Metric]**](Metric.md) | The datapoints that needs to do forecasting | 
**algorithm** | **str** | Forecast method for the report. Acceptable values are: Linear, ARIMA | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


