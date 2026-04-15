# RestResourceUpdateCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collectors** | **list[str]** | The collectors for which devices should be updated, if include type is 4 | [optional] 
**groups** | **list[str]** | The groups for which devices should be updated, if include type is 3 | [optional] 
**type** | **int** | What types of IPs should be included for update. Options are 1 (update all), 2 (update devices discovered by this netscan), 3 (update by group list), 4 (update by collector list), 5 (do not update) | [optional] [default to 2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

