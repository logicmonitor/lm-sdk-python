# DashboardGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **object** | The template which is used for import dashboard group | [optional] 
**full_path** | **str** | The full path of the dashboard group | [optional] 
**user_permission** | **str** | The permission of the user that made the API call | [optional] 
**widget_tokens** | [**list[WidgetToken]**](WidgetToken.md) | The tokens assigned at the group level | [optional] 
**name** | **str** | The name of the dashboard group | 
**num_of_direct_sub_groups** | **int** | The number of groups directly under the Dashboard Group | [optional] 
**num_of_dashboards** | **int** | The number of dashboards that belong to the Dashboard Group and any sub-groups | [optional] 
**description** | **str** | This is a description of the dashboard group | [optional] 
**id** | **int** | The Id of the dashboard group  | [optional] 
**dashboards** | [**list[DashboardData]**](DashboardData.md) | The dashboards that belong to the group | [optional] 
**parent_id** | **int** | The Id of the parent dashboard group | [optional] 
**num_of_direct_dashboards** | **int** | The number of dashboards that belong directly to the Dashboard Group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


