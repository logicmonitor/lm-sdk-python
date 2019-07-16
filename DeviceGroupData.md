# DeviceGroupData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** | The Applies to custom query for this group (only for dynamic groups) | [optional] 
**aws_regions_info** | **str** | The number of instances in each AWS region (only applies to AWS groups) | [optional] 
**azure_regions_info** | **str** | The number of instances in each Azure region (only applies to Azure groups) | [optional] 
**description** | **str** | The description of the device group | [optional] 
**full_path** | **str** | The full path of the device group (i.e. if the group &#39;Dev&#39; is under a parent group named &#39;Production&#39;, the fullPath would be &#39;Production/Dev&#39; | [optional] 
**gcp_regions_info** | **str** |  | [optional] 
**group_type** | **str** | The type of device group: normal and dynamic device groups will have groupType&#x3D;Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3) | [optional] 
**id** | **int** | The id of the device group | [optional] 
**name** | **str** | The name of the device group | [optional] 
**num_of_direct_devices** | **int** | The number of AWS and normal devices that belong only to this device group (doesn&#39;t include devices in sub-groups) | [optional] 
**num_of_direct_sub_groups** | **int** | The number of sub-groups that belong only to this device group (doesn&#39;t include groups under sub-groups) | [optional] 
**num_of_hosts** | **int** | The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups) | [optional] 
**user_permission** | **str** | The permissions for the device group that are granted to the user that made this API request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


