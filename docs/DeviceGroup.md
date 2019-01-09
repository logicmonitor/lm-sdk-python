# DeviceGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_path** | **str** | The full path of the device group (i.e. if the group &#39;Dev&#39; is under a parent group named &#39;Production&#39;, the fullPath would be &#39;Production/Dev&#39; | [optional] 
**group_type** | **str** | The type of device group: normal and dynamic device groups will have groupType&#x3D;Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3) | [optional] 
**num_of_aws_devices** | **int** | The number of AWS devices that belong to this device group (includes AWS devices in sub groups) | [optional] 
**description** | **str** | The description of the device group | [optional] 
**applies_to** | **str** | The Applies to custom query for this group (only for dynamic groups) | [optional] 
**gcp_test_result_code** | **int** | The Status code result returned by the transaction that tests the GCP credentials associated with the GCP group | [optional] 
**disable_alerting** | **bool** | Indicates whether alerting is disabled (true) or enabled (false) for this device group | [optional] 
**aws_regions_info** | **str** | The number of instances in each AWS region (only applies to AWS groups) | [optional] 
**created_on** | **int** | The time, in epoch seconds format, that the device group was created | [optional] 
**has_netflow_enabled_devices** | **bool** | Whether if any Netflow enabled devices in this device group | [optional] 
**num_of_azure_devices** | **int** | The number of Azure devices that belong to this device group (includes Azure devices in sub groups) | [optional] 
**default_collector_description** | **str** | The description of the default collector assigned to the device group | [optional] 
**default_collector_id** | **int** | The Id of the default collector assigned to the device group | [optional] 
**aws_test_result** | [**AwsAccountTestResult**](AwsAccountTestResult.md) | The String result returned by the transaction that tests the AWS credentials associated with the AWS group | [optional] 
**extra** | **object** | The extra setting for cloud group | [optional] 
**num_of_direct_sub_groups** | **int** | The number of sub-groups that belong only to this device group (doesn&#39;t include groups under sub-groups) | [optional] 
**num_of_direct_devices** | **int** | The number of AWS and normal devices that belong only to this device group (doesn&#39;t include devices in sub-groups) | [optional] 
**id** | **int** | The id of the device group | [optional] 
**enable_netflow** | **bool** | Indicates whether Netflow is enabled (true) or disabled (false) for the device group | [optional] 
**azure_test_result_code** | **int** | The Status code result returned by the transaction that tests the Azure credentials associated with the Azure group | [optional] 
**effective_alert_enabled** | **bool** | Whether or not alerting is effectively disabled for this device group (alerting may be disabled at a higher level, e.g. parent group) | [optional] 
**default_collector_group_description** | **str** | The description of the default collector group assigned to the device group | [optional] 
**user_permission** | **str** | The permissions for the device group that are granted to the user that made this API request | [optional] 
**gcp_regions_info** | **str** |  | [optional] 
**default_collector_group_id** | **int** | The collector group id of the default collector assigned to the device group | [optional] 
**group_status** | **str** | normal | dead  The status of this device group, where possible statuses are normal and dead. A group with a status of dead may indicate that one or more devices are dead within the group | [optional] 
**num_of_gcp_devices** | **int** |  | [optional] 
**azure_test_result** | [**AzureAccountTestResult**](AzureAccountTestResult.md) | The String result returned by the transaction that tests the Azure credentials associated with the Azure group | [optional] 
**parent_id** | **int** | The id of the parent group for this device group (the root device group has an Id of 1) | [optional] 
**aws_test_result_code** | **int** | The Status code result returned by the transaction that tests the AWS credentials associated with the AWS group | [optional] 
**default_load_balance_collector_group_id** | **int** | The id of the default Load Balanced Collector Group assigned to the device group | [optional] 
**custom_properties** | [**list[NameAndValue]**](NameAndValue.md) | The properties associated with this device group | [optional] 
**num_of_hosts** | **int** | The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups) | [optional] 
**name** | **str** | The name of the device group | 
**gcp_test_result** | [**GcpAccountTestResult**](GcpAccountTestResult.md) | The result returned by the transaction that tests the GCP credentials associated with the GCP group | [optional] 
**azure_regions_info** | **str** | The number of instances in each Azure region (only applies to Azure groups) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


