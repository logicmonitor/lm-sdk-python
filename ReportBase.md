# ReportBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastmodify_user_id** | **int** | The Id of the user that last modified the report | [optional] 
**delivery** | **str** | Whether or not the report is configured to be delivered via email. Acceptable values are: none, email | [optional] 
**user_permission** | **str** | The permissions associated with the user who made the API call | [optional] 
**last_generate_on** | **int** | The time, in epoch format, that the report was last generated | [optional] 
**report_link_num** | **int** | The number of links associated with the report, where each link corresponds to a generated report | [optional] 
**group_id** | **int** | The Id of the group the report is in, where Id&#x3D;0 is the root report group | [optional] 
**format** | **str** | The format of the report. Allowable values are: HTML, PDF, CSV, WORD | [optional] 
**description** | **str** | The description of the report | [optional] 
**last_generate_size** | **int** | The size of the report, in Bytes, the last time it was generated | [optional] 
**custom_report_type_id** | **int** | The id of the custom report template, if the report is a custom report. An id of 0 indicates that the report is not a custom report | [optional] 
**type** | **str** | The report type. Acceptable values are: Alert,Alert SLA,Alert threshold,Alert trends,Host CPU,Host group inventory,Host inventory,Host metric trends,Interfaces Bandwidth,Netflow device metric,Service Level Agreement,Website Service Overview,Word template,Audit Log,Alert Forecasting,Dashboard,Website SLA,User,Role | 
**last_generate_pages** | **int** | The number of pages in the report, the last time it was generated | [optional] 
**schedule** | **str** | A cron schedule that indicates when the report will be delivered via email | [optional] 
**recipients** | [**list[ReportRecipient]**](ReportRecipient.md) | If the report is configured to be delivered via email, this object provides the recipients that the report will be delivered to | [optional] 
**custom_report_type_name** | **str** | The name of the custom report template | [optional] 
**name** | **str** | The name of the report | 
**enable_view_as_other_user** | **bool** | Whether or not other users are allowed to view the report as the user who last modified the report | [optional] 
**lastmodify_user_name** | **str** | The username of the user that last modified the report | [optional] 
**id** | **int** | The id of the report | [optional] 
**schedule_timezone** | **str** | The sepecific timezone for the scheduled report | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


