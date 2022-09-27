# AutoDiscoveryConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistent_instance** | **bool** | persist discovered instance | [optional] 
**schedule_interval** | **int** | auto discovery schedule interval in minutes, 0 means host or data source changed, values can be 0|15|60|1440 | [optional] 
**delete_inactive_instance** | **bool** | delete inactive instance | [optional] 
**method** | [**AutoDiscoveryMethod**](AutoDiscoveryMethod.md) | method used to do auto discovery instance | 
**instance_auto_group_method** | **str** | auto group method | [optional] 
**instance_auto_group_method_params** | **str** | auto group method&#39;s parameters | [optional] 
**filters** | [**list[AutoDiscoveryFilter]**](AutoDiscoveryFilter.md) |  | [optional] 
**disable_instance** | **bool** | disable discovered instance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


