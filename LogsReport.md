# LogsReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitions** | **list[str]** | The partition for the report | [optional] 
**logs_data_type** | **str** | The type of logs data to include: basic, aggregation, or both | [optional] 
**graph_type** | **str** | The graph type for logs report visualization | [optional] 
**date_range** | **str** | The Time Range configured for the report. For example, Last 2 hours, Last 24 hours, etc. | [optional] 
**timezone** | **str** | The specific timezone for the report | [optional] 
**columns** | [**list[RestLogsDynamicColumnV3]**](RestLogsDynamicColumnV3.md) | The columns displayed in the report | [optional] 
**query** | **str** | The query for the report | [optional] 
**is_visualization_enabled** | **bool** | Whether visualization is enabled for the logs report | [optional] 
**ordering_config** | [**list[OrderingConfig]**](OrderingConfig.md) | The ordering configuration for logs report sections | [optional] 
**pie_slice_label** | **str** | The slice label column used for pie graph type | [optional] 
**pie_data_column** | **str** | The data column used for pie graph type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

