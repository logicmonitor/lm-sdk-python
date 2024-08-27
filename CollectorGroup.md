# CollectorGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_permission** | **str** | The permission level of the user that made the API request | [optional] 
**num_of_collectors** | **int** | The number of collectors that belong to the group | [optional] 
**auto_balance_instance_count_threshold** | **int** | Threshold for instance count strategy to check if a collector has high load | [optional] 
**description** | **str** | The description of the collector group | [optional] 
**highest_priority_collector_status** | [**RestHighestPriorityCollectorStatus**](RestHighestPriorityCollectorStatus.md) |  | [optional] 
**platform** | **str** | The platform limitation | [optional] 
**auto_balance** | **bool** | Whether the collector has autoBalance set as true or false | [optional] 
**custom_properties** | [**list[NameAndValue]**](NameAndValue.md) | The custom properties defined for the collector group | [optional] 
**num_of_hosts** | **int** | The number of hosts that belong to the group | [optional] 
**num_of_instances** | **int** | The number of instances that belong to the group | [optional] 
**name** | **str** | The name of the Collector Group | 
**auto_balance_strategy** | **str** | The auto balance strategy | [optional] 
**create_on** | **int** | The time at which the group was created in epoch format | [optional] 
**id** | **int** | The id of the Collector Group | [optional] 
**mismatch_version** | **bool** | Specifies if the version of all collectors in group is same | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

