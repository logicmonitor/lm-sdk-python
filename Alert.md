# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** | The device specific LogicModule Id | [optional] 
**instance_name** | **str** | The name of the instance in alert | [optional] 
**monitor_object_id** | **int** | The id of the object that the alert is associated with | [optional] 
**end_epoch** | **int** | The time (in epoch format) that the alert ended | [optional] 
**rule** | **str** | The rule the alert matches | [optional] 
**threshold** | **str** | The threshold associated with the object in alert | [optional] 
**type** | **str** | The type of alert | [optional] 
**start_epoch** | **int** | The time (in epoch format) that the alert started | [optional] 
**internal_id** | **str** | The internal id for the alert | [optional] 
**ack_comment** | **str** | The comment submitted with the acknowledgement | [optional] 
**monitor_object_name** | **str** | The name of the object that the alert is associated with | [optional] 
**data_point_name** | **str** | The name of the datapoint in alert | [optional] 
**instance_id** | **int** | The id of the instance in alert | [optional] 
**data_point_id** | **int** | The id of the datapoint in alert | [optional] 
**next_recipient** | **int** | The next recipient in the escalation chain for this alert | [optional] 
**id** | **str** | The alert id | [optional] 
**detail_message** | **object** | The alert message, if needMessage&#x3D;true is included in the query parameters | [optional] 
**rule_id** | **int** | The id of the rule the alert matches | [optional] 
**alert_value** | **str** | The value that triggered the alert | [optional] 
**acked_by** | **str** | The user that acknowledged the alert | [optional] 
**severity** | **int** | The alert severity, where 2&#x3D;warning, 3&#x3D;error and 4&#x3D;critical | [optional] 
**sdted** | **bool** | Whether or not the alert was triggered during an SDT | [optional] 
**acked_epoch** | **int** | The time (in epoch format) that the alert was acknowledged | [optional] 
**chain** | **str** | The escalation chain the alert was routed to | [optional] 
**sdt** | **object** | The active SDT, if one exists | [optional] 
**sub_chain_id** | **int** | The id of the sub time based chain | [optional] 
**received_list** | **str** | The recipients that have received the alert | [optional] 
**monitor_object_type** | **str** |  | [optional] 
**custom_columns** | **object** | The property or token values that should display with the alert details. Note that if referencing tokens, you&#39;ll need to URL encode the # symbol. | [optional] 
**acked** | **bool** | Whether or not the alert has been acknowledged | [optional] 
**resource_template_type** | **str** | The type of the logicmodule in alert | [optional] 
**clear_value** | **str** | The value that cleared the alert | [optional] 
**instance_description** | **str** | The description of the instance in alert | [optional] 
**monitor_object_groups** | **object** | Information about the groups the object is a member of | [optional] 
**chain_id** | **int** | The id of the escalation chain the alert was routed to | [optional] 
**resource_template_id** | **int** | The id of the datasource in alert | [optional] 
**cleared** | **bool** | Whether or not the alert has cleared | [optional] 
**resource_template_name** | **str** | The name of the datasource in alert | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


