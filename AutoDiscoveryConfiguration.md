# AutoDiscoveryConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistent_instance** | **bool** | Persist discovered instance | [optional] 
**schedule_interval** | **int** | Auto discovery schedule interval in minutes. 0 means host or data source changed. The values can be 0|15|60|1440 | [optional] 
**delete_inactive_instance** | **bool** | Delete inactive instance | [optional] 
**method** | [**AutoDiscoveryMethod**](AutoDiscoveryMethod.md) |  | 
**instance_auto_group_method** | **str** | Auto group method. The values can be none|netscaler|netscalerservicegroup|regex|esx|ilp | [optional] 
**instance_auto_group_method_params** | **str** | Auto group method&#x27;s parameters | [optional] 
**filters** | [**list[AutoDiscoveryFilter]**](AutoDiscoveryFilter.md) |  | [optional] 
**disable_instance** | **bool** | Disable discovered instance | [optional] 
**show_deleted_instance_days** | **int** | show deleted instance days | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

