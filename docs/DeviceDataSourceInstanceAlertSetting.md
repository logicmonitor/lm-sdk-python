# DeviceDataSourceInstanceAlertSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_alert_expr** | **str** | The global alert expression for this datapoint | [optional] 
**alert_clear_interval** | **int** | The interval of alert clear transition | [optional] 
**disable_alerting** | **bool** | Whether or not alerting will be disabled for the datapoint | [optional] 
**alert_expr_note** | **str** | The note associated with the current alert threshold settings | [optional] 
**data_point_description** | **str** | The description of the datapoint the alert settings apply to | [optional] 
**data_source_instance_id** | **int** | The id of the DataSource instance alert settings apply to | [optional] 
**disable_dp_alert_host_groups** | **str** | The group full path lists who disable alert for this datapoint on devicegroup level | [optional] 
**data_point_name** | **str** | The name of the datapoint the alert settings apply to | [optional] 
**data_point_id** | **int** | The id of the Datapoint alert settings apply to | [optional] 
**device_group_id** | **int** | The ID of the device group | [optional] 
**parent_device_group_alert_expr_list** | [**list[DeviceGroupAlertThresholdInfo]**](DeviceGroupAlertThresholdInfo.md) | Device group alert expression list base on the priority. The first is the highest priority and effected on this instance | [optional] 
**alerting_disabled_on** | **str** | The datapoint is effected alert disabled by which group | [optional] 
**id** | **int** | The id of this alert setting | [optional] 
**data_source_instance_alias** | **str** | The alias (name) of the DataSource instance the alert settings apply to | [optional] 
**device_group_full_path** | **str** | The full path of the device group | [optional] 
**alert_expr** | **str** | The thresholds that should be associated with the datapoint. Note that you need to have a space between the operator and each threshold (e.g. &gt; 1 2 3) | [optional] 
**alert_transition_interval** | **int** | The interval of alert transition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


