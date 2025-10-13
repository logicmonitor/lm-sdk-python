# GenerateReportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_admin_id** | **int** | Generate the report with the admin. 0 mean current user | [optional] 
**report_id** | **int** | The id of the report to run | [optional] 
**receive_emails** | **str** | The email addresses that LogicMonitor should send the report to, separated by commas. If set to null, the report will be generated immediately and the response will contain the report file URLOtherwise, the report will be generated in the background and delivered to the specified email addresses | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

