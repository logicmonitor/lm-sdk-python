# ActionRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datapoint** | **str** | The datapoint for which the action rule is configured to match | [optional] 
**instance** | **str** | The instance for which the action rule is configured to match | [optional] 
**devices** | **list[str]** | The devices for which the action rule is configured to match | [optional] 
**datasource** | **str** | The datasource for which the action rule is configured to match | [optional] 
**resource_properties** | [**list[RestDeviceProperty]**](RestDeviceProperty.md) | The resource property filters list | [optional] 
**name** | **str** | The name of the action rule | 
**id** | **int** | The Id of the action rule | [optional] 
**level_str** | **str** | The severity levels for which the action rule is configured to match. | 
**device_groups** | **list[str]** | The device groups for which the action rule is configured to match | 
**action_chain_id** | **int** | The action chain id for the action rule | 
**action_chain** | [**ActionChainSummary**](ActionChainSummary.md) |  | [optional] 
**enabled** | **bool** | Whether action Rule is enabled or not | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

