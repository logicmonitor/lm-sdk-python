# ExcludeDuplicateIps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectors** | **list[str]** | The collectors for which monitored devices should be used to identify and exclude duplicate IPs, if duplicate type is 4 | [optional] 
**groups** | **list[str]** | The groups for which devices should be used to identify and exclude duplicate IPs, if duplicate type is 3 | [optional] 
**type** | **int** | What types of duplicate IPs should be excluded. Options are 1 (matching any monitored devices), 2 (matching devices already discovered by this scan), 3 (matching devices in these groups), and 4 (matching devices assigned to these collectors) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


