# AdrOutputList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Next page cursor for diagnostic results (v4 logs meta.cursor): device history when start/end set; or alert latest-executions when moduleType is diagnostic. Not set when moduleType is both. | [optional] 
**total** | **int** | Number of items returned | [optional] 
**sort** | **str** | Sort applied to history results (echo of request, e.g. -startTime). | [optional] 
**items** | [**list[AdrOutput]**](AdrOutput.md) | Matched ADR execution result rows | [optional] 
**remediation_cursor** | **str** | Next page cursor for remediation results (v4 logs meta.cursor): device history when start/end set; or alert latest-executions when moduleType is remediation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

