# Admin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_name** | **str** | The last name associated with the user | [optional] 
**note** | **str** | Any notes assocaited with the user | [optional] 
**view_permission** | **object** | The account tabs that will be visible to the user | [optional] 
**timezone** | **str** | The timezone of the user | [optional] 
**roles** | [**list[Role]**](Role.md) | The roles assigned to the user | 
**last_login_on** | **int** | The time that the user last logged in, in epoch format | [optional] 
**last_action_on_local** | **str** | The time, in local format, of the user&#39;s last action | [optional] 
**sms_email_format** | **str** | sms | fullText, where sms &#x3D; 160 characters and fullText&#x3D; all characters | [optional] 
**apionly** | **bool** | Whether it is a API only user | [optional] 
**api_tokens** | [**list[APIToken]**](APIToken.md) | Any API Tokens associated with the user | [optional] 
**password** | **str** | The password associated with the user | 
**last_action** | **str** | The last action taken by the user | [optional] 
**training_email** | **str** | The email address for user&#39;s Training account | [optional] 
**last_action_on** | **int** | The time, in epoch format, of the user&#39;s last action | [optional] 
**id** | **int** | The Id of the user | [optional] 
**email** | **str** | The email address associated with the user | 
**contact_method** | **str** | email | smsemail | [optional] 
**accept_eula_on** | **int** | The time, in epoch format, that the user accepted the EULA (if required to) | [optional] 
**sms_email** | **str** | The sms email address associated with the user | [optional] 
**two_fa_enabled** | **bool** | Whether or not two factor authentication is enabled for the user | [optional] 
**first_name** | **str** | The first name associated with the user | [optional] 
**phone** | **str** | The phone number associated with the user | [optional] 
**created_by** | **str** | Who created the user. This may be another user, SAML or LogicMonitor | [optional] 
**force_password_change** | **bool** | Whether or not the user should be forced to change their password on the next login | [optional] 
**accept_eula** | **bool** | Whether or not the user is required to accept the EULA (end user license agreement) | [optional] 
**username** | **str** | The username associated with the user | 
**status** | **str** | The user&#39;s status. Should be one of active and suspended | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


