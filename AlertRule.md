# AlertRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint** | **str** | The datapoint for which the alert rule is configured to match | [optional] 
**instance** | **str** | The instance for which the alert rule is configured to match | [optional] 
**devices** | **list[str]** | The device names and service names for which the alert rule is configured to match | [optional] 
**escalating_chain_id** | **int** | The id of the escalation chain associated with the alert rule | 
**resource_properties** | [**list[DeviceProperty]**](DeviceProperty.md) | The resource property filters list | [optional] 
**send_anomaly_suppressed_alert** | **bool** | Whether or not send anomaly suppressed alert | 
**priority** | **int** | The priority associated with the alert rule | 
**suppress_alert_ack_sdt** | **bool** | Whether or not status notifications for acknowledgements and SDTs should be sent to the alert rule | [optional] 
**datasource** | **str** | The datasource for which the alert rule is configured to match | [optional] 
**suppress_alert_clear** | **bool** | Whether or not alert clear notifications should be sent to the alert rule | [optional] 
**name** | **str** | The name of the alert rule | 
**id** | **int** | The Id of the alert rule | [optional] 
**level_str** | **str** | The alert severity levels for which the alert rule is configured to match.  The values can be All|Warn|Error|Critical | [optional] 
**device_groups** | **list[str]** | The device groups and service groups for which the alert rule is configured to match | [optional] 
**escalating_chain** | **object** | The escalation chain associated with the alert rule | [optional] 
**escalation_interval** | **int** | The escalation interval associated with the alert rule, in minutes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

