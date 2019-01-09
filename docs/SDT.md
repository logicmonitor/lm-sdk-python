# SDT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_time_on_local** | **str** | The date, time and time zone that the SDT will end at | [optional] 
**timezone** | **str** | The specific timezone for SDT | [optional] 
**sdt_type** | **str** |  | [optional] 
**month_day** | **int** | 1 | 2....| 31 The day of the month that the SDT will be active for a monthly SDT | [optional] 
**week_of_month** | **str** | The weel of the month that the SDT will be active for a monthly SDT | [optional] 
**admin** | **str** | The name of the user that created the SDT | [optional] 
**end_date_time** | **int** | The epoch time, in milliseconds, that the SDT will end | [optional] 
**type** | **str** | The type resource that this SDT is for: ServiceSDT | ServiceGroupSDT | DeviceSDT | DeviceGroupSDT | CollectorSDT | DeviceBatchJobSDT | DeviceDataSourceSDT | DeviceEventSourceSDT | DeviceDataSourceInstanceSDT | DeviceDataSourceInstanceGroupSDT | 
**is_effective** | **bool** | true: the SDT is currently actice false: the SDT is currently inactive | [optional] 
**minute** | **int** | 1 | 2....| 60 The minute of the hour that the SDT should begin for a repeating SDT | [optional] 
**duration** | **int** | The duration of the SDT in minutes | [optional] 
**end_hour** | **int** | 1 | 2....| 24 The hour that the SDT ends for a repeating SDT | [optional] 
**start_date_time** | **int** | The epoch time, in milliseconds, that the SDT will start | [optional] 
**hour** | **int** | 1 | 2....| 24 The hour that the SDT will start for a repeating SDT (daily, weekly, or monthly) | [optional] 
**start_date_time_on_local** | **str** | The date, time and time zone that the SDT will end at | [optional] 
**week_day** | **str** |  | [optional] 
**comment** | **str** | The notes associated with the SDT | [optional] 
**id** | **str** | The Id of the SDT. This value will be in the following format \&quot;XX_##\&quot; where XX will refer to the type of SDT and ## will refer to the number of SDTs of that type | [optional] 
**end_minute** | **int** | 1 | 2....| 60 The minute of the hour that the SDT ends for a repeating SDT | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


