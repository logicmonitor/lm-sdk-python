# Netscan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | **str** | The user that created the policy | [optional] 
**collector_group_name** | **str** | The name of the group of the Collector associated with this Netscan | [optional] 
**method** | **str** | The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script | 
**collector_group** | **int** | The ID of the group of the Collector associated with this Netscan | [optional] 
**description** | **str** | The description of the Netscan Policy | [optional] 
**next_start** | **str** | The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule | [optional] 
**duplicate** | [**ExcludeDuplicateIps**](ExcludeDuplicateIps.md) | Information that determines how duplicate discovered devices should be handled | 
**version** | **int** | The Id of the device | [optional] 
**collector** | **int** | The ID of the Collector associated with this Netscan | 
**schedule** | [**NetScanSchedule**](NetScanSchedule.md) | Information related to the recurring execution schedule for the Netscan Policy | [optional] 
**collector_description** | **str** | The description of the Collector associated with this Netscan | [optional] 
**name** | **str** | The name of the Netscan Policy | 
**next_start_epoch** | **int** | The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule | [optional] 
**id** | **int** | The ID of the Netscan Policy | [optional] 
**nsg_id** | **int** | The ID of the group the policy belongs to | [optional] 
**group** | **str** | The group the Netscan policy should belong to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


