# RestSDTV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** | Notes regarding the SDT | [optional] 
**timezone** | **str** | The specific timezone for SDT | [optional] 
**default_value** | **datetime** |  | [optional] 
**month_day** | **int** | The values can be -3 | 1 | 2....| 31. Specifies the day of the month that the SDT will be active for a monthly SDT. Use -3 for the last day of the month. | [optional] 
**type** | **str** | The type of resource that this SDT is for. The values can be CollectorSDT | DeviceDataSourceInstanceSDT | DeviceBatchJobSDT | DeviceClusterAlertDefSDT | DeviceDataSourceInstanceGroupSDT | DeviceDataSourceSDT | DeviceEventSourceSDT | ResourceGroupSDT | ResourceSDT | WebsiteCheckpointSDT | WebsiteGroupSDT | WebsiteSDT | DeviceLogPipeLineResourceSDT | 
**duration** | **int** | The duration of the SDT in minutes | [optional] 
**data_source_id** | **int** | The id of the datasource instance that the SDT will be associated with | [optional] 
**hour** | **int** | The values can be 1 | 2....| 24. Specifies the hour that the SDT will start for a repeating SDT (daily, weekly, or monthly) | [optional] 
**week_day** | **str** | The week day of sdt. For weekly SDT, supports comma-separated values like &#x27;Monday,Friday&#x27;. Values can be SUNDAY|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY | [optional] 
**ended_at_ms** | **int** | The time milliseconds that the SDT will end or has ended. | [optional] 
**resource_group_id** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**id** | **str** | The Id of the SDT. This value will be in the following format \&quot;XX_##\&quot; where XX will refer to the type of SDT and ## will refer to the number of SDTs of that type | [optional] 
**end_minute** | **int** | The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT ends for a repeating SDT | [optional] 
**identifier** | [**ObjectIdentifier**](ObjectIdentifier.md) |  | [optional] 
**target_id** | [**ModelAndId**](ModelAndId.md) |  | [optional] 
**device_data_source_id** | **int** | The id of the device datasource instance group that the SDT will be associated with | [optional] 
**week_of_month** | **str** | The week of the month that the SDT will be active for a monthly SDT | [optional] 
**into_rest_response** | [**RestResponse**](RestResponse.md) |  | [optional] 
**website_group_id** | **int** | The Id of the service group that the SDT applies to | 
**is_effective** | **bool** | The values can be true|false, where true: the SDT is currently active false: the SDT is currently inactive | [optional] 
**minute** | **int** | The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT should begin for a repeating SDT | [optional] 
**recurrence** | **str** | Describes how and when the SDT recures | 
**end_hour** | **int** | The values can be 1 | 2....| 24. Specifies the hour that the SDT ends for a repeating SDT | [optional] 
**related_into_rest_response** | [**RestResponse**](RestResponse.md) |  | [optional] 
**created_by** | **str** | SDT creator&#x27;s username | [optional] 
**started_at_ms** | **int** | The time in milliseconds that the SDT will start or has started | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

