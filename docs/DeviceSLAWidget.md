# DeviceSLAWidget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_in_week** | **str** | The days that SLA should be computed for, separated by commas. 1&#x3D;Sunday, 2&#x3D;Monday, 3&#x3D;Tuesday, 4&#x3D;Wednesday, 5&#x3D;Thursday, 6&#x3D;Friday, 7&#x3D;Saturday. | [optional] 
**display_type** | **int** | Whether or not selected metrics should be combined into one number (displayType:0) or should be displayed individually, up to four metrics (displayType:1) | [optional] 
**top_x** | **int** | Top list size for each point, 1 means aggregate | [optional] 
**timezone** | **str** | The specific timezone for the widget | [optional] 
**bottom_label** | **str** | The services that should be used to compute the SLA, where each service should include serviceGroup and service | [optional] 
**period_in_one_day** | **str** | The period during the selected days that the SLA should be computed for. * &#x3D; all day, or a time range can be specified in the format of \&quot;hh:mm TO hh:mm\&quot;, e.g. \&quot;01:15 TO 17:15\&quot; | [optional] 
**metrics** | [**list[SlaMetric]**](SlaMetric.md) | The metrics (datapoints) that should be used to compute the SLA, where each service should include groupName (can be *), deviceName (can be *), dataSourceId or dataSourceFullName, instances (can be *), metric (datapoint), threshold, and exclusionSDTType (empty string means SDT periods will not be excluded, \&quot;group\&quot; means SDT periods at the device group level will be excluded, and \&quot;device\&quot; means SDT periods at the device level will be excluded) | 
**unmonitored_time_type** | **int** | How no data should be treated: 0 &#x3D; unmonitored time will be ignored &amp; subtracted from the total possible time, 1 &#x3D; unmonitored time will be subtracted from uptime and counted as a violation, 2 &#x3D; unmonitored time will be added to uptime and counted as available | [optional] 
**color_thresholds** | [**list[ColorThreshold]**](ColorThreshold.md) | The threshold of color changes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


