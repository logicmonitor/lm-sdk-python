# EventSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_body_template** | **str** | The alert message body for the EventSource | [optional] 
**alert_effective_ival** | **int** | The time in minutes after which the alert should clear | 
**alert_level** | **str** | The default alert level: warn | error |critical | [optional] 
**alert_subject_template** | **str** | The alert message subject for the EventSource | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**clear_after_ack** | **bool** | Whether or not the alert should clear after acknowledgement | [optional] 
**collector** | **str** | The EventSource type: logfile | snmptrap | syslog | wineventlog | scriptevent | [optional] 
**description** | **str** | The description for the LMModule | [optional] 
**filters** | [**list[RestEventSourceFilter]**](RestEventSourceFilter.md) | The filters for the EventSource | [optional] 
**group** | **str** | The group the LMModule is in | [optional] 
**id** | **int** | The ID of the LMModule | 
**name** | **str** | The name of the EventSource | 
**tags** | **str** | The Tags for the LMModule | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**version** | **int** | The epoch time of the last update to the EventSource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


