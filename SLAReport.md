# SLAReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range** | **str** | The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**timezone** | **str** | The specific timezone for the report | [optional] 
**display_with_availability** | **bool** | If true, only devices with less than 100% availability will be displayed in the report | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns displayed in the report | [optional] 
**display_summary** | **bool** | If true, the SLA summary (total %) will be displayed | [optional] 
**day_in_one_week** | **str** | The days of the week that the SLA report should take into account, where multiple values are separated by commas and * refers to all days of the week | [optional] 
**period_in_one_day** | **str** | The hours of each selected day that the SLA report should take into account, where * refers to all hours | [optional] 
**metrics** | [**list[SlaMetric]**](SlaMetric.md) | The datapoints and corresponding SLA thresholds that will be included in the report, where each metric includes seven fields: groupName, deviceName, dataSourceFullName, dataSourceId, instances, metric and threshold. Threshold should comprise of an operator and a number separated by a space, where valid operators are &gt;, &lt;, !&#x3D;, &#x3D;, &gt;&#x3D; and &lt;&#x3D; | 
**unmonitored_time** | **int** | 0|1|2 - How the time we have no data for the device should be counted, where 1 &#x3D; ignore no data (subtract from total time), 2 &#x3D; count as violation (subtract from uptime), 3 &#x3D; count as available (add to uptime) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


