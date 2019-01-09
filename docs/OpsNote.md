# OpsNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | The note message | 
**created_by** | **str** | The user that created the Ops Note | [optional] 
**scopes** | [**list[OpsNoteScope]**](OpsNoteScope.md) | The scopes associated with the note. Each scope has a type of device, service, deviceGroup or serviceGroup. A note with no scope will show up for everything in the account | [optional] 
**id** | **str** | The id associated with the Ops Note | [optional] 
**happen_on_in_sec** | **int** | The date and time associated with the note, in epoch seconds format | [optional] 
**tags** | [**list[OpsNoteTagBase]**](OpsNoteTagBase.md) | The tags that should be associated with the note. Each tag has a unique id and a name - you can either include the name of a new or existing tag, or the id of an existing tag | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


