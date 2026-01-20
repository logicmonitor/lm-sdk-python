# UptimeWebCheck

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**JSONObject**](JSONObject.md) |  | [optional] 
**schema** | **str** | The scheme or protocol associated with the URL to check. Acceptable values are: http, https | [optional] 
**test_location** | [**WebsiteLocation**](WebsiteLocation.md) |  | 
**overall_alert_level** | **str** | The values can be warn|error|critical The level of alert to trigger if the website device device fails the number of checks specified by transition from the test locations specified by globalSmAlertCond | [optional] 
**polling_interval** | **int** | The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 The polling interval for the website device device, in units of minutes. This value indicates how often the website device device is checked. The minimum is 1 minute, and the maximum is 10 minutes | [optional] 
**last_updated** | **int** | The time (in epoch format) that the website device was updated | [optional] 
**stop_monitoring_by_folder** | **bool** | The values can be true|false where true: monitoring is disabled for all services in the website device device&#x27;s folder false: monitoring is not disabled for all services in website device device&#x27;s folder | [optional] 
**trigger_ssl_expiration_alert** | **bool** | Whether or not SSL expiration alerts should be triggered | [optional] 
**group_ids** | **list[int]** | The ids of the groups the website device is in | [optional] 
**stop_monitoring** | **bool** | The values can be true|false where true: monitoring is disabled for the website device device false: monitoring is enabled for the website device device If stopMonitoring&#x3D;true, then alerting will also be disabled by default for the website device device | [optional] 
**trigger_ssl_status_alert** | **bool** | Whether or not SSL status alerts should be triggered | [optional] 
**page_load_alert_time_in_ms** | **int** | The time in milliseconds that the page must load within for each step to avoid triggering an alert | [optional] 
**individual_sm_alert_enable** | **bool** | The values can be true|false where true: an alert will be triggered if a check fails from an individual test location false: an alert will not be triggered if a check fails from an individual test location | [optional] 
**checkpoints** | [**list[WebsiteCheckPoint]**](WebsiteCheckPoint.md) | The checkpoints from which the website device device is monitored. This object should reference each location specified in testLocation in addition to an &#x27;Overall&#x27; checkpoint | [optional] 
**steps** | [**list[UptimeWebCheckStep]**](UptimeWebCheckStep.md) | Required for type&#x3D;webcheck, an object comprising one or more steps, see the table below for the properties included in each step | [optional] 
**ignore_ssl** | **bool** | Whether or not SSL should be ignored, the default value is true | [optional] 
**transition** | **int** | The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 30 | 60 The number of checks that must fail before an alert is triggered | [optional] 
**global_sm_alert_cond** | **int** | The number of test locations that checks must fail at to trigger an alert, where the alert triggered will be consistent with the value of overallAlertLevel. Possible values and corresponding number of Site Monitor locations are 0 : all 1 : half 2 : more than one 3 : any | [optional] 
**cloned_from_host_id** | **str** | The id of the host from which the website device was cloned | [optional] 
**is_internal** | **bool** | Whether or not the website device is internal | [optional] 
**collectors** | [**list[WebsiteDeviceCollectorInfo]**](WebsiteDeviceCollectorInfo.md) | The collectors that are monitoring the website device, if the website device is internal | [optional] 
**domain** | **str** | Required for type&#x3D;webcheck, the domain of the service. This is the base URL of the service | [optional] 
**use_default_location_setting** | **bool** | The values can be true|false where true: The checkpoint locations configured in the website device device Default Settings will be used false: The checkpoint locations specified in the testLocation will be used | [optional] 
**use_default_alert_setting** | **bool** | The values can be true|false where true: The alert settings configured in the website device device Default Settings will be used false: Service Default Settings will not be used, and you will need to specify individualSMAlertEnable, individualAlertLevel, globalSmAlertConf, overallAlertLevel and pollingInterval | [optional] 
**individual_alert_level** | **str** | The values can be warn|error|critical The level of alert to trigger if the website device device fails a check from an individual test location | [optional] 
**properties** | [**list[NameAndValue]**](NameAndValue.md) | The properties associated with the website device | [optional] 
**status** | **str** | Whether the website device is dead (the collector is down) or not | [optional] 
**alert_expr** | **str** | The threshold (in days) for triggering SSL certification alerts | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

