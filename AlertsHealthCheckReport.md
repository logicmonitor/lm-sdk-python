# AlertsHealthCheckReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | Filter for the alert level (e.g., all, error, critical). | [optional] 
**active_only** | **bool** | true: only alerts that are still alerting (i.e. haven&#x27;t yet cleared) will be displayed in the report false: active alerts and cleared alerts will both be displayed in the report | [optional] 
**chain** | **str** | Filter for the escalation chain. Glob expressions are supported. | [optional] 
**instance** | **str** | Filter to restrict the report to a specific  instance. Glob expressions are supported. | [optional] 
**anomaly** | **str** | Filter alerts by anomaly status. | [optional] 
**date_range** | **str** | The Time Range configured for the report. For example, Last 2 hours, Last 24 hours, etc. | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns that will be displayed in the report. You should specify the columns in the order in which you&#x27;d like them to be displayed. All column names need to be included in this object, but each column should have an associated isHidden field that indicates whether it is displayed or not. Severity, Group, Device, Instance, Datapoint, Thresholds, Value, Began, End, Rule, Chain, Acked, Acked By, Acked On, Notes, In SDT,Dependancy Role,Notification State | [optional] 
**data_point** | **str** | Filter to restrict the report to a specific datapoint. Glob expressions are supported. | [optional] 
**sdt_filter** | **str** | Filter alerts based on SDT status. | [optional] 
**rule** | **str** | Filter for the rule. Glob expressions are supported. | [optional] 
**monitored_object_groups** | **str** | The resource groups selected for the report filter | [optional] 
**ack_filter** | **str** | Filter by acknowledgement status: all, acked, or nonacked. | [optional] 
**dependency_routing_state** | **str** |  | [optional] 
**dependency_role** | **str** |  | [optional] 
**clear_filter** | **str** | yes: Only cleared alerts will be included in the response. no: only active alerts will be included in the response. all: both active and cleared alerts will be included in the response | [optional] 
**host** | **str** | Filter to restrict the report to a specific device. Glob expressions are supported. | [optional] 
**host_group** | **str** | Filter to restrict the report to a specific group. Glob expressions are supported. | [optional] 
**data_source** | **str** | Filter to restrict the report to a specific datasource instance. Glob expressions are supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

