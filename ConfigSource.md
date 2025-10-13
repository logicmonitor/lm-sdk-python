# ConfigSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**display_name** | **str** | The ConfigSource display name | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**collect_method** | **str** | The method to collect data | [optional] 
**origin_registry_id** | **str** | The Registry ID of the Exchange Integration this module is based from, including this field will set this as the module&#x27;s import base and mark the ID&#x27;s version as audited | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 
**collector_attribute** | [**CollectorAttribute**](CollectorAttribute.md) |  | [optional] 
**auto_discovery_config** | [**AutoDiscoveryConfiguration**](AutoDiscoveryConfiguration.md) |  | [optional] 
**ad_parameters** | [**DataSource**](DataSource.md) |  | [optional] 
**config_checks** | [**list[ConfigCheck]**](ConfigCheck.md) | The List of ConfigChecks | [optional] 
**enable_auto_discovery** | **bool** | Enable active discovery if ConfigSource has multiple instances. true|false | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**version** | **int** | The ConfigSource version | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**audit_version** | **int** | The ConfigSource audit version | [optional] 
**has_multi_instances** | **bool** | Whether the ConfigSource has multiple instances. true|false | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**collect_interval** | **int** | The ConfigSource data collect interval | [optional] 
**name** | **str** | The config source name | [optional] 
**timestamp_format** | **str** | Timestamp format. ex. yyyy-MM-dd hh:mm:ss | [optional] 
**file_format** | **str** | Configuration file format. The values can be arbitrary|unix|java-properties|JSON|XML | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

