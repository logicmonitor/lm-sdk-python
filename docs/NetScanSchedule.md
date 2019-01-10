# NetScanSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** | The cron schedule for when the scan should be run | [optional] 
**recipients** | **list[str]** | The recipients that should receive the notification of the scan finish | [optional] 
**timezone** | **str** | The timezone for the schedule | [optional] 
**type** | **str** | The type of schedule. Possible values are manual (no schedule), hourly, daily, weekly, monthly | [optional] 
**notify** | **bool** | Whether or not an email should be sent when the scan finishes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


