<<<<<<< HEAD
# \DefaultApi
=======
# logicmonitor.DefaultApi
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

All URIs are relative to *https://localhost/santaba/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
<<<<<<< HEAD
[**AckAlertById**](DefaultApi.md#AckAlertById) | **Post** /alert/alerts/{id}/ack | ack alert by id
[**AckCollectorDownAlertById**](DefaultApi.md#AckCollectorDownAlertById) | **Post** /setting/collectors/{id}/ackdown | ack collector down alert
[**AddAdmin**](DefaultApi.md#AddAdmin) | **Post** /setting/admins | add admin
[**AddAlertNoteById**](DefaultApi.md#AddAlertNoteById) | **Post** /alert/alerts/{id}/note | add alert note
[**AddAlertRule**](DefaultApi.md#AddAlertRule) | **Post** /setting/alert/rules | add alert rule
[**AddApiTokenByAdminId**](DefaultApi.md#AddApiTokenByAdminId) | **Post** /setting/admins/{adminId}/apitokens | add apiToken by admin
[**AddCollector**](DefaultApi.md#AddCollector) | **Post** /setting/collectors | add collector
[**AddCollectorGroup**](DefaultApi.md#AddCollectorGroup) | **Post** /setting/collectors/groups | add collector group
[**AddDashboard**](DefaultApi.md#AddDashboard) | **Post** /dashboard/dashboards | add dashboard
[**AddDashboardGroup**](DefaultApi.md#AddDashboardGroup) | **Post** /dashboard/groups | add dashboard group
[**AddDevice**](DefaultApi.md#AddDevice) | **Post** /device/devices | add a new device
[**AddDeviceDatasourceInstance**](DefaultApi.md#AddDeviceDatasourceInstance) | **Post** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | add device instance 
[**AddDeviceDatasourceInstanceGroup**](DefaultApi.md#AddDeviceDatasourceInstanceGroup) | **Post** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | add device datasource instance group 
[**AddDeviceGroup**](DefaultApi.md#AddDeviceGroup) | **Post** /device/groups | add device group
[**AddDeviceGroupProperty**](DefaultApi.md#AddDeviceGroupProperty) | **Post** /device/groups/{gid}/properties | add device group property
[**AddDeviceProperty**](DefaultApi.md#AddDeviceProperty) | **Post** /device/devices/{deviceId}/properties | add device property
[**AddRole**](DefaultApi.md#AddRole) | **Post** /setting/roles | add role
[**AddServiceGroup**](DefaultApi.md#AddServiceGroup) | **Post** /service/groups | add service group
[**DeleteAdminById**](DefaultApi.md#DeleteAdminById) | **Delete** /setting/admins/{id} | delete admin
[**DeleteAlertRuleById**](DefaultApi.md#DeleteAlertRuleById) | **Delete** /setting/alert/rules/{id} | delete alert rule
[**DeleteApiTokenById**](DefaultApi.md#DeleteApiTokenById) | **Delete** /setting/admins/{adminId}/apitokens/{apitokenId} | delete apiToken 
[**DeleteCollectorById**](DefaultApi.md#DeleteCollectorById) | **Delete** /setting/collectors/{id} | delete collector
[**DeleteCollectorGroupById**](DefaultApi.md#DeleteCollectorGroupById) | **Delete** /setting/collectors/groups/{id} | delete collector group
[**DeleteDashboardById**](DefaultApi.md#DeleteDashboardById) | **Delete** /dashboard/dashboards/{id} | delete dashboard
[**DeleteDashboardGroupById**](DefaultApi.md#DeleteDashboardGroupById) | **Delete** /dashboard/groups/{id} | delete dashboard group
[**DeleteDevice**](DefaultApi.md#DeleteDevice) | **Delete** /device/devices/{id} | delete a device
[**DeleteDeviceGroupById**](DefaultApi.md#DeleteDeviceGroupById) | **Delete** /device/groups/{id} | delete device group
[**DeleteDeviceGroupPropertyByName**](DefaultApi.md#DeleteDeviceGroupPropertyByName) | **Delete** /device/groups/{gid}/properties/{name} | delete device group property
[**DeleteDevicePropertyByName**](DefaultApi.md#DeleteDevicePropertyByName) | **Delete** /device/devices/{deviceId}/properties/{name} | delete device  property
[**DeleteRoleById**](DefaultApi.md#DeleteRoleById) | **Delete** /setting/roles/{id} | delete role
[**DeleteServiceGroupById**](DefaultApi.md#DeleteServiceGroupById) | **Delete** /service/groups/{id} | delete service group
[**GetAdminById**](DefaultApi.md#GetAdminById) | **Get** /setting/admins/{id} | get admin
[**GetAdminList**](DefaultApi.md#GetAdminList) | **Get** /setting/admins | get admin list
[**GetAlertById**](DefaultApi.md#GetAlertById) | **Get** /alert/alerts/{id} | get alert
[**GetAlertList**](DefaultApi.md#GetAlertList) | **Get** /alert/alerts | get alert list
[**GetAlertListByDeviceGroupId**](DefaultApi.md#GetAlertListByDeviceGroupId) | **Get** /device/groups/{id}/alerts | get device group alerts
[**GetAlertListByDeviceId**](DefaultApi.md#GetAlertListByDeviceId) | **Get** /device/devices/{id}/alerts | get alerts
[**GetAlertRuleById**](DefaultApi.md#GetAlertRuleById) | **Get** /setting/alert/rules/{id} | get alert rule by id
[**GetAlertRuleList**](DefaultApi.md#GetAlertRuleList) | **Get** /setting/alert/rules | get alert rule list
[**GetApiTokenListByAdminId**](DefaultApi.md#GetApiTokenListByAdminId) | **Get** /setting/admins/{adminId}/apitokens | get apiToken by admin
[**GetCollectorById**](DefaultApi.md#GetCollectorById) | **Get** /setting/collectors/{id} | get collector
[**GetCollectorGroupById**](DefaultApi.md#GetCollectorGroupById) | **Get** /setting/collectors/groups/{id} | get collector group
[**GetCollectorGroupList**](DefaultApi.md#GetCollectorGroupList) | **Get** /setting/collectors/groups | get collector group list
[**GetCollectorList**](DefaultApi.md#GetCollectorList) | **Get** /setting/collectors | get collector list
[**GetDashboardById**](DefaultApi.md#GetDashboardById) | **Get** /dashboard/dashboards/{id} | get dashboard
[**GetDashboardGroupById**](DefaultApi.md#GetDashboardGroupById) | **Get** /dashboard/groups/{id} | get dashboard group
[**GetDashboardGroupList**](DefaultApi.md#GetDashboardGroupList) | **Get** /dashboard/groups | get dashboard group list
[**GetDashboardList**](DefaultApi.md#GetDashboardList) | **Get** /dashboard/dashboards | get dashboard list
[**GetDeviceById**](DefaultApi.md#GetDeviceById) | **Get** /device/devices/{id} | get device by id
[**GetDeviceDatasourceById**](DefaultApi.md#GetDeviceDatasourceById) | **Get** /device/devices/{deviceId}/devicedatasources/{id} | get device datasource 
[**GetDeviceDatasourceDataById**](DefaultApi.md#GetDeviceDatasourceDataById) | **Get** /device/devices/{deviceId}/devicedatasources/{id}/data | get device datasource data 
[**GetDeviceDatasourceInstanceAlertSettingById**](DefaultApi.md#GetDeviceDatasourceInstanceAlertSettingById) | **Get** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | get device instance alert setting
[**GetDeviceDatasourceInstanceById**](DefaultApi.md#GetDeviceDatasourceInstanceById) | **Get** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | get device instance 
[**GetDeviceDatasourceInstanceData**](DefaultApi.md#GetDeviceDatasourceInstanceData) | **Get** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/data | get device instance data
[**GetDeviceDatasourceInstanceGraphData**](DefaultApi.md#GetDeviceDatasourceInstanceGraphData) | **Get** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/graphs/{graphId}/data | get device instance graph data 
[**GetDeviceDatasourceInstanceGroupById**](DefaultApi.md#GetDeviceDatasourceInstanceGroupById) | **Get** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | get device datasource instance group 
[**GetDeviceDatasourceInstanceGroupOverviewGraphData**](DefaultApi.md#GetDeviceDatasourceInstanceGroupOverviewGraphData) | **Get** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/graphs/{ographId}/data | get device instance group overview graph data 
[**GetDeviceDatasourceList**](DefaultApi.md#GetDeviceDatasourceList) | **Get** /device/devices/{deviceId}/devicedatasources | get device datasource list 
[**GetDeviceGroupById**](DefaultApi.md#GetDeviceGroupById) | **Get** /device/groups/{id} | get device group
[**GetDeviceGroupDatasourceAlertSetting**](DefaultApi.md#GetDeviceGroupDatasourceAlertSetting) | **Get** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | get device group datasource alert setting 
[**GetDeviceGroupDatasourceById**](DefaultApi.md#GetDeviceGroupDatasourceById) | **Get** /device/groups/{deviceGroupId}/datasources/{id} | get device group datasource
[**GetDeviceGroupDatasourceList**](DefaultApi.md#GetDeviceGroupDatasourceList) | **Get** /device/groups/{deviceGroupId}/datasources | get device group datasource list
[**GetDeviceGroupList**](DefaultApi.md#GetDeviceGroupList) | **Get** /device/groups | get device group list
[**GetDeviceGroupProperties**](DefaultApi.md#GetDeviceGroupProperties) | **Get** /device/groups/{gid}/properties | get device group properties
[**GetDeviceGroupPropertyByName**](DefaultApi.md#GetDeviceGroupPropertyByName) | **Get** /device/groups/{gid}/properties/{name} | get device group property by name
[**GetDeviceInstanceGraphDataOnlyByInstanceId**](DefaultApi.md#GetDeviceInstanceGraphDataOnlyByInstanceId) | **Get** /device/devicedatasourceinstances/{instanceId}/graphs/{graphId}/data | get device instance graphData
[**GetDeviceList**](DefaultApi.md#GetDeviceList) | **Get** /device/devices | get device list
[**GetDevicePropertiesList**](DefaultApi.md#GetDevicePropertiesList) | **Get** /device/devices/{deviceId}/properties | get device properties
[**GetDevicePropertyByName**](DefaultApi.md#GetDevicePropertyByName) | **Get** /device/devices/{deviceId}/properties/{name} | get device property by name
[**GetImmediateDeviceListByDeviceGroupId**](DefaultApi.md#GetImmediateDeviceListByDeviceGroupId) | **Get** /device/groups/{id}/devices | get immediate devices under group
[**GetRoleById**](DefaultApi.md#GetRoleById) | **Get** /setting/roles/{id} | get role by id
[**GetRoleList**](DefaultApi.md#GetRoleList) | **Get** /setting/roles | get role list
[**GetServiceGraphData**](DefaultApi.md#GetServiceGraphData) | **Get** /service/services/{serviceId}/checkpoints/{checkpointId}/graphs/{graphName}/data | get service graph data
[**GetServiceGroupById**](DefaultApi.md#GetServiceGroupById) | **Get** /service/groups/{id} | get service group
[**GetServiceGroupList**](DefaultApi.md#GetServiceGroupList) | **Get** /service/groups | get service group list
[**GetSiteMonitorCheckPointList**](DefaultApi.md#GetSiteMonitorCheckPointList) | **Get** /service/smcheckpoints | get site monitor checkpoint list
[**GetUnmonitoredDeviceList**](DefaultApi.md#GetUnmonitoredDeviceList) | **Get** /device/unmonitoreddevices | get unmonitored device list
[**InstallCollector**](DefaultApi.md#InstallCollector) | **Get** /setting/collectors/{collectorId}/installers/{osAndArch} | install collector
[**PatchDeviceById**](DefaultApi.md#PatchDeviceById) | **Patch** /device/devices/{id} | patch a device
[**PatchDeviceGroupById**](DefaultApi.md#PatchDeviceGroupById) | **Patch** /device/groups/{id} | patch device group
[**PatchServiceGroupById**](DefaultApi.md#PatchServiceGroupById) | **Patch** /service/groups/{id} | patch service group
[**ScheduleAutoDiscoveryByDeviceId**](DefaultApi.md#ScheduleAutoDiscoveryByDeviceId) | **Post** /device/devices/{id}/scheduleAutoDiscovery | schedule auto discovery for a host
[**UpdateAdminById**](DefaultApi.md#UpdateAdminById) | **Put** /setting/admins/{id} | update admin
[**UpdateAlertRuleById**](DefaultApi.md#UpdateAlertRuleById) | **Put** /setting/alert/rules/{id} | update alert rule
[**UpdateApiTokenByAdminId**](DefaultApi.md#UpdateApiTokenByAdminId) | **Put** /setting/admins/{adminId}/apitokens/{apitokenId} | update apiToken by admin
[**UpdateCollectorById**](DefaultApi.md#UpdateCollectorById) | **Put** /setting/collectors/{id} | update collector
[**UpdateCollectorGroupById**](DefaultApi.md#UpdateCollectorGroupById) | **Put** /setting/collectors/groups/{id} | update collector group
[**UpdateDashboardById**](DefaultApi.md#UpdateDashboardById) | **Put** /dashboard/dashboards/{id} | update dashboard
[**UpdateDashboardGroupById**](DefaultApi.md#UpdateDashboardGroupById) | **Put** /dashboard/groups/{id} | update dashboard group
[**UpdateDevice**](DefaultApi.md#UpdateDevice) | **Put** /device/devices/{id} | update a device
[**UpdateDeviceDatasourceInstanceAlertSettingById**](DefaultApi.md#UpdateDeviceDatasourceInstanceAlertSettingById) | **Put** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**UpdateDeviceDatasourceInstanceById**](DefaultApi.md#UpdateDeviceDatasourceInstanceById) | **Put** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance 
[**UpdateDeviceDatasourceInstanceGroupById**](DefaultApi.md#UpdateDeviceDatasourceInstanceGroupById) | **Put** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group 
[**UpdateDeviceGroupById**](DefaultApi.md#UpdateDeviceGroupById) | **Put** /device/groups/{id} | update device group
[**UpdateDeviceGroupDatasourceAlertSetting**](DefaultApi.md#UpdateDeviceGroupDatasourceAlertSetting) | **Put** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting 
[**UpdateDeviceGroupPropertyByName**](DefaultApi.md#UpdateDeviceGroupPropertyByName) | **Put** /device/groups/{gid}/properties/{name} | update device group property
[**UpdateDevicePropertyByName**](DefaultApi.md#UpdateDevicePropertyByName) | **Put** /device/devices/{deviceId}/properties/{name} | update device  property
[**UpdateRoleById**](DefaultApi.md#UpdateRoleById) | **Put** /setting/roles/{id} | update role
[**UpdateServiceGroupById**](DefaultApi.md#UpdateServiceGroupById) | **Put** /service/groups/{id} | update service group


# **AckAlertById**
> RestNullObjectResponse AckAlertById($body, $id)
=======
[**ack_alert_by_id**](DefaultApi.md#ack_alert_by_id) | **POST** /alert/alerts/{id}/ack | ack alert by id
[**ack_collector_down_alert_by_id**](DefaultApi.md#ack_collector_down_alert_by_id) | **POST** /setting/collectors/{id}/ackdown | ack collector down alert
[**add_admin**](DefaultApi.md#add_admin) | **POST** /setting/admins | add admin
[**add_alert_note_by_id**](DefaultApi.md#add_alert_note_by_id) | **POST** /alert/alerts/{id}/note | add alert note
[**add_alert_rule**](DefaultApi.md#add_alert_rule) | **POST** /setting/alert/rules | add alert rule
[**add_api_token_by_admin_id**](DefaultApi.md#add_api_token_by_admin_id) | **POST** /setting/admins/{adminId}/apitokens | add apiToken by admin
[**add_collector**](DefaultApi.md#add_collector) | **POST** /setting/collectors | add collector
[**add_collector_group**](DefaultApi.md#add_collector_group) | **POST** /setting/collectors/groups | add collector group
[**add_dashboard**](DefaultApi.md#add_dashboard) | **POST** /dashboard/dashboards | add dashboard
[**add_dashboard_group**](DefaultApi.md#add_dashboard_group) | **POST** /dashboard/groups | add dashboard group
[**add_device**](DefaultApi.md#add_device) | **POST** /device/devices | add a new device
[**add_device_datasource_instance**](DefaultApi.md#add_device_datasource_instance) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | add device instance 
[**add_device_datasource_instance_group**](DefaultApi.md#add_device_datasource_instance_group) | **POST** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | add device datasource instance group 
[**add_device_group**](DefaultApi.md#add_device_group) | **POST** /device/groups | add device group
[**add_device_group_property**](DefaultApi.md#add_device_group_property) | **POST** /device/groups/{gid}/properties | add device group property
[**add_device_property**](DefaultApi.md#add_device_property) | **POST** /device/devices/{deviceId}/properties | add device property
[**add_role**](DefaultApi.md#add_role) | **POST** /setting/roles | add role
[**add_service_group**](DefaultApi.md#add_service_group) | **POST** /service/groups | add service group
[**delete_admin_by_id**](DefaultApi.md#delete_admin_by_id) | **DELETE** /setting/admins/{id} | delete admin
[**delete_alert_rule_by_id**](DefaultApi.md#delete_alert_rule_by_id) | **DELETE** /setting/alert/rules/{id} | delete alert rule
[**delete_api_token_by_id**](DefaultApi.md#delete_api_token_by_id) | **DELETE** /setting/admins/{adminId}/apitokens/{apitokenId} | delete apiToken 
[**delete_collector_by_id**](DefaultApi.md#delete_collector_by_id) | **DELETE** /setting/collectors/{id} | delete collector
[**delete_collector_group_by_id**](DefaultApi.md#delete_collector_group_by_id) | **DELETE** /setting/collectors/groups/{id} | delete collector group
[**delete_dashboard_by_id**](DefaultApi.md#delete_dashboard_by_id) | **DELETE** /dashboard/dashboards/{id} | delete dashboard
[**delete_dashboard_group_by_id**](DefaultApi.md#delete_dashboard_group_by_id) | **DELETE** /dashboard/groups/{id} | delete dashboard group
[**delete_device**](DefaultApi.md#delete_device) | **DELETE** /device/devices/{id} | delete a device
[**delete_device_group_by_id**](DefaultApi.md#delete_device_group_by_id) | **DELETE** /device/groups/{id} | delete device group
[**delete_device_group_property_by_name**](DefaultApi.md#delete_device_group_property_by_name) | **DELETE** /device/groups/{gid}/properties/{name} | delete device group property
[**delete_device_property_by_name**](DefaultApi.md#delete_device_property_by_name) | **DELETE** /device/devices/{deviceId}/properties/{name} | delete device  property
[**delete_role_by_id**](DefaultApi.md#delete_role_by_id) | **DELETE** /setting/roles/{id} | delete role
[**delete_service_group_by_id**](DefaultApi.md#delete_service_group_by_id) | **DELETE** /service/groups/{id} | delete service group
[**get_admin_by_id**](DefaultApi.md#get_admin_by_id) | **GET** /setting/admins/{id} | get admin
[**get_admin_list**](DefaultApi.md#get_admin_list) | **GET** /setting/admins | get admin list
[**get_alert_by_id**](DefaultApi.md#get_alert_by_id) | **GET** /alert/alerts/{id} | get alert
[**get_alert_list**](DefaultApi.md#get_alert_list) | **GET** /alert/alerts | get alert list
[**get_alert_list_by_device_group_id**](DefaultApi.md#get_alert_list_by_device_group_id) | **GET** /device/groups/{id}/alerts | get device group alerts
[**get_alert_list_by_device_id**](DefaultApi.md#get_alert_list_by_device_id) | **GET** /device/devices/{id}/alerts | get alerts
[**get_alert_rule_by_id**](DefaultApi.md#get_alert_rule_by_id) | **GET** /setting/alert/rules/{id} | get alert rule by id
[**get_alert_rule_list**](DefaultApi.md#get_alert_rule_list) | **GET** /setting/alert/rules | get alert rule list
[**get_api_token_list_by_admin_id**](DefaultApi.md#get_api_token_list_by_admin_id) | **GET** /setting/admins/{adminId}/apitokens | get apiToken by admin
[**get_collector_by_id**](DefaultApi.md#get_collector_by_id) | **GET** /setting/collectors/{id} | get collector
[**get_collector_group_by_id**](DefaultApi.md#get_collector_group_by_id) | **GET** /setting/collectors/groups/{id} | get collector group
[**get_collector_group_list**](DefaultApi.md#get_collector_group_list) | **GET** /setting/collectors/groups | get collector group list
[**get_collector_list**](DefaultApi.md#get_collector_list) | **GET** /setting/collectors | get collector list
[**get_dashboard_by_id**](DefaultApi.md#get_dashboard_by_id) | **GET** /dashboard/dashboards/{id} | get dashboard
[**get_dashboard_group_by_id**](DefaultApi.md#get_dashboard_group_by_id) | **GET** /dashboard/groups/{id} | get dashboard group
[**get_dashboard_group_list**](DefaultApi.md#get_dashboard_group_list) | **GET** /dashboard/groups | get dashboard group list
[**get_dashboard_list**](DefaultApi.md#get_dashboard_list) | **GET** /dashboard/dashboards | get dashboard list
[**get_device_by_id**](DefaultApi.md#get_device_by_id) | **GET** /device/devices/{id} | get device by id
[**get_device_datasource_by_id**](DefaultApi.md#get_device_datasource_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id} | get device datasource 
[**get_device_datasource_data_by_id**](DefaultApi.md#get_device_datasource_data_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/data | get device datasource data 
[**get_device_datasource_instance_alert_setting_by_id**](DefaultApi.md#get_device_datasource_instance_alert_setting_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | get device instance alert setting
[**get_device_datasource_instance_by_id**](DefaultApi.md#get_device_datasource_instance_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | get device instance 
[**get_device_datasource_instance_data**](DefaultApi.md#get_device_datasource_instance_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/data | get device instance data
[**get_device_datasource_instance_graph_data**](DefaultApi.md#get_device_datasource_instance_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/graphs/{graphId}/data | get device instance graph data 
[**get_device_datasource_instance_group_by_id**](DefaultApi.md#get_device_datasource_instance_group_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | get device datasource instance group 
[**get_device_datasource_instance_group_overview_graph_data**](DefaultApi.md#get_device_datasource_instance_group_overview_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/graphs/{ographId}/data | get device instance group overview graph data 
[**get_device_datasource_list**](DefaultApi.md#get_device_datasource_list) | **GET** /device/devices/{deviceId}/devicedatasources | get device datasource list 
[**get_device_group_by_id**](DefaultApi.md#get_device_group_by_id) | **GET** /device/groups/{id} | get device group
[**get_device_group_datasource_alert_setting**](DefaultApi.md#get_device_group_datasource_alert_setting) | **GET** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | get device group datasource alert setting 
[**get_device_group_datasource_by_id**](DefaultApi.md#get_device_group_datasource_by_id) | **GET** /device/groups/{deviceGroupId}/datasources/{id} | get device group datasource
[**get_device_group_datasource_list**](DefaultApi.md#get_device_group_datasource_list) | **GET** /device/groups/{deviceGroupId}/datasources | get device group datasource list
[**get_device_group_list**](DefaultApi.md#get_device_group_list) | **GET** /device/groups | get device group list
[**get_device_group_properties**](DefaultApi.md#get_device_group_properties) | **GET** /device/groups/{gid}/properties | get device group properties
[**get_device_group_property_by_name**](DefaultApi.md#get_device_group_property_by_name) | **GET** /device/groups/{gid}/properties/{name} | get device group property by name
[**get_device_instance_graph_data_only_by_instance_id**](DefaultApi.md#get_device_instance_graph_data_only_by_instance_id) | **GET** /device/devicedatasourceinstances/{instanceId}/graphs/{graphId}/data | get device instance graphData
[**get_device_list**](DefaultApi.md#get_device_list) | **GET** /device/devices | get device list
[**get_device_properties_list**](DefaultApi.md#get_device_properties_list) | **GET** /device/devices/{deviceId}/properties | get device properties
[**get_device_property_by_name**](DefaultApi.md#get_device_property_by_name) | **GET** /device/devices/{deviceId}/properties/{name} | get device property by name
[**get_immediate_device_list_by_device_group_id**](DefaultApi.md#get_immediate_device_list_by_device_group_id) | **GET** /device/groups/{id}/devices | get immediate devices under group
[**get_role_by_id**](DefaultApi.md#get_role_by_id) | **GET** /setting/roles/{id} | get role by id
[**get_role_list**](DefaultApi.md#get_role_list) | **GET** /setting/roles | get role list
[**get_service_graph_data**](DefaultApi.md#get_service_graph_data) | **GET** /service/services/{serviceId}/checkpoints/{checkpointId}/graphs/{graphName}/data | get service graph data
[**get_service_group_by_id**](DefaultApi.md#get_service_group_by_id) | **GET** /service/groups/{id} | get service group
[**get_service_group_list**](DefaultApi.md#get_service_group_list) | **GET** /service/groups | get service group list
[**get_site_monitor_check_point_list**](DefaultApi.md#get_site_monitor_check_point_list) | **GET** /service/smcheckpoints | get site monitor checkpoint list
[**get_unmonitored_device_list**](DefaultApi.md#get_unmonitored_device_list) | **GET** /device/unmonitoreddevices | get unmonitored device list
[**install_collector**](DefaultApi.md#install_collector) | **GET** /setting/collectors/{collectorId}/installers/{osAndArch} | install collector
[**patch_device_by_id**](DefaultApi.md#patch_device_by_id) | **PATCH** /device/devices/{id} | patch a device
[**patch_device_group_by_id**](DefaultApi.md#patch_device_group_by_id) | **PATCH** /device/groups/{id} | patch device group
[**patch_service_group_by_id**](DefaultApi.md#patch_service_group_by_id) | **PATCH** /service/groups/{id} | patch service group
[**schedule_auto_discovery_by_device_id**](DefaultApi.md#schedule_auto_discovery_by_device_id) | **POST** /device/devices/{id}/scheduleAutoDiscovery | schedule auto discovery for a host
[**update_admin_by_id**](DefaultApi.md#update_admin_by_id) | **PUT** /setting/admins/{id} | update admin
[**update_alert_rule_by_id**](DefaultApi.md#update_alert_rule_by_id) | **PUT** /setting/alert/rules/{id} | update alert rule
[**update_api_token_by_admin_id**](DefaultApi.md#update_api_token_by_admin_id) | **PUT** /setting/admins/{adminId}/apitokens/{apitokenId} | update apiToken by admin
[**update_collector_by_id**](DefaultApi.md#update_collector_by_id) | **PUT** /setting/collectors/{id} | update collector
[**update_collector_group_by_id**](DefaultApi.md#update_collector_group_by_id) | **PUT** /setting/collectors/groups/{id} | update collector group
[**update_dashboard_by_id**](DefaultApi.md#update_dashboard_by_id) | **PUT** /dashboard/dashboards/{id} | update dashboard
[**update_dashboard_group_by_id**](DefaultApi.md#update_dashboard_group_by_id) | **PUT** /dashboard/groups/{id} | update dashboard group
[**update_device**](DefaultApi.md#update_device) | **PUT** /device/devices/{id} | update a device
[**update_device_datasource_instance_alert_setting_by_id**](DefaultApi.md#update_device_datasource_instance_alert_setting_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**update_device_datasource_instance_by_id**](DefaultApi.md#update_device_datasource_instance_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance 
[**update_device_datasource_instance_group_by_id**](DefaultApi.md#update_device_datasource_instance_group_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group 
[**update_device_group_by_id**](DefaultApi.md#update_device_group_by_id) | **PUT** /device/groups/{id} | update device group
[**update_device_group_datasource_alert_setting**](DefaultApi.md#update_device_group_datasource_alert_setting) | **PUT** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting 
[**update_device_group_property_by_name**](DefaultApi.md#update_device_group_property_by_name) | **PUT** /device/groups/{gid}/properties/{name} | update device group property
[**update_device_property_by_name**](DefaultApi.md#update_device_property_by_name) | **PUT** /device/devices/{deviceId}/properties/{name} | update device  property
[**update_role_by_id**](DefaultApi.md#update_role_by_id) | **PUT** /setting/roles/{id} | update role
[**update_service_group_by_id**](DefaultApi.md#update_service_group_by_id) | **PUT** /service/groups/{id} | update service group


# **ack_alert_by_id**
> RestNullObjectResponse ack_alert_by_id(body, id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

ack alert by id



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestAlertAck() # RestAlertAck | 
id = 'id_example' # str | 

try: 
    # ack alert by id
    api_response = api_instance.ack_alert_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ack_alert_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertAck**](RestAlertAck.md)|  | 
<<<<<<< HEAD
 **id** | **string**|  | 
=======
 **id** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AckCollectorDownAlertById**
> RestNullObjectResponse AckCollectorDownAlertById($id, $body)
=======
# **ack_collector_down_alert_by_id**
> RestNullObjectResponse ack_collector_down_alert_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

ack collector down alert



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestAckCollectorDown() # RestAckCollectorDown | 

try: 
    # ack collector down alert
    api_response = api_instance.ack_collector_down_alert_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ack_collector_down_alert_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestAckCollectorDown**](RestAckCollectorDown.md)|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddAdmin**
> RestAdminResponse AddAdmin($body)
=======
# **add_admin**
> RestAdminResponse add_admin(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestAdmin() # RestAdmin | 

try: 
    # add admin
    api_response = api_instance.add_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_admin: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAdmin**](RestAdmin.md)|  | 

### Return type

[**RestAdminResponse**](RestAdminResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddAlertNoteById**
> RestNullObjectResponse AddAlertNoteById($body, $id)
=======
# **add_alert_note_by_id**
> RestNullObjectResponse add_alert_note_by_id(body, id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add alert note



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestAlertAck() # RestAlertAck | 
id = 'id_example' # str | 

try: 
    # add alert note
    api_response = api_instance.add_alert_note_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_alert_note_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertAck**](RestAlertAck.md)|  | 
<<<<<<< HEAD
 **id** | **string**|  | 
=======
 **id** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddAlertRule**
> RestAlertRuleResponse AddAlertRule($body)
=======
# **add_alert_rule**
> RestAlertRuleResponse add_alert_rule(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add alert rule



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestAlertRule() # RestAlertRule | 

try: 
    # add alert rule
    api_response = api_instance.add_alert_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_alert_rule: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertRule**](RestAlertRule.md)|  | 

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddApiTokenByAdminId**
> RestApiTokenResponse AddApiTokenByAdminId($adminId, $body)
=======
# **add_api_token_by_admin_id**
> RestApiTokenResponse add_api_token_by_admin_id(admin_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add apiToken by admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
admin_id = 56 # int | 
body = logicmonitor.RestAPIToken() # RestAPIToken | 

try: 
    # add apiToken by admin
    api_response = api_instance.add_api_token_by_admin_id(admin_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_api_token_by_admin_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **adminId** | **int32**|  | 
 **body** | [**RestApiToken**](RestAPIToken.md)|  | 
=======
 **admin_id** | **int**|  | 
 **body** | [**RestAPIToken**](RestAPIToken.md)|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddCollector**
> RestCollectorResponse AddCollector($body)
=======
# **add_collector**
> RestCollectorResponse add_collector(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add collector



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestCollector() # RestCollector | 

try: 
    # add collector
    api_response = api_instance.add_collector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_collector: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestCollector**](RestCollector.md)|  | 

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddCollectorGroup**
> RestCollectorGroupResponse AddCollectorGroup($body)
=======
# **add_collector_group**
> RestCollectorGroupResponse add_collector_group(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add collector group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestCollectorGroup() # RestCollectorGroup | 

try: 
    # add collector group
    api_response = api_instance.add_collector_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_collector_group: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestCollectorGroup**](RestCollectorGroup.md)|  | 

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDashboard**
> RestDashboardV1Response AddDashboard($body)
=======
# **add_dashboard**
> RestDashboardV1Response add_dashboard(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add dashboard



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDashboardV1() # RestDashboardV1 | 

try: 
    # add dashboard
    api_response = api_instance.add_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_dashboard: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDashboardV1**](RestDashboardV1.md)|  | 

### Return type

[**RestDashboardV1Response**](RestDashboardV1Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDashboardGroup**
> RestDashboardGroupResponse AddDashboardGroup($body)
=======
# **add_dashboard_group**
> RestDashboardGroupResponse add_dashboard_group(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add dashboard group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDashboardGroup() # RestDashboardGroup | 

try: 
    # add dashboard group
    api_response = api_instance.add_dashboard_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_dashboard_group: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDashboardGroup**](RestDashboardGroup.md)|  | 

### Return type

[**RestDashboardGroupResponse**](RestDashboardGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDevice**
> RestDeviceResponse AddDevice($body, $addFromWizard)
=======
# **add_device**
> RestDeviceResponse add_device(body, add_from_wizard=add_from_wizard)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add a new device



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDevice() # RestDevice | 
add_from_wizard = false # bool |  (optional) (default to false)

try: 
    # add a new device
    api_response = api_instance.add_device(body, add_from_wizard=add_from_wizard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
<<<<<<< HEAD
 **addFromWizard** | **bool**|  | [optional] [default to false]
=======
 **add_from_wizard** | **bool**|  | [optional] [default to false]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDeviceDatasourceInstance**
> RestDeviceDataSourceInstanceResponse AddDeviceDatasourceInstance($deviceId, $hdsId, $body)
=======
# **add_device_datasource_instance**
> RestDeviceDataSourceInstanceResponse add_device_datasource_instance(device_id, hds_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add device instance 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
body = logicmonitor.RestDeviceDataSourceInstance() # RestDeviceDataSourceInstance | 

try: 
    # add device instance 
    api_response = api_instance.add_device_datasource_instance(device_id, hds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device_datasource_instance: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceDataSourceInstance**](RestDeviceDataSourceInstance.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDeviceDatasourceInstanceGroup**
> RestDeviceDataSourceInstanceGroupResponse AddDeviceDatasourceInstanceGroup($deviceId, $deviceDsId, $body)
=======
# **add_device_datasource_instance_group**
> RestDeviceDataSourceInstanceGroupResponse add_device_datasource_instance_group(device_id, device_ds_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add device datasource instance group 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
device_ds_id = 56 # int | 
body = logicmonitor.RestDeviceDataSourceInstanceGroup() # RestDeviceDataSourceInstanceGroup | 

try: 
    # add device datasource instance group 
    api_response = api_instance.add_device_datasource_instance_group(device_id, device_ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device_datasource_instance_group: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **deviceDsId** | **int32**|  | 
=======
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceDataSourceInstanceGroup**](RestDeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDeviceGroup**
> RestDeviceGroupResponse AddDeviceGroup($body)
=======
# **add_device_group**
> RestDeviceGroupResponse add_device_group(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add device group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDeviceGroup() # RestDeviceGroup | 

try: 
    # add device group
    api_response = api_instance.add_device_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device_group: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDeviceGroupProperty**
> RestPropertyResponse AddDeviceGroupProperty($gid, $body)
=======
# **add_device_group_property**
> RestPropertyResponse add_device_group_property(gid, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add device group property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
gid = 56 # int | 
body = logicmonitor.RestProperty() # RestProperty | 

try: 
    # add device group property
    api_response = api_instance.add_device_group_property(gid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device_group_property: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **gid** | **int32**|  | 
=======
 **gid** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddDeviceProperty**
> RestPropertyResponse AddDeviceProperty($deviceId, $body)
=======
# **add_device_property**
> RestPropertyResponse add_device_property(device_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add device property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
body = logicmonitor.RestProperty() # RestProperty | 

try: 
    # add device property
    api_response = api_instance.add_device_property(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_device_property: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
=======
 **device_id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddRole**
> RestRoleResponse AddRole($body)
=======
# **add_role**
> RestRoleResponse add_role(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add role



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestRole() # RestRole | 

try: 
    # add role
    api_response = api_instance.add_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_role: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestRole**](RestRole.md)|  | 

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **AddServiceGroup**
> RestServiceGroupResponse AddServiceGroup($body)
=======
# **add_service_group**
> RestServiceGroupResponse add_service_group(body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

add service group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestServiceGroup() # RestServiceGroup | 

try: 
    # add service group
    api_response = api_instance.add_service_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_service_group: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteAdminById**
> RestNullObjectResponse DeleteAdminById($id)
=======
# **delete_admin_by_id**
> RestNullObjectResponse delete_admin_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete admin
    api_response = api_instance.delete_admin_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_admin_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteAlertRuleById**
> RestAlertRuleResponse DeleteAlertRuleById($id)
=======
# **delete_alert_rule_by_id**
> RestAlertRuleResponse delete_alert_rule_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete alert rule



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete alert rule
    api_response = api_instance.delete_alert_rule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_alert_rule_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteApiTokenById**
> RestApiTokenResponse DeleteApiTokenById($adminId, $apitokenId)
=======
# **delete_api_token_by_id**
> RestApiTokenResponse delete_api_token_by_id(admin_id, apitoken_id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete apiToken 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
admin_id = 56 # int | 
apitoken_id = 56 # int | 

try: 
    # delete apiToken 
    api_response = api_instance.delete_api_token_by_id(admin_id, apitoken_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_api_token_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **adminId** | **int32**|  | 
 **apitokenId** | **int32**|  | 
=======
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteCollectorById**
> RestCollectorResponse DeleteCollectorById($id)
=======
# **delete_collector_by_id**
> RestCollectorResponse delete_collector_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete collector



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete collector
    api_response = api_instance.delete_collector_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collector_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteCollectorGroupById**
> RestCollectorGroupResponse DeleteCollectorGroupById($id)
=======
# **delete_collector_group_by_id**
> RestCollectorGroupResponse delete_collector_group_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete collector group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete collector group
    api_response = api_instance.delete_collector_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collector_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDashboardById**
> RestNullObjectResponse DeleteDashboardById($id)
=======
# **delete_dashboard_by_id**
> RestNullObjectResponse delete_dashboard_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete dashboard



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete dashboard
    api_response = api_instance.delete_dashboard_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dashboard_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDashboardGroupById**
> RestNullObjectResponse DeleteDashboardGroupById($id)
=======
# **delete_dashboard_group_by_id**
> RestNullObjectResponse delete_dashboard_group_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete dashboard group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete dashboard group
    api_response = api_instance.delete_dashboard_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dashboard_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDevice**
> RestNullObjectResponse DeleteDevice($id)
=======
# **delete_device**
> RestNullObjectResponse delete_device(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete a device



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete a device
    api_response = api_instance.delete_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_device: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDeviceGroupById**
> RestNullObjectResponse DeleteDeviceGroupById($id, $deleteChildren)
=======
# **delete_device_group_by_id**
> RestNullObjectResponse delete_device_group_by_id(id, delete_children=delete_children)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete device group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
delete_children = false # bool |  (optional) (default to false)

try: 
    # delete device group
    api_response = api_instance.delete_device_group_by_id(id, delete_children=delete_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_device_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **deleteChildren** | **bool**|  | [optional] [default to false]
=======
 **id** | **int**|  | 
 **delete_children** | **bool**|  | [optional] [default to false]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDeviceGroupPropertyByName**
> RestNullObjectResponse DeleteDeviceGroupPropertyByName($gid, $name)
=======
# **delete_device_group_property_by_name**
> RestNullObjectResponse delete_device_group_property_by_name(gid, name)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete device group property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
gid = 56 # int | 
name = 'name_example' # str | 

try: 
    # delete device group property
    api_response = api_instance.delete_device_group_property_by_name(gid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_device_group_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **gid** | **int32**|  | 
 **name** | **string**|  | 
=======
 **gid** | **int**|  | 
 **name** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteDevicePropertyByName**
> RestNullObjectResponse DeleteDevicePropertyByName($deviceId, $name)
=======
# **delete_device_property_by_name**
> RestNullObjectResponse delete_device_property_by_name(device_id, name)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete device  property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
name = 'name_example' # str | 

try: 
    # delete device  property
    api_response = api_instance.delete_device_property_by_name(device_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_device_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **name** | **string**|  | 
=======
 **device_id** | **int**|  | 
 **name** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteRoleById**
> RestRoleResponse DeleteRoleById($id)
=======
# **delete_role_by_id**
> RestRoleResponse delete_role_by_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete role



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # delete role
    api_response = api_instance.delete_role_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_role_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **DeleteServiceGroupById**
> RestNullObjectResponse DeleteServiceGroupById($id, $deleteChildren)
=======
# **delete_service_group_by_id**
> RestNullObjectResponse delete_service_group_by_id(id, delete_children=delete_children)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

delete service group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
delete_children = 0 # int |  (optional) (default to 0)

try: 
    # delete service group
    api_response = api_instance.delete_service_group_by_id(id, delete_children=delete_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_service_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **deleteChildren** | **int32**|  | [optional] [default to 0]
=======
 **id** | **int**|  | 
 **delete_children** | **int**|  | [optional] [default to 0]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAdminById**
> RestAdminResponse GetAdminById($id, $fields)
=======
# **get_admin_by_id**
> RestAdminResponse get_admin_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get admin
    api_response = api_instance.get_admin_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_admin_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAdminResponse**](RestAdminResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAdminList**
> RestAdminPaginationResponse GetAdminList($fields, $size, $offset, $filter)
=======
# **get_admin_list**
> RestAdminPaginationResponse get_admin_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get admin list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get admin list
    api_response = api_instance.get_admin_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_admin_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAdminPaginationResponse**](RestAdminPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertById**
> RestAlertResponse GetAlertById($id, $needMessage, $customColumns, $fields)
=======
# **get_alert_by_id**
> RestAlertResponse get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get alert



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 'id_example' # str | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try: 
    # get alert
    api_response = api_instance.get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **string**|  | 
 **needMessage** | **bool**|  | [optional] [default to false]
 **customColumns** | **string**|  | [optional] 
 **fields** | **string**|  | [optional] 
=======
 **id** | **str**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertResponse**](RestAlertResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertList**
> RestAlertPaginationResponse GetAlertList($needMessage, $customColumns, $fields, $size, $offset, $searchId, $filter)
=======
# **get_alert_list**
> RestAlertPaginationResponse get_alert_list(need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get alert list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
search_id = 'search_id_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try: 
    # get alert list
    api_response = api_instance.get_alert_list(need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **needMessage** | **bool**|  | [optional] [default to false]
 **customColumns** | **string**|  | [optional] 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **searchId** | **string**|  | [optional] 
 **filter** | **string**|  | [optional] 
=======
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertListByDeviceGroupId**
> RestAlertPaginationResponse GetAlertListByDeviceGroupId($id, $needMessage, $customColumns, $fields, $size, $offset, $searchId, $filter)
=======
# **get_alert_list_by_device_group_id**
> RestAlertPaginationResponse get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group alerts



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
search_id = 'search_id_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try: 
    # get device group alerts
    api_response = api_instance.get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_list_by_device_group_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **needMessage** | **bool**|  | [optional] [default to false]
 **customColumns** | **string**|  | [optional] 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **searchId** | **string**|  | [optional] 
 **filter** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertListByDeviceId**
> RestAlertPaginationResponse GetAlertListByDeviceId($id, $needMessage, $customColumns, $fields, $size, $offset, $searchId, $filter)
=======
# **get_alert_list_by_device_id**
> RestAlertPaginationResponse get_alert_list_by_device_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get alerts



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
search_id = 'search_id_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)

try: 
    # get alerts
    api_response = api_instance.get_alert_list_by_device_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_list_by_device_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **needMessage** | **bool**|  | [optional] [default to false]
 **customColumns** | **string**|  | [optional] 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **searchId** | **string**|  | [optional] 
 **filter** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertRuleById**
> RestAlertRuleResponse GetAlertRuleById($id, $fields)
=======
# **get_alert_rule_by_id**
> RestAlertRuleResponse get_alert_rule_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get alert rule by id



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get alert rule by id
    api_response = api_instance.get_alert_rule_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_rule_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetAlertRuleList**
> RestAlertRulePaginationResponse GetAlertRuleList($fields, $size, $offset, $filter)
=======
# **get_alert_rule_list**
> RestAlertRulePaginationResponse get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get alert rule list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get alert rule list
    api_response = api_instance.get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_alert_rule_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertRulePaginationResponse**](RestAlertRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetApiTokenListByAdminId**
> RestApiTokenPaginationResponse GetApiTokenListByAdminId($adminId, $fields, $size, $offset, $filter)
=======
# **get_api_token_list_by_admin_id**
> RestApiTokenPaginationResponse get_api_token_list_by_admin_id(admin_id, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get apiToken by admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
admin_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get apiToken by admin
    api_response = api_instance.get_api_token_list_by_admin_id(admin_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_token_list_by_admin_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **adminId** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **admin_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestApiTokenPaginationResponse**](RestApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetCollectorById**
> RestCollectorResponse GetCollectorById($id, $fields)
=======
# **get_collector_by_id**
> RestCollectorResponse get_collector_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get collector



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get collector
    api_response = api_instance.get_collector_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_collector_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetCollectorGroupById**
> RestCollectorGroupResponse GetCollectorGroupById($id, $fields)
=======
# **get_collector_group_by_id**
> RestCollectorGroupResponse get_collector_group_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get collector group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get collector group
    api_response = api_instance.get_collector_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_collector_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetCollectorGroupList**
> RestCollectorGroupPaginationResponse GetCollectorGroupList($fields, $size, $offset, $filter)
=======
# **get_collector_group_list**
> RestCollectorGroupPaginationResponse get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get collector group list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get collector group list
    api_response = api_instance.get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_collector_group_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorGroupPaginationResponse**](RestCollectorGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetCollectorList**
> RestCollectorPaginationResponse GetCollectorList($fields, $size, $offset, $filter)
=======
# **get_collector_list**
> RestCollectorPaginationResponse get_collector_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get collector list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get collector list
    api_response = api_instance.get_collector_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_collector_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestCollectorPaginationResponse**](RestCollectorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDashboardById**
> RestDashboardV1Response GetDashboardById($id, $fields)
=======
# **get_dashboard_by_id**
> RestDashboardV1Response get_dashboard_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get dashboard



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get dashboard
    api_response = api_instance.get_dashboard_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDashboardV1Response**](RestDashboardV1Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDashboardGroupById**
> RestDashboardGroupResponse GetDashboardGroupById($id, $fields)
=======
# **get_dashboard_group_by_id**
> RestDashboardGroupResponse get_dashboard_group_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get dashboard group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get dashboard group
    api_response = api_instance.get_dashboard_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDashboardGroupResponse**](RestDashboardGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDashboardGroupList**
> RestDashboardGroupPaginationResponse GetDashboardGroupList($fields, $size, $offset, $filter)
=======
# **get_dashboard_group_list**
> RestDashboardGroupPaginationResponse get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get dashboard group list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get dashboard group list
    api_response = api_instance.get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_group_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDashboardGroupPaginationResponse**](RestDashboardGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDashboardList**
> RestDashboardV1PaginationResponse GetDashboardList($fields, $size, $offset, $filter)
=======
# **get_dashboard_list**
> RestDashboardV1PaginationResponse get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get dashboard list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get dashboard list
    api_response = api_instance.get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dashboard_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDashboardV1PaginationResponse**](RestDashboardV1PaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceById**
> RestDeviceResponse GetDeviceById($id, $fields)
=======
# **get_device_by_id**
> RestDeviceResponse get_device_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device by id



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device by id
    api_response = api_instance.get_device_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceById**
> RestDeviceDatasourceResponse GetDeviceDatasourceById($deviceId, $id, $fields)
=======
# **get_device_datasource_by_id**
> RestDeviceDatasourceResponse get_device_datasource_by_id(device_id, id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device datasource 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device datasource 
    api_response = api_instance.get_device_datasource_by_id(device_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDatasourceResponse**](RestDeviceDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceDataById**
> RestDeviceDatasourceDataResponse GetDeviceDatasourceDataById($deviceId, $id, $period, $start, $end, $datapoints, $format)
=======
# **get_device_datasource_data_by_id**
> RestDeviceDatasourceDataResponse get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device datasource data 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
id = 56 # int | 
period = 1 # float |  (optional) (default to 1)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try: 
    # get device datasource data 
    api_response = api_instance.get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_data_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **id** | **int32**|  | 
 **period** | **float64**|  | [optional] [default to 1]
 **start** | **int64**|  | [optional] [default to 0]
 **end** | **int64**|  | [optional] [default to 0]
 **datapoints** | **string**|  | [optional] 
 **format** | **string**|  | [optional] [default to json]
=======
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDatasourceDataResponse**](RestDeviceDatasourceDataResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceAlertSettingById**
> RestDeviceDataSourceInstanceAlertSettingResponse GetDeviceDatasourceInstanceAlertSettingById($deviceId, $hdsId, $instanceId, $id, $fields)
=======
# **get_device_datasource_instance_alert_setting_by_id**
> RestDeviceDataSourceInstanceAlertSettingResponse get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance alert setting



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device instance alert setting
    api_response = api_instance.get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **instanceId** | **int32**|  | 
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDataSourceInstanceAlertSettingResponse**](RestDeviceDataSourceInstanceAlertSettingResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceById**
> RestDeviceDataSourceInstanceResponse GetDeviceDatasourceInstanceById($deviceId, $hdsId, $id, $fields)
=======
# **get_device_datasource_instance_by_id**
> RestDeviceDataSourceInstanceResponse get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device instance 
    api_response = api_instance.get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceData**
> RestDeviceDataSourceInstanceDataResponse GetDeviceDatasourceInstanceData($deviceId, $hdsId, $id, $period, $start, $end, $datapoints, $format)
=======
# **get_device_datasource_instance_data**
> RestDeviceDataSourceInstanceDataResponse get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance data



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
id = 56 # int | 
period = 1 # float |  (optional) (default to 1)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try: 
    # get device instance data
    api_response = api_instance.get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_data: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **id** | **int32**|  | 
 **period** | **float64**|  | [optional] [default to 1]
 **start** | **int64**|  | [optional] [default to 0]
 **end** | **int64**|  | [optional] [default to 0]
 **datapoints** | **string**|  | [optional] 
 **format** | **string**|  | [optional] [default to json]
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDataSourceInstanceDataResponse**](RestDeviceDataSourceInstanceDataResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceGraphData**
> RestGraphPlotResponse GetDeviceDatasourceInstanceGraphData($deviceId, $hdsId, $id, $graphId, $start, $end, $format)
=======
# **get_device_datasource_instance_graph_data**
> RestGraphPlotResponse get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance graph data 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
id = 56 # int | 
graph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try: 
    # get device instance graph data 
    api_response = api_instance.get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_graph_data: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **id** | **int32**|  | 
 **graphId** | **int32**|  | 
 **start** | **int64**|  | [optional] 
 **end** | **int64**|  | [optional] 
 **format** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceGroupById**
> RestDeviceDataSourceInstanceGroupResponse GetDeviceDatasourceInstanceGroupById($deviceId, $deviceDsId, $id, $fields)
=======
# **get_device_datasource_instance_group_by_id**
> RestDeviceDataSourceInstanceGroupResponse get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device datasource instance group 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
device_ds_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device datasource instance group 
    api_response = api_instance.get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **deviceDsId** | **int32**|  | 
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceInstanceGroupOverviewGraphData**
> RestGraphPlotResponse GetDeviceDatasourceInstanceGroupOverviewGraphData($deviceId, $deviceDsId, $dsigId, $ographId, $start, $end, $format)
=======
# **get_device_datasource_instance_group_overview_graph_data**
> RestGraphPlotResponse get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance group overview graph data 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
device_ds_id = 56 # int | 
dsig_id = 56 # int | 
ograph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try: 
    # get device instance group overview graph data 
    api_response = api_instance.get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_instance_group_overview_graph_data: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **deviceDsId** | **int32**|  | 
 **dsigId** | **int32**|  | 
 **ographId** | **int32**|  | 
 **start** | **int64**|  | [optional] 
 **end** | **int64**|  | [optional] 
 **format** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **dsig_id** | **int**|  | 
 **ograph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceDatasourceList**
> RestDeviceDatasourcePaginationResponse GetDeviceDatasourceList($deviceId, $fields, $size, $offset, $filter)
=======
# **get_device_datasource_list**
> RestDeviceDatasourcePaginationResponse get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device datasource list 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device datasource list 
    api_response = api_instance.get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_datasource_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceDatasourcePaginationResponse**](RestDeviceDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupById**
> RestDeviceGroupResponse GetDeviceGroupById($id, $fields)
=======
# **get_device_group_by_id**
> RestDeviceGroupResponse get_device_group_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device group
    api_response = api_instance.get_device_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupDatasourceAlertSetting**
> RestDeviceGroupDatasourceAlertConfigResponse GetDeviceGroupDatasourceAlertSetting($deviceGroupId, $dsId, $fields)
=======
# **get_device_group_datasource_alert_setting**
> RestDeviceGroupDatasourceAlertConfigResponse get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group datasource alert setting 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_group_id = 56 # int | 
ds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device group datasource alert setting 
    api_response = api_instance.get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_datasource_alert_setting: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceGroupId** | **int32**|  | 
 **dsId** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupDatasourceAlertConfigResponse**](RestDeviceGroupDatasourceAlertConfigResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupDatasourceById**
> RestDeviceGroupDatasourceResponse GetDeviceGroupDatasourceById($deviceGroupId, $id, $fields)
=======
# **get_device_group_datasource_by_id**
> RestDeviceGroupDatasourceResponse get_device_group_datasource_by_id(device_group_id, id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group datasource



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_group_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device group datasource
    api_response = api_instance.get_device_group_datasource_by_id(device_group_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_datasource_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceGroupId** | **int32**|  | 
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupDatasourceResponse**](RestDeviceGroupDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupDatasourceList**
> RestDeviceGroupDatasourceResponse GetDeviceGroupDatasourceList($deviceGroupId, $fields, $size, $offset, $filter)
=======
# **get_device_group_datasource_list**
> RestDeviceGroupDatasourceResponse get_device_group_datasource_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group datasource list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_group_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device group datasource list
    api_response = api_instance.get_device_group_datasource_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_datasource_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceGroupId** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **device_group_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupDatasourceResponse**](RestDeviceGroupDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupList**
> RestDeviceGroupPaginationResponse GetDeviceGroupList($fields, $size, $offset, $filter)
=======
# **get_device_group_list**
> RestDeviceGroupPaginationResponse get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device group list
    api_response = api_instance.get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupPaginationResponse**](RestDeviceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupProperties**
> RestPropertyPaginationResponse GetDeviceGroupProperties($gid, $fields, $size, $offset, $filter)
=======
# **get_device_group_properties**
> RestPropertyPaginationResponse get_device_group_properties(gid, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group properties



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
gid = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device group properties
    api_response = api_instance.get_device_group_properties(gid, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_properties: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **gid** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **gid** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestPropertyPaginationResponse**](RestPropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceGroupPropertyByName**
> RestPropertyResponse GetDeviceGroupPropertyByName($gid, $name, $fields)
=======
# **get_device_group_property_by_name**
> RestPropertyResponse get_device_group_property_by_name(gid, name, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device group property by name



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
gid = 56 # int | 
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device group property by name
    api_response = api_instance.get_device_group_property_by_name(gid, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_group_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **gid** | **int32**|  | 
 **name** | **string**|  | 
 **fields** | **string**|  | [optional] 
=======
 **gid** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceInstanceGraphDataOnlyByInstanceId**
> RestGraphPlotResponse GetDeviceInstanceGraphDataOnlyByInstanceId($instanceId, $graphId, $start, $end, $format)
=======
# **get_device_instance_graph_data_only_by_instance_id**
> RestGraphPlotResponse get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device instance graphData



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
instance_id = 56 # int | 
graph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try: 
    # get device instance graphData
    api_response = api_instance.get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_instance_graph_data_only_by_instance_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **instanceId** | **int32**|  | 
 **graphId** | **int32**|  | 
 **start** | **int64**|  | [optional] 
 **end** | **int64**|  | [optional] 
 **format** | **string**|  | [optional] 
=======
 **instance_id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDeviceList**
> RestDevicePaginationResponse GetDeviceList($fields, $size, $offset, $filter)
=======
# **get_device_list**
> RestDevicePaginationResponse get_device_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device list
    api_response = api_instance.get_device_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDevicePaginationResponse**](RestDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDevicePropertiesList**
> RestPropertyPaginationResponse GetDevicePropertiesList($deviceId, $fields, $size, $offset, $filter)
=======
# **get_device_properties_list**
> RestPropertyPaginationResponse get_device_properties_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device properties



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get device properties
    api_response = api_instance.get_device_properties_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_properties_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestPropertyPaginationResponse**](RestPropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetDevicePropertyByName**
> RestPropertyResponse GetDevicePropertyByName($deviceId, $name, $fields)
=======
# **get_device_property_by_name**
> RestPropertyResponse get_device_property_by_name(device_id, name, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get device property by name



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try: 
    # get device property by name
    api_response = api_instance.get_device_property_by_name(device_id, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_device_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **name** | **string**|  | 
 **fields** | **string**|  | [optional] 
=======
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetImmediateDeviceListByDeviceGroupId**
> RestDevicePaginationResponse GetImmediateDeviceListByDeviceGroupId($id, $fields, $size, $offset, $filter)
=======
# **get_immediate_device_list_by_device_group_id**
> RestDevicePaginationResponse get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get immediate devices under group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get immediate devices under group
    api_response = api_instance.get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_immediate_device_list_by_device_group_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDevicePaginationResponse**](RestDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetRoleById**
> RestRoleResponse GetRoleById($id, $fields)
=======
# **get_role_by_id**
> RestRoleResponse get_role_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get role by id



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get role by id
    api_response = api_instance.get_role_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_role_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetRoleList**
> RestRolePaginationResponse GetRoleList($fields, $size, $offset, $filter)
=======
# **get_role_list**
> RestRolePaginationResponse get_role_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get role list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get role list
    api_response = api_instance.get_role_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_role_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestRolePaginationResponse**](RestRolePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetServiceGraphData**
> RestGraphPlotResponse GetServiceGraphData($serviceId, $checkpointId, $graphName, $start, $end, $format)
=======
# **get_service_graph_data**
> RestGraphPlotResponse get_service_graph_data(service_id, checkpoint_id, graph_name, start=start, end=end, format=format)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get service graph data



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
service_id = 56 # int | 
checkpoint_id = 56 # int | 
graph_name = 'graph_name_example' # str | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try: 
    # get service graph data
    api_response = api_instance.get_service_graph_data(service_id, checkpoint_id, graph_name, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_graph_data: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **serviceId** | **int32**|  | 
 **checkpointId** | **int32**|  | 
 **graphName** | **string**|  | 
 **start** | **int64**|  | [optional] 
 **end** | **int64**|  | [optional] 
 **format** | **string**|  | [optional] 
=======
 **service_id** | **int**|  | 
 **checkpoint_id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetServiceGroupById**
> RestServiceGroupResponse GetServiceGroupById($id, $fields)
=======
# **get_service_group_by_id**
> RestServiceGroupResponse get_service_group_by_id(id, fields=fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get service group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try: 
    # get service group
    api_response = api_instance.get_service_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **fields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetServiceGroupList**
> RestServiceGroupPaginationResponse GetServiceGroupList($fields, $size, $offset, $filter)
=======
# **get_service_group_list**
> RestServiceGroupPaginationResponse get_service_group_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get service group list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get service group list
    api_response = api_instance.get_service_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_service_group_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestServiceGroupPaginationResponse**](RestServiceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetSiteMonitorCheckPointList**
> RestSmCheckPointPaginationResponse GetSiteMonitorCheckPointList($fields, $size, $offset, $filter)
=======
# **get_site_monitor_check_point_list**
> RestSMCheckPointPaginationResponse get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get site monitor checkpoint list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get site monitor checkpoint list
    api_response = api_instance.get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_site_monitor_check_point_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 

### Return type

[**RestSmCheckPointPaginationResponse**](RestSMCheckPointPaginationResponse.md)
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestSMCheckPointPaginationResponse**](RestSMCheckPointPaginationResponse.md)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **GetUnmonitoredDeviceList**
> RestUnmonitoredDevicePaginationResponse GetUnmonitoredDeviceList($fields, $size, $offset, $filter)
=======
# **get_unmonitored_device_list**
> RestUnmonitoredDevicePaginationResponse get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

get unmonitored device list



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try: 
    # get unmonitored device list
    api_response = api_instance.get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_unmonitored_device_list: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **fields** | **string**|  | [optional] 
 **size** | **int32**|  | [optional] [default to 50]
 **offset** | **int32**|  | [optional] [default to 0]
 **filter** | **string**|  | [optional] 
=======
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestUnmonitoredDevicePaginationResponse**](RestUnmonitoredDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **InstallCollector**
> *os.File InstallCollector($collectorId, $osAndArch, $collectorVersion, $token, $monitorOthers, $collectorSize, $useEA)
=======
# **install_collector**
> file install_collector(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

install collector



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
collector_id = 56 # int | 
os_and_arch = 'os_and_arch_example' # str | 
collector_version = 56 # int |  (optional)
token = 'token_example' # str |  (optional)
monitor_others = true # bool |  (optional) (default to true)
collector_size = 'medium' # str |  (optional) (default to medium)
use_ea = false # bool |  (optional) (default to false)

try: 
    # install collector
    api_response = api_instance.install_collector(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->install_collector: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **collectorId** | **int32**|  | 
 **osAndArch** | **string**|  | 
 **collectorVersion** | **int32**|  | [optional] 
 **token** | **string**|  | [optional] 
 **monitorOthers** | **bool**|  | [optional] [default to true]
 **collectorSize** | **string**|  | [optional] [default to medium]
 **useEA** | **bool**|  | [optional] [default to false]

### Return type

[***os.File**](*os.File.md)
=======
 **collector_id** | **int**|  | 
 **os_and_arch** | **str**|  | 
 **collector_version** | **int**|  | [optional] 
 **token** | **str**|  | [optional] 
 **monitor_others** | **bool**|  | [optional] [default to true]
 **collector_size** | **str**|  | [optional] [default to medium]
 **use_ea** | **bool**|  | [optional] [default to false]

### Return type

[**file**](file.md)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **PatchDeviceById**
> RestDeviceResponse PatchDeviceById($body, $id, $opType, $patchFields)
=======
# **patch_device_by_id**
> RestDeviceResponse patch_device_by_id(body, id, op_type=op_type, patch_fields=patch_fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

patch a device



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDevice() # RestDevice | 
id = 56 # int | 
op_type = 'refresh' # str |  (optional) (default to refresh)
patch_fields = 'patch_fields_example' # str |  (optional)

try: 
    # patch a device
    api_response = api_instance.patch_device_by_id(body, id, op_type=op_type, patch_fields=patch_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_device_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
<<<<<<< HEAD
 **id** | **int32**|  | 
 **opType** | **string**|  | [optional] [default to refresh]
 **patchFields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **PatchDeviceGroupById**
> RestDeviceGroupResponse PatchDeviceGroupById($id, $body, $opType, $patchFields)
=======
# **patch_device_group_by_id**
> RestDeviceGroupResponse patch_device_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

patch device group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestDeviceGroup() # RestDeviceGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)
patch_fields = 'patch_fields_example' # str |  (optional)

try: 
    # patch device group
    api_response = api_instance.patch_device_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_device_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 
 **opType** | **string**|  | [optional] [default to refresh]
 **patchFields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **PatchServiceGroupById**
> RestServiceGroupResponse PatchServiceGroupById($id, $body, $opType, $patchFields)
=======
# **patch_service_group_by_id**
> RestServiceGroupResponse patch_service_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

patch service group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestServiceGroup() # RestServiceGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)
patch_fields = 'patch_fields_example' # str |  (optional)

try: 
    # patch service group
    api_response = api_instance.patch_service_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_service_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 
 **opType** | **string**|  | [optional] [default to refresh]
 **patchFields** | **string**|  | [optional] 
=======
 **id** | **int**|  | 
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **ScheduleAutoDiscoveryByDeviceId**
> RestStringResponse ScheduleAutoDiscoveryByDeviceId($id)
=======
# **schedule_auto_discovery_by_device_id**
> RestStringResponse schedule_auto_discovery_by_device_id(id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

schedule auto discovery for a host



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 

try: 
    # schedule auto discovery for a host
    api_response = api_instance.schedule_auto_discovery_by_device_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->schedule_auto_discovery_by_device_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestStringResponse**](RestStringResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateAdminById**
> RestAdminResponse UpdateAdminById($id, $body, $changePassword)
=======
# **update_admin_by_id**
> RestAdminResponse update_admin_by_id(id, body, change_password=change_password)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestAdmin() # RestAdmin | 
change_password = false # bool |  (optional) (default to false)

try: 
    # update admin
    api_response = api_instance.update_admin_by_id(id, body, change_password=change_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_admin_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **body** | [**RestAdmin**](RestAdmin.md)|  | 
 **changePassword** | **bool**|  | [optional] [default to false]
=======
 **id** | **int**|  | 
 **body** | [**RestAdmin**](RestAdmin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAdminResponse**](RestAdminResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateAlertRuleById**
> RestAlertRuleResponse UpdateAlertRuleById($body, $id)
=======
# **update_alert_rule_by_id**
> RestAlertRuleResponse update_alert_rule_by_id(body, id)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update alert rule



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestAlertRule() # RestAlertRule | 
id = 56 # int | 

try: 
    # update alert rule
    api_response = api_instance.update_alert_rule_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_alert_rule_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertRule**](RestAlertRule.md)|  | 
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateApiTokenByAdminId**
> RestApiTokenResponse UpdateApiTokenByAdminId($adminId, $apitokenId, $body)
=======
# **update_api_token_by_admin_id**
> RestApiTokenResponse update_api_token_by_admin_id(admin_id, apitoken_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update apiToken by admin



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
admin_id = 56 # int | 
apitoken_id = 56 # int | 
body = logicmonitor.RestAPIToken() # RestAPIToken | 

try: 
    # update apiToken by admin
    api_response = api_instance.update_api_token_by_admin_id(admin_id, apitoken_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_api_token_by_admin_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **adminId** | **int32**|  | 
 **apitokenId** | **int32**|  | 
 **body** | [**RestApiToken**](RestAPIToken.md)|  | 
=======
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**RestAPIToken**](RestAPIToken.md)|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateCollectorById**
> RestCollectorResponse UpdateCollectorById($id, $body)
=======
# **update_collector_by_id**
> RestCollectorResponse update_collector_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update collector



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestCollector() # RestCollector | 

try: 
    # update collector
    api_response = api_instance.update_collector_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_collector_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestCollector**](RestCollector.md)|  | 

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateCollectorGroupById**
> RestCollectorGroupResponse UpdateCollectorGroupById($id, $body)
=======
# **update_collector_group_by_id**
> RestCollectorGroupResponse update_collector_group_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update collector group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestCollectorGroup() # RestCollectorGroup | 

try: 
    # update collector group
    api_response = api_instance.update_collector_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_collector_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestCollectorGroup**](RestCollectorGroup.md)|  | 

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDashboardById**
> RestDashboardV1Response UpdateDashboardById($id, $body, $overwriteGroupFields)
=======
# **update_dashboard_by_id**
> RestDashboardV1Response update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update dashboard



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestDashboardV1() # RestDashboardV1 | 
overwrite_group_fields = false # bool |  (optional) (default to false)

try: 
    # update dashboard
    api_response = api_instance.update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dashboard_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
 **body** | [**RestDashboardV1**](RestDashboardV1.md)|  | 
 **overwriteGroupFields** | **bool**|  | [optional] [default to false]
=======
 **id** | **int**|  | 
 **body** | [**RestDashboardV1**](RestDashboardV1.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDashboardV1Response**](RestDashboardV1Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDashboardGroupById**
> RestDashboardGroupResponse UpdateDashboardGroupById($id, $body)
=======
# **update_dashboard_group_by_id**
> RestDashboardGroupResponse update_dashboard_group_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update dashboard group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestDashboardGroup() # RestDashboardGroup | 

try: 
    # update dashboard group
    api_response = api_instance.update_dashboard_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dashboard_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDashboardGroup**](RestDashboardGroup.md)|  | 

### Return type

[**RestDashboardGroupResponse**](RestDashboardGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDevice**
> RestDeviceResponse UpdateDevice($body, $id, $opType)
=======
# **update_device**
> RestDeviceResponse update_device(body, id, op_type=op_type)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update a device



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
body = logicmonitor.RestDevice() # RestDevice | 
id = 56 # int | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try: 
    # update a device
    api_response = api_instance.update_device(body, id, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
<<<<<<< HEAD
 **id** | **int32**|  | 
 **opType** | **string**|  | [optional] [default to refresh]
=======
 **id** | **int**|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceDatasourceInstanceAlertSettingById**
> RestDeviceDataSourceInstanceAlertSettingResponse UpdateDeviceDatasourceInstanceAlertSettingById($deviceId, $hdsId, $instanceId, $id, $body)
=======
# **update_device_datasource_instance_alert_setting_by_id**
> RestDeviceDataSourceInstanceAlertSettingResponse update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device instance alert setting



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
id = 56 # int | 
body = logicmonitor.RestDeviceDataSourceInstanceAlertSetting() # RestDeviceDataSourceInstanceAlertSetting | 

try: 
    # update device instance alert setting
    api_response = api_instance.update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **instanceId** | **int32**|  | 
 **id** | **int32**|  | 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceDataSourceInstanceAlertSetting**](RestDeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceAlertSettingResponse**](RestDeviceDataSourceInstanceAlertSettingResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceDatasourceInstanceById**
> RestDeviceDataSourceInstanceResponse UpdateDeviceDatasourceInstanceById($deviceId, $hdsId, $id, $body)
=======
# **update_device_datasource_instance_by_id**
> RestDeviceDataSourceInstanceResponse update_device_datasource_instance_by_id(device_id, hds_id, id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device instance 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
hds_id = 56 # int | 
id = 56 # int | 
body = logicmonitor.RestDeviceDataSourceInstance() # RestDeviceDataSourceInstance | 

try: 
    # update device instance 
    api_response = api_instance.update_device_datasource_instance_by_id(device_id, hds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_datasource_instance_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **hdsId** | **int32**|  | 
 **id** | **int32**|  | 
=======
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceDataSourceInstance**](RestDeviceDataSourceInstance.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceDatasourceInstanceGroupById**
> RestDeviceDataSourceInstanceGroupResponse UpdateDeviceDatasourceInstanceGroupById($deviceId, $deviceDsId, $id, $body)
=======
# **update_device_datasource_instance_group_by_id**
> RestDeviceDataSourceInstanceGroupResponse update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device datasource instance group 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
device_ds_id = 56 # int | 
id = 56 # int | 
body = logicmonitor.RestDeviceDataSourceInstanceGroup() # RestDeviceDataSourceInstanceGroup | 

try: 
    # update device datasource instance group 
    api_response = api_instance.update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_datasource_instance_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **deviceDsId** | **int32**|  | 
 **id** | **int32**|  | 
=======
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceDataSourceInstanceGroup**](RestDeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceGroupById**
> RestDeviceGroupResponse UpdateDeviceGroupById($id, $body)
=======
# **update_device_group_by_id**
> RestDeviceGroupResponse update_device_group_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestDeviceGroup() # RestDeviceGroup | 

try: 
    # update device group
    api_response = api_instance.update_device_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceGroupDatasourceAlertSetting**
> RestDeviceGroupDatasourceAlertConfigResponse UpdateDeviceGroupDatasourceAlertSetting($deviceGroupId, $dsId, $body)
=======
# **update_device_group_datasource_alert_setting**
> RestDeviceGroupDatasourceAlertConfigResponse update_device_group_datasource_alert_setting(device_group_id, ds_id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device group datasource alert setting 



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_group_id = 56 # int | 
ds_id = 56 # int | 
body = logicmonitor.RestDeviceGroupDataSourceAlertConfig() # RestDeviceGroupDataSourceAlertConfig | 

try: 
    # update device group datasource alert setting 
    api_response = api_instance.update_device_group_datasource_alert_setting(device_group_id, ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_group_datasource_alert_setting: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceGroupId** | **int32**|  | 
 **dsId** | **int32**|  | 
=======
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestDeviceGroupDataSourceAlertConfig**](RestDeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**RestDeviceGroupDatasourceAlertConfigResponse**](RestDeviceGroupDatasourceAlertConfigResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDeviceGroupPropertyByName**
> RestPropertyResponse UpdateDeviceGroupPropertyByName($gid, $name, $body)
=======
# **update_device_group_property_by_name**
> RestPropertyResponse update_device_group_property_by_name(gid, name, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device group property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
gid = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor.RestProperty() # RestProperty | 

try: 
    # update device group property
    api_response = api_instance.update_device_group_property_by_name(gid, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_group_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **gid** | **int32**|  | 
 **name** | **string**|  | 
=======
 **gid** | **int**|  | 
 **name** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateDevicePropertyByName**
> RestPropertyResponse UpdateDevicePropertyByName($deviceId, $name, $body)
=======
# **update_device_property_by_name**
> RestPropertyResponse update_device_property_by_name(device_id, name, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update device  property



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
device_id = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor.RestProperty() # RestProperty | 

try: 
    # update device  property
    api_response = api_instance.update_device_property_by_name(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_device_property_by_name: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **deviceId** | **int32**|  | 
 **name** | **string**|  | 
=======
 **device_id** | **int**|  | 
 **name** | **str**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateRoleById**
> RestRoleResponse UpdateRoleById($id, $body)
=======
# **update_role_by_id**
> RestRoleResponse update_role_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update role



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestRole() # RestRole | 

try: 
    # update role
    api_response = api_instance.update_role_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_role_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestRole**](RestRole.md)|  | 

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<<<<<<< HEAD
# **UpdateServiceGroupById**
> RestServiceGroupResponse UpdateServiceGroupById($id, $body)
=======
# **update_service_group_by_id**
> RestServiceGroupResponse update_service_group_by_id(id, body)
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

update service group



<<<<<<< HEAD
=======
### Example 
```python
from __future__ import print_function
import time
import logicmonitor
from logicmonitor.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
logicmonitor.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# logicmonitor.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = logicmonitor.DefaultApi()
id = 56 # int | 
body = logicmonitor.RestServiceGroup() # RestServiceGroup | 

try: 
    # update service group
    api_response = api_instance.update_service_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_service_group_by_id: %s\n" % e)
```
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
<<<<<<< HEAD
 **id** | **int32**|  | 
=======
 **id** | **int**|  | 
>>>>>>> 38b4e78ee2e1185895ba586df7218ce4c61573cf
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

