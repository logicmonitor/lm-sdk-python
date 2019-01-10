# WebCheck

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema** | **str** | The scheme or protocol associated with the URL to check. Acceptable values are: http, https | [optional] 
**trigger_ssl_expiration_alert** | **bool** | Whether or not SSL expiration alerts should be triggered | [optional] 
**trigger_ssl_status_alert** | **bool** | Whether or not SSL status alerts should be triggered | [optional] 
**domain** | **str** | The domain of the service. This is the base URL of the service | 
**page_load_alert_time_in_ms** | **int** | The time in milliseconds that the page must load within for each step to avoid triggering an alert | [optional] 
**ignore_ssl** | **bool** | Whether or not SSL should be ignored | [optional] 
**steps** | [**list[WebCheckStep]**](WebCheckStep.md) | An object comprising one or more steps, see the table below for the properties included in each step | [optional] 
**alert_expr** | **str** | The threshold (in days) for triggering SSL certification alerts | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


