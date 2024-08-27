# LogSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_method** | **str** |  | [optional] 
**applies_to_script** | **str** | The appliesToScript | [optional] 
**resource_mapping** | [**list[RestLogSourceResourceMappingV3]**](RestLogSourceResourceMappingV3.md) | resource mapping | [optional] 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**collection_attribute** | [**RestLogSourceCollectionAttributesV3Object**](RestLogSourceCollectionAttributesV3Object.md) |  | [optional] 
**changelogs** | [**list[UpdateReasons]**](UpdateReasons.md) |  | [optional] 
**description** | **str** | description | [optional] 
**filters** | [**list[RestLogSourceFilterV3]**](RestLogSourceFilterV3.md) |  | [optional] 
**technical_notes** | **str** | The technicalNotes | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**tags** | **list[str]** | tags | [optional] 
**log_fields** | [**list[RestLogSourceLogFieldV3]**](RestLogSourceLogFieldV3.md) |  | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**name** | **str** | The log source name | [optional] 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**collection_interval** | [**Duration**](Duration.md) |  | [optional] 
**group** | **str** | group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

