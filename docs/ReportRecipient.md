# ReportRecipient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addition_info** | **str** | If the type is admin and the method is email, the field should indicate the actual email address of the admin | [optional] 
**method** | **str** | This should always be email | [optional] 
**type** | **str** | Where admin refers to a user in the account and arbitrary refers to an email address not associated with a user account.Acceptable values are: admin, arbitrary | 
**addr** | **str** | This should be a username if type&#x3D;admin, or an email address if type&#x3D;arbitrary | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


