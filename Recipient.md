# Recipient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Recipient method for each type.  The values can be EMAIL|SMEMAIL|VOICE|SMS              group: \&quot;method\&quot; not used             arbitrary: The method should be email.             admin: The method should be email, smsEmail, voice, sms, or defaultMethod;  | 
**contact** | **str** | Contact details, email address or phone number | [optional] 
**type** | **str** | The recipient type.  The values can be GROUP|ARBITRARY|ADMIN, where Admin &#x3D; a user, and Arbitrary &#x3D; an arbitrary email | 
**addr** | **str** | The recipient address.  The value will be user name if method &#x3D; admin, or the email address if method &#x3D; arbitrary | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

