# DeviceGroupAlertThresholdInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_anomaly_alert_generation** | **str** | enable anomaly alert generation | [optional] 
**alert_for_no_data** | **int** | The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert) | [optional] 
**user_permission** | **str** |  | [optional] 
**enable_anomaly_alert_suppression** | **str** | enable anomaly alert suppression | [optional] 
**group_id** | **int** |  | [optional] 
**alert_clear_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before the alert will be cleared | [optional] 
**alert_enabled** | **bool** |  | [optional] 
**group_full_path** | **str** |  | [optional] 
**alert_expr** | **str** |  | [optional] 
**alert_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before it will be triggered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

