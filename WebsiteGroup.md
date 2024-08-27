# WebsiteGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_path** | **str** | The full path of the group | [optional] 
**stop_monitoring** | **bool** | The values can be true|false where true: monitoring is disabled for the websites in the group false: monitoring is enabled for the websites in the group If stopMonitoring&#x3D;true, then alerting will also be disabled by default for the websites in the group | [optional] 
**user_permission** | **str** | The permission level of the user that made the API request. The values can be write|read|ack | [optional] 
**test_location** | [**WebsiteLocation**](WebsiteLocation.md) |  | [optional] 
**has_websites_disabled** | **bool** | Indicates if there are websites disabled in this group | [optional] 
**description** | **str** | The description of the group | [optional] 
**disable_alerting** | **bool** | The values can be true|false where true: alerting is disabled for the websites in the group false: alerting is enabled for the websites in the group If stopMonitoring&#x3D;true, then alerting will also be disabled by default for the websites in the group | [optional] 
**role_privileges** | **list[str]** | The privilege operations of the user&#x27;s role that made the API request.  The array can contain the values ack, sdt and/or threshold | [optional] 
**parent_id** | **int** | The Id of the parent group. If parentId&#x3D;1 then the group exists under the root group | [optional] 
**num_of_direct_websites** | **int** | The number of direct websites in this group | [optional] 
**name** | **str** | The name of the group | 
**num_of_direct_sub_groups** | **int** | The number of direct website groups in this group (excluding those in subgroups) | [optional] 
**id** | **int** | The Id of the group | [optional] 
**num_of_websites** | **int** | The number of websites in the service group, including the websites in sub groups | [optional] 
**properties** | [**list[NameAndValue]**](NameAndValue.md) | The website folder properties | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

