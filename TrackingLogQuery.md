# TrackingLogQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | **list[str]** | partitions associated with the query | [optional] 
**is_paused** | **bool** | flag stating paused status of tracked query | [optional] 
**query** | **str** | query for log filter | 
**group_id** | **int** | Group ID associated with the tracked query. Defaults to &#x27;ungrouped&#x27; if not provided. | [optional] 
**create_epoch** | **int** | epoch of creation date | [optional] 
**last_update_epoch** | **int** | epoch of last update date | [optional] 
**label** | **str** | label for log filter | 
**version** | **str** | query grammar version | 
**aggregate** | **bool** |  | [optional] 
**group_name** | **str** | Group name associated with the tracked query | [optional] 
**tracked_query_uuid** | **str** | tracked query uuid for log filter | 
**admin_id** | **int** | admin id | [optional] 
**id** | **int** | id of record | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

