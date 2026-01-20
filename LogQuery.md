# LogQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | **list[str]** | partitions associated with the query | [optional] 
**trackable** | **bool** |  | [optional] 
**identifier** | [**ObjectIdentifier**](ObjectIdentifier.md) |  | [optional] 
**start_ms** | **int** | start time epoch in ms for log filter | [optional] 
**end_ms** | **int** | end time epoch in ms for log filter | [optional] 
**query** | **str** | query for log filter | [optional] 
**group_id** | **int** | group id | [optional] 
**into_rest_response** | [**RestResponse**](RestResponse.md) |  | [optional] 
**label** | **str** | label for log filter | [optional] 
**favourite** | **bool** |  | [optional] 
**version** | **str** | query grammar version | 
**duration** | **str** | time range | [optional] 
**admin_name** | **str** | username associated with the log query | [optional] 
**group_name** | **str** | log query group name | [optional] 
**related_into_rest_response** | [**RestResponse**](RestResponse.md) |  | [optional] 
**model** | **str** |  | [optional] 
**id** | **str** | uuid of record | 
**is_aggregate** | **bool** | is aggregate query or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

