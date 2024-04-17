# ResourceDataSourceAlertThresholdInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_anomaly_alert_generation** | **str** | enable anomaly alert generation | [optional] 
**alert_for_no_data** | **str** | The triggered alert level if we cannot collect data for this datapoint. The values can be 0-4 (0:unused alert, 1:alert ok, 2:warn alert, 2:error alert, 4:critical alert) | [optional] 
**enable_anomaly_alert_suppression** | **str** | enable anomaly alert suppression | [optional] 
**alert_clear_transition_interval** | **str** | The count that the alert must exist for this many poll cycles before the alert will be cleared | [optional] 
**alert_enabled** | **bool** |  | [optional] 
**resource_datasource_id** | **int** |  | [optional] 
**alert_expr** | **str** |  | [optional] 
**alert_transition_interval** | **str** | The count that the alert must exist for this many poll cycles before it will be triggered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


