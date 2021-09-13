# AlertSlaReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts_val_type** | **str** | host | group. The type of entities specified in the hostsVal field | [optional] 
**date_range** | **str** | The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**hosts_val** | **str** | The devices OR groups (use full path) selected for the report, where multiple entities are separated by commas. Note that glob is supported | [optional] 
**data_point** | **str** | The datapoints selected for the report, where multiple datapoints are separated by commas | [optional] 
**alert_level** | **str** | Warn | Error | Critical. The minimum severity of the alert statuses you’d like to evaluate for the specified devices and device groups | [optional] 
**alert_rule** | **str** | The name of the Alert Rule that the datapoint alert you’re evaluating will be routed to. Note that if you do not select the correct alert rule, no matching alerts will be displayed | [optional] 
**data_source** | **str** | The datasource instance selected for the report, in the format DatasourceName-InstanceName (If it is a single instance datasource you can just leave it at DatasourceName) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


