# EscalatingChain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_alerting** | **bool** | Whether or not chain in alerting | [optional] 
**throttling_alerts** | **int** | Maximum number of alerts can be sent during a throttle period | [optional] 
**enable_throttling** | **bool** | If throttle needs to be enabled then true if not then false. | [optional] 
**destinations** | [**list[Chain]**](Chain.md) | The chain destinations | 
**name** | **str** | The chain name | 
**description** | **str** | The description for chain | [optional] 
**id** | **int** | The Id of the chain | [optional] 
**cc_destinations** | [**list[Recipient]**](Recipient.md) | The chain&#39;s cc destinations | [optional] 
**throttling_period** | **int** | The throttle period | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


