# NMapNetscan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_network_and_broadcast** | **bool** | Include Network &amp; Broadcast Address for CIDR based netscan | 
**subnet** | **str** | The subnet to scan for nmap scans | 
**ddr** | [**NMapDDR**](NMapDDR.md) | Information related to including / excluding discovered devices in / from monitoring | [optional] 
**credentials** | [**RestNMapNetscanPolicyCredential**](RestNMapNetscanPolicyCredential.md) | The credentials to be used for the scan | [optional] 
**exclude** | **str** | The subnet to exclude from scanning from nmap scans | [optional] 
**ports** | [**RestNetscanPorts**](RestNetscanPorts.md) | The ports that should be used in the Netscan | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


