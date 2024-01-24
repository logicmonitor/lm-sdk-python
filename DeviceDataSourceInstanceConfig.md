# DeviceDataSourceInstanceConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_name** | **str** | Device datasource instance name | [optional] 
**device_data_source_id** | **int** | Device datasource id | [optional] 
**exclude_lines** | **list[int]** | advanceDiffChecker | [optional] 
**config_status** | **int** | Configuration file collect status | [optional] 
**version** | **int** | Config version | [optional] 
**device_id** | **int** | Device id | [optional] 
**delta_config** | [**list[DeviceDataSourceInstanceConfigDiff]**](DeviceDataSourceInstanceConfigDiff.md) | Configuration file diff | [optional] 
**device_display_name** | **str** | Device display name | [optional] 
**data_source_name** | **str** | Datasource name | [optional] 
**alerts** | [**list[DeviceDataSourceInstanceConfigAlert]**](DeviceDataSourceInstanceConfigAlert.md) | Alerts associated to this configuration file | [optional] 
**data_source_id** | **int** | Configsource id | [optional] 
**instance_id** | **int** | Device datasource instance id | [optional] 
**config_err_msg** | **str** | Configuration file collect error message | [optional] 
**change_status** | **str** | Configuration file change status, if the first configuration then it is Added, else Changed, values can be : Add|Change  | [optional] 
**id** | **str** | The id of the datasource | [optional] 
**poll_timestamp** | **int** | Datasource poll timestamp in milliseconds | [optional] 
**config** | **str** | Configuration file content | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


