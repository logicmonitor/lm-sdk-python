# AlertThresholdReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sorted_by** | **str** | host | datasource | datapoint host: displayed thresholds will be sorted by device datasource: displayed thresholds will be sorted by datasource instance datapoint: displayed thresholds will be sorted by datapoint (metric) | [optional] 
**data_source_instance_name** | **str** | The name of the datasource instance to be included in the report, where the syntax should be dataSourceDisplayName-InstanceName. If you&#39;re referencing a single instance datasource, you can just specify dataSourceDisplayName. Glob expressions supported | [optional] 
**columns** | [**list[DynamicColumn]**](DynamicColumn.md) | The columns that will be displayed in the report. You should specify the columns in the order in which you&#39;d like them to be displayed | [optional] 
**data_point** | **str** | The datapoint to be included in the report. Glob expressions supported | [optional] 
**device_display_name** | **str** | The display name of the device(s) to be included in the report. Glob expressions supported | [optional] 
**exclude_global** | **bool** | true: only variations from the global thresholds will be displayed false: all thresholds will be displayed, including global thresholds an custom group and instance level thresholds | [optional] 
**group_full_path** | **str** | The full path of the group whose member devices you are going to include in the report. Glob expressions supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


