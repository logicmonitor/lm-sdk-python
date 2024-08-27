# BatchJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_monitoring** | **bool** | Whether to enable active monitoring of job start | [optional] 
**access_groups** | [**list[AccessGroup]**](AccessGroup.md) | Module&#x27;s access groups | [optional] 
**alert_level** | **str** | alert level if job doesn&#x27;t start on time, effective if activeMonitoring true | 
**description** | **str** | The description for the LMModule | [optional] 
**applies_to** | **str** | The Applies To for the LMModule | [optional] 
**technology** | **str** | The Technical Notes for the LMModule | [optional] 
**lineage_id** | **str** | The lineageId the LMModule belongs to | [optional] 
**cron_schedule** | **str** | Cron schedule expression, only the latter 5 ,effective if activeMonitoring true | 
**tags** | **str** | The Tags for the LMModule | [optional] 
**installation_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**cron_time_zone** | **str** | Cron timezone, effective if activeMonitoring true | 
**alert_body** | **str** | Alert message body | 
**start_mrtie** | **int** | Max Relative Time Interval Error, effective if activeMonitoring true | [optional] 
**checksum** | **str** | The metadata checksum for the LMModule content | [optional] 
**name** | **str** | JobMonitor name | 
**alert_subject** | **str** | Alert message subject | 
**id** | **int** | The ID of the LMModule | [optional] 
**access_group_ids** | **list[int]** | The Access Groups Id&#x27;s | [optional] 
**longest_run_time_in_minute** | **int** | Max job run time in minutes | [optional] 
**alert_effective_ival** | **int** | JobMonitor alert effective interval in minutes | 
**group** | **str** | The group the LMModule is in | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

