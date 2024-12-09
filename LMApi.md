# logicmonitor_sdk.LMApi

All URIs are relative to */santaba/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_by_id**](LMApi.md#ack_alert_by_id) | **POST** /alert/alerts/{id}/ack | ack alert by id
[**ack_collector_down_alert_by_id**](LMApi.md#ack_collector_down_alert_by_id) | **POST** /setting/collector/collectors/{id}/ackdown | ack collector down alert
[**add_access_group**](LMApi.md#add_access_group) | **POST** /setting/accessgroup/add | Create a access group
[**add_admin**](LMApi.md#add_admin) | **POST** /setting/admins | add user
[**add_alert_note_by_id**](LMApi.md#add_alert_note_by_id) | **POST** /alert/alerts/{id}/note | add alert note
[**add_alert_rule**](LMApi.md#add_alert_rule) | **POST** /setting/alert/rules | add alert rule
[**add_api_token_by_admin_id**](LMApi.md#add_api_token_by_admin_id) | **POST** /setting/admins/{adminId}/apitokens | add api tokens for a user
[**add_applies_to_function**](LMApi.md#add_applies_to_function) | **POST** /setting/functions | add applies to function
[**add_collector**](LMApi.md#add_collector) | **POST** /setting/collector/collectors | add collector
[**add_collector_group**](LMApi.md#add_collector_group) | **POST** /setting/collector/groups | add collector group
[**add_config_source**](LMApi.md#add_config_source) | **POST** /setting/configsources | add config source
[**add_dashboard**](LMApi.md#add_dashboard) | **POST** /dashboard/dashboards | add dashboard
[**add_dashboard_group**](LMApi.md#add_dashboard_group) | **POST** /dashboard/groups | add dashboard group
[**add_dashboard_group_asynchronously**](LMApi.md#add_dashboard_group_asynchronously) | **POST** /dashboard/groups/{id}/asyncclone | add dashboard group asynchronously
[**add_datasource_by_id**](LMApi.md#add_datasource_by_id) | **POST** /setting/datasources | add datasource
[**add_device**](LMApi.md#add_device) | **POST** /device/devices | add a new device
[**add_device_datasource_instance**](LMApi.md#add_device_datasource_instance) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | add device instance 
[**add_device_datasource_instance_group**](LMApi.md#add_device_datasource_instance_group) | **POST** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | add device datasource instance group 
[**add_device_group**](LMApi.md#add_device_group) | **POST** /device/groups | add device group
[**add_device_group_cluster_alert_conf**](LMApi.md#add_device_group_cluster_alert_conf) | **POST** /device/groups/{deviceGroupId}/clusterAlertConf | Add cluster alert configuration
[**add_device_group_property**](LMApi.md#add_device_group_property) | **POST** /device/groups/{gid}/properties | add device group property
[**add_device_property**](LMApi.md#add_device_property) | **POST** /device/devices/{deviceId}/properties | add device property
[**add_dns_mapping**](LMApi.md#add_dns_mapping) | **POST** /setting/dnsmappings | Add dns mapping
[**add_escalation_chain**](LMApi.md#add_escalation_chain) | **POST** /setting/alert/chains | add escalation chain
[**add_event_source**](LMApi.md#add_event_source) | **POST** /setting/eventsources | add eventSource
[**add_job_monitor**](LMApi.md#add_job_monitor) | **POST** /setting/batchjobs | Add JobMonitor
[**add_log_source**](LMApi.md#add_log_source) | **POST** /setting/logsources | add log source 
[**add_netscan**](LMApi.md#add_netscan) | **POST** /setting/netscans | add a new netscan
[**add_oid**](LMApi.md#add_oid) | **POST** /setting/oids | add a new OID
[**add_ops_note**](LMApi.md#add_ops_note) | **POST** /setting/opsnotes | add opsnote
[**add_property_rule**](LMApi.md#add_property_rule) | **POST** /setting/propertyrules | add a new property rule
[**add_recipient_group**](LMApi.md#add_recipient_group) | **POST** /setting/recipientgroups | add recipient group
[**add_report**](LMApi.md#add_report) | **POST** /report/reports | add report
[**add_report_group**](LMApi.md#add_report_group) | **POST** /report/groups | add report group
[**add_role**](LMApi.md#add_role) | **POST** /setting/roles | add role
[**add_sdt**](LMApi.md#add_sdt) | **POST** /sdt/sdts | add SDT (Response may contain extra fields depending upon the type of SDT being added)
[**add_topology_source**](LMApi.md#add_topology_source) | **POST** /setting/topologysources | Add TopologySource
[**add_website**](LMApi.md#add_website) | **POST** /website/websites | add website
[**add_website_group**](LMApi.md#add_website_group) | **POST** /website/groups | add website group
[**add_widget**](LMApi.md#add_widget) | **POST** /dashboard/widgets | add widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**collect_device_config_source_config**](LMApi.md#collect_device_config_source_config) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/configCollection | collect a config for a device
[**create_log_partition**](LMApi.md#create_log_partition) | **POST** /log/partitions | Create a new log partition
[**delete_access_group**](LMApi.md#delete_access_group) | **DELETE** /setting/accessgroup/{id} | Delete access group
[**delete_admin_by_id**](LMApi.md#delete_admin_by_id) | **DELETE** /setting/admins/{id} | delete user
[**delete_alert_rule_by_id**](LMApi.md#delete_alert_rule_by_id) | **DELETE** /setting/alert/rules/{id} | delete alert rule
[**delete_api_token_by_id**](LMApi.md#delete_api_token_by_id) | **DELETE** /setting/admins/{adminId}/apitokens/{apitokenId} | delete apiToken
[**delete_applies_to_function_by_id**](LMApi.md#delete_applies_to_function_by_id) | **DELETE** /setting/functions/{id} | delete applies to function
[**delete_collector_by_id**](LMApi.md#delete_collector_by_id) | **DELETE** /setting/collector/collectors/{id} | delete collector
[**delete_collector_group_by_id**](LMApi.md#delete_collector_group_by_id) | **DELETE** /setting/collector/groups/{id} | delete collector group
[**delete_config_source_by_id**](LMApi.md#delete_config_source_by_id) | **DELETE** /setting/configsources/{id} | delete config source by id
[**delete_dashboard_by_id**](LMApi.md#delete_dashboard_by_id) | **DELETE** /dashboard/dashboards/{id} | delete dashboard
[**delete_dashboard_group_by_id**](LMApi.md#delete_dashboard_group_by_id) | **DELETE** /dashboard/groups/{id} | delete dashboard group
[**delete_datasource_by_id**](LMApi.md#delete_datasource_by_id) | **DELETE** /setting/datasources/{id} | delete datasource
[**delete_device_by_id**](LMApi.md#delete_device_by_id) | **DELETE** /device/devices/{id} | delete a device
[**delete_device_datasource_instance_by_id**](LMApi.md#delete_device_datasource_instance_by_id) | **DELETE** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | delete a device instance
[**delete_device_group_by_id**](LMApi.md#delete_device_group_by_id) | **DELETE** /device/groups/{id} | delete device group
[**delete_device_group_cluster_alert_conf_by_id**](LMApi.md#delete_device_group_cluster_alert_conf_by_id) | **DELETE** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Delete cluster alert configuration
[**delete_device_group_property_by_name**](LMApi.md#delete_device_group_property_by_name) | **DELETE** /device/groups/{gid}/properties/{name} | delete device group property
[**delete_device_property_by_name**](LMApi.md#delete_device_property_by_name) | **DELETE** /device/devices/{deviceId}/properties/{name} | delete device property
[**delete_escalation_chain_by_id**](LMApi.md#delete_escalation_chain_by_id) | **DELETE** /setting/alert/chains/{id} | delete escalation chain
[**delete_event_source_by_id**](LMApi.md#delete_event_source_by_id) | **DELETE** /setting/eventsources/{id} | delete eventSource by id
[**delete_job_monitor**](LMApi.md#delete_job_monitor) | **DELETE** /setting/batchjobs/{id} | Delete JobMonitor
[**delete_log_partition_by_id**](LMApi.md#delete_log_partition_by_id) | **DELETE** /log/partitions/{id} | Delete a log partition by ID
[**delete_log_source**](LMApi.md#delete_log_source) | **DELETE** /setting/logsources/{id} | delete log source 
[**delete_netscan_by_id**](LMApi.md#delete_netscan_by_id) | **DELETE** /setting/netscans/{id} | delete a netscan
[**delete_oid**](LMApi.md#delete_oid) | **DELETE** /setting/oids/{id} | delete a OID
[**delete_ops_note_by_id**](LMApi.md#delete_ops_note_by_id) | **DELETE** /setting/opsnotes/{id} | delete opsnote
[**delete_property_rule**](LMApi.md#delete_property_rule) | **DELETE** /setting/propertyrules/{id} | delete a property rule
[**delete_recipient_group_by_id**](LMApi.md#delete_recipient_group_by_id) | **DELETE** /setting/recipientgroups/{id} | delete recipient group
[**delete_report_by_id**](LMApi.md#delete_report_by_id) | **DELETE** /report/reports/{id} | delete report
[**delete_report_group_by_id**](LMApi.md#delete_report_group_by_id) | **DELETE** /report/groups/{id} | delete report group
[**delete_role_by_id**](LMApi.md#delete_role_by_id) | **DELETE** /setting/roles/{id} | delete role
[**delete_sdt_by_id**](LMApi.md#delete_sdt_by_id) | **DELETE** /sdt/sdts/{id} | delete SDT
[**delete_topology_source**](LMApi.md#delete_topology_source) | **DELETE** /setting/topologysources/{id} | Delete TopologySource
[**delete_website_by_id**](LMApi.md#delete_website_by_id) | **DELETE** /website/websites/{id} | delete website
[**delete_website_group_by_id**](LMApi.md#delete_website_group_by_id) | **DELETE** /website/groups/{id} | delete website group
[**delete_widget_by_id**](LMApi.md#delete_widget_by_id) | **DELETE** /dashboard/widgets/{id} | delete widget
[**discover_subscriptions**](LMApi.md#discover_subscriptions) | **POST** /azure/functions/discoverSubscriptions | view subscriptions
[**escalated_alert_by_id**](LMApi.md#escalated_alert_by_id) | **POST** /alert/alerts/{id}/escalate | escalate alert by id
[**execute_debug_command**](LMApi.md#execute_debug_command) | **POST** /debug | Execute a Collector debug command
[**fetch_device_instances_data**](LMApi.md#fetch_device_instances_data) | **POST** /device/instances/datafetch | fetch device instances data
[**fetch_report_using_task_id**](LMApi.md#fetch_report_using_task_id) | **GET** /report/reports/{id}/tasks/{taskId} | get report for task Id
[**generate_report_by_id**](LMApi.md#generate_report_by_id) | **POST** /report/reports/{id}/executions | run a report
[**get_access_group_by_id**](LMApi.md#get_access_group_by_id) | **GET** /setting/accessgroup/{id} | Get access group by id
[**get_access_group_list**](LMApi.md#get_access_group_list) | **GET** /setting/accessgroup | Get access group list
[**get_admin_by_id**](LMApi.md#get_admin_by_id) | **GET** /setting/admins/{id} | get user
[**get_admin_list**](LMApi.md#get_admin_list) | **GET** /setting/admins | get user list
[**get_alert_by_id**](LMApi.md#get_alert_by_id) | **GET** /alert/alerts/{id} | get alert
[**get_alert_list**](LMApi.md#get_alert_list) | **GET** /alert/alerts | get alert list
[**get_alert_list_by_device_group_id**](LMApi.md#get_alert_list_by_device_group_id) | **GET** /device/groups/{id}/alerts | get device group alerts
[**get_alert_list_by_device_id**](LMApi.md#get_alert_list_by_device_id) | **GET** /device/devices/{id}/alerts | get alerts
[**get_alert_rule_by_id**](LMApi.md#get_alert_rule_by_id) | **GET** /setting/alert/rules/{id} | get alert rule by id
[**get_alert_rule_list**](LMApi.md#get_alert_rule_list) | **GET** /setting/alert/rules | get alert rule list
[**get_all_log_partitions**](LMApi.md#get_all_log_partitions) | **GET** /log/partitions | Retrieve a list of all log partitions
[**get_all_sdt_list_by_device_id**](LMApi.md#get_all_sdt_list_by_device_id) | **GET** /device/devices/{id}/sdts | get SDTs for a device
[**get_all_sdt_list_by_website_group_id**](LMApi.md#get_all_sdt_list_by_website_group_id) | **GET** /website/groups/{id}/sdts | get a list of SDTs for a website group (Response may contain extra fields depending upon the type of SDT)
[**get_api_token_list**](LMApi.md#get_api_token_list) | **GET** /setting/admins/apitokens | get a list of api tokens across users
[**get_api_token_list_by_admin_id**](LMApi.md#get_api_token_list_by_admin_id) | **GET** /setting/admins/{adminId}/apitokens | get api tokens for a user
[**get_applies_to_function_by_id**](LMApi.md#get_applies_to_function_by_id) | **GET** /setting/functions/{id} | get applies to function
[**get_applies_to_function_list**](LMApi.md#get_applies_to_function_list) | **GET** /setting/functions | get applies to function list
[**get_associated_device_list_by_data_source_id**](LMApi.md#get_associated_device_list_by_data_source_id) | **GET** /setting/datasources/{id}/devices | get devices associated with a datasource
[**get_audit_log_by_id**](LMApi.md#get_audit_log_by_id) | **GET** /setting/accesslogs/{id} | Get audit log by id
[**get_audit_log_list**](LMApi.md#get_audit_log_list) | **GET** /setting/accesslogs | Get audit logs
[**get_aws_account_id**](LMApi.md#get_aws_account_id) | **GET** /aws/accountId | Get AWS account ID
[**get_aws_external_id**](LMApi.md#get_aws_external_id) | **GET** /aws/externalId | Get AWS external ID
[**get_collector_by_id**](LMApi.md#get_collector_by_id) | **GET** /setting/collector/collectors/{id} | get collector
[**get_collector_group_by_id**](LMApi.md#get_collector_group_by_id) | **GET** /setting/collector/groups/{id} | get collector group
[**get_collector_group_list**](LMApi.md#get_collector_group_list) | **GET** /setting/collector/groups | get collector group list
[**get_collector_installer**](LMApi.md#get_collector_installer) | **GET** /setting/collector/collectors/{collectorId}/installers/{osAndArch} | get collector installer
[**get_collector_list**](LMApi.md#get_collector_list) | **GET** /setting/collector/collectors | get collector list
[**get_collector_version_list**](LMApi.md#get_collector_version_list) | **GET** /setting/collector/collectors/versions | get collector version list
[**get_config_source_by_id**](LMApi.md#get_config_source_by_id) | **GET** /setting/configsources/{id} | get config source by id
[**get_config_source_list**](LMApi.md#get_config_source_list) | **GET** /setting/configsources | get config source list
[**get_contract_info_by_company**](LMApi.md#get_contract_info_by_company) | **GET** /usage/contractInfo | get contract info by company
[**get_dashboard_by_id**](LMApi.md#get_dashboard_by_id) | **GET** /dashboard/dashboards/{id} | get dashboard
[**get_dashboard_group_by_id**](LMApi.md#get_dashboard_group_by_id) | **GET** /dashboard/groups/{id} | get dashboard group
[**get_dashboard_group_list**](LMApi.md#get_dashboard_group_list) | **GET** /dashboard/groups | get dashboard group list
[**get_dashboard_list**](LMApi.md#get_dashboard_list) | **GET** /dashboard/dashboards | get dashboard list
[**get_data_source_overview_graph_by_id**](LMApi.md#get_data_source_overview_graph_by_id) | **GET** /setting/datasources/{dsId}/ographs/{id} | get datasource overview graph by id
[**get_data_source_overview_graph_list**](LMApi.md#get_data_source_overview_graph_list) | **GET** /setting/datasources/{dsId}/ographs | get datasource overview graph list
[**get_datasource_by_id**](LMApi.md#get_datasource_by_id) | **GET** /setting/datasources/{id} | get datasource by id
[**get_datasource_list**](LMApi.md#get_datasource_list) | **GET** /setting/datasources | get datasource list
[**get_debug_command_result**](LMApi.md#get_debug_command_result) | **GET** /debug/{id} | Get the result of a Collector debug command using sessionId
[**get_delta_devices**](LMApi.md#get_delta_devices) | **GET** /device/devices/delta/{deltaId} | Get delta devices using deltaId
[**get_delta_id_with_devices**](LMApi.md#get_delta_id_with_devices) | **GET** /device/devices/delta | Get filter matched devices with new deltaId
[**get_device_by_id**](LMApi.md#get_device_by_id) | **GET** /device/devices/{id} | get device by id
[**get_device_config_source_config_by_id**](LMApi.md#get_device_config_source_config_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/{id} | get a config for a device
[**get_device_config_source_config_list**](LMApi.md#get_device_config_source_config_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config | get detailed config information for the instance
[**get_device_datasource_by_id**](LMApi.md#get_device_datasource_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id} | get device datasource 
[**get_device_datasource_data_by_id**](LMApi.md#get_device_datasource_data_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/data | get device datasource data 
[**get_device_datasource_instance_alert_setting_by_id**](LMApi.md#get_device_datasource_instance_alert_setting_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | get device instance alert setting
[**get_device_datasource_instance_alert_setting_list_of_device**](LMApi.md#get_device_datasource_instance_alert_setting_list_of_device) | **GET** /device/devices/{deviceId}/alertsettings | get a list of alert settings for a device
[**get_device_datasource_instance_alert_setting_list_of_dsi**](LMApi.md#get_device_datasource_instance_alert_setting_list_of_dsi) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings | get a list of alert settings for a device datasource instance
[**get_device_datasource_instance_by_id**](LMApi.md#get_device_datasource_instance_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | get device instance 
[**get_device_datasource_instance_data**](LMApi.md#get_device_datasource_instance_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/data | get device instance data
[**get_device_datasource_instance_graph_data**](LMApi.md#get_device_datasource_instance_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/graphs/{graphId}/data | get device instance graph data 
[**get_device_datasource_instance_group_by_id**](LMApi.md#get_device_datasource_instance_group_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | get device datasource instance group 
[**get_device_datasource_instance_group_list**](LMApi.md#get_device_datasource_instance_group_list) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | get device datasource instance group list 
[**get_device_datasource_instance_group_overview_graph_data**](LMApi.md#get_device_datasource_instance_group_overview_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/graphs/{ographId}/data | get device instance group overview graph data 
[**get_device_datasource_instance_list**](LMApi.md#get_device_datasource_instance_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | get device instance list
[**get_device_datasource_instance_sdt_history**](LMApi.md#get_device_datasource_instance_sdt_history) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/historysdts | get device instance SDT history
[**get_device_datasource_list**](LMApi.md#get_device_datasource_list) | **GET** /device/devices/{deviceId}/devicedatasources | get device datasource list 
[**get_device_group_by_id**](LMApi.md#get_device_group_by_id) | **GET** /device/groups/{id} | get device group
[**get_device_group_cluster_alert_conf_by_id**](LMApi.md#get_device_group_cluster_alert_conf_by_id) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Get cluster alert configuration by id
[**get_device_group_cluster_alert_conf_list**](LMApi.md#get_device_group_cluster_alert_conf_list) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf | get a list of cluster alert configurations for a device group
[**get_device_group_datasource_alert_setting**](LMApi.md#get_device_group_datasource_alert_setting) | **GET** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | get device group datasource alert setting 
[**get_device_group_datasource_by_id**](LMApi.md#get_device_group_datasource_by_id) | **GET** /device/groups/{deviceGroupId}/datasources/{id} | get device group datasource
[**get_device_group_datasource_list**](LMApi.md#get_device_group_datasource_list) | **GET** /device/groups/{deviceGroupId}/datasources | get device group datasource list
[**get_device_group_list**](LMApi.md#get_device_group_list) | **GET** /device/groups | get device group list
[**get_device_group_property_by_name**](LMApi.md#get_device_group_property_by_name) | **GET** /device/groups/{gid}/properties/{name} | get device group property by name
[**get_device_group_property_list**](LMApi.md#get_device_group_property_list) | **GET** /device/groups/{gid}/properties | get device group properties
[**get_device_group_sdt_list**](LMApi.md#get_device_group_sdt_list) | **GET** /device/groups/{id}/sdts | get device group SDTs
[**get_device_instance_graph_data_only_by_instance_id**](LMApi.md#get_device_instance_graph_data_only_by_instance_id) | **GET** /device/devicedatasourceinstances/{instanceId}/graphs/{graphId}/data | get device instance data
[**get_device_instance_list**](LMApi.md#get_device_instance_list) | **GET** /device/devices/{id}/instances | get device instance list
[**get_device_list**](LMApi.md#get_device_list) | **GET** /device/devices | get device list
[**get_device_property_by_name**](LMApi.md#get_device_property_by_name) | **GET** /device/devices/{deviceId}/properties/{name} | get device property by name
[**get_device_property_list**](LMApi.md#get_device_property_list) | **GET** /device/devices/{deviceId}/properties | get device properties
[**get_escalation_chain_by_id**](LMApi.md#get_escalation_chain_by_id) | **GET** /setting/alert/chains/{id} | get escalation chain by id
[**get_escalation_chain_list**](LMApi.md#get_escalation_chain_list) | **GET** /setting/alert/chains | get escalation chain list
[**get_event_source_by_id**](LMApi.md#get_event_source_by_id) | **GET** /setting/eventsources/{id} | get eventSource by id
[**get_event_source_list**](LMApi.md#get_event_source_list) | **GET** /setting/eventsources | get eventSource list
[**get_external_api_stats**](LMApi.md#get_external_api_stats) | **GET** /apiStats/externalApis | get external api stats info
[**get_immediate_device_list_by_device_group_id**](LMApi.md#get_immediate_device_list_by_device_group_id) | **GET** /device/groups/{id}/devices | get immediate devices under group
[**get_immediate_website_list_by_website_group_id**](LMApi.md#get_immediate_website_list_by_website_group_id) | **GET** /website/groups/{id}/websites | get a list of websites for a group (Response may contain extra fields depending upon the type of check { PingCheck | WebCheck} being added)
[**get_integration_audit_logs**](LMApi.md#get_integration_audit_logs) | **GET** /setting/integrations/auditlogs | get integration audit logs list
[**get_job_monitor_by_id**](LMApi.md#get_job_monitor_by_id) | **GET** /setting/batchjobs/{id} | Get JobMonitor by id
[**get_job_monitor_list**](LMApi.md#get_job_monitor_list) | **GET** /setting/batchjobs | Get JobMonitor List
[**get_log_source_by_id**](LMApi.md#get_log_source_by_id) | **GET** /setting/logsources/{id} | get log source 
[**get_log_source_list**](LMApi.md#get_log_source_list) | **GET** /setting/logsources | get log source list
[**get_metrics_usage**](LMApi.md#get_metrics_usage) | **GET** /metrics/usage | get metrics usage
[**get_netflow_endpoint_list**](LMApi.md#get_netflow_endpoint_list) | **GET** /device/devices/{id}/endpoints | get netflow endpoints
[**get_netflow_flow_list**](LMApi.md#get_netflow_flow_list) | **GET** /device/devices/{id}/flows | get netflow flows
[**get_netflow_port_list**](LMApi.md#get_netflow_port_list) | **GET** /device/devices/{id}/ports | get netflow ports
[**get_netscan_by_id**](LMApi.md#get_netscan_by_id) | **GET** /setting/netscans/{id} | get netscan by id
[**get_netscan_list**](LMApi.md#get_netscan_list) | **GET** /setting/netscans | get netscan list
[**get_oid_by_id**](LMApi.md#get_oid_by_id) | **GET** /setting/oids/{id} | get OID by id
[**get_oid_list**](LMApi.md#get_oid_list) | **GET** /setting/oids | get OID&#x27;s list
[**get_ops_note_by_id**](LMApi.md#get_ops_note_by_id) | **GET** /setting/opsnotes/{id} | get opsnote by id
[**get_ops_note_list**](LMApi.md#get_ops_note_list) | **GET** /setting/opsnotes | get opsnote list
[**get_partition_by_id**](LMApi.md#get_partition_by_id) | **GET** /log/partitions/{id} | Retrieve details of a specific log partition
[**get_property_rules_by_id**](LMApi.md#get_property_rules_by_id) | **GET** /setting/propertyrules/{id} | get property rules by id
[**get_property_rules_list**](LMApi.md#get_property_rules_list) | **GET** /setting/propertyrules | get property rules list
[**get_recipient_group_by_id**](LMApi.md#get_recipient_group_by_id) | **GET** /setting/recipientgroups/{id} | get recipient group by id
[**get_recipient_group_list**](LMApi.md#get_recipient_group_list) | **GET** /setting/recipientgroups | get recipient group List
[**get_report_by_id**](LMApi.md#get_report_by_id) | **GET** /report/reports/{id} | get report by id
[**get_report_group_by_id**](LMApi.md#get_report_group_by_id) | **GET** /report/groups/{id} | get report group by id
[**get_report_group_list**](LMApi.md#get_report_group_list) | **GET** /report/groups | get report group list
[**get_report_list**](LMApi.md#get_report_list) | **GET** /report/reports | get report list
[**get_retention_list**](LMApi.md#get_retention_list) | **GET** /log/partitions/retentions | Retrieve the list of log retentions
[**get_role_by_id**](LMApi.md#get_role_by_id) | **GET** /setting/roles/{id} | get role by id
[**get_role_list**](LMApi.md#get_role_list) | **GET** /setting/roles | get role list
[**get_sdt_by_id**](LMApi.md#get_sdt_by_id) | **GET** /sdt/sdts/{id} | get SDT by id (Response may contain extra fields depending upon the type of SDT of given id)
[**get_sdt_history_by_device_data_source_id**](LMApi.md#get_sdt_history_by_device_data_source_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/historysdts | get SDT history for the device dataSource
[**get_sdt_history_by_device_group_id**](LMApi.md#get_sdt_history_by_device_group_id) | **GET** /device/groups/{id}/historysdts | get SDT history for the group
[**get_sdt_history_by_device_id**](LMApi.md#get_sdt_history_by_device_id) | **GET** /device/devices/{id}/historysdts | get SDT history for the device
[**get_sdt_history_by_website_group_id**](LMApi.md#get_sdt_history_by_website_group_id) | **GET** /website/groups/{id}/historysdts | get SDT history for the website group (Response may contain extra fields depending upon the type of SDT)
[**get_sdt_history_by_website_id**](LMApi.md#get_sdt_history_by_website_id) | **GET** /website/websites/{id}/historysdts | get SDT history for the website (Response may contain extra fields depending upon the type of SDT)
[**get_sdt_list**](LMApi.md#get_sdt_list) | **GET** /sdt/sdts | get SDT list
[**get_site_monitor_check_point_list**](LMApi.md#get_site_monitor_check_point_list) | **GET** /website/smcheckpoints | get website checkpoint list
[**get_top_talkers_graph**](LMApi.md#get_top_talkers_graph) | **GET** /device/devices/{id}/topTalkersGraph | get top talkers graph
[**get_topology_source_by_id**](LMApi.md#get_topology_source_by_id) | **GET** /setting/topologysources/{id} | Get TopologySource by id
[**get_topology_source_list**](LMApi.md#get_topology_source_list) | **GET** /setting/topologysources | Get TopologySource List
[**get_unmonitored_device_list**](LMApi.md#get_unmonitored_device_list) | **GET** /device/unmonitoreddevices | get unmonitored device list
[**get_update_reason_list_by_config_source_id**](LMApi.md#get_update_reason_list_by_config_source_id) | **GET** /setting/configsources/{id}/updatereasons | get update history for a configSource
[**get_update_reason_list_by_data_source_id**](LMApi.md#get_update_reason_list_by_data_source_id) | **GET** /setting/datasources/{id}/updatereasons | get update history for a datasource
[**get_v4_metadata**](LMApi.md#get_v4_metadata) | **GET** /setting/logicmodules/metadata | get metadata
[**get_website_alert_list_by_website_id**](LMApi.md#get_website_alert_list_by_website_id) | **GET** /website/websites/{id}/alerts | get alerts for a website
[**get_website_by_id**](LMApi.md#get_website_by_id) | **GET** /website/websites/{id} | get website by id
[**get_website_checkpoint_data_by_id**](LMApi.md#get_website_checkpoint_data_by_id) | **GET** /website/websites/{srvId}/checkpoints/{checkId}/data | get data for a website checkpoint
[**get_website_data_by_graph_name**](LMApi.md#get_website_data_by_graph_name) | **GET** /website/websites/{id}/graphs/{graphName}/data | get website data by graph name
[**get_website_graph_data**](LMApi.md#get_website_graph_data) | **GET** /website/websites/{websiteId}/checkpoints/{checkpointId}/graphs/{graphName}/data | get website graph data
[**get_website_group_by_id**](LMApi.md#get_website_group_by_id) | **GET** /website/groups/{id} | get website group
[**get_website_group_list**](LMApi.md#get_website_group_list) | **GET** /website/groups | get website group list
[**get_website_list**](LMApi.md#get_website_list) | **GET** /website/websites | get website list
[**get_website_property_list_by_website_id**](LMApi.md#get_website_property_list_by_website_id) | **GET** /website/websites/{id}/properties | get a list of properties for a website
[**get_website_sdt_list_by_website_id**](LMApi.md#get_website_sdt_list_by_website_id) | **GET** /website/websites/{id}/sdts | get a list of SDTs for a website
[**get_widget_by_id**](LMApi.md#get_widget_by_id) | **GET** /dashboard/widgets/{id} | get widget by id (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**get_widget_data_by_id**](LMApi.md#get_widget_data_by_id) | **GET** /dashboard/widgets/{id}/data | get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**get_widget_list**](LMApi.md#get_widget_list) | **GET** /dashboard/widgets | get widget list (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**get_widget_list_by_dashboard_id**](LMApi.md#get_widget_list_by_dashboard_id) | **GET** /dashboard/dashboards/{id}/widgets | get widget list by DashboardId
[**import_batch_job**](LMApi.md#import_batch_job) | **POST** /setting/batchjobs/importxml | import batch job via xml
[**import_config_source**](LMApi.md#import_config_source) | **POST** /setting/configsources/importxml | import config source via xml
[**import_data_source**](LMApi.md#import_data_source) | **POST** /setting/datasources/importxml | import datasource via xml
[**import_event_source**](LMApi.md#import_event_source) | **POST** /setting/eventsources/importxml | import eventsource via xml
[**map_un_map_module_to_access_group**](LMApi.md#map_un_map_module_to_access_group) | **POST** /setting/accessgroup/mapunmap/modules | Create a mapping of access group &amp; module
[**partition_action**](LMApi.md#partition_action) | **POST** /log/partitions/{id}/{action} | Perform an action on a specified log partition
[**patch_access_group**](LMApi.md#patch_access_group) | **PATCH** /setting/accessgroup/{id} | Update access group
[**patch_admin_by_id**](LMApi.md#patch_admin_by_id) | **PATCH** /setting/admins/{id} | update user
[**patch_alert_rule_by_id**](LMApi.md#patch_alert_rule_by_id) | **PATCH** /setting/alert/rules/{id} | update alert rule
[**patch_api_token_by_admin_id**](LMApi.md#patch_api_token_by_admin_id) | **PATCH** /setting/admins/{adminId}/apitokens/{apitokenId} | update api tokens for a user
[**patch_applies_to_function**](LMApi.md#patch_applies_to_function) | **PATCH** /setting/functions/{id} | update applies to function
[**patch_collector_by_id**](LMApi.md#patch_collector_by_id) | **PATCH** /setting/collector/collectors/{id} | update collector
[**patch_collector_group_by_id**](LMApi.md#patch_collector_group_by_id) | **PATCH** /setting/collector/groups/{id} | update collector group
[**patch_config_source_by_id**](LMApi.md#patch_config_source_by_id) | **PATCH** /setting/configsources/{id} | update config source by id
[**patch_dashboard_by_id**](LMApi.md#patch_dashboard_by_id) | **PATCH** /dashboard/dashboards/{id} | update dashboard
[**patch_dashboard_group_by_id**](LMApi.md#patch_dashboard_group_by_id) | **PATCH** /dashboard/groups/{id} | update dashboard group
[**patch_datasource_by_id**](LMApi.md#patch_datasource_by_id) | **PATCH** /setting/datasources/{id} | update datasource
[**patch_default_dashboard**](LMApi.md#patch_default_dashboard) | **PATCH** /setting/userdata/{id} | update default dashboard
[**patch_device**](LMApi.md#patch_device) | **PATCH** /device/devices/{id} | update a device
[**patch_device_datasource_instance_alert_setting_by_id**](LMApi.md#patch_device_datasource_instance_alert_setting_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**patch_device_datasource_instance_by_id**](LMApi.md#patch_device_datasource_instance_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**patch_device_datasource_instance_group_by_id**](LMApi.md#patch_device_datasource_instance_group_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group
[**patch_device_group_by_id**](LMApi.md#patch_device_group_by_id) | **PATCH** /device/groups/{id} | update device group
[**patch_device_group_cluster_alert_conf_by_id**](LMApi.md#patch_device_group_cluster_alert_conf_by_id) | **PATCH** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**patch_device_group_datasource_alert_setting**](LMApi.md#patch_device_group_datasource_alert_setting) | **PATCH** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting
[**patch_device_group_datasource_by_id**](LMApi.md#patch_device_group_datasource_by_id) | **PATCH** /device/groups/{deviceGroupId}/datasources/{id} | update device group datasource
[**patch_device_group_property_by_name**](LMApi.md#patch_device_group_property_by_name) | **PATCH** /device/groups/{gid}/properties/{name} | update device group property
[**patch_device_property_by_name**](LMApi.md#patch_device_property_by_name) | **PATCH** /device/devices/{deviceId}/properties/{name} | update device property
[**patch_escalation_chain_by_id**](LMApi.md#patch_escalation_chain_by_id) | **PATCH** /setting/alert/chains/{id} | update escalation chain
[**patch_event_source_by_id**](LMApi.md#patch_event_source_by_id) | **PATCH** /setting/eventsources/{id} | update eventSource by id
[**patch_job_monitor**](LMApi.md#patch_job_monitor) | **PATCH** /setting/batchjobs/{id} | Update JobMonitor
[**patch_log_partition**](LMApi.md#patch_log_partition) | **PATCH** /log/partitions | Update an existing log partition
[**patch_log_source**](LMApi.md#patch_log_source) | **PATCH** /setting/logsources/{id} | update log source 
[**patch_netscan**](LMApi.md#patch_netscan) | **PATCH** /setting/netscans/{id} | update a netscan
[**patch_oid**](LMApi.md#patch_oid) | **PATCH** /setting/oids/{id} | update a OID
[**patch_ops_note_by_id**](LMApi.md#patch_ops_note_by_id) | **PATCH** /setting/opsnotes/{id} | update opsnote
[**patch_property_rule**](LMApi.md#patch_property_rule) | **PATCH** /setting/propertyrules/{id} | update a property rule
[**patch_recipient_group_by_id**](LMApi.md#patch_recipient_group_by_id) | **PATCH** /setting/recipientgroups/{id} | update recipient group
[**patch_report_by_id**](LMApi.md#patch_report_by_id) | **PATCH** /report/reports/{id} | update report
[**patch_report_group_by_id**](LMApi.md#patch_report_group_by_id) | **PATCH** /report/groups/{id} | update report group
[**patch_role_by_id**](LMApi.md#patch_role_by_id) | **PATCH** /setting/roles/{id} | update role
[**patch_sdt_by_id**](LMApi.md#patch_sdt_by_id) | **PATCH** /sdt/sdts/{id} | update SDT (Response may contain extra fields depending upon the type of SDT being updated)
[**patch_topology_source**](LMApi.md#patch_topology_source) | **PATCH** /setting/topologysources/{id} | Update TopologySource
[**patch_website_by_id**](LMApi.md#patch_website_by_id) | **PATCH** /website/websites/{id} | update website
[**patch_website_group_by_id**](LMApi.md#patch_website_group_by_id) | **PATCH** /website/groups/{id} | update website group
[**patch_widget_by_id**](LMApi.md#patch_widget_by_id) | **PATCH** /dashboard/widgets/{id} | update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**schedule_auto_discovery_by_device_id**](LMApi.md#schedule_auto_discovery_by_device_id) | **POST** /device/devices/{id}/scheduleAutoDiscovery | schedule active discovery for a device
[**test_aws_account**](LMApi.md#test_aws_account) | **POST** /aws/functions/testAccount | test AWS account
[**test_azure_account**](LMApi.md#test_azure_account) | **POST** /azure/functions/testAccount | test Azure account
[**test_gcp_account**](LMApi.md#test_gcp_account) | **POST** /gcp/functions/testAccount | test GCP account
[**test_saa_s_account**](LMApi.md#test_saa_s_account) | **POST** /saas/functions/testAccount | test SaaS account
[**update_access_group**](LMApi.md#update_access_group) | **PUT** /setting/accessgroup/{id} | Update access group
[**update_admin_by_id**](LMApi.md#update_admin_by_id) | **PUT** /setting/admins/{id} | update user
[**update_alert_rule_by_id**](LMApi.md#update_alert_rule_by_id) | **PUT** /setting/alert/rules/{id} | update alert rule
[**update_api_token_by_admin_id**](LMApi.md#update_api_token_by_admin_id) | **PUT** /setting/admins/{adminId}/apitokens/{apitokenId} | update api tokens for a user
[**update_applies_to_function**](LMApi.md#update_applies_to_function) | **PUT** /setting/functions/{id} | update applies to function
[**update_collector_by_id**](LMApi.md#update_collector_by_id) | **PUT** /setting/collector/collectors/{id} | update collector
[**update_collector_group_by_id**](LMApi.md#update_collector_group_by_id) | **PUT** /setting/collector/groups/{id} | update collector group
[**update_config_source_by_id**](LMApi.md#update_config_source_by_id) | **PUT** /setting/configsources/{id} | update config source by id
[**update_dashboard_by_id**](LMApi.md#update_dashboard_by_id) | **PUT** /dashboard/dashboards/{id} | update dashboard
[**update_dashboard_group_by_id**](LMApi.md#update_dashboard_group_by_id) | **PUT** /dashboard/groups/{id} | update dashboard group
[**update_datasource_by_id**](LMApi.md#update_datasource_by_id) | **PUT** /setting/datasources/{id} | update datasource
[**update_default_dashboard**](LMApi.md#update_default_dashboard) | **PUT** /setting/userdata/{id} | update default dashboard
[**update_device**](LMApi.md#update_device) | **PUT** /device/devices/{id} | update a device
[**update_device_datasource_instance_alert_setting_by_id**](LMApi.md#update_device_datasource_instance_alert_setting_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**update_device_datasource_instance_by_id**](LMApi.md#update_device_datasource_instance_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**update_device_datasource_instance_group_by_id**](LMApi.md#update_device_datasource_instance_group_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | update device datasource instance group
[**update_device_group_by_id**](LMApi.md#update_device_group_by_id) | **PUT** /device/groups/{id} | update device group
[**update_device_group_cluster_alert_conf_by_id**](LMApi.md#update_device_group_cluster_alert_conf_by_id) | **PUT** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**update_device_group_datasource_alert_setting**](LMApi.md#update_device_group_datasource_alert_setting) | **PUT** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | update device group datasource alert setting
[**update_device_group_datasource_by_id**](LMApi.md#update_device_group_datasource_by_id) | **PUT** /device/groups/{deviceGroupId}/datasources/{id} | update device group datasource
[**update_device_group_property_by_name**](LMApi.md#update_device_group_property_by_name) | **PUT** /device/groups/{gid}/properties/{name} | update device group property
[**update_device_property_by_name**](LMApi.md#update_device_property_by_name) | **PUT** /device/devices/{deviceId}/properties/{name} | update device property
[**update_escalation_chain_by_id**](LMApi.md#update_escalation_chain_by_id) | **PUT** /setting/alert/chains/{id} | update escalation chain
[**update_event_source_by_id**](LMApi.md#update_event_source_by_id) | **PUT** /setting/eventsources/{id} | update eventSource by id
[**update_instance_group_alert_threshold**](LMApi.md#update_instance_group_alert_threshold) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/datapoints/{dpId}/alertconfig | update instance group alert threshold (Setting the threshold at default group is not allowed)
[**update_job_monitor**](LMApi.md#update_job_monitor) | **PUT** /setting/batchjobs/{id} | Update JobMonitor
[**update_log_partition**](LMApi.md#update_log_partition) | **PUT** /log/partitions | Update an existing log partition
[**update_log_source**](LMApi.md#update_log_source) | **PUT** /setting/logsources/{id} | update log source 
[**update_netscan**](LMApi.md#update_netscan) | **PUT** /setting/netscans/{id} | update a netscan
[**update_oid**](LMApi.md#update_oid) | **PUT** /setting/oids/{id} | update a OID
[**update_ops_note_by_id**](LMApi.md#update_ops_note_by_id) | **PUT** /setting/opsnotes/{id} | update opsnote
[**update_property_rule**](LMApi.md#update_property_rule) | **PUT** /setting/propertyrules/{id} | update a property rule
[**update_recipient_group_by_id**](LMApi.md#update_recipient_group_by_id) | **PUT** /setting/recipientgroups/{id} | update recipient group
[**update_report_by_id**](LMApi.md#update_report_by_id) | **PUT** /report/reports/{id} | update report
[**update_report_group_by_id**](LMApi.md#update_report_group_by_id) | **PUT** /report/groups/{id} | update report group
[**update_role_by_id**](LMApi.md#update_role_by_id) | **PUT** /setting/roles/{id} | update role
[**update_sdt_by_id**](LMApi.md#update_sdt_by_id) | **PUT** /sdt/sdts/{id} | update SDT (Response may contain extra fields depending upon the type of SDT being updated)
[**update_topology_source**](LMApi.md#update_topology_source) | **PUT** /setting/topologysources/{id} | Update TopologySource
[**update_website_by_id**](LMApi.md#update_website_by_id) | **PUT** /website/websites/{id} | update website
[**update_website_group_by_id**](LMApi.md#update_website_group_by_id) | **PUT** /website/groups/{id} | update website group
[**update_widget_by_id**](LMApi.md#update_widget_by_id) | **PUT** /dashboard/widgets/{id} | update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**verify_aws_billing_permissions**](LMApi.md#verify_aws_billing_permissions) | **POST** /aws/functions/verifyBillingPermissions | verify AWS Billing Permissions
[**verify_storage_accounts_permissions**](LMApi.md#verify_storage_accounts_permissions) | **POST** /azure/functions/verifyStorageAccountsPermissions | view storage accounts

# **ack_alert_by_id**
> object ack_alert_by_id(body, id)

ack alert by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertAck() # AlertAck | 
id = 'id_example' # str | 

try:
    # ack alert by id
    api_response = api_instance.ack_alert_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->ack_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAck**](AlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ack_collector_down_alert_by_id**
> object ack_collector_down_alert_by_id(id, body)

ack collector down alert

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AckCollectorDown() # AckCollectorDown | 

try:
    # ack collector down alert
    api_response = api_instance.ack_collector_down_alert_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->ack_collector_down_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AckCollectorDown**](AckCollectorDown.md)|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_access_group**
> AccessGroup add_access_group(body=body)

Create a access group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AccessGroup() # AccessGroup |  (optional)

try:
    # Create a access group
    api_response = api_instance.add_access_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_access_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessGroup**](AccessGroup.md)|  | [optional] 

### Return type

[**AccessGroup**](AccessGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_admin**
> Admin add_admin(body)

add user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Admin() # Admin | 

try:
    # add user
    api_response = api_instance.add_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Admin**](Admin.md)|  | 

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_note_by_id**
> object add_alert_note_by_id(body, id)

add alert note

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertAck() # AlertAck | 
id = 'id_example' # str | 

try:
    # add alert note
    api_response = api_instance.add_alert_note_by_id(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_alert_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertAck**](AlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_rule**
> AlertRule add_alert_rule(body)

add alert rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # add alert rule
    api_response = api_instance.add_alert_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_alert_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_api_token_by_admin_id**
> APIToken add_api_token_by_admin_id(admin_id, body, type=type)

add api tokens for a user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 
type = 'API Token' # str |  (optional) (default to API Token)

try:
    # add api tokens for a user
    api_response = api_instance.add_api_token_by_admin_id(admin_id, body, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 
 **type** | **str**|  | [optional] [default to API Token]

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_applies_to_function**
> AppliesToFunction add_applies_to_function(body=body)

add applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.AppliesToFunction() # AppliesToFunction |  (optional)

try:
    # add applies to function
    api_response = api_instance.add_applies_to_function(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_applies_to_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppliesToFunction**](AppliesToFunction.md)|  | [optional] 

### Return type

[**AppliesToFunction**](AppliesToFunction.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_collector**
> Collector add_collector(body)

add collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Collector() # Collector | 

try:
    # add collector
    api_response = api_instance.add_collector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_collector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Collector**](Collector.md)|  | 

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_collector_group**
> CollectorGroup add_collector_group(body)

add collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 

try:
    # add collector group
    api_response = api_instance.add_collector_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_collector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_config_source**
> ConfigSource add_config_source(body=body)

add config source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ConfigSource() # ConfigSource |  (optional)

try:
    # add config source
    api_response = api_instance.add_config_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_config_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfigSource**](ConfigSource.md)|  | [optional] 

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard**
> Dashboard add_dashboard(body)

add dashboard

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Dashboard() # Dashboard | 

try:
    # add dashboard
    api_response = api_instance.add_dashboard(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Dashboard**](Dashboard.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard_group**
> DashboardGroup add_dashboard_group(body)

add dashboard group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # add dashboard group
    api_response = api_instance.add_dashboard_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dashboard_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dashboard_group_asynchronously**
> RestDashboardGroupAsyncCloneResponse add_dashboard_group_asynchronously(id, body=body, recursive=recursive)

add dashboard group asynchronously

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup |  (optional)
recursive = true # bool |  (optional) (default to true)

try:
    # add dashboard group asynchronously
    api_response = api_instance.add_dashboard_group_asynchronously(id, body=body, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dashboard_group_asynchronously: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | [optional] 
 **recursive** | **bool**|  | [optional] [default to true]

### Return type

[**RestDashboardGroupAsyncCloneResponse**](RestDashboardGroupAsyncCloneResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_datasource_by_id**
> DataSource add_datasource_by_id(body=body, create_graph=create_graph)

add datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DataSource() # DataSource |  (optional)
create_graph = false # bool |  (optional) (default to false)

try:
    # add datasource
    api_response = api_instance.add_datasource_by_id(body=body, create_graph=create_graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataSource**](DataSource.md)|  | [optional] 
 **create_graph** | **bool**|  | [optional] [default to false]

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device**
> Device add_device(body, start=start, end=end, netflow_filter=netflow_filter, add_from_wizard=add_from_wizard)

add a new device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
add_from_wizard = false # bool |  (optional) (default to false)

try:
    # add a new device
    api_response = api_instance.add_device(body, start=start, end=end, netflow_filter=netflow_filter, add_from_wizard=add_from_wizard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **add_from_wizard** | **bool**|  | [optional] [default to false]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance**
> DeviceDataSourceInstance add_device_datasource_instance(device_id, hds_id, body)

add device instance 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 

try:
    # add device instance 
    api_response = api_instance.add_device_datasource_instance(device_id, hds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_datasource_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance_group**
> DeviceDataSourceInstanceGroup add_device_datasource_instance_group(device_id, device_ds_id, body)

add device datasource instance group 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # add device datasource instance group 
    api_response = api_instance.add_device_datasource_instance_group(device_id, device_ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_datasource_instance_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group**
> DeviceGroup add_device_group(body)

add device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 

try:
    # add device group
    api_response = api_instance.add_device_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group_cluster_alert_conf**
> DeviceClusterAlertConfig add_device_group_cluster_alert_conf(device_group_id, body)

Add cluster alert configuration

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Add cluster alert configuration
    api_response = api_instance.add_device_group_cluster_alert_conf(device_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group_cluster_alert_conf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group_property**
> EntityProperty add_device_group_property(gid, body)

add device group property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # add device group property
    api_response = api_instance.add_device_group_property(gid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_group_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_property**
> EntityProperty add_device_property(device_id, body)

add device property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # add device property
    api_response = api_instance.add_device_property(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dns_mapping**
> RestDNSMappingV3 add_dns_mapping(body=body)

Add dns mapping

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestDNSMappingV3() # RestDNSMappingV3 |  (optional)

try:
    # Add dns mapping
    api_response = api_instance.add_dns_mapping(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_dns_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDNSMappingV3**](RestDNSMappingV3.md)|  | [optional] 

### Return type

[**RestDNSMappingV3**](RestDNSMappingV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_escalation_chain**
> EscalatingChain add_escalation_chain(body)

add escalation chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # add escalation chain
    api_response = api_instance.add_escalation_chain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_escalation_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_event_source**
> EventSource add_event_source(body=body)

add eventSource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.EventSource() # EventSource |  (optional)

try:
    # add eventSource
    api_response = api_instance.add_event_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_event_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventSource**](EventSource.md)|  | [optional] 

### Return type

[**EventSource**](EventSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_job_monitor**
> BatchJob add_job_monitor(body=body)

Add JobMonitor

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.BatchJob() # BatchJob |  (optional)

try:
    # Add JobMonitor
    api_response = api_instance.add_job_monitor(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_job_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchJob**](BatchJob.md)|  | [optional] 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_log_source**
> LogSource add_log_source(body=body)

add log source 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.LogSource() # LogSource |  (optional)

try:
    # add log source 
    api_response = api_instance.add_log_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_log_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogSource**](LogSource.md)|  | [optional] 

### Return type

[**LogSource**](LogSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_netscan**
> Netscan add_netscan(body=body)

add a new netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)

try:
    # add a new netscan
    api_response = api_instance.add_netscan(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Netscan**](Netscan.md)|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_oid**
> RestOidV3 add_oid(body=body)

add a new OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestOidV3() # RestOidV3 |  (optional)

try:
    # add a new OID
    api_response = api_instance.add_oid(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_oid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestOidV3**](RestOidV3.md)|  | [optional] 

### Return type

[**RestOidV3**](RestOidV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ops_note**
> OpsNote add_ops_note(body)

add opsnote

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # add opsnote
    api_response = api_instance.add_ops_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_ops_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_property_rule**
> PropertyRule add_property_rule(body=body)

add a new property rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.PropertyRule() # PropertyRule |  (optional)

try:
    # add a new property rule
    api_response = api_instance.add_property_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_property_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PropertyRule**](PropertyRule.md)|  | [optional] 

### Return type

[**PropertyRule**](PropertyRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_recipient_group**
> RecipientGroup add_recipient_group(body)

add recipient group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # add recipient group
    api_response = api_instance.add_recipient_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_recipient_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_report**
> ReportBase add_report(body)

add report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # add report
    api_response = api_instance.add_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_report_group**
> ReportGroup add_report_group(body)

add report group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # add report group
    api_response = api_instance.add_report_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_report_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> Role add_role(body)

add role

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Role() # Role | 

try:
    # add role
    api_response = api_instance.add_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_sdt**
> SDT add_sdt(body)

add SDT (Response may contain extra fields depending upon the type of SDT being added)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # add SDT (Response may contain extra fields depending upon the type of SDT being added)
    api_response = api_instance.add_sdt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_sdt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_topology_source**
> TopologySource add_topology_source(body=body)

Add TopologySource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.TopologySource() # TopologySource |  (optional)

try:
    # Add TopologySource
    api_response = api_instance.add_topology_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_topology_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopologySource**](TopologySource.md)|  | [optional] 

### Return type

[**TopologySource**](TopologySource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_website**
> Website add_website(body)

add website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Website() # Website | 

try:
    # add website
    api_response = api_instance.add_website(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_website: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Website**](Website.md)|  | 

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_website_group**
> WebsiteGroup add_website_group(body)

add website group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 

try:
    # add website group
    api_response = api_instance.add_website_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_website_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_widget**
> Widget add_widget(body)

add widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # add widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.add_widget(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_widget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_device_config_source_config**
> object collect_device_config_source_config(device_id, hds_id, instance_id)

collect a config for a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 

try:
    # collect a config for a device
    api_response = api_instance.collect_device_config_source_config(device_id, hds_id, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->collect_device_config_source_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_log_partition**
> Pagination create_log_partition(body=body)

Create a new log partition

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.LogPartition() # LogPartition |  (optional)

try:
    # Create a new log partition
    api_response = api_instance.create_log_partition(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->create_log_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogPartition**](LogPartition.md)|  | [optional] 

### Return type

[**Pagination**](Pagination.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_group**
> object delete_access_group(id)

Delete access group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete access group
    api_response = api_instance.delete_access_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_access_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_admin_by_id**
> object delete_admin_by_id(id)

delete user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete user
    api_response = api_instance.delete_admin_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_by_id**
> object delete_alert_rule_by_id(id)

delete alert rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete alert rule
    api_response = api_instance.delete_alert_rule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token_by_id**
> object delete_api_token_by_id(admin_id, apitoken_id)

delete apiToken

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 

try:
    # delete apiToken
    api_response = api_instance.delete_api_token_by_id(admin_id, apitoken_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_api_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_applies_to_function_by_id**
> object delete_applies_to_function_by_id(id, ignore_reference=ignore_reference)

delete applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
ignore_reference = false # bool |  (optional) (default to false)

try:
    # delete applies to function
    api_response = api_instance.delete_applies_to_function_by_id(id, ignore_reference=ignore_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_applies_to_function_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ignore_reference** | **bool**|  | [optional] [default to false]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_by_id**
> object delete_collector_by_id(id)

delete collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete collector
    api_response = api_instance.delete_collector_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_group_by_id**
> object delete_collector_group_by_id(id)

delete collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete collector group
    api_response = api_instance.delete_collector_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_source_by_id**
> ConfigSource delete_config_source_by_id(id)

delete config source by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete config source by id
    api_response = api_instance.delete_config_source_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_config_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_by_id**
> object delete_dashboard_by_id(id)

delete dashboard

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete dashboard
    api_response = api_instance.delete_dashboard_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_group_by_id**
> object delete_dashboard_group_by_id(id, allow_non_empty_group=allow_non_empty_group)

delete dashboard group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
allow_non_empty_group = false # bool |  (optional) (default to false)

try:
    # delete dashboard group
    api_response = api_instance.delete_dashboard_group_by_id(id, allow_non_empty_group=allow_non_empty_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **allow_non_empty_group** | **bool**|  | [optional] [default to false]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasource_by_id**
> object delete_datasource_by_id(id)

delete datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete datasource
    api_response = api_instance.delete_datasource_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id**
> object delete_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, delete_hard=delete_hard)

delete a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
delete_hard = true # bool |  (optional) (default to true)

try:
    # delete a device
    api_response = api_instance.delete_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, delete_hard=delete_hard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **delete_hard** | **bool**|  | [optional] [default to true]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_datasource_instance_by_id**
> object delete_device_datasource_instance_by_id(device_id, hds_id, id)

delete a device instance

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 

try:
    # delete a device instance
    api_response = api_instance.delete_device_datasource_instance_by_id(device_id, hds_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_by_id**
> object delete_device_group_by_id(id, delete_children=delete_children, delete_hard=delete_hard)

delete device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
delete_children = false # bool |  (optional) (default to false)
delete_hard = true # bool |  (optional) (default to true)

try:
    # delete device group
    api_response = api_instance.delete_device_group_by_id(id, delete_children=delete_children, delete_hard=delete_hard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **bool**|  | [optional] [default to false]
 **delete_hard** | **bool**|  | [optional] [default to true]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_cluster_alert_conf_by_id**
> object delete_device_group_cluster_alert_conf_by_id(device_group_id, id)

Delete cluster alert configuration

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 

try:
    # Delete cluster alert configuration
    api_response = api_instance.delete_device_group_cluster_alert_conf_by_id(device_group_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_property_by_name**
> object delete_device_group_property_by_name(gid, name)

delete device group property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 

try:
    # delete device group property
    api_response = api_instance.delete_device_group_property_by_name(gid, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_property_by_name**
> object delete_device_property_by_name(device_id, name)

delete device property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 

try:
    # delete device property
    api_response = api_instance.delete_device_property_by_name(device_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_escalation_chain_by_id**
> object delete_escalation_chain_by_id(id)

delete escalation chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete escalation chain
    api_response = api_instance.delete_escalation_chain_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_source_by_id**
> object delete_event_source_by_id(id)

delete eventSource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete eventSource by id
    api_response = api_instance.delete_event_source_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_event_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_monitor**
> object delete_job_monitor(id)

Delete JobMonitor

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete JobMonitor
    api_response = api_instance.delete_job_monitor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_job_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_partition_by_id**
> Response delete_log_partition_by_id(id)

Delete a log partition by ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a log partition by ID
    api_response = api_instance.delete_log_partition_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_log_partition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Response**](Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_source**
> object delete_log_source(id)

delete log source 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete log source 
    api_response = api_instance.delete_log_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_log_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_netscan_by_id**
> object delete_netscan_by_id(id)

delete a netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete a netscan
    api_response = api_instance.delete_netscan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_netscan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oid**
> object delete_oid(id)

delete a OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete a OID
    api_response = api_instance.delete_oid(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_oid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ops_note_by_id**
> object delete_ops_note_by_id(id)

delete opsnote

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete opsnote
    api_response = api_instance.delete_ops_note_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property_rule**
> object delete_property_rule(id)

delete a property rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete a property rule
    api_response = api_instance.delete_property_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_property_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipient_group_by_id**
> object delete_recipient_group_by_id(id)

delete recipient group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete recipient group
    api_response = api_instance.delete_recipient_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_by_id**
> object delete_report_by_id(id)

delete report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete report
    api_response = api_instance.delete_report_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report_group_by_id**
> object delete_report_group_by_id(id)

delete report group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete report group
    api_response = api_instance.delete_report_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_by_id**
> object delete_role_by_id(id)

delete role

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete role
    api_response = api_instance.delete_role_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sdt_by_id**
> object delete_sdt_by_id(id)

delete SDT

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # delete SDT
    api_response = api_instance.delete_sdt_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_source**
> object delete_topology_source(id)

Delete TopologySource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete TopologySource
    api_response = api_instance.delete_topology_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_topology_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_by_id**
> object delete_website_by_id(id)

delete website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete website
    api_response = api_instance.delete_website_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_website_group_by_id**
> object delete_website_group_by_id(id, delete_children=delete_children)

delete website group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
delete_children = 0 # int |  (optional) (default to 0)

try:
    # delete website group
    api_response = api_instance.delete_website_group_by_id(id, delete_children=delete_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **int**|  | [optional] [default to 0]

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_widget_by_id**
> object delete_widget_by_id(id)

delete widget

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # delete widget
    api_response = api_instance.delete_widget_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_subscriptions**
> AzureSubscriptionIdPaginationResponse discover_subscriptions(body)

view subscriptions

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestAzureSubscriptionsDiscoverV3() # RestAzureSubscriptionsDiscoverV3 | 

try:
    # view subscriptions
    api_response = api_instance.discover_subscriptions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->discover_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAzureSubscriptionsDiscoverV3**](RestAzureSubscriptionsDiscoverV3.md)|  | 

### Return type

[**AzureSubscriptionIdPaginationResponse**](AzureSubscriptionIdPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **escalated_alert_by_id**
> object escalated_alert_by_id(id)

escalate alert by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # escalate alert by id
    api_response = api_instance.escalated_alert_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->escalated_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_debug_command**
> Debug execute_debug_command(body=body, collector_id=collector_id)

Execute a Collector debug command

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.Debug() # Debug |  (optional)
collector_id = -1 # int |  (optional) (default to -1)

try:
    # Execute a Collector debug command
    api_response = api_instance.execute_debug_command(body=body, collector_id=collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->execute_debug_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Debug**](Debug.md)|  | [optional] 
 **collector_id** | **int**|  | [optional] [default to -1]

### Return type

[**Debug**](Debug.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_device_instances_data**
> DeviceInstanceDataPaginationResponse fetch_device_instances_data(body, period=period, start=start, end=end, aggregate=aggregate)

fetch device instances data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DeviceInstances() # DeviceInstances | 
period = 1.0 # float |  (optional) (default to 1.0)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
aggregate = 'none' # str | the aggregate option (optional) (default to none)

try:
    # fetch device instances data
    api_response = api_instance.fetch_device_instances_data(body, period=period, start=start, end=end, aggregate=aggregate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->fetch_device_instances_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceInstances**](DeviceInstances.md)|  | 
 **period** | **float**|  | [optional] [default to 1.0]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **aggregate** | **str**| the aggregate option | [optional] [default to none]

### Return type

[**DeviceInstanceDataPaginationResponse**](DeviceInstanceDataPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_report_using_task_id**
> GenerateReportResult fetch_report_using_task_id(id, task_id)

get report for task Id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
task_id = 'task_id_example' # str | 

try:
    # get report for task Id
    api_response = api_instance.fetch_report_using_task_id(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->fetch_report_using_task_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **task_id** | **str**|  | 

### Return type

[**GenerateReportResult**](GenerateReportResult.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_report_by_id**
> GenerateReportResult generate_report_by_id(id, body=body)

run a report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.GenerateReportRequest() # GenerateReportRequest |  (optional)

try:
    # run a report
    api_response = api_instance.generate_report_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->generate_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**GenerateReportRequest**](GenerateReportRequest.md)|  | [optional] 

### Return type

[**GenerateReportResult**](GenerateReportResult.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_group_by_id**
> AccessGroup get_access_group_by_id(id, fields=fields)

Get access group by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # Get access group by id
    api_response = api_instance.get_access_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_access_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AccessGroup**](AccessGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_group_list**
> AccessGroupPaginationResponse get_access_group_list(fields=fields, size=size, offset=offset, filter=filter)

Get access group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get access group list
    api_response = api_instance.get_access_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_access_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AccessGroupPaginationResponse**](AccessGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_by_id**
> Admin get_admin_by_id(id, fields=fields)

get user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get user
    api_response = api_instance.get_admin_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_list**
> AdminPaginationResponse get_admin_list(type=type, permission=permission, filter_group_string=filter_group_string, fields=fields, size=size, offset=offset, filter=filter)

get user list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
type = 'type_example' # str |  (optional)
permission = 'permission_example' # str |  (optional)
filter_group_string = 'filter_group_string_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get user list
    api_response = api_instance.get_admin_list(type=type, permission=permission, filter_group_string=filter_group_string, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_admin_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **permission** | **str**|  | [optional] 
 **filter_group_string** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AdminPaginationResponse**](AdminPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> Alert get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)

get alert

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get alert
    api_response = api_instance.get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Alert**](Alert.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list**
> AlertListPaginationResponse get_alert_list(fields=fields, size=size, offset=offset, filter=filter)

get alert list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alert list
    api_response = api_instance.get_alert_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertListPaginationResponse**](AlertListPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_group_id**
> AlertPaginationResponse get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)

get device group alerts

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group alerts
    api_response = api_instance.get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_id**
> AlertPaginationResponse get_alert_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)

get alerts

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
bound = 'instances' # str |  (optional) (default to instances)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alerts
    api_response = api_instance.get_alert_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **bound** | **str**|  | [optional] [default to instances]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_by_id**
> AlertRule get_alert_rule_by_id(id, fields=fields)

get alert rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get alert rule by id
    api_response = api_instance.get_alert_rule_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_list**
> AlertRulePaginationResponse get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)

get alert rule list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alert rule list
    api_response = api_instance.get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_rule_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertRulePaginationResponse**](AlertRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_log_partitions**
> Pagination get_all_log_partitions()

Retrieve a list of all log partitions

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Retrieve a list of all log partitions
    api_response = api_instance.get_all_log_partitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_log_partitions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Pagination**](Pagination.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sdt_list_by_device_id**
> SDTPaginationResponse get_all_sdt_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get SDTs for a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDTs for a device
    api_response = api_instance.get_all_sdt_list_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_sdt_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sdt_list_by_website_group_id**
> SDTPaginationResponse get_all_sdt_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of SDTs for a website group (Response may contain extra fields depending upon the type of SDT)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of SDTs for a website group (Response may contain extra fields depending upon the type of SDT)
    api_response = api_instance.get_all_sdt_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_sdt_list_by_website_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_list**
> ApiTokenPaginationResponse get_api_token_list(type=type, permission=permission, fields=fields, size=size, offset=offset, filter=filter)

get a list of api tokens across users

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
type = 'type_example' # str |  (optional)
permission = 'permission_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of api tokens across users
    api_response = api_instance.get_api_token_list(type=type, permission=permission, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_api_token_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **permission** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ApiTokenPaginationResponse**](ApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_list_by_admin_id**
> ApiTokenPaginationResponse get_api_token_list_by_admin_id(admin_id, type=type, permission=permission, fields=fields, size=size, offset=offset, filter=filter)

get api tokens for a user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
type = 'type_example' # str |  (optional)
permission = 'permission_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get api tokens for a user
    api_response = api_instance.get_api_token_list_by_admin_id(admin_id, type=type, permission=permission, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_api_token_list_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **type** | **str**|  | [optional] 
 **permission** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ApiTokenPaginationResponse**](ApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applies_to_function_by_id**
> AppliesToFunction get_applies_to_function_by_id(id)

get applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get applies to function
    api_response = api_instance.get_applies_to_function_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_applies_to_function_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AppliesToFunction**](AppliesToFunction.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applies_to_function_list**
> RestAppliesToFunctionPaginationResponse get_applies_to_function_list(fields=fields, size=size, offset=offset, filter=filter)

get applies to function list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get applies to function list
    api_response = api_instance.get_applies_to_function_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_applies_to_function_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestAppliesToFunctionPaginationResponse**](RestAppliesToFunctionPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_associated_device_list_by_data_source_id**
> DeviceDataSourceAssociatedPaginationResponse get_associated_device_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)

get devices associated with a datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get devices associated with a datasource
    api_response = api_instance.get_associated_device_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_associated_device_list_by_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceAssociatedPaginationResponse**](DeviceDataSourceAssociatedPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_by_id**
> AuditLog get_audit_log_by_id(id)

Get audit log by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get audit log by id
    api_response = api_instance.get_audit_log_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_audit_log_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AuditLog**](AuditLog.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_list**
> AccessLogPaginationResponse get_audit_log_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

Get audit logs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'format_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get audit logs
    api_response = api_instance.get_audit_log_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_audit_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AccessLogPaginationResponse**](AccessLogPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_account_id**
> AwsAccountId get_aws_account_id()

Get AWS account ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Get AWS account ID
    api_response = api_instance.get_aws_account_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_aws_account_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsAccountId**](AwsAccountId.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_external_id**
> AwsExternalId get_aws_external_id()

Get AWS external ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Get AWS external ID
    api_response = api_instance.get_aws_external_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_aws_external_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsExternalId**](AwsExternalId.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_by_id**
> Collector get_collector_by_id(id, fields=fields)

get collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get collector
    api_response = api_instance.get_collector_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_by_id**
> CollectorGroup get_collector_group_by_id(id, fields=fields)

get collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get collector group
    api_response = api_instance.get_collector_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_list**
> CollectorGroupPaginationResponse get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)

get collector group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get collector group list
    api_response = api_instance.get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**CollectorGroupPaginationResponse**](CollectorGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_installer**
> str get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)

get collector installer

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | 
os_and_arch = 'os_and_arch_example' # str | 
collector_version = 56 # int | The version of the installer you'd like to download. This defaults to the latest GD Collector, unless useEA is true (optional)
token = 'token_example' # str |  (optional)
monitor_others = true # bool |  (optional) (default to true)
collector_size = 'medium' # str | The size of the Collector you'd like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory), extra large (requires 16GB memory), double extra large (requires 32GB memory). Requires collector version 22.180 or higher. Defaults to small (optional) (default to medium)
use_ea = false # bool | If true, the latest EA Collector version will be used. Defaults to false (optional) (default to false)

try:
    # get collector installer
    api_response = api_instance.get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_installer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**|  | 
 **os_and_arch** | **str**|  | 
 **collector_version** | **int**| The version of the installer you&#x27;d like to download. This defaults to the latest GD Collector, unless useEA is true | [optional] 
 **token** | **str**|  | [optional] 
 **monitor_others** | **bool**|  | [optional] [default to true]
 **collector_size** | **str**| The size of the Collector you&#x27;d like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory), extra large (requires 16GB memory), double extra large (requires 32GB memory). Requires collector version 22.180 or higher. Defaults to small | [optional] [default to medium]
 **use_ea** | **bool**| If true, the latest EA Collector version will be used. Defaults to false | [optional] [default to false]

### Return type

**str**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_list**
> CollectorPaginationResponse get_collector_list(fields=fields, size=size, offset=offset, filter=filter)

get collector list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get collector list
    api_response = api_instance.get_collector_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**CollectorPaginationResponse**](CollectorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_version_list**
> CollectorVersionPaginationResponse get_collector_version_list(fields=fields, size=size, offset=offset, filter=filter)

get collector version list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get collector version list
    api_response = api_instance.get_collector_version_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**CollectorVersionPaginationResponse**](CollectorVersionPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_source_by_id**
> ConfigSource get_config_source_by_id(id, format=format)

get config source by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # get config source by id
    api_response = api_instance.get_config_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_config_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_source_list**
> ConfigsourcePaginationResponse get_config_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

get config source list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get config source list
    api_response = api_instance.get_config_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_config_source_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ConfigsourcePaginationResponse**](ConfigsourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_info_by_company**
> RestContractInfoBaseV3 get_contract_info_by_company()

get contract info by company

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get contract info by company
    api_response = api_instance.get_contract_info_by_company()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_contract_info_by_company: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestContractInfoBaseV3**](RestContractInfoBaseV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id**
> Dashboard get_dashboard_by_id(id, template=template, format=format, fields=fields)

get dashboard

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
template = false # bool |  (optional) (default to false)
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)

try:
    # get dashboard
    api_response = api_instance.get_dashboard_by_id(id, template=template, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template** | **bool**|  | [optional] [default to false]
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_by_id**
> DashboardGroup get_dashboard_group_by_id(id, template=template, format=format, fields=fields)

get dashboard group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
template = false # bool |  (optional) (default to false)
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)

try:
    # get dashboard group
    api_response = api_instance.get_dashboard_group_by_id(id, template=template, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template** | **bool**|  | [optional] [default to false]
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_list**
> DashboardGroupPaginationResponse get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get dashboard group list
    api_response = api_instance.get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DashboardGroupPaginationResponse**](DashboardGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_list**
> DashboardPaginationResponse get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get dashboard list
    api_response = api_instance.get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DashboardPaginationResponse**](DashboardPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_overview_graph_by_id**
> DataSourceOverviewGraph get_data_source_overview_graph_by_id(ds_id, id)

get datasource overview graph by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
ds_id = 56 # int | 
id = 56 # int | 

try:
    # get datasource overview graph by id
    api_response = api_instance.get_data_source_overview_graph_by_id(ds_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_data_source_overview_graph_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ds_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

[**DataSourceOverviewGraph**](DataSourceOverviewGraph.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_overview_graph_list**
> DatasourceOverviewGraphPaginationResponse get_data_source_overview_graph_list(ds_id, fields=fields, size=size, offset=offset, filter=filter)

get datasource overview graph list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
ds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get datasource overview graph list
    api_response = api_instance.get_data_source_overview_graph_list(ds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_data_source_overview_graph_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DatasourceOverviewGraphPaginationResponse**](DatasourceOverviewGraphPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_by_id**
> DataSource get_datasource_by_id(id, format=format, fields=fields)

get datasource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)

try:
    # get datasource by id
    api_response = api_instance.get_datasource_by_id(id, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_list**
> DatasourcePaginationResponse get_datasource_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

get datasource list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get datasource list
    api_response = api_instance.get_datasource_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DatasourcePaginationResponse**](DatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_command_result**
> Debug get_debug_command_result(id, collector_id=collector_id)

Get the result of a Collector debug command using sessionId

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
collector_id = -1 # int |  (optional) (default to -1)

try:
    # Get the result of a Collector debug command using sessionId
    api_response = api_instance.get_debug_command_result(id, collector_id=collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_debug_command_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collector_id** | **int**|  | [optional] [default to -1]

### Return type

[**Debug**](Debug.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delta_devices**
> DeviceDeltaPaginationResponse get_delta_devices(delta_id)

Get delta devices using deltaId

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
delta_id = 'delta_id_example' # str | 

try:
    # Get delta devices using deltaId
    api_response = api_instance.get_delta_devices(delta_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_delta_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delta_id** | **str**|  | 

### Return type

[**DeviceDeltaPaginationResponse**](DeviceDeltaPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delta_id_with_devices**
> DeviceDeltaPaginationResponse get_delta_id_with_devices(delta_id=delta_id)

Get filter matched devices with new deltaId

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
delta_id = 'delta_id_example' # str |  (optional)

try:
    # Get filter matched devices with new deltaId
    api_response = api_instance.get_delta_id_with_devices(delta_id=delta_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_delta_id_with_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delta_id** | **str**|  | [optional] 

### Return type

[**DeviceDeltaPaginationResponse**](DeviceDeltaPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> Device get_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields)

get device by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get device by id
    api_response = api_instance.get_device_by_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_config_source_config_by_id**
> DeviceDataSourceInstanceConfig get_device_config_source_config_by_id(device_id, hds_id, instance_id, id, format=format, start_epoch=start_epoch, fields=fields)

get a config for a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
id = 'id_example' # str | 
format = 'json' # str |  (optional) (default to json)
start_epoch = 0 # int |  (optional) (default to 0)
fields = 'fields_example' # str |  (optional)

try:
    # get a config for a device
    api_response = api_instance.get_device_config_source_config_by_id(device_id, hds_id, instance_id, id, format=format, start_epoch=start_epoch, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]
 **start_epoch** | **int**|  | [optional] [default to 0]
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceConfig**](DeviceDataSourceInstanceConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_config_source_config_list**
> DeviceDatasourceInstanceConfigPaginationResponse get_device_config_source_config_list(device_id, hds_id, instance_id, fields=fields, size=size, offset=offset, filter=filter)

get detailed config information for the instance

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | 
instance_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get detailed config information for the instance
    api_response = api_instance.get_device_config_source_config_list(device_id, hds_id, instance_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstanceConfigPaginationResponse**](DeviceDatasourceInstanceConfigPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_by_id**
> DeviceDataSource get_device_datasource_by_id(device_id, id, fields=fields)

get device datasource 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device datasource 
    api_response = api_instance.get_device_datasource_by_id(device_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSource**](DeviceDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_data_by_id**
> DeviceDataSourceData get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format, aggregate=aggregate)

get device datasource data 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
period = 1.0 # float |  (optional) (default to 1.0)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)
aggregate = 'none' # str | the aggregate option (optional) (default to none)

try:
    # get device datasource data 
    api_response = api_instance.get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format, aggregate=aggregate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1.0]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]
 **aggregate** | **str**| the aggregate option | [optional] [default to none]

### Return type

[**DeviceDataSourceData**](DeviceDataSourceData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)

get device instance alert setting

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device instance alert setting
    api_response = api_instance.get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_list_of_device**
> DeviceDataSourceInstanceAlertSettingPaginationResponse get_device_datasource_instance_alert_setting_list_of_device(device_id, start=start, end=end, netflow_filter=netflow_filter, size=size, offset=offset)

get a list of alert settings for a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # get a list of alert settings for a device
    api_response = api_instance.get_device_datasource_instance_alert_setting_list_of_device(device_id, start=start, end=end, netflow_filter=netflow_filter, size=size, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_list_of_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**DeviceDataSourceInstanceAlertSettingPaginationResponse**](DeviceDataSourceInstanceAlertSettingPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_list_of_dsi**
> DeviceDataSourceInstanceAlertSettingPaginationResponse get_device_datasource_instance_alert_setting_list_of_dsi(device_id, hds_id, instance_id, size=size, offset=offset)

get a list of alert settings for a device datasource instance

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # get a list of alert settings for a device datasource instance
    api_response = api_instance.get_device_datasource_instance_alert_setting_list_of_dsi(device_id, hds_id, instance_id, size=size, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_list_of_dsi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**DeviceDataSourceInstanceAlertSettingPaginationResponse**](DeviceDataSourceInstanceAlertSettingPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_by_id**
> DeviceDataSourceInstance get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)

get device instance 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device instance 
    api_response = api_instance.get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_data**
> DeviceDataSourceInstanceData get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get device instance data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
period = 1.0 # float |  (optional) (default to 1.0)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)

try:
    # get device instance data
    api_response = api_instance.get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1.0]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**DeviceDataSourceInstanceData**](DeviceDataSourceInstanceData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_graph_data**
> GraphPlot get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)

get device instance graph data 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
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
    print("Exception when calling LMApi->get_device_datasource_instance_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)

get device datasource instance group 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device datasource instance group 
    api_response = api_instance.get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_list**
> DeviceDatasourceInstanceGroupPaginationResponse get_device_datasource_instance_group_list(device_id, device_ds_id, fields=fields, size=size, offset=offset, filter=filter)

get device datasource instance group list 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device datasource instance group list 
    api_response = api_instance.get_device_datasource_instance_group_list(device_id, device_ds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstanceGroupPaginationResponse**](DeviceDatasourceInstanceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_overview_graph_data**
> GraphPlot get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)

get device instance group overview graph data 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
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
    print("Exception when calling LMApi->get_device_datasource_instance_group_overview_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **dsig_id** | **int**|  | 
 **ograph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_list**
> DeviceDatasourceInstancePaginationResponse get_device_datasource_instance_list(device_id, hds_id, fields=fields, size=size, offset=offset, filter=filter)

get device instance list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device instance list
    api_response = api_instance.get_device_datasource_instance_list(device_id, hds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstancePaginationResponse**](DeviceDatasourceInstancePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_sdt_history**
> DeviceGroupSDTHistoryPaginationResponse get_device_datasource_instance_sdt_history(device_id, hds_id, id, fields=fields, size=size, offset=offset, filter=filter)

get device instance SDT history

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device instance SDT history
    api_response = api_instance.get_device_datasource_instance_sdt_history(device_id, hds_id, id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_sdt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupSDTHistoryPaginationResponse**](DeviceGroupSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_list**
> DeviceDatasourcePaginationResponse get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device datasource list 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
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
    print("Exception when calling LMApi->get_device_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourcePaginationResponse**](DeviceDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> DeviceGroup get_device_group_by_id(id, fields=fields)

get device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group
    api_response = api_instance.get_device_group_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig get_device_group_cluster_alert_conf_by_id(device_group_id, id)

Get cluster alert configuration by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 

try:
    # Get cluster alert configuration by id
    api_response = api_instance.get_device_group_cluster_alert_conf_by_id(device_group_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_cluster_alert_conf_list**
> DeviceClusterAlertConfigPaginationResponse get_device_group_cluster_alert_conf_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)

get a list of cluster alert configurations for a device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of cluster alert configurations for a device group
    api_response = api_instance.get_device_group_cluster_alert_conf_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_cluster_alert_conf_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceClusterAlertConfigPaginationResponse**](DeviceClusterAlertConfigPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)

get device group datasource alert setting 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group datasource alert setting 
    api_response = api_instance.get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_by_id**
> DeviceGroupDataSource get_device_group_datasource_by_id(device_group_id, id, fields=fields)

get device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group datasource
    api_response = api_instance.get_device_group_datasource_by_id(device_group_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**DeviceGroupDataSource**](DeviceGroupDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_list**
> DeviceGroupDatasourcePaginationResponse get_device_group_datasource_list(device_group_id, include_disabled_data_source_without_instance=include_disabled_data_source_without_instance, fields=fields, size=size, offset=offset, filter=filter)

get device group datasource list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
include_disabled_data_source_without_instance = false # bool |  (optional) (default to false)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group datasource list
    api_response = api_instance.get_device_group_datasource_list(device_group_id, include_disabled_data_source_without_instance=include_disabled_data_source_without_instance, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_datasource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **include_disabled_data_source_without_instance** | **bool**|  | [optional] [default to false]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupDatasourcePaginationResponse**](DeviceGroupDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_list**
> DeviceGroupPaginationResponse get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)

get device group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group list
    api_response = api_instance.get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupPaginationResponse**](DeviceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_property_by_name**
> EntityProperty get_device_group_property_by_name(gid, name, fields=fields)

get device group property by name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get device group property by name
    api_response = api_instance.get_device_group_property_by_name(gid, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_property_list**
> PropertyPaginationResponse get_device_group_property_list(gid, fields=fields, size=size, offset=offset, filter=filter)

get device group properties

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group properties
    api_response = api_instance.get_device_group_property_list(gid, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_property_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_sdt_list**
> SDTPaginationResponse get_device_group_sdt_list(id, fields=fields, size=size, offset=offset, filter=filter)

get device group SDTs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device group SDTs
    api_response = api_instance.get_device_group_sdt_list(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_group_sdt_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_instance_graph_data_only_by_instance_id**
> GraphPlot get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)

get device instance data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
instance_id = 56 # int | 
graph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get device instance data
    api_response = api_instance.get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_instance_graph_data_only_by_instance_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_instance_list**
> DeviceDatasourceInstancePaginationResponse get_device_instance_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get device instance list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device instance list
    api_response = api_instance.get_device_instance_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDatasourceInstancePaginationResponse**](DeviceDatasourceInstancePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_list**
> DevicePaginationResponse get_device_list(start=start, end=end, netflow_filter=netflow_filter, include_deleted_resources=include_deleted_resources, fields=fields, size=size, offset=offset, filter=filter)

get device list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
include_deleted_resources = false # bool |  (optional) (default to false)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device list
    api_response = api_instance.get_device_list(start=start, end=end, netflow_filter=netflow_filter, include_deleted_resources=include_deleted_resources, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **include_deleted_resources** | **bool**|  | [optional] [default to false]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DevicePaginationResponse**](DevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_property_by_name**
> EntityProperty get_device_property_by_name(device_id, name, fields=fields)

get device property by name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get device property by name
    api_response = api_instance.get_device_property_by_name(device_id, name, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_property_list**
> PropertyPaginationResponse get_device_property_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device properties

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device properties
    api_response = api_instance.get_device_property_list(device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_property_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation_chain_by_id**
> EscalatingChain get_escalation_chain_by_id(id, fields=fields)

get escalation chain by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get escalation chain by id
    api_response = api_instance.get_escalation_chain_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation_chain_list**
> EscalationChainPaginationResponse get_escalation_chain_list(fields=fields, size=size, offset=offset, filter=filter)

get escalation chain list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get escalation chain list
    api_response = api_instance.get_escalation_chain_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_escalation_chain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**EscalationChainPaginationResponse**](EscalationChainPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_source_by_id**
> EventSource get_event_source_by_id(id, format=format)

get eventSource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # get eventSource by id
    api_response = api_instance.get_event_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_event_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**EventSource**](EventSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_source_list**
> EventSourcePaginationResponse get_event_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

get eventSource list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get eventSource list
    api_response = api_instance.get_event_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_event_source_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**EventSourcePaginationResponse**](EventSourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_api_stats**
> ApiPerfMetrics get_external_api_stats()

get external api stats info

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get external api stats info
    api_response = api_instance.get_external_api_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_external_api_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiPerfMetrics**](ApiPerfMetrics.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_device_list_by_device_group_id**
> DevicePaginationResponse get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get immediate devices under group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
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
    print("Exception when calling LMApi->get_immediate_device_list_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DevicePaginationResponse**](DevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_website_list_by_website_group_id**
> WebsitePaginationResponse get_immediate_website_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of websites for a group (Response may contain extra fields depending upon the type of check { PingCheck | WebCheck} being added)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of websites for a group (Response may contain extra fields depending upon the type of check { PingCheck | WebCheck} being added)
    api_response = api_instance.get_immediate_website_list_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_immediate_website_list_by_website_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsitePaginationResponse**](WebsitePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_audit_logs**
> IntegrationAuditLogPaginationResponse get_integration_audit_logs(format=format)

get integration audit logs list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'format_example' # str |  (optional)

try:
    # get integration audit logs list
    api_response = api_instance.get_integration_audit_logs(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_integration_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

[**IntegrationAuditLogPaginationResponse**](IntegrationAuditLogPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_monitor_by_id**
> BatchJob get_job_monitor_by_id(id, format=format)

Get JobMonitor by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # Get JobMonitor by id
    api_response = api_instance.get_job_monitor_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_job_monitor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_monitor_list**
> BatchJobPaginationResponse get_job_monitor_list(format=format)

Get JobMonitor List

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)

try:
    # Get JobMonitor List
    api_response = api_instance.get_job_monitor_list(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_job_monitor_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]

### Return type

[**BatchJobPaginationResponse**](BatchJobPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_source_by_id**
> LogSource get_log_source_by_id(id, format=format)

get log source 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
format = 'json' # str |  (optional) (default to json)

try:
    # get log source 
    api_response = api_instance.get_log_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**LogSource**](LogSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_source_list**
> LogSourcePaginationResponse get_log_source_list(format=format)

get log source list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)

try:
    # get log source list
    api_response = api_instance.get_log_source_list(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_source_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]

### Return type

[**LogSourcePaginationResponse**](LogSourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_usage**
> Usage get_metrics_usage()

get metrics usage

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get metrics usage
    api_response = api_instance.get_metrics_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_metrics_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Usage**](Usage.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_endpoint_list**
> EndpointPaginationResponse get_netflow_endpoint_list(id, start=start, end=end, netflow_filter=netflow_filter, port=port, fields=fields, size=size, offset=offset, filter=filter)

get netflow endpoints

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
port = 'port_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow endpoints
    api_response = api_instance.get_netflow_endpoint_list(id, start=start, end=end, netflow_filter=netflow_filter, port=port, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_endpoint_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**EndpointPaginationResponse**](EndpointPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_flow_list**
> FlowRecordPaginationResponse get_netflow_flow_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get netflow flows

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow flows
    api_response = api_instance.get_netflow_flow_list(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_flow_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**FlowRecordPaginationResponse**](FlowRecordPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netflow_port_list**
> PortPaginationResponse get_netflow_port_list(id, start=start, end=end, netflow_filter=netflow_filter, ip=ip, fields=fields, size=size, offset=offset, filter=filter)

get netflow ports

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow ports
    api_response = api_instance.get_netflow_port_list(id, start=start, end=end, netflow_filter=netflow_filter, ip=ip, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_port_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PortPaginationResponse**](PortPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netscan_by_id**
> Netscan get_netscan_by_id(id)

get netscan by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get netscan by id
    api_response = api_instance.get_netscan_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netscan_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_netscan_list**
> NetscanPaginationResponse get_netscan_list(fields=fields, size=size, offset=offset, filter=filter)

get netscan list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netscan list
    api_response = api_instance.get_netscan_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netscan_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**NetscanPaginationResponse**](NetscanPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oid_by_id**
> RestOidV3 get_oid_by_id(id)

get OID by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get OID by id
    api_response = api_instance.get_oid_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_oid_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestOidV3**](RestOidV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oid_list**
> OidSourcePaginationResponse get_oid_list()

get OID's list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get OID's list
    api_response = api_instance.get_oid_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_oid_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OidSourcePaginationResponse**](OidSourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ops_note_by_id**
> OpsNote get_ops_note_by_id(id, fields=fields)

get opsnote by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
fields = 'fields_example' # str |  (optional)

try:
    # get opsnote by id
    api_response = api_instance.get_ops_note_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ops_note_list**
> OpsNotePaginationResponse get_ops_note_list(fields=fields, size=size, offset=offset, filter=filter)

get opsnote list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str | Filter the response based on tags, createdBy, happenedOn, monitorObjectGroups, monitorObjectNames, or _all field values (optional)

try:
    # get opsnote list
    api_response = api_instance.get_ops_note_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_ops_note_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**| Filter the response based on tags, createdBy, happenedOn, monitorObjectGroups, monitorObjectNames, or _all field values | [optional] 

### Return type

[**OpsNotePaginationResponse**](OpsNotePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_partition_by_id**
> LogPartition get_partition_by_id(id)

Retrieve details of a specific log partition

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Retrieve details of a specific log partition
    api_response = api_instance.get_partition_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_partition_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_rules_by_id**
> PropertyRule get_property_rules_by_id(id, format=format)

get property rules by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # get property rules by id
    api_response = api_instance.get_property_rules_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_property_rules_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**PropertyRule**](PropertyRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_rules_list**
> PropertyRulePaginationResponse get_property_rules_list(format=format, fields=fields, size=size, offset=offset, filter=filter)

get property rules list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
format = 'json' # str |  (optional) (default to json)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get property rules list
    api_response = api_instance.get_property_rules_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_property_rules_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] [default to json]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyRulePaginationResponse**](PropertyRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_group_by_id**
> RecipientGroup get_recipient_group_by_id(id)

get recipient group by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get recipient group by id
    api_response = api_instance.get_recipient_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_group_list**
> RecipientGroupPaginationResponse get_recipient_group_list(fields=fields, size=size, offset=offset, filter=filter)

get recipient group List

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get recipient group List
    api_response = api_instance.get_recipient_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recipient_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RecipientGroupPaginationResponse**](RecipientGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_id**
> ReportBase get_report_by_id(id, fields=fields)

get report by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get report by id
    api_response = api_instance.get_report_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_group_by_id**
> ReportGroup get_report_group_by_id(id)

get report group by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get report group by id
    api_response = api_instance.get_report_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_group_list**
> ReportGroupPaginationResponse get_report_group_list(fields=fields, size=size, offset=offset, filter=filter)

get report group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get report group list
    api_response = api_instance.get_report_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ReportGroupPaginationResponse**](ReportGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_list**
> ReportPaginationResponse get_report_list(fields=fields, size=size, offset=offset, filter=filter)

get report list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get report list
    api_response = api_instance.get_report_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**ReportPaginationResponse**](ReportPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_retention_list**
> Pagination get_retention_list()

Retrieve the list of log retentions

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Retrieve the list of log retentions
    api_response = api_instance.get_retention_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_retention_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Pagination**](Pagination.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> Role get_role_by_id(id, fields=fields)

get role by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get role by id
    api_response = api_instance.get_role_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_list**
> RolePaginationResponse get_role_list(exclude_admin=exclude_admin, fields=fields, size=size, offset=offset, filter=filter)

get role list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
exclude_admin = false # bool |  (optional) (default to false)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get role list
    api_response = api_instance.get_role_list(exclude_admin=exclude_admin, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_admin** | **bool**|  | [optional] [default to false]
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RolePaginationResponse**](RolePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_by_id**
> SDT get_sdt_by_id(id)

get SDT by id (Response may contain extra fields depending upon the type of SDT of given id)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # get SDT by id (Response may contain extra fields depending upon the type of SDT of given id)
    api_response = api_instance.get_sdt_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_data_source_id**
> DeviceDataSourceSDTHistoryPaginationResponse get_sdt_history_by_device_data_source_id(device_id, id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the device dataSource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the device dataSource
    api_response = api_instance.get_sdt_history_by_device_data_source_id(device_id, id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceSDTHistoryPaginationResponse**](DeviceDataSourceSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_group_id**
> DeviceGroupSDTHistoryPaginationResponse get_sdt_history_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the group
    api_response = api_instance.get_sdt_history_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceGroupSDTHistoryPaginationResponse**](DeviceGroupSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_device_id**
> DeviceSDTHistoryPaginationResponse get_sdt_history_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the device
    api_response = api_instance.get_sdt_history_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DeviceSDTHistoryPaginationResponse**](DeviceSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_website_group_id**
> WebsiteGroupSDTHistoryPaginationResponse get_sdt_history_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the website group (Response may contain extra fields depending upon the type of SDT)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the website group (Response may contain extra fields depending upon the type of SDT)
    api_response = api_instance.get_sdt_history_by_website_group_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_website_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsiteGroupSDTHistoryPaginationResponse**](WebsiteGroupSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_history_by_website_id**
> WebsiteSDTHistoryPaginationResponse get_sdt_history_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the website (Response may contain extra fields depending upon the type of SDT)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the website (Response may contain extra fields depending upon the type of SDT)
    api_response = api_instance.get_sdt_history_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsiteSDTHistoryPaginationResponse**](WebsiteSDTHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sdt_list**
> SDTPaginationResponse get_sdt_list(fields=fields, size=size, offset=offset, filter=filter)

get SDT list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT list
    api_response = api_instance.get_sdt_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_monitor_check_point_list**
> SiteMonitorCheckPointPaginationResponse get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)

get website checkpoint list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website checkpoint list
    api_response = api_instance.get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_site_monitor_check_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SiteMonitorCheckPointPaginationResponse**](SiteMonitorCheckPointPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top_talkers_graph**
> GraphPlot get_top_talkers_graph(id, start=start, end=end, netflow_filter=netflow_filter, format=format, keyword=keyword)

get top talkers graph

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
format = 'format_example' # str |  (optional)
keyword = 'keyword_example' # str |  (optional)

try:
    # get top talkers graph
    api_response = api_instance.get_top_talkers_graph(id, start=start, end=end, netflow_filter=netflow_filter, format=format, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_top_talkers_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 
 **keyword** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_source_by_id**
> TopologySource get_topology_source_by_id(id, format=format)

Get TopologySource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # Get TopologySource by id
    api_response = api_instance.get_topology_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_topology_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**TopologySource**](TopologySource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology_source_list**
> TopologySourcePaginationResponse get_topology_source_list()

Get TopologySource List

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # Get TopologySource List
    api_response = api_instance.get_topology_source_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_topology_source_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TopologySourcePaginationResponse**](TopologySourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmonitored_device_list**
> UnmonitoredDevicePaginationResponse get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)

get unmonitored device list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get unmonitored device list
    api_response = api_instance.get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_unmonitored_device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**UnmonitoredDevicePaginationResponse**](UnmonitoredDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_update_reason_list_by_config_source_id**
> ConfigSourceUpdateReasonsPaginationResponse get_update_reason_list_by_config_source_id(id)

get update history for a configSource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get update history for a configSource
    api_response = api_instance.get_update_reason_list_by_config_source_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_update_reason_list_by_config_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ConfigSourceUpdateReasonsPaginationResponse**](ConfigSourceUpdateReasonsPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_update_reason_list_by_data_source_id**
> DataSourceUpdateReasonsPaginationResponse get_update_reason_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)

get update history for a datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get update history for a datasource
    api_response = api_instance.get_update_reason_list_by_data_source_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_update_reason_list_by_data_source_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**DataSourceUpdateReasonsPaginationResponse**](DataSourceUpdateReasonsPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v4_metadata**
> Response get_v4_metadata()

get metadata

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

try:
    # get metadata
    api_response = api_instance.get_v4_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_v4_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Response**](Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_alert_list_by_website_id**
> AlertPaginationResponse get_website_alert_list_by_website_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)

get alerts for a website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
need_message = false # bool |  (optional) (default to false)
custom_columns = 'custom_columns_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alerts for a website
    api_response = api_instance.get_website_alert_list_by_website_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_alert_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**AlertPaginationResponse**](AlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_by_id**
> Website get_website_by_id(id, format=format)

get website by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
format = 'json' # str |  (optional) (default to json)

try:
    # get website by id
    api_response = api_instance.get_website_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_checkpoint_data_by_id**
> WebsiteCheckpointRawData get_website_checkpoint_data_by_id(srv_id, check_id, period=period, start=start, end=end, datapoints=datapoints, format=format, aggregate=aggregate)

get data for a website checkpoint

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
srv_id = 56 # int | 
check_id = 56 # int | 
period = 1.0 # float |  (optional) (default to 1.0)
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
datapoints = 'datapoints_example' # str |  (optional)
format = 'json' # str |  (optional) (default to json)
aggregate = 'none' # str | the aggregate option (optional) (default to none)

try:
    # get data for a website checkpoint
    api_response = api_instance.get_website_checkpoint_data_by_id(srv_id, check_id, period=period, start=start, end=end, datapoints=datapoints, format=format, aggregate=aggregate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_checkpoint_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **srv_id** | **int**|  | 
 **check_id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1.0]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]
 **aggregate** | **str**| the aggregate option | [optional] [default to none]

### Return type

[**WebsiteCheckpointRawData**](WebsiteCheckpointRawData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_data_by_graph_name**
> GraphPlot get_website_data_by_graph_name(id, graph_name, start=start, end=end, format=format)

get website data by graph name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
graph_name = 'graph_name_example' # str | 
start = 0 # int |  (optional) (default to 0)
end = 0 # int |  (optional) (default to 0)
format = 'format_example' # str |  (optional)

try:
    # get website data by graph name
    api_response = api_instance.get_website_data_by_graph_name(id, graph_name, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_data_by_graph_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_graph_data**
> GraphPlot get_website_graph_data(website_id, checkpoint_id, graph_name, start=start, end=end, format=format)

get website graph data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
website_id = 56 # int | 
checkpoint_id = 56 # int | 
graph_name = 'graph_name_example' # str | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get website graph data
    api_response = api_instance.get_website_graph_data(website_id, checkpoint_id, graph_name, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **int**|  | 
 **checkpoint_id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**GraphPlot**](GraphPlot.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_group_by_id**
> WebsiteGroup get_website_group_by_id(id)

get website group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 

try:
    # get website group
    api_response = api_instance.get_website_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_group_list**
> WebsiteGroupPaginationResponse get_website_group_list(fields=fields, size=size, offset=offset, filter=filter)

get website group list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website group list
    api_response = api_instance.get_website_group_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsiteGroupPaginationResponse**](WebsiteGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_list**
> WebsitePaginationResponse get_website_list(collector_ids=collector_ids, fields=fields, size=size, offset=offset, filter=filter)

get website list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_ids = 'collector_ids_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get website list
    api_response = api_instance.get_website_list(collector_ids=collector_ids, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_ids** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WebsitePaginationResponse**](WebsitePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_property_list_by_website_id**
> PropertyPaginationResponse get_website_property_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of properties for a website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of properties for a website
    api_response = api_instance.get_website_property_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_property_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**PropertyPaginationResponse**](PropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_website_sdt_list_by_website_id**
> SDTPaginationResponse get_website_sdt_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)

get a list of SDTs for a website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get a list of SDTs for a website
    api_response = api_instance.get_website_sdt_list_by_website_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_sdt_list_by_website_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**SDTPaginationResponse**](SDTPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_by_id**
> Widget get_widget_by_id(id, fields=fields)

get widget by id (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # get widget by id (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.get_widget_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_data_by_id**
> WidgetData get_widget_data_by_id(id, start=start, end=end, format=format)

get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.get_widget_data_by_id(id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**WidgetData**](WidgetData.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_list**
> WidgetPaginationResponse get_widget_list(fields=fields, size=size, offset=offset, filter=filter)

get widget list (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get widget list (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.get_widget_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WidgetPaginationResponse**](WidgetPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_list_by_dashboard_id**
> WidgetPaginationResponse get_widget_list_by_dashboard_id(id, fields=fields, size=size, offset=offset, filter=filter)

get widget list by DashboardId

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get widget list by DashboardId
    api_response = api_instance.get_widget_list_by_dashboard_id(id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_list_by_dashboard_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**WidgetPaginationResponse**](WidgetPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_batch_job**
> object import_batch_job(file)

import batch job via xml

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # import batch job via xml
    api_response = api_instance.import_batch_job(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_batch_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_config_source**
> object import_config_source(file)

import config source via xml

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # import config source via xml
    api_response = api_instance.import_config_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_config_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data_source**
> object import_data_source(file)

import datasource via xml

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # import datasource via xml
    api_response = api_instance.import_data_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_event_source**
> object import_event_source(file)

import eventsource via xml

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # import eventsource via xml
    api_response = api_instance.import_event_source(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_event_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_un_map_module_to_access_group**
> RestMapModuleV3 map_un_map_module_to_access_group(body=body)

Create a mapping of access group & module

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestMapModuleV3() # RestMapModuleV3 |  (optional)

try:
    # Create a mapping of access group & module
    api_response = api_instance.map_un_map_module_to_access_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->map_un_map_module_to_access_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestMapModuleV3**](RestMapModuleV3.md)|  | [optional] 

### Return type

[**RestMapModuleV3**](RestMapModuleV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partition_action**
> LogPartition partition_action(id, action)

Perform an action on a specified log partition

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
action = 'action_example' # str | 

try:
    # Perform an action on a specified log partition
    api_response = api_instance.partition_action(id, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->partition_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **action** | **str**|  | 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_access_group**
> AccessGroup patch_access_group(id, body)

Update access group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AccessGroup() # AccessGroup | 

try:
    # Update access group
    api_response = api_instance.patch_access_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_access_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AccessGroup**](AccessGroup.md)|  | 

### Return type

[**AccessGroup**](AccessGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_admin_by_id**
> Admin patch_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)

update user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Admin() # Admin | 
change_password = false # bool |  (optional) (default to false)
validation_only = false # bool |  (optional) (default to false)

try:
    # update user
    api_response = api_instance.patch_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Admin**](Admin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]
 **validation_only** | **bool**|  | [optional] [default to false]

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alert_rule_by_id**
> AlertRule patch_alert_rule_by_id(id, body)

update alert rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # update alert rule
    api_response = api_instance.patch_alert_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_api_token_by_admin_id**
> APIToken patch_api_token_by_admin_id(admin_id, apitoken_id, body)

update api tokens for a user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 

try:
    # update api tokens for a user
    api_response = api_instance.patch_api_token_by_admin_id(admin_id, apitoken_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_applies_to_function**
> AppliesToFunction patch_applies_to_function(id, body=body, reason=reason, ignore_reference=ignore_reference)

update applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AppliesToFunction() # AppliesToFunction |  (optional)
reason = 'reason_example' # str |  (optional)
ignore_reference = false # bool |  (optional) (default to false)

try:
    # update applies to function
    api_response = api_instance.patch_applies_to_function(id, body=body, reason=reason, ignore_reference=ignore_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_applies_to_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AppliesToFunction**](AppliesToFunction.md)|  | [optional] 
 **reason** | **str**|  | [optional] 
 **ignore_reference** | **bool**|  | [optional] [default to false]

### Return type

[**AppliesToFunction**](AppliesToFunction.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_collector_by_id**
> Collector patch_collector_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)

update collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Collector() # Collector | 
auto_balance_monitored_devices = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update collector
    api_response = api_instance.patch_collector_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Collector**](Collector.md)|  | 
 **auto_balance_monitored_devices** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_collector_group_by_id**
> CollectorGroup patch_collector_group_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)

update collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 
auto_balance_monitored_devices = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update collector group
    api_response = api_instance.patch_collector_group_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 
 **auto_balance_monitored_devices** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_config_source_by_id**
> ConfigSource patch_config_source_by_id(id, body=body, reason=reason)

update config source by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ConfigSource() # ConfigSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update config source by id
    api_response = api_instance.patch_config_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_config_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ConfigSource**](ConfigSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dashboard_by_id**
> Dashboard patch_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)

update dashboard

The template field works only for the POST API

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Dashboard() # Dashboard | 
overwrite_group_fields = false # bool |  (optional) (default to false)

try:
    # update dashboard
    api_response = api_instance.patch_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Dashboard**](Dashboard.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dashboard_group_by_id**
> DashboardGroup patch_dashboard_group_by_id(id, body)

update dashboard group

The template field works only for the POST API

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # update dashboard group
    api_response = api_instance.patch_dashboard_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_datasource_by_id**
> DataSource patch_datasource_by_id(id, body=body, reason=reason, force_unique_identifier=force_unique_identifier, force_restricted_change_key=force_restricted_change_key)

update datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DataSource() # DataSource |  (optional)
reason = 'reason_example' # str |  (optional)
force_unique_identifier = false # bool |  (optional) (default to false)
force_restricted_change_key = 'force_restricted_change_key_example' # str |  (optional)

try:
    # update datasource
    api_response = api_instance.patch_datasource_by_id(id, body=body, reason=reason, force_unique_identifier=force_unique_identifier, force_restricted_change_key=force_restricted_change_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DataSource**](DataSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 
 **force_unique_identifier** | **bool**|  | [optional] [default to false]
 **force_restricted_change_key** | **str**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_default_dashboard**
> object patch_default_dashboard(id, body=body)

update default dashboard

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.RestUserCustomizedDataV3() # RestUserCustomizedDataV3 |  (optional)

try:
    # update default dashboard
    api_response = api_instance.patch_default_dashboard(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_default_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RestUserCustomizedDataV3**](RestUserCustomizedDataV3.md)|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device**
> Device patch_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)

update a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update a device
    api_response = api_instance.patch_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting patch_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)

update device instance alert setting

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceAlertSetting() # DeviceDataSourceInstanceAlertSetting | 

try:
    # update device instance alert setting
    api_response = api_instance.patch_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_by_id**
> DeviceDataSourceInstance patch_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)

update device instance

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device instance
    api_response = api_instance.patch_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup patch_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)

update device datasource instance group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # update device datasource instance group
    api_response = api_instance.patch_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_by_id**
> DeviceGroup patch_device_group_by_id(id, body, op_type=op_type)

update device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device group
    api_response = api_instance.patch_device_group_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig patch_device_group_cluster_alert_conf_by_id(device_group_id, id, body)

Update cluster alert configuration

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Update cluster alert configuration
    api_response = api_instance.patch_device_group_cluster_alert_conf_by_id(device_group_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig patch_device_group_datasource_alert_setting(device_group_id, ds_id, body)

update device group datasource alert setting

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSourceAlertConfig() # DeviceGroupDataSourceAlertConfig | 

try:
    # update device group datasource alert setting
    api_response = api_instance.patch_device_group_datasource_alert_setting(device_group_id, ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **body** | [**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_datasource_by_id**
> DeviceGroupDataSource patch_device_group_datasource_by_id(device_group_id, id, body=body)

update device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSource() # DeviceGroupDataSource |  (optional)

try:
    # update device group datasource
    api_response = api_instance.patch_device_group_datasource_by_id(device_group_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceGroupDataSource**](DeviceGroupDataSource.md)|  | [optional] 

### Return type

[**DeviceGroupDataSource**](DeviceGroupDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_property_by_name**
> EntityProperty patch_device_group_property_by_name(gid, name, body)

update device group property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device group property
    api_response = api_instance.patch_device_group_property_by_name(gid, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_property_by_name**
> EntityProperty patch_device_property_by_name(device_id, name, body)

update device property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device property
    api_response = api_instance.patch_device_property_by_name(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_escalation_chain_by_id**
> EscalatingChain patch_escalation_chain_by_id(id, body)

update escalation chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # update escalation chain
    api_response = api_instance.patch_escalation_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_event_source_by_id**
> EventSource patch_event_source_by_id(id, body=body, reason=reason)

update eventSource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EventSource() # EventSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update eventSource by id
    api_response = api_instance.patch_event_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_event_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EventSource**](EventSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**EventSource**](EventSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_job_monitor**
> BatchJob patch_job_monitor(id, body=body, reason=reason)

Update JobMonitor

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.BatchJob() # BatchJob |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update JobMonitor
    api_response = api_instance.patch_job_monitor(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_job_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**BatchJob**](BatchJob.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_partition**
> LogPartition patch_log_partition(body=body)

Update an existing log partition

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.LogPartition() # LogPartition |  (optional)

try:
    # Update an existing log partition
    api_response = api_instance.patch_log_partition(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogPartition**](LogPartition.md)|  | [optional] 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_source**
> LogSource patch_log_source(id, body=body, reason=reason)

update log source 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.LogSource() # LogSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update log source 
    api_response = api_instance.patch_log_source(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**LogSource**](LogSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**LogSource**](LogSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_netscan**
> Netscan patch_netscan(id, body=body, reason=reason)

update a netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a netscan
    api_response = api_instance.patch_netscan(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Netscan**](Netscan.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_oid**
> RestOidV3 patch_oid(id, body=body)

update a OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RestOidV3() # RestOidV3 |  (optional)

try:
    # update a OID
    api_response = api_instance.patch_oid(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_oid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestOidV3**](RestOidV3.md)|  | [optional] 

### Return type

[**RestOidV3**](RestOidV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_ops_note_by_id**
> OpsNote patch_ops_note_by_id(id, body)

update opsnote

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # update opsnote
    api_response = api_instance.patch_ops_note_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_property_rule**
> PropertyRule patch_property_rule(id, body=body, reason=reason)

update a property rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.PropertyRule() # PropertyRule |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a property rule
    api_response = api_instance.patch_property_rule(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_property_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**PropertyRule**](PropertyRule.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**PropertyRule**](PropertyRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recipient_group_by_id**
> RecipientGroup patch_recipient_group_by_id(id, body)

update recipient group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # update recipient group
    api_response = api_instance.patch_recipient_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_report_by_id**
> ReportBase patch_report_by_id(id, body)

update report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # update report
    api_response = api_instance.patch_report_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_report_group_by_id**
> ReportGroup patch_report_group_by_id(id, body)

update report group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # update report group
    api_response = api_instance.patch_report_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_role_by_id**
> Role patch_role_by_id(id, body)

update role

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Role() # Role | 

try:
    # update role
    api_response = api_instance.patch_role_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sdt_by_id**
> SDT patch_sdt_by_id(id, body)

update SDT (Response may contain extra fields depending upon the type of SDT being updated)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # update SDT (Response may contain extra fields depending upon the type of SDT being updated)
    api_response = api_instance.patch_sdt_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_topology_source**
> TopologySource patch_topology_source(id, body=body, reason=reason)

Update TopologySource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.TopologySource() # TopologySource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update TopologySource
    api_response = api_instance.patch_topology_source(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_topology_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**TopologySource**](TopologySource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**TopologySource**](TopologySource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_by_id**
> Website patch_website_by_id(id, body, op_type=op_type)

update website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Website() # Website | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update website
    api_response = api_instance.patch_website_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Website**](Website.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_group_by_id**
> WebsiteGroup patch_website_group_by_id(id, body, op_type=op_type)

update website group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update website group
    api_response = api_instance.patch_website_group_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_widget_by_id**
> Widget patch_widget_by_id(id, body)

update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.patch_widget_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_auto_discovery_by_device_id**
> object schedule_auto_discovery_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter)

schedule active discovery for a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)

try:
    # schedule active discovery for a device
    api_response = api_instance.schedule_auto_discovery_by_device_id(id, start=start, end=end, netflow_filter=netflow_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->schedule_auto_discovery_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_aws_account**
> RestCloudOkPermissionsV3 test_aws_account(body)

test AWS account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestAwsAccountTestV3() # RestAwsAccountTestV3 | 

try:
    # test AWS account
    api_response = api_instance.test_aws_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->test_aws_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAwsAccountTestV3**](RestAwsAccountTestV3.md)|  | 

### Return type

[**RestCloudOkPermissionsV3**](RestCloudOkPermissionsV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_azure_account**
> RestCloudOkPermissionsV3 test_azure_account(body)

test Azure account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestAzureAccountTestV3() # RestAzureAccountTestV3 | 

try:
    # test Azure account
    api_response = api_instance.test_azure_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->test_azure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAzureAccountTestV3**](RestAzureAccountTestV3.md)|  | 

### Return type

[**RestCloudOkPermissionsV3**](RestCloudOkPermissionsV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gcp_account**
> RestCloudOkPermissionsV3 test_gcp_account(body)

test GCP account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestGcpAccountTestV3() # RestGcpAccountTestV3 | 

try:
    # test GCP account
    api_response = api_instance.test_gcp_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->test_gcp_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestGcpAccountTestV3**](RestGcpAccountTestV3.md)|  | 

### Return type

[**RestCloudOkPermissionsV3**](RestCloudOkPermissionsV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_saa_s_account**
> RestCloudOkPermissionsV3 test_saa_s_account(body)

test SaaS account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestSaaSAccountTestV3() # RestSaaSAccountTestV3 | 

try:
    # test SaaS account
    api_response = api_instance.test_saa_s_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->test_saa_s_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestSaaSAccountTestV3**](RestSaaSAccountTestV3.md)|  | 

### Return type

[**RestCloudOkPermissionsV3**](RestCloudOkPermissionsV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_group**
> AccessGroup update_access_group(id, body)

Update access group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AccessGroup() # AccessGroup | 

try:
    # Update access group
    api_response = api_instance.update_access_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_access_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AccessGroup**](AccessGroup.md)|  | 

### Return type

[**AccessGroup**](AccessGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_by_id**
> Admin update_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)

update user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Admin() # Admin | 
change_password = false # bool |  (optional) (default to false)
validation_only = false # bool |  (optional) (default to false)

try:
    # update user
    api_response = api_instance.update_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_admin_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Admin**](Admin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]
 **validation_only** | **bool**|  | [optional] [default to false]

### Return type

[**Admin**](Admin.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule_by_id**
> AlertRule update_alert_rule_by_id(id, body)

update alert rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AlertRule() # AlertRule | 

try:
    # update alert rule
    api_response = api_instance.update_alert_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_alert_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AlertRule**](AlertRule.md)|  | 

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_token_by_admin_id**
> APIToken update_api_token_by_admin_id(admin_id, apitoken_id, body)

update api tokens for a user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
admin_id = 56 # int | 
apitoken_id = 56 # int | 
body = logicmonitor_sdk.APIToken() # APIToken | 

try:
    # update api tokens for a user
    api_response = api_instance.update_api_token_by_admin_id(admin_id, apitoken_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_api_token_by_admin_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**APIToken**](APIToken.md)|  | 

### Return type

[**APIToken**](APIToken.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_applies_to_function**
> AppliesToFunction update_applies_to_function(id, body=body, reason=reason, ignore_reference=ignore_reference)

update applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.AppliesToFunction() # AppliesToFunction |  (optional)
reason = 'reason_example' # str |  (optional)
ignore_reference = false # bool |  (optional) (default to false)

try:
    # update applies to function
    api_response = api_instance.update_applies_to_function(id, body=body, reason=reason, ignore_reference=ignore_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_applies_to_function: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**AppliesToFunction**](AppliesToFunction.md)|  | [optional] 
 **reason** | **str**|  | [optional] 
 **ignore_reference** | **bool**|  | [optional] [default to false]

### Return type

[**AppliesToFunction**](AppliesToFunction.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_by_id**
> Collector update_collector_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)

update collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Collector() # Collector | 
auto_balance_monitored_devices = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update collector
    api_response = api_instance.update_collector_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Collector**](Collector.md)|  | 
 **auto_balance_monitored_devices** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Collector**](Collector.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_group_by_id**
> CollectorGroup update_collector_group_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)

update collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.CollectorGroup() # CollectorGroup | 
auto_balance_monitored_devices = false # bool |  (optional) (default to false)
force_update_failed_over_devices = false # bool |  (optional) (default to false)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update collector group
    api_response = api_instance.update_collector_group_by_id(id, body, auto_balance_monitored_devices=auto_balance_monitored_devices, force_update_failed_over_devices=force_update_failed_over_devices, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_collector_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**CollectorGroup**](CollectorGroup.md)|  | 
 **auto_balance_monitored_devices** | **bool**|  | [optional] [default to false]
 **force_update_failed_over_devices** | **bool**|  | [optional] [default to false]
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**CollectorGroup**](CollectorGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_source_by_id**
> ConfigSource update_config_source_by_id(id, body=body, reason=reason)

update config source by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ConfigSource() # ConfigSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update config source by id
    api_response = api_instance.update_config_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_config_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ConfigSource**](ConfigSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_by_id**
> Dashboard update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)

update dashboard

The template field works only for the POST API

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Dashboard() # Dashboard | 
overwrite_group_fields = false # bool |  (optional) (default to false)

try:
    # update dashboard
    api_response = api_instance.update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_dashboard_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Dashboard**](Dashboard.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_group_by_id**
> DashboardGroup update_dashboard_group_by_id(id, body)

update dashboard group

The template field works only for the POST API

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DashboardGroup() # DashboardGroup | 

try:
    # update dashboard group
    api_response = api_instance.update_dashboard_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DashboardGroup**](DashboardGroup.md)|  | 

### Return type

[**DashboardGroup**](DashboardGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datasource_by_id**
> DataSource update_datasource_by_id(id, body=body, reason=reason, force_unique_identifier=force_unique_identifier, force_restricted_change_key=force_restricted_change_key)

update datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DataSource() # DataSource |  (optional)
reason = 'reason_example' # str |  (optional)
force_unique_identifier = false # bool |  (optional) (default to false)
force_restricted_change_key = 'force_restricted_change_key_example' # str |  (optional)

try:
    # update datasource
    api_response = api_instance.update_datasource_by_id(id, body=body, reason=reason, force_unique_identifier=force_unique_identifier, force_restricted_change_key=force_restricted_change_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DataSource**](DataSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 
 **force_unique_identifier** | **bool**|  | [optional] [default to false]
 **force_restricted_change_key** | **str**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_dashboard**
> object update_default_dashboard(id, body=body)

update default dashboard

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.RestUserCustomizedDataV3() # RestUserCustomizedDataV3 |  (optional)

try:
    # update default dashboard
    api_response = api_instance.update_default_dashboard(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_default_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RestUserCustomizedDataV3**](RestUserCustomizedDataV3.md)|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)

update a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Device() # Device | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update a device
    api_response = api_instance.update_device(id, body, start=start, end=end, netflow_filter=netflow_filter, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Device**](Device.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_alert_setting_by_id**
> DeviceDataSourceInstanceAlertSetting update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)

update device instance alert setting

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | Device-DataSource ID
instance_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceAlertSetting() # DeviceDataSourceInstanceAlertSetting | 

try:
    # update device instance alert setting
    api_response = api_instance.update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_alert_setting_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| Device-DataSource ID | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**DeviceDataSourceInstanceAlertSetting**](DeviceDataSourceInstanceAlertSetting.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_by_id**
> DeviceDataSourceInstance update_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)

update device instance

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
hds_id = 56 # int | The device-datasource ID
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstance() # DeviceDataSourceInstance | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device instance
    api_response = api_instance.update_device_datasource_instance_by_id(device_id, hds_id, id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**| The device-datasource ID | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)

update device datasource instance group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # update device datasource instance group
    api_response = api_instance.update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **id** | **int**|  | 
 **body** | [**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**DeviceDataSourceInstanceGroup**](DeviceDataSourceInstanceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_by_id**
> DeviceGroup update_device_group_by_id(id, body, op_type=op_type)

update device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroup() # DeviceGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update device group
    api_response = api_instance.update_device_group_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DeviceGroup**](DeviceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**DeviceGroup**](DeviceGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_cluster_alert_conf_by_id**
> DeviceClusterAlertConfig update_device_group_cluster_alert_conf_by_id(device_group_id, id, body)

Update cluster alert configuration

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceClusterAlertConfig() # DeviceClusterAlertConfig | 

try:
    # Update cluster alert configuration
    api_response = api_instance.update_device_group_cluster_alert_conf_by_id(device_group_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_cluster_alert_conf_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)|  | 

### Return type

[**DeviceClusterAlertConfig**](DeviceClusterAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_datasource_alert_setting**
> DeviceGroupDataSourceAlertConfig update_device_group_datasource_alert_setting(device_group_id, ds_id, body)

update device group datasource alert setting

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
ds_id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSourceAlertConfig() # DeviceGroupDataSourceAlertConfig | 

try:
    # update device group datasource alert setting
    api_response = api_instance.update_device_group_datasource_alert_setting(device_group_id, ds_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_datasource_alert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **body** | [**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**DeviceGroupDataSourceAlertConfig**](DeviceGroupDataSourceAlertConfig.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_datasource_by_id**
> DeviceGroupDataSource update_device_group_datasource_by_id(device_group_id, id, body=body)

update device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_group_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceGroupDataSource() # DeviceGroupDataSource |  (optional)

try:
    # update device group datasource
    api_response = api_instance.update_device_group_datasource_by_id(device_group_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**DeviceGroupDataSource**](DeviceGroupDataSource.md)|  | [optional] 

### Return type

[**DeviceGroupDataSource**](DeviceGroupDataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_property_by_name**
> EntityProperty update_device_group_property_by_name(gid, name, body)

update device group property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
gid = 56 # int | group ID
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device group property
    api_response = api_instance.update_device_group_property_by_name(gid, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_group_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**| group ID | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_property_by_name**
> EntityProperty update_device_property_by_name(device_id, name, body)

update device property

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
name = 'name_example' # str | 
body = logicmonitor_sdk.EntityProperty() # EntityProperty | 

try:
    # update device property
    api_response = api_instance.update_device_property_by_name(device_id, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_property_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**EntityProperty**](EntityProperty.md)|  | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_escalation_chain_by_id**
> EscalatingChain update_escalation_chain_by_id(id, body)

update escalation chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EscalatingChain() # EscalatingChain | 

try:
    # update escalation chain
    api_response = api_instance.update_escalation_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_escalation_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EscalatingChain**](EscalatingChain.md)|  | 

### Return type

[**EscalatingChain**](EscalatingChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_source_by_id**
> EventSource update_event_source_by_id(id, body=body, reason=reason)

update eventSource by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.EventSource() # EventSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update eventSource by id
    api_response = api_instance.update_event_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_event_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**EventSource**](EventSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**EventSource**](EventSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_group_alert_threshold**
> object update_instance_group_alert_threshold(device_id, device_ds_id, dsig_id, dp_id, body=body)

update instance group alert threshold (Setting the threshold at default group is not allowed)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_id = 56 # int | 
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
dsig_id = 56 # int | 
dp_id = 56 # int | 
body = logicmonitor_sdk.RestDeviceInstanceGroupAlertConfigV3() # RestDeviceInstanceGroupAlertConfigV3 |  (optional)

try:
    # update instance group alert threshold (Setting the threshold at default group is not allowed)
    api_response = api_instance.update_instance_group_alert_threshold(device_id, device_ds_id, dsig_id, dp_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_instance_group_alert_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **dsig_id** | **int**|  | 
 **dp_id** | **int**|  | 
 **body** | [**RestDeviceInstanceGroupAlertConfigV3**](RestDeviceInstanceGroupAlertConfigV3.md)|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_monitor**
> BatchJob update_job_monitor(id, body=body, reason=reason)

Update JobMonitor

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.BatchJob() # BatchJob |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update JobMonitor
    api_response = api_instance.update_job_monitor(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_job_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**BatchJob**](BatchJob.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_partition**
> LogPartition update_log_partition(body=body)

Update an existing log partition

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.LogPartition() # LogPartition |  (optional)

try:
    # Update an existing log partition
    api_response = api_instance.update_log_partition(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogPartition**](LogPartition.md)|  | [optional] 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_source**
> LogSource update_log_source(id, body=body, reason=reason)

update log source 

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.LogSource() # LogSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update log source 
    api_response = api_instance.update_log_source(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**LogSource**](LogSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**LogSource**](LogSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_netscan**
> Netscan update_netscan(id, body=body, reason=reason)

update a netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Netscan() # Netscan |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a netscan
    api_response = api_instance.update_netscan(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_netscan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Netscan**](Netscan.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**Netscan**](Netscan.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oid**
> RestOidV3 update_oid(id, body=body)

update a OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RestOidV3() # RestOidV3 |  (optional)

try:
    # update a OID
    api_response = api_instance.update_oid(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_oid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestOidV3**](RestOidV3.md)|  | [optional] 

### Return type

[**RestOidV3**](RestOidV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ops_note_by_id**
> OpsNote update_ops_note_by_id(id, body)

update opsnote

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.OpsNote() # OpsNote | 

try:
    # update opsnote
    api_response = api_instance.update_ops_note_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_ops_note_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**OpsNote**](OpsNote.md)|  | 

### Return type

[**OpsNote**](OpsNote.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property_rule**
> PropertyRule update_property_rule(id, body=body, reason=reason)

update a property rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.PropertyRule() # PropertyRule |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # update a property rule
    api_response = api_instance.update_property_rule(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_property_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**PropertyRule**](PropertyRule.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**PropertyRule**](PropertyRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipient_group_by_id**
> RecipientGroup update_recipient_group_by_id(id, body)

update recipient group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.RecipientGroup() # RecipientGroup | 

try:
    # update recipient group
    api_response = api_instance.update_recipient_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_recipient_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RecipientGroup**](RecipientGroup.md)|  | 

### Return type

[**RecipientGroup**](RecipientGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id**
> ReportBase update_report_by_id(id, body)

update report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportBase() # ReportBase | 

try:
    # update report
    api_response = api_instance.update_report_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_report_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportBase**](ReportBase.md)|  | 

### Return type

[**ReportBase**](ReportBase.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_group_by_id**
> ReportGroup update_report_group_by_id(id, body)

update report group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.ReportGroup() # ReportGroup | 

try:
    # update report group
    api_response = api_instance.update_report_group_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_report_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ReportGroup**](ReportGroup.md)|  | 

### Return type

[**ReportGroup**](ReportGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_by_id**
> Role update_role_by_id(id, body)

update role

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Role() # Role | 

try:
    # update role
    api_response = api_instance.update_role_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sdt_by_id**
> SDT update_sdt_by_id(id, body)

update SDT (Response may contain extra fields depending upon the type of SDT being updated)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | 
body = logicmonitor_sdk.SDT() # SDT | 

try:
    # update SDT (Response may contain extra fields depending upon the type of SDT being updated)
    api_response = api_instance.update_sdt_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_sdt_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SDT**](SDT.md)|  | 

### Return type

[**SDT**](SDT.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology_source**
> TopologySource update_topology_source(id, body=body, reason=reason)

Update TopologySource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.TopologySource() # TopologySource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update TopologySource
    api_response = api_instance.update_topology_source(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_topology_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**TopologySource**](TopologySource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**TopologySource**](TopologySource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_by_id**
> Website update_website_by_id(id, body, op_type=op_type)

update website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Website() # Website | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update website
    api_response = api_instance.update_website_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_website_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Website**](Website.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**Website**](Website.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_group_by_id**
> WebsiteGroup update_website_group_by_id(id, body, op_type=op_type)

update website group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.WebsiteGroup() # WebsiteGroup | 
op_type = 'refresh' # str |  (optional) (default to refresh)

try:
    # update website group
    api_response = api_instance.update_website_group_by_id(id, body, op_type=op_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_website_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**WebsiteGroup**](WebsiteGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**WebsiteGroup**](WebsiteGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_widget_by_id**
> Widget update_widget_by_id(id, body)

update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | 
body = logicmonitor_sdk.Widget() # Widget | 

try:
    # update widget (Based upon widget type the request and response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.update_widget_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_widget_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Widget**](Widget.md)|  | 

### Return type

[**Widget**](Widget.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_aws_billing_permissions**
> RestAWSVerifyBillingPermissionsV3 verify_aws_billing_permissions(body)

verify AWS Billing Permissions

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestAwsAccountTestV3() # RestAwsAccountTestV3 | 

try:
    # verify AWS Billing Permissions
    api_response = api_instance.verify_aws_billing_permissions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->verify_aws_billing_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAwsAccountTestV3**](RestAwsAccountTestV3.md)|  | 

### Return type

[**RestAWSVerifyBillingPermissionsV3**](RestAWSVerifyBillingPermissionsV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_storage_accounts_permissions**
> RestResponse verify_storage_accounts_permissions(body)

view storage accounts

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestAzureStorageAccountVerify() # RestAzureStorageAccountVerify | 

try:
    # view storage accounts
    api_response = api_instance.verify_storage_accounts_permissions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->verify_storage_accounts_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAzureStorageAccountVerify**](RestAzureStorageAccountVerify.md)|  | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

