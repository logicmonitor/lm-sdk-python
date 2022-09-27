# CollectorGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_permission** | **str** | The permission level of the user that made the API request | [optional] 
**num_of_collectors** | **int** | The number of Collectors that belong to the group | [optional] 
**auto_balance_instance_count_threshold** | **int** | threshold for instance count strategy to check if a collector has high load | [optional] 
**description** | **str** | The description of the Collector Group | [optional] 
**highest_priority_collector_status** | [**RestHighestPriorityCollectorStatus**](RestHighestPriorityCollectorStatus.md) | The status of the highest priority sub collector | [optional] 
**platform** | **str** | the platform limitation | [optional] 
**auto_balance** | **bool** | if the collector has autoBalance set as true or false | [optional] 
**custom_properties** | [**list[NameAndValue]**](NameAndValue.md) | The custom properties defined for the Collector group | [optional] 
**num_of_hosts** | **int** | The number of hosts that belong to the group | [optional] 
**num_of_instances** | **int** | The number of instances that belong to the group | [optional] 
**name** | **str** | The name of the Collector Group | 
**auto_balance_strategy** | **str** | the auto balance strategy | [optional] 
**create_on** | **int** | The time at which the group was created, in epoch format | [optional] 
**id** | **int** | The id of the Collector Group | [optional] 
**mismatch_version** | **bool** | specifies if the version of all collectors in group is same | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


