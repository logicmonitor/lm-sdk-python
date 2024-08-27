# PropertyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_option** | **str** | The property rule schedule option. The values can be onAP|onAPpropertyChanges | [optional] 
**groovy_script** | **str** | groovy script | [optional] 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Access group Details in response | [optional] 
**windows_script** | **str** | external windows script name | [optional] 
**data_type** | **int** | The data type of property source, default is 0. The values can be  0: property source  1: raw ERI    | [optional] 
**description** | **str** | The property rule description | [optional] 
**applies_to** | **str** | The property rule applies to | [optional] 
**technology** | **str** | The technology notes | [optional] 
**linux_cmdline** | **str** | external linux script args | [optional] 
**version** | **int** | The property rule version | [optional] 
**windows_cmdline** | **str** | external windows script args | [optional] 
**lineage_id** | **str** | LM module lineageId | [optional] 
**tags** | **str** | The property rule tags | [optional] 
**audit_version** | **int** | The property rule auditVersion | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**script_type** | **str** | script type: embed | powershell | external | [optional] 
**name** | **str** | The property rule name | [optional] 
**checksum** | **str** | LM module checksum | [optional] 
**interval** | **int** | The collect interval of raw ERI | [optional] 
**id** | **int** |  | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**linux_script** | **str** | external linux script name | [optional] 
**group** | **str** | The property rule group name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

