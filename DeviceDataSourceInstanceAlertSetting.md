# DeviceDataSourceInstanceAlertSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_alert_expr** | **str** | The global alert expression for this datapoint | [optional] 
**parent_instance_group_alert_expr** | [**InstanceGroupAlertThresholdInfo**](InstanceGroupAlertThresholdInfo.md) | Instance group alert expression list base on the priority. The first is the highest priority and effected on this instance | [optional] 
**alert_for_no_data** | **int** | alert for no data | [optional] 
**post_processor_param** | **str** | The post processor parameter for complex DataPoint and instance level configCheck threshold. | [optional] 
**disable_alerting** | **bool** | Whether or not alerting will be disabled for the datapoint | [optional] 
**global_alert_transition_interval** | **str** |  | [optional] 
**data_point_description** | **str** | The description of the datapoint the alert settings apply to | [optional] 
**global_enable_anomaly_alert_generation** | **str** | The global enable anomaly alert generation | [optional] 
**enable_anomaly_alert_generation** | **str** | enable anomaly alert generation | [optional] 
**disable_dp_alert_host_groups** | **str** | The group full path lists who disable alert for this datapoint on devicegroup level | [optional] 
**data_point_name** | **str** | The name of the datapoint the alert settings apply to | [optional] 
**data_point_id** | **int** | The id of the Datapoint alert settings apply to | [optional] 
**global_enable_anomaly_alert_suppression** | **str** | The global enable anomaly alert suppression | [optional] 
**device_group_id** | **int** | The ID of the device group | [optional] 
**id** | **int** | The id of this alert setting | [optional] 
**global_alert_clear_transition_interval** | **str** |  | [optional] 
**device_group_full_path** | **str** | The full path of the device group | [optional] 
**alert_transition_interval** | **int** | The interval of alert transition | [optional] 
**global_alert_for_no_data** | **str** |  | [optional] 
**enable_anomaly_alert_suppression** | **str** | enable anomaly alert suppression | [optional] 
**alert_clear_interval** | **int** | The interval of alert clear transition | [optional] 
**critical_ad_adv_setting** | **str** |  | [optional] 
**alert_expr_note** | **str** | The note associated with the current alert threshold settings | [optional] 
**ad_adv_setting_enabled** | **bool** |  | [optional] 
**error_ad_adv_setting** | **str** |  | [optional] 
**data_source_instance_id** | **int** | The id of the DataSource instance alert settings apply to | [optional] 
**warn_ad_adv_setting** | **str** |  | [optional] 
**global_post_processor_param** | **str** | The post processor parameters for complex DataPoints and global level configCheck threshold. | [optional] 
**parent_device_group_alert_expr_list** | [**list[DeviceGroupAlertThresholdInfo]**](DeviceGroupAlertThresholdInfo.md) | Device group alert expression list base on the priority. The first is the highest priority and effected on this instance | [optional] 
**alerting_disabled_on** | **str** | The datapoint is effected alert disabled by which group | [optional] 
**data_source_instance_alias** | **str** | The alias (name) of the DataSource instance the alert settings apply to | [optional] 
**collection_interval** | **int** | Collection Interval | [optional] 
**alert_expr** | **str** | The thresholds that should be associated with the datapoint. Note that you need to have a space between the operator and each threshold (e.g. &gt; 1 2 3) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


