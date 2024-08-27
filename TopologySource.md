# TopologySource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collector_attribute** | [**ScriptCollectorAttribute**](ScriptCollectorAttribute.md) |  | 
**collection_method** | **str** | The topology will be build on properties or traditional way, default &#x27;script&#x27; | 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**version** | **int** | The TopologySource version | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**audit_version** | **int** | The TopologySource audit Version | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**collect_interval** | **int** | The TopologySource data collect interval in seconds, default 3600 | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**name** | **str** | The TopologySource name | 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

