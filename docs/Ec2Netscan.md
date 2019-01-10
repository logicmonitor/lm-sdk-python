# Ec2Netscan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddr** | [**Ec2DDR**](Ec2DDR.md) |  | [optional] 
**credentials** | [**EC2NetscanPolicyCredential**](EC2NetscanPolicyCredential.md) | The credentials to be used for the scan | 
**accessibility** | **str** | Which IP the EC2 instance should be monitored with for nec2 scans: private or public | 
**dead_operation** | **str** | How dead EC2 instances should be handled for nec2 scans. Must be Manually | [optional] 
**ports** | [**NetscanPorts**](NetscanPorts.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


