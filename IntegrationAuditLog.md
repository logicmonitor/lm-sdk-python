# IntegrationAuditLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **str** | HTTP request headers used in alert delivery | [optional] 
**alert_type** | **int** | The type of the alert | [optional] 
**integration_name** | **str** | The name of integration | [optional] 
**num_retries** | **int** | The number of times delivery was retried | [optional] 
**integration_alert_status** | **str** | The Integration Alert Status used for delivery | [optional] 
**error_message** | **str** | Error message (if any) from ADC | [optional] 
**external_ticket_id** | **str** | The parsed External Ticket ID from alert delivery | [optional] 
**payload_format** | **str** | The outbound payload format | [optional] 
**url** | **str** | The URL where the alert was delivered to | [optional] 
**happened_on_ms** | **int** | When the delivery result was saved in LMES | [optional] 
**integration_type** | **str** | The type of integration | [optional] 
**alert_instance_id** | **str** | The id of the alert instance | [optional] 
**payload** | **str** | The HTTP Request payload | [optional] 
**http_response_code** | **int** | The HTTP Response Code received from 3rd party API | [optional] 
**id** | **str** | The id of audit log record | [optional] 
**alert_id** | **str** | The id of the alert | [optional] 
**http_response** | **str** | The HTTP Response Body received after alert delivery | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


