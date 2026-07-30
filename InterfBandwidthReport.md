# InterfBandwidthReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts_val_type** | **str** | host | group. The type of entities specified in the hostsVal field | [optional] 
**percentile** | **int** | 95|90|85 Example 95: Calculates 95% of the dataset  | [optional] 
**date_range** | **str** | The Time Range configured for the report. Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**hosts_val** | **str** | The devices OR groups selected for the report, where multiple entities are separated by commas | [optional] 
**is_base1024** | **bool** | true | false false: Scale the number using 1000  true: Scale the number using 1024 | 
**top10_only** | **bool** | true | false false: Metrics will be displayed for all selected devices or groups true: Metrics will only be displayed for the top ten device or groupsThis field is deprecated, use topN field for more flexible top N selection | 
**data_format** | **str** | bps|Bps|Kbps|Mbps Converts the data in the given data format  | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns displayed in the report | [optional] 
**row_format** | **int** | 0 | 1 0: Text only - metrics will be displayed in a tabular format. 1: One graph per instance - metrics will be displayed in a tabular format and one graph will be displayed per instance | [optional] 
**property_filter_metric** | [**ReportPropertyFilterMetricV3**](ReportPropertyFilterMetricV3.md) |  | [optional] 
**metrics** | [**list[Metric]**](Metric.md) | The datapoint or calculation on a datapoint that will be included in the report, where each datapoint/calculation is specified by three fields: dataSourceId, instances (glob is okay) | 
**top_n** | **str** | Top N selection: 5|10|25|50|100|all | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

