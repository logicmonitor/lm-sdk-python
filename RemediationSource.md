# RemediationSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Access group Details in response | [optional] 
**groovy_script** | **str** | groovy script | [optional] 
**data_type** | **int** | The data type of remediation  source, default is 0. The values can be  0: remediation  source  1: raw ERI    | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**source** | **str** | The remediation  source | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**origin_registry_id** | **str** | The Registry ID of the Exchange Integration this module is based from, including this field will set this as the module&#x27;s import base and mark the ID&#x27;s version as audited | [optional] 
**script_type** | **str** | script type: groovy | powershell | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**name** | **str** | The remediation  source name | [optional] 
**in_use** | **str** | The remediation  source is in use | [optional] 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**installation_statuses** | **list[str]** | The remediation  Installation status | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

