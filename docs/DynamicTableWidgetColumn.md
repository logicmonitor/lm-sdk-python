# DynamicTableWidgetColumn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpn** | **str** | The expression in this field will be performed on the datapoint. The Column name should be referenced as the datapoint | [optional] 
**data_point_name** | **str** | The name of the datapoint | [optional] 
**display_type** | **str** | The display type, it includes two options: raw|percent | [optional] 
**min_value** | **float** | The minimum value of the table widget | [optional] 
**data_point_id** | **int** | The id of the datapoint | 
**max_value** | **float** | The maximum value of the table widget | [optional] 
**color_thresholds** | [**list[ColorThreshold]**](ColorThreshold.md) | The threshold of color changes | [optional] 
**column_name** | **str** | The name for the column | 
**enable_forecast** | **bool** | Whether or not forecasting is enabled | [optional] 
**rounding_decimal** | **int** | The number of decimal points to round the value to. Options are 0, 1 and 2 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


