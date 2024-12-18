# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_collector_group_id** | **int** | The id of the Collector Group associated with the device&#x27;s log collection | [optional] 
**disable_alerting** | **bool** | Indicates whether alerting is disabled (true) or enabled (false) for this device | [optional] 
**netflow_collector_group_id** | **int** | The id of the Collector Group associated with the device&#x27;s netflow collector | [optional] 
**role_privileges** | **list[str]** | The role privilege operation(s) for this device that are granted to the user who made the API request | [optional] 
**system_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any system properties (aside from system.categories) defined for this device | [optional] 
**is_preferred_log_collector_configured** | **bool** | Indicates whether Preferred Log Collector is configured  (true) or not (false) for the device | [optional] 
**host_status** | **str** | The status of this device, where possible statuses are normal, dead and dead-collector | [optional] 
**auto_balanced_collector_group_id** | **int** | The Auto Balanced Collector Group id. 0 means not monitored by ABCG | [optional] 
**inherited_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any properties inherit from parents | [optional] 
**id** | **int** | The Id of the device | [optional] 
**synthetics_collector_ids** | **list[int]** | The list of ids of the collectors currently monitoring the resource and discovering instances | [optional] 
**up_time_in_seconds** | **int** | The uptime of the device in seconds. This value will always be the largest value reported by the following datasources: Host Uptime- SNMPUptime- SNMP_Engine_Uptime- WinSystemUptime- NimbleUptime- | [optional] 
**device_type** | **int** | The type of device: 0 indicates a regular device, 1 indicates an APPGROUP device, 2 indicates an AWS device, 3 indicates a service device, 4 indicates an Azure device, 6 indicates a biz_service device, 7 indicates a GCP device, 8 indicates K8S device | [optional] 
**current_collector_id** | **int** | The id of the collector currently monitoring the device and discovering instances | [optional] 
**netflow_collector_id** | **int** | The Id of the netflow collector associated with the device | [optional] 
**auto_props_assigned_on** | **int** | The time, in epoch seconds format, that properties were first discovered for this device | [optional] 
**updated_on** | **int** | The time, in epoch seconds format, that the device was last updated | [optional] 
**preferred_collector_group_id** | **int** | The id of the Collector Group associated with the device&#x27;s preferred collector | [optional] 
**custom_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any non-system properties (aside from system.categories) defined for this device | [optional] 
**collector_description** | **str** | The description/name of the collector for this device | [optional] 
**preferred_collector_id** | **int** | The Id of the preferred collector assigned to monitor the device | 
**last_rawdata_time** | **int** | The last time, in epoch seconds, that raw Netflow data was reported | [optional] 
**name** | **str** | The host name or IP address of the device | 
**deleted_time_in_ms** | **int** | The time in milliseconds that the device has been dead for, or since the AWS device was filtered out | [optional] 
**netflow_collector_group_name** | **str** | The name of the Collector Group associated with the device&#x27;s netflow collector | [optional] 
**azure_state** | **int** | The Azure instance state (if applicable): 1 indicates that the instance is running, 2 indicates that the instance is stopped and 3 the instance is terminated. | [optional] 
**related_device_id** | **int** | The Id of the AWS EC2 instance related to this device, if one exists in the LogicMonitor account. This value defaults to -1, which indicates that there are no related devices | [optional] 
**log_collector_group_name** | **str** | The name of the Collector Group associated with the device&#x27;s. | [optional] 
**display_name** | **str** | The display name of the device | 
**log_collector_description** | **str** | The description/name of the log collector for this device | [optional] 
**link** | **str** | The URL link associated with the device | [optional] 
**aws_state** | **int** | The AWS instance state (if applicable): 1 indicates that the instance is running, 2 indicates that the instance is stopped and 3 the instance is terminated | [optional] 
**description** | **str** | The device description | [optional] 
**created_on** | **int** | The time, in epoch seconds format, that the device was added to your LogicMonitor account | [optional] 
**gcp_state** | **int** | The GCP instance state (if applicable): 1 indicates that the instance is running, 2 indicates that the instance is stopped and 3 the instance is terminated. | [optional] 
**auto_props_updated_on** | **int** | The time, in epoch seconds, that auto properties last ran and updated the properties table for this device | [optional] 
**scan_config_id** | **int** | The Id of the netscan configuration which was used to discover this device. 0 indicates that the device was not discovered by a scan | [optional] 
**enable_netflow** | **bool** | Indicates whether Netflow is enabled (true) or disabled (false) for the device | [optional] 
**last_data_time** | **int** | The last time, in epoch seconds, that the device received Netflow data | [optional] 
**host_group_ids** | **str** | The Id(s) of the groups the device is in, where multiple group ids are comma separated | [optional] 
**resource_ids** | [**list[NameAndValue]**](NameAndValue.md) | Any non-system properties (aside from system.categories) defined for this device | [optional] 
**op** | **str** | whether to use AND or OR for device matching | [optional] 
**current_log_collector_id** | **int** | The id of the Log collector currently collecting logs. | [optional] 
**log_collector_id** | **int** | The Id of the netflow collector associated with the device | [optional] 
**netflow_collector_description** | **str** | The description/name of the netflow collector for this device | [optional] 
**user_permission** | **str** | The read and/or write permissions for this device that are granted to the user who made the API request | [optional] 
**preferred_collector_group_name** | **str** | The name of the Collector Group associated with the device&#x27;s preferred collector | [optional] 
**auto_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any auto properties assigned to the device | [optional] 
**to_delete_time_in_ms** | **int** | The number of milliseconds until the device will be automatically deleted from your LogicMonitor account (a value of zero indicates that a future delete time/date has not been scheduled) | [optional] 
**contains_multi_value** | **bool** | request contains multi value field | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

