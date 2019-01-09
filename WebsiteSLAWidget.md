# WebsiteSLAWidget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_in_week** | **str** | The days that SLA should be computed for, separated by commas. 1&#x3D;Sunday, 2&#x3D;Monday, 3&#x3D;Tuesday, 4&#x3D;Wednesday, 5&#x3D;Thursday, 6&#x3D;Friday, 7&#x3D;Saturday | [optional] 
**timezone** | **str** | The specific timezone for the widget | [optional] 
**period_in_one_day** | **str** | The period during the selected days that the SLA should be computed for. * &#x3D; all day, or a time range can be specified in the format of \&quot;hh:mm TO hh:mm\&quot;, e.g. \&quot;01:15 TO 17:15\&quot; | [optional] 
**items** | [**list[WebsiteItemConfig]**](WebsiteItemConfig.md) | The websites that should be used to compute the SLA | 
**color_thresholds** | [**list[ColorThreshold]**](ColorThreshold.md) | The threshold of color changes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


