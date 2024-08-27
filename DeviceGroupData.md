# DeviceGroupData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_path** | **str** | The full path of the device group (i.e. if the group &#x27;Dev&#x27; is under a parent group named &#x27;Production&#x27;, the fullPath would be &#x27;Production/Dev&#x27; | [optional] 
**group_type** | **str** | The type of device group: normal and dynamic device groups will have groupType&#x3D;Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3) | [optional] 
**user_permission** | **str** | The permissions for the device group that are granted to the user that made this API request | [optional] 
**gcp_regions_info** | **str** |  | [optional] 
**description** | **str** | The description of the device group | [optional] 
**applies_to** | **str** | The Applies to custom query for this group (only for dynamic groups) | [optional] 
**role_privileges** | **list[str]** | The role privilege operations for the device group that are granted to the user that made this API request | [optional] 
**aws_regions_info** | **str** | The number of instances in each AWS region (only applies to AWS groups) | [optional] 
**num_of_hosts** | **int** | The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups) | [optional] 
**name** | **str** | The name of the device group | [optional] 
**num_of_direct_sub_groups** | **int** | The number of sub-groups that belong only to this device group (doesn&#x27;t include groups under sub-groups) | [optional] 
**num_of_direct_devices** | **int** | The number of AWS and normal devices that belong only to this device group (doesn&#x27;t include devices in sub-groups) | [optional] 
**id** | **int** | The id of the device group | [optional] 
**azure_regions_info** | **str** | The number of instances in each Azure region (only applies to Azure groups) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

