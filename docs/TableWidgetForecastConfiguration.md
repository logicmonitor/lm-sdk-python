# TableWidgetForecastConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** |  The minimum alert severity the forecasting should include, one of warn | error | critical | [optional] 
**confidence** | **int** | The percent confidence that should be required for a forecasted alert. | [optional] 
**time_range** | **str** | The training data time range (the data on which forecasting is calculated). Options are Last 7 days, Last 14 days, Last 30 days, Last calendar month, Last 365 days or a custom time range | [optional] 
**algorithm** | **str** | Forecast method for the widget :Linear | ARIMA | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


