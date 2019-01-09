# Website

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **object** | The website template | [optional] 
**stop_monitoring** | **bool** | true: monitoring is disabled for the website false: monitoring is enabled for the website If stopMonitoring&#x3D;true, then alerting will also by default be disabled for the website | [optional] 
**user_permission** | **str** | write | read | ack. The permission level of the user that made the API request | [optional] 
**test_location** | [**WebsiteLocation**](WebsiteLocation.md) | The locations from which the website is monitored. If the website is internal, this field should include Collectors. If Non-Internal, possible test locations are: 1 : US - LA 2 : US - DC 3 : US - SF 4 : Europe - Dublin 5 : Asia - Singapore 6 : Australia - Sydney testLocation:\&quot;{all:true}\&quot; indicates that the service will be monitored from all checkpoint locations testLocation:\&quot;{smgIds:[1,2,3]}\&quot; indicates that the service will be monitored from checkpoint locations 1, 2 and 3 testLocation:\&quot;{collectorIds:[85,90]}\&quot; indicates that the service will be monitored by Collectors 85 and 90 | 
**group_id** | **int** | The id of the group the website is in | [optional] 
**overall_alert_level** | **str** | warn | error | critical The level of alert to trigger if the website fails the number of checks specified by transition from the test locations specified by globalSmAlertCond | [optional] 
**polling_interval** | **int** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 The polling interval for the website, in units of minutes. This value indicates how often the website is checked. The minimum is 1 minute, and the maximum is 10 minutes | [optional] 
**description** | **str** | The description of the website | [optional] 
**individual_sm_alert_enable** | **bool** | true: an alert will be triggered if a check fails from an individual test location false: an alert will not be triggered if a check fails from an individual test location | [optional] 
**checkpoints** | [**list[WebsiteCheckPoint]**](WebsiteCheckPoint.md) | The checkpoints from the which the website is monitored. This object should reference each location specified in testLocation in addition to an &#39;Overall&#39; checkpoint | [optional] 
**disable_alerting** | **bool** | true: alerting is disabled for the website false: alerting is enabled for the website If stopMonitoring&#x3D;true, then alerting will also by default be disabled for the website | [optional] 
**type** | **str** | The type of the website. Acceptable values are: pingcheck, webcheck | 
**transition** | **int** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 30 | 60 The number of checks that must fail before an alert is triggered | [optional] 
**global_sm_alert_cond** | **int** | The number of test locations that checks must fail at to trigger an alert, where the alert triggered will be consistent with the value of overallAlertLevel. Possible values and corresponding number of Site Monitor locations are 0 : all 1 : half 2 : more than one 3 : any | [optional] 
**is_internal** | **bool** | Whether or not the website is internal | [optional] 
**stop_monitoring_by_folder** | **bool** | true: monitoring is disabled for all services in the website&#39;s folder false: monitoring is not disabled for all services in website&#39;s folder | [optional] 
**collectors** | [**list[WebsiteCollectorInfo]**](WebsiteCollectorInfo.md) | The collectors that are monitoring the website, if the website is internal | [optional] 
**name** | **str** | The name of the website | 
**id** | **int** | The id of the website | [optional] 
**use_default_location_setting** | **bool** | true: The checkpoint locations configured in the website Default Settings will be used false: The checkpoint locations specified in the testLocation will be used | [optional] 
**use_default_alert_setting** | **bool** | true: The alert settings configured in the website Default Settings will be used false: Service Default Settings will not be used, and you will need to specify individualSMAlertEnable, individualAlertLevel, globalSmAlertConf, overallAlertLevel and pollingInterval | [optional] 
**individual_alert_level** | **str** | warn | error | critical The level of alert to trigger if the website fails a check from an individual test location | [optional] 
**properties** | [**list[NameAndValue]**](NameAndValue.md) | The properties associated with the website | [optional] 
**status** | **str** | Whether is the website dead (the collector is down) or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


