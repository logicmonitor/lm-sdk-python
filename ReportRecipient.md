# ReportRecipient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addition_info** | **str** | If the type is admin and the method is email, the field should indicate the actual email address of the admin | [optional] 
**method** | **str** | Specifies the method to get the report. This should always be email | [optional] 
**type** | **str** | Specifies the recipient type. The values can be admin|arbitrary|group, where admin refers to a user in the account and arbitrary refers to an email address not associated with a user account. | 
**addr** | **str** | This should be a username if type&#x3D;admin, or an email address if type&#x3D;arbitrary | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


