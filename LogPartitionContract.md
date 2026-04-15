# LogPartitionContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_epoch** | **int** | Contract start time in epoch seconds | [optional] 
**contract_interval_hours** | **int** | Contract interval in hours: 0 &#x3D; monthly (1st of next month), 24 &#x3D; daily, 168 &#x3D; weekly (next Monday), or custom hours | [optional] 
**to_epoch** | **int** | Contract end time in epoch seconds | [optional] 
**limit_reached_at** | **int** | Timestamp when usage limit was reached | [optional] 
**usage_limit** | **str** | Usage limit | [optional] 
**auto_restart_on_renewal** | **bool** | Auto restart ingestion on renewal | [optional] 
**id** | **int** | Contract Id | [optional] 
**state** | **str** | Contract state (active, future, expired) | [optional] 
**sku** | **str** | Subscription SKU | [optional] 
**retention** | **int** | Retention period in days | [optional] 
**stop_ingestion_on_limit** | **bool** | Stop ingestion when limit exceeded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

