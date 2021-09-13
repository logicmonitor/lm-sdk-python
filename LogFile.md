# LogFile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path of the log file to monitor | [optional] 
**excludes** | **list[str]** | The regex or plain text to look for in the file and not trigger alert if found | [optional] 
**use_glob** | **bool** | Whether or not glob is used in the path | [optional] 
**encoding** | **str** | The file encoding: default | auto | UTF-8 | UTF-16 | [optional] 
**matches** | [**list[MatchPattern]**](MatchPattern.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


