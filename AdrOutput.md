# AdrOutput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executed_by** | **str** | User or principal that triggered the execution (when available) | [optional] 
**remediation_source_id** | **int** | Remediation Source module id when sourceType is remediationSource | [optional] 
**execution_status** | **str** | Execution status name (enum string from collector pipeline) | [optional] 
**module_name** | **str** | Logic module display name | [optional] 
**host_id** | **int** | Device (resource) id | [optional] 
**triggered_type** | **str** | How the execution was triggered (e.g. manual, automatic) | [optional] 
**output** | **str** | Script output / message captured for this execution | [optional] 
**execution_id** | **int** | LogicModule execution id | [optional] 
**source_type** | **str** | Row kind: diagnosticSource or remediationSource (exact values as in the JSON response). | [optional] 
**diagnostic_source_id** | **int** | Diagnostic Source module id when sourceType is diagnosticSource | [optional] 
**start_time** | **int** | Execution start time in epoch seconds (UTC), when available | [optional] 
**alert_id** | **str** | Alert id when the execution was tied to an alert (may be empty). | [optional] 
**end_time** | **int** | Execution end or log timestamp in epoch seconds (UTC), when available | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

