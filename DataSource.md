# DataSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eri_discovery_config** | [**ScriptERIDiscoveryAttributeV3**](ScriptERIDiscoveryAttributeV3.md) |  | [optional] 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**display_name** | **str** | The data source display name | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**collect_method** | **str** | The  method to collect data. The values can be snmp|ping|exs|webpage|wmi|cim|datadump|dns|ipmi|jdbb|script|udp|tcp|xen | 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**data_points** | [**list[DataPoint]**](DataPoint.md) | The data point list | [optional] 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 
**collector_attribute** | [**CollectorAttribute**](CollectorAttribute.md) |  | 
**auto_discovery_config** | [**AutoDiscoveryConfiguration**](AutoDiscoveryConfiguration.md) |  | [optional] 
**payload_version** | **int** | The DataSource payload version for custom metrics | [optional] 
**use_wild_value_as_uuid** | **bool** | Use wild-value as unique identifier in case of multi instance datasource: true|false | [optional] 
**enable_auto_discovery** | **bool** | Enable Auto Discovery or not when this data source has multi instance: false|true | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**version** | **int** | The data source version | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**audit_version** | **int** | The data source audit version | [optional] 
**has_multi_instances** | **bool** | If the DataSource has multi instance: true|false | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**eri_discovery_interval** | **int** | The DataSource data collect interval | [optional] 
**enable_eri_discovery** | **bool** | Enable ERI Discovery or not: false|true | [optional] 
**collect_interval** | **int** | The DataSource data collect interval | 
**name** | **str** | The data source name | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

