# EventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**event_source** | [**EventSource**](EventSource.md) |  | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**collector** | **str** | The EventSource collector type. The values can be wineventlog | syslog | snmptrap | echo | logfile | scriptevent | awsrss | azurerss | azureadvisor | gcpatom | awsrdspievent | azureresourcehealthevent | azureemergingissue | azureloganalyticsworkspacesevent | awstrustedadvisor | awshealth | awsorganizationalhealth | ipmievent | [optional] 
**origin_registry_id** | **str** | The Registry ID of the Exchange Integration this module is based from, including this field will set this as the module&#x27;s import base and mark the ID&#x27;s version as audited | [optional] 
**alert_body_template** | **str** | The alert message body for the EventSource | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 
**suppress_duplicates_es** | **bool** | Whether or not duplicate alerts have to be suppressed | [optional] 
**alert_subject_template** | **str** | The alert message subject for the EventSource | [optional] 
**event_source_filters** | [**list[EventSourceFilter]**](EventSourceFilter.md) |  | [optional] 
**alert_level** | **str** | The default alert level. The values can be warn | error | critical | doMapping | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**filters** | [**list[RestEventSourceFilter]**](RestEventSourceFilter.md) | The filters for the EventSource | [optional] 
**version** | **int** | The epoch time of the last update to the EventSource | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**audit_version** | **int** | The auditVersion of the EventSource | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**name** | **str** | The name of the EventSource | 
**clear_after_ack** | **bool** | Whether or not the alert should clear after acknowledgement | [optional] 
**is_in_use** | **bool** | Whether the LM module is currently in use | [optional] 
**alert_effective_ival** | **int** | The time in minutes after which the alert should clear | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

