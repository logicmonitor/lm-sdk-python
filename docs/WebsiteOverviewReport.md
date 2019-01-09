# WebsiteOverviewReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_types** | **list[int]** | The information that should be included in the report. Options include 1: availability, 2: alerts, 3: graphs | [optional] 
**exclude100_availability** | **bool** | Whether or not websites with 100% availability should be ignored | [optional] 
**display_type** | **int** | 1 | 2 1: Display overall locations 2: Display overall and individual locations | [optional] 
**exclude_sdt** | **bool** | Whether or not SDTs periods should be considered for the website&#39;s availability | [optional] 
**date_range** | **str** | The Time Range configured for the report: Last 2 hours | Last 24 hours | Last calendar day | Last 7 days | Last 14 days | Last 30 days | Last calendar month | Last 365 days | Any custom date range in this format: YYYY-MM-dd hh:mm TO YYYY-MM-dd hh:mm | [optional] 
**items_type** | **str** | The type of entities specified in the servicesVal field. Acceptable values are: website, group | 
**items** | **str** | The websites OR website groups (full path) selected for the report, where multiple entities are separated by commas | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


