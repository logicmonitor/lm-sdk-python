# Recipient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | EMAIL|SMEMAIL|VOICE|SMS, Recipient method for each type             group: \&quot;method\&quot; not used             arbitrary: the method should be email.             admin: the method  Should be email, smsEmail, voice, sms, or defaultMethod;  | 
**contact** | **str** | contact details, email address or phone number | [optional] 
**type** | **str** | GROUP|ARBITRARY|ADMIN, where Admin &#x3D; a user, and Arbitrary &#x3D; an arbitrary email | 
**addr** | **str** | the user name if method &#x3D; admin, or the email address if method &#x3D; arbitrary | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


