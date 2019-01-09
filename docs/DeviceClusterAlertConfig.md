# DeviceClusterAlertConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_by** | **str** | host | instance - Whether the cluster alert is based on an alert count across devices or instances | [optional] 
**data_point_name** | **str** | The name of the dataPoint you want to base the cluster alert on | [optional] 
**data_source_id** | **int** | The id of the dataSource you want to base the cluster alert on | [optional] 
**data_point_id** | **int** | The id of the dataPoint you want to base the cluster alert on | [optional] 
**min_alert_level** | **int** | The alert level that must be present for the devices or instances to trigger the cluster alert. Acceptable values are: 2, 3, 4 | [optional] 
**data_source_display_name** | **str** | The display name of the dataSource you want to base the cluster alert on | [optional] 
**disable_alerting** | **bool** | Whether or not alerting will be disabled | [optional] 
**id** | **int** | The id of the cluster alert configuration | [optional] 
**suppress_ind_alert** | **bool** | Whether or not alerting will be suppressed for individual alerts | [optional] 
**threshold_type** | **str** | whether the alert expression should be evaluated as a total number of devices or instances (absolute) or as a percentage of devices or instances (percentage). Acceptable values are: absolute, percentage | [optional] 
**data_point_description** | **str** | The description of the dataPoint you want to base the cluster alert on | [optional] 
**alert_expr** | **str** | The expression that indicates the number of objects (devices or instances) that need to be in alert to trigger the cluster alert. E.g. &gt; 5 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


