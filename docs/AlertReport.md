# AlertReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_only** | **bool** | true: only alerts that are still alerting (i.e. haven&#39;t yet cleared) will be displayed in the report false: active alerts and cleared alerts will both be displayed in the report | [optional] 
**sorted_by** | **str** | count | host | dataPoint | level | startOn | ackedOn. How displayed alerts will be sorted in the report. Note that if summaryOnly is set to true, you are limited to sortedBy&#x3D; count | host | dataPoint. If summaryOnly is set to false, you cannot set sortedBy &#x3D; count | [optional] 
**chain** | **str** | All alerts displayed in the report must have been routed to the Escalation Chains specified in this filter | [optional] 
**date_range** | **str** | The Time Range configured for the report. Options include: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**level** | **str** | all | error | critical all: alerts of all severity levels will be displayed if they match the filter criteria error: only error and critical alerts that match the filter criteria will be displayed critical: only critical alerts that match the filter criteria will be displayed | [optional] 
**timing** | **str** | overlap | start - Any alerts active during the specified dateRange will be displayed in the report if time&#x3D;overlap. If time&#x3D;start, only alerts that started during the specified dateRange will be displayed in the report | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns that will be displayed in the report. You should specify the columns in the order in which you&#39;d like them to be displayed. All column names need to be included in this object, but each column should have an associated isHidden field that indicates whether it is displayed or not. NOTE that if summaryOnly is set to true you can only include these columns: Alerts, Group, Device, Instance, Datapoint. If summaryOnly is set to false you can include these columns: Severity, Group, Device, Instance, Datapoint, Thresholds, Value, Began, End, Rule, Chain, Acked, Acked By, Acked On, Notes, In SDT | [optional] 
**data_point** | **str** | The group filter used to determine which alerts will appear in the report. Glob expression supported | [optional] 
**sdt_filter** | **str** | all | sdt | nonsdt all: alerts that are in SDT and that aren&#39;t in SDT that meet the report criteria will be displayed sdt: only alerts that are in SDT and that meet the report criteria will be displayed nonsdt: only alerts that aren&#39;t in SDT and that meet the report criteria will be displayed | [optional] 
**rule** | **str** | All alerts displayed in the report must have been routed to the Rules specified in this filter | [optional] 
**ack_filter** | **str** | all | acked | nonacked all: both acknowledged and non-acknowledged alerts that meet the report criteria will be displayed acked: only acknowledged alerts that meet the report criteria will be displayed nonacked: only non-acknowledged alerts that meet the report criteria will be displayed | [optional] 
**device_display_name** | **str** | The device filter used to determine which alerts will appear in the report. Glob expressions supported | [optional] 
**summary_only** | **bool** | true: a column will be added to the report detailing the number of times each alert occurred false: the number of times each alert occurred will not be displayed in the report | [optional] 
**data_source_instance_name** | **str** | The instance filter used to determine which alerts will appear in the report. Glob expressions supported | [optional] 
**data_source** | **str** | All alerts displayed in the report must have been triggered for the Datasources specified in this filter | [optional] 
**group_full_path** | **str** | The group filter used to determine which alerts will appear in the report. Glob expressions supported | [optional] 
**include_preexist** | **bool** | true: alerts that started prior to the specified dateRange but that meet all other criteria will be displayed in the report false: only alerts that started during the specified dateRange will be displayed in the report | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


