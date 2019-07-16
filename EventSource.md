# EventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_subject_template** | **str** | The alert message subject for the EventSource | [optional] 
**alert_level** | **str** | The default alert level: warn | error |critical | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**filters** | [**list[RestEventSourceFilter]**](RestEventSourceFilter.md) | The filters for the EventSource | [optional] 
**version** | **int** | The epoch time of the last update to the EventSource | [optional] 
**collector** | **str** | The EventSource type: logfile | snmptrap | syslog | wineventlog | scriptevent | [optional] 
**tags** | **str** | The Tags for the LMModule | [optional] 
**alert_body_template** | **str** | The alert message body for the EventSource | [optional] 
**name** | **str** | The name of the EventSource | 
**clear_after_ack** | **bool** | Whether or not the alert should clear after acknowledgement | [optional] 
**id** | **int** | The ID of the LMModule | 
**alert_effective_ival** | **int** | The time in minutes after which the alert should clear | 
**group** | **str** | The group the LMModule is in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


