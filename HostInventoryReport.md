# HostInventoryReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sorted_by** | **str** | Specify a property that is included in the &#39;properties&#39; list that should be used to sort the devices/groups displayed in the report | [optional] 
**hosts_val_type** | **str** | host | group. The type of entities specified in the hostsVal field | [optional] 
**hosts_val** | **str** | The devices OR groups (full path) selected for the report, where multiple entities are separated by commas | [optional] 
**metrics** | [**list[HostInventoryMetric]**](HostInventoryMetric.md) | The instances will be included in the report | [optional] 
**properties** | **list[str]** | The properties that should be displayed in the report | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


