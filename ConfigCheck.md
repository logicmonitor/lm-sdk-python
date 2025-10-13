# ConfigCheck

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_clear_alert** | **bool** | Clear alert after ACKED or not | [optional] 
**origin_id** | **str** | Portable id for origin tracking | [optional] 
**name** | **str** | The ConfigCheck name | [optional] 
**alert_level** | **int** | The triggered alert level if config check failure. The values can be 1|2|3|4 where, 1: no alert, 2: warn alert, 3: error alert, 4: critical alert | [optional] 
**description** | **str** | The ConfigCheck description | [optional] 
**config_source_id** | **int** | The ConfigSource id | [optional] 
**id** | **int** | The ConfigCheck id | [optional] 
**type** | **str** | The ConfigCheck type. The values can be fetch|ignore|missing|value|groovy | [optional] 
**alert_effective_ival** | **int** | Alert effective interval | [optional] 
**script** | [**JSONObject**](JSONObject.md) |  | [optional] 
**alert_transition_interval** | **int** | The count that the alert must exist for these many poll cycles before it will be triggered | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

