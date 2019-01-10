# CustomGraph

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_data_points** | [**list[CustomVirtualDataPoint]**](CustomVirtualDataPoint.md) | The virtual datapoints added to the widget (note that a virtual datapoint must be referenced in a graph line to be displayed) | [optional] 
**min_value** | **object** | The minimum value that should be displayed on the y-axis | [optional] 
**top_x** | **int** | The number of lines to display for each configured datapoint | [optional] 
**max_value** | **object** | The maximum value that should be displayed on the y-axis | [optional] 
**data_points** | [**list[CustomFlexibleVirtualDataSourceEx]**](CustomFlexibleVirtualDataSourceEx.md) | The datapoints added to the widget (note that a datapoint must be referenced in a graph line to be displayed) | 
**vertical_label** | **str** | The label that will be display along the y axis | [optional] 
**id** | **int** | The unique id of the custom graph displayed by this widget (not to be confused with the widget id) | [optional] 
**aggregate** | **bool** | true: You can set this field to true to aggregate results into one line. false: Results will not be aggregated | [optional] 
**desc** | **bool** | Whether the top X are displayed (false) or the bottom X are displayed (true) | [optional] 
**scale_unit** | **int** | The base scale unit (1000 or 1024) | [optional] 
**global_consolidate_function** | **str** | The function for global consolidate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


