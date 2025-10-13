# DeviceEventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_source_id** | **int** | event source id | [optional] 
**alert_status** | **str** | alert status | [optional] 
**stop_monitoring** | **bool** | stop monitoring this host event source | [optional] 
**event_source_name** | **str** | event source name defined where creating a event source | [optional] 
**disable_alerting** | **bool** | stop alerting for this host event source | [optional] 
**event_source_description** | **str** | event source description defined where creating a event source | [optional] 
**event_type** | **str** | event source collector type | [optional] 
**device_id** | **int** | Id of the Device | [optional] 
**sdt_status** | **str** | sdt status, three level sdt status: parent-self-child | [optional] 
**device_display_name** | **str** | device display name | [optional] 
**groups_disabled_this_source** | [**list[TreeNode]**](TreeNode.md) | All groups that disable this datasource. | [optional] 
**event_source_group_name** | **str** | event source group name defined where creating a event source | [optional] 
**sdt_at** | **str** | sdt on which level, host group or host | [optional] 
**alerting_disabled_on** | [**TreeNode**](TreeNode.md) |  | [optional] 
**id** | **int** | device event source id | [optional] 
**alert_status_priority** | **int** | the alert status priority, more smaller value more critical  | [optional] 
**alert_disable_status** | **str** | alert disable status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

