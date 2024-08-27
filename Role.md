# Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_remote_session_in_company_level** | **bool** | Whether Remote Session should be enabled at the account level | [optional] 
**privileges** | [**list[Privilege]**](Privilege.md) | The account privileges associated with the role. Privileges can be added to a role for each area of your account | 
**user_permission** | **str** | The permission of current role with the admin. The values can be write|read|none | [optional] 
**description** | **str** | The description of the role | [optional] 
**custom_help_label** | **str** | The label for the custom help URL as it will appear in the &#x27;Help &amp; Support&#x27; dropdown menu | [optional] 
**custom_help_url** | **str** | The URL that should be added to the &#x27;Help &amp; Support&#x27; dropdown menu | [optional] 
**associated_user_count** | **int** | The count of the users which are belongs to the role | [optional] 
**name** | **str** | The name of the role | 
**id** | **int** | The Id of the role | [optional] 
**two_fa_required** | **bool** | Whether Two-Factor Authentication should be required for this role | [optional] 
**require_eula** | **bool** | Whether or not users assigned this role should be required to acknowledge the EULA (end user license agreement) | [optional] 
**acct_require_two_fa** | **bool** | Whether Two-Factor Authentication should be required for the entire account | [optional] 
**role_group_id** | **int** | The group Id of the role | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

