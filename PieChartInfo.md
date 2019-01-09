# PieChartInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_slices_can_be_shown** | **int** | The maximum number of slices you&#39;d like displayed in the pie chart | [optional] 
**virtual_data_points** | [**list[VirtualDataPoint]**](VirtualDataPoint.md) | The virtual datapoints added to the widget. Note that virtual datapoints must be included in the pieChartItems object to be displayed in the widget | [optional] 
**show_labels_and_lines_on_pc** | **bool** | Whether or not labels and lines should be displayed on the pie chart | [optional] 
**counters** | [**list[Counter]**](Counter.md) | The counter is used for saving applyTo expression, it&#39;s mainly used for count device | [optional] 
**data_points** | [**list[PieChartDataPoint]**](PieChartDataPoint.md) | The datapoints added to the widget. Note that datapoints must be included in the pieChartItems object to be displayed in the widget | [optional] 
**hide_zero_percent_slices** | **bool** | Whether items at 0% should be hidden | [optional] 
**group_remaining_as_others** | **bool** | If the number of slices exceeds the maxSlicesCanBeShown, this value indicates whether the remaining slices should be grouped together | [optional] 
**pie_chart_items** | [**list[PieChartItem]**](PieChartItem.md) | The datapoints and virtual datapoints that will be displayed in the pie chart | 
**title** | **str** | The title that will be displayed above the pie chart | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


