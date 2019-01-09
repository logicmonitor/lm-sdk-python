# AlertRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint** | **str** | The datapoint the alert rule is configured to match | [optional] 
**instance** | **str** | The instance the alert rule is configured to match | [optional] 
**devices** | **list[str]** | The device names and service names the alert rule is configured to match | [optional] 
**escalating_chain_id** | **int** | The id of the escalation chain associated with the alert rule | 
**priority** | **int** | The priority associated with the alert rule | 
**suppress_alert_ack_sdt** | **bool** | Whether or not status notifications for acknowledgements and SDTs should be sent to the alert rule | [optional] 
**datasource** | **str** | The datasource the alert rule is configured to match | [optional] 
**suppress_alert_clear** | **bool** | Whether or not alert clear notifications should be sent to the alert rule | [optional] 
**name** | **str** | The name of the alert rule | 
**id** | **int** | The Id of the alert rule | [optional] 
**level_str** | **str** | The alert severity levels the alert rule is configured to match. Acceptable values are: All, Warn, Error, Critical | [optional] 
**device_groups** | **list[str]** | The device groups and service groups the alert rule is configured to match | [optional] 
**escalating_chain** | **object** | The escalation chain associated with the alert rule | [optional] 
**escalation_interval** | **int** | The escalation interval associated with the alert rule, in minutes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


