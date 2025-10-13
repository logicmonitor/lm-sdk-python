# RestOidV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Access group Details in response | [optional] 
**origin_registry_id** | **str** | The Registry ID of the Exchange Integration this module is based from, including this field will set this as the module&#x27;s import base and mark the ID&#x27;s version as audited | [optional] 
**checksum** | **str** | Checksum generated from the content of the module | [optional] 
**id** | **int** | Local ID of the module | [optional] 
**oid** | **str** | The OID pattern to match to | 
**categories** | **str** | Categories to match the OID on | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**lineage_id** | **str** | The lineage ID that the LMModule belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

