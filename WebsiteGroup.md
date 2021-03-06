# WebsiteGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the group | [optional] 
**disable_alerting** | **bool** | true: alerting is disabled for the websites in the group false: alerting is enabled for the websites in the group If stopMonitoring&#x3D;true, then alerting will also by default be disabled for the websites in the group | [optional] 
**full_path** | **str** | The full path of the group | [optional] 
**has_websites_disabled** | **bool** |  | [optional] 
**id** | **int** | The Id of the group | [optional] 
**name** | **str** | The name of the group | 
**num_of_direct_sub_groups** | **int** | The number of direct website groups in this group (exlcuding those in subgroups) | [optional] 
**num_of_direct_websites** | **int** |  | [optional] 
**num_of_websites** | **int** |  | [optional] 
**parent_id** | **int** | The Id of the parent group. If parentId&#x3D;1 then the group exists under the root  group | [optional] 
**properties** | [**list[NameAndValue]**](NameAndValue.md) |  | [optional] 
**stop_monitoring** | **bool** | true: monitoring is disabled for the websites in the group false: monitoring is enabled for the websites in the group If stopMonitoring&#x3D;true, then alerting will also by default be disabled for the websites in the group | [optional] 
**test_location** | [**WebsiteLocation**](WebsiteLocation.md) |  | [optional] 
**user_permission** | **str** | The permission level of the user that made the API request. Acceptable values are: write, read, ack | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


