# Dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the dashboard | [optional] 
**full_name** | **str** | Full name of the dashboard, including group path | [optional] 
**group_full_path** | **str** | The full path (excluding root group) of the group the dashboard belongs to | [optional] 
**group_id** | **int** | The id of the group the dashboard belongs to | [optional] 
**group_name** | **str** | The name of group where created dashboard will reside | [optional] 
**id** | **int** | The Id of the dashboard | [optional] 
**name** | **str** | The name of the dashboard | 
**owner** | **str** | This field will be empty unless the dashboard is a private dashboard, in which case the owner will be listed | [optional] 
**sharable** | **bool** | Whether or not the dashboard is sharable. This value will always be true unless the dashboard is a private dashboard | [optional] 
**template** | **object** | The template which is used for import dashboard | [optional] 
**user_permission** | **str** | The permission of the user that made the API call | [optional] 
**widget_tokens** | [**list[WidgetToken]**](WidgetToken.md) | If useDynamicWidget&#x3D;true, this field must at least contain tokens defaultDeviceGroup and defaultServiceGroup | [optional] 
**widgets_config** | **object** | Information about widget configuration used by the UI | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


