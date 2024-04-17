# RestDeviceInstanceGroupAlertConfigV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_for_no_data** | **int** | The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert) | [optional] 
**enable_anomaly_alert_suppression** | **str** |  | [optional] 
**global_alert_for_no_data** | **int** | The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert) | [optional] 
**alert_enable** | **bool** |  | [optional] 
**critical_ad_adv_setting** | **str** |  | [optional] 
**alert_clear_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before the alert will be cleared (0-60) | [optional] 
**global_alert_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before it will be triggered | [optional] 
**alert_expr_note** | **str** |  | [optional] 
**ad_adv_setting_enabled** | **bool** |  | [optional] 
**error_ad_adv_setting** | **str** |  | [optional] 
**warn_ad_adv_setting** | **str** |  | [optional] 
**global_alert_clear_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before the alert will be cleared | [optional] 
**alert_expr** | **str** |  | [optional] 
**alert_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before it will be triggered (0-60) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


