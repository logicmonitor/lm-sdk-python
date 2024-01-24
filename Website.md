# Website

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **object** | The website template | [optional] 
**test_location** | [**WebsiteLocation**](WebsiteLocation.md) | The locations from which the website is monitored. If the website is internal, this field should include Collectors. If Non-Internal, possible test locations are: 1 : US - LA 2 : US - DC 3 : US - SF 4 : Europe - Dublin 5 : Asia - Singapore 6 : Australia - Sydney testLocation:\&quot;{all:true}\&quot; indicates that the service will be monitored from all checkpoint locations testLocation:\&quot;{smgIds:[1,2,3]}\&quot; indicates that the service will be monitored from checkpoint locations 1, 2 and 3 testLocation:\&quot;{collectorIds:[85,90]}\&quot; indicates that the service will be monitored by Collectors 85 and 90 | 
**group_id** | **int** | The id of the group the website is in | [optional] 
**overall_alert_level** | **str** | The values can be warn|error|critical The level of alert to trigger if the website fails the number of checks specified by transition from the test locations specified by globalSmAlertCond | [optional] 
**polling_interval** | **int** | The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 The polling interval for the website, in units of minutes. This value indicates how often the website is checked. The minimum is 1 minute, and the maximum is 10 minutes | [optional] 
**description** | **str** | The description of the website | [optional] 
**disable_alerting** | **bool** | The values can be true|false where true: alerting is disabled for the website false: alerting is enabled for the website If stopMonitoring&#x3D;true, then alerting will also be disabled by default for the website | [optional] 
**type** | **str** | The values can be pingcheck|webcheck Specifies the type of service | 
**role_privileges** | **list[str]** | The role privilege operation(s) for this website that are granted to the user who made the API request | [optional] 
**last_updated** | **int** | The time (in epoch format) that the website was updated | [optional] 
**stop_monitoring_by_folder** | **bool** | The values can be true|false where true: monitoring is disabled for all services in the website&#39;s folder false: monitoring is not disabled for all services in website&#39;s folder | [optional] 
**id** | **int** | The id of the website | [optional] 
**stop_monitoring** | **bool** | The values can be true|false where true: monitoring is disabled for the website false: monitoring is enabled for the website If stopMonitoring&#x3D;true, then alerting will also be disabled by default for the website | [optional] 
**user_permission** | **str** | The values can be write|read|ack. The permission level of the user that made the API request | [optional] 
**individual_sm_alert_enable** | **bool** | The values can be true|false where true: an alert will be triggered if a check fails from an individual test location false: an alert will not be triggered if a check fails from an individual test location | [optional] 
**checkpoints** | [**list[WebsiteCheckPoint]**](WebsiteCheckPoint.md) | The checkpoints from the which the website is monitored. This object should reference each location specified in testLocation in addition to an &#39;Overall&#39; checkpoint | [optional] 
**steps** | [**list[WebCheckStep]**](WebCheckStep.md) | Required for type&#x3D;webcheck , An object comprising one or more steps, see the table below for the properties included in each step | [optional] 
**transition** | **int** | The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 30 | 60 The number of checks that must fail before an alert is triggered | [optional] 
**global_sm_alert_cond** | **int** | The number of test locations that checks must fail at to trigger an alert, where the alert triggered will be consistent with the value of overallAlertLevel. Possible values and corresponding number of Site Monitor locations are 0 : all 1 : half 2 : more than one 3 : any | [optional] 
**is_internal** | **bool** | Whether or not the website is internal | [optional] 
**collectors** | [**list[WebsiteCollectorInfo]**](WebsiteCollectorInfo.md) | The collectors that are monitoring the website, if the website is internal | [optional] 
**domain** | **str** | Required for type&#x3D;webcheck , The domain of the service. This is the base URL of the service | [optional] 
**name** | **str** | The name of the website | 
**use_default_location_setting** | **bool** | The values can be true|false where true: The checkpoint locations configured in the website Default Settings will be used false: The checkpoint locations specified in the testLocation will be used | [optional] 
**use_default_alert_setting** | **bool** | The values can be true|false where true: The alert settings configured in the website Default Settings will be used false: Service Default Settings will not be used, and you will need to specify individualSMAlertEnable, individualAlertLevel, globalSmAlertConf, overallAlertLevel and pollingInterval | [optional] 
**individual_alert_level** | **str** | The values can be warn|error|critical The level of alert to trigger if the website fails a check from an individual test location | [optional] 
**properties** | [**list[NameAndValue]**](NameAndValue.md) | The properties associated with the website | [optional] 
**status** | **str** | Whether the website is dead (the collector is down) or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


