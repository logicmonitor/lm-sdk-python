# logicmonitor_sdk.LMApi

All URIs are relative to */santaba/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alert_by_id**](LMApi.md#ack_alert_by_id) | **POST** /alert/alerts/{id}/ack | Acknowledge alert by ID
[**ack_collector_down_alert_by_id**](LMApi.md#ack_collector_down_alert_by_id) | **POST** /setting/collector/collectors/{id}/ackdown | ack collector down alert
[**add_access_group**](LMApi.md#add_access_group) | **POST** /setting/accessgroup/add | Create a access group
[**add_action_chain**](LMApi.md#add_action_chain) | **POST** /setting/action/chains | Add action chain
[**add_action_rule**](LMApi.md#add_action_rule) | **POST** /setting/action/rules | Add Action Rule
[**add_admin**](LMApi.md#add_admin) | **POST** /setting/admins | add user
[**add_alert_note_by_id**](LMApi.md#add_alert_note_by_id) | **POST** /alert/alerts/{id}/note | Add alert note
[**add_alert_rule**](LMApi.md#add_alert_rule) | **POST** /setting/alert/rules | add alert rule
[**add_api_token_by_admin_id**](LMApi.md#add_api_token_by_admin_id) | **POST** /setting/admins/{adminId}/apitokens | Add API tokens for a user
[**add_applies_to_function**](LMApi.md#add_applies_to_function) | **POST** /setting/functions | Add applies to function
[**add_collector**](LMApi.md#add_collector) | **POST** /setting/collector/collectors | add collector
[**add_collector_group**](LMApi.md#add_collector_group) | **POST** /setting/collector/groups | Add collector group
[**add_config_source**](LMApi.md#add_config_source) | **POST** /setting/configsources | Add a new config source
[**add_dashboard**](LMApi.md#add_dashboard) | **POST** /dashboard/dashboards | add dashboard
[**add_dashboard_group**](LMApi.md#add_dashboard_group) | **POST** /dashboard/groups | add dashboard group
[**add_dashboard_group_asynchronously**](LMApi.md#add_dashboard_group_asynchronously) | **POST** /dashboard/groups/{id}/asyncclone | add dashboard group asynchronously
[**add_datasource_by_id**](LMApi.md#add_datasource_by_id) | **POST** /setting/datasources | Add datasource
[**add_device**](LMApi.md#add_device) | **POST** /device/devices | add a new device (Request schema may change depending upon the type of uptime device being added)
[**add_device_datasource_instance**](LMApi.md#add_device_datasource_instance) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | add device instance
[**add_device_datasource_instance_group**](LMApi.md#add_device_datasource_instance_group) | **POST** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | Add device datasource instance group
[**add_device_group**](LMApi.md#add_device_group) | **POST** /device/groups | add device group
[**add_device_group_cluster_alert_conf**](LMApi.md#add_device_group_cluster_alert_conf) | **POST** /device/groups/{deviceGroupId}/clusterAlertConf | Add cluster alert configuration
[**add_device_group_property**](LMApi.md#add_device_group_property) | **POST** /device/groups/{gid}/properties | Add device group property
[**add_device_property**](LMApi.md#add_device_property) | **POST** /device/devices/{deviceId}/properties | Add device property
[**add_diagnostic_source**](LMApi.md#add_diagnostic_source) | **POST** /setting/diagnosticsources | Add diagnostics source
[**add_dns_mapping**](LMApi.md#add_dns_mapping) | **POST** /setting/dnsmappings | Add DNS mapping
[**add_escalation_chain**](LMApi.md#add_escalation_chain) | **POST** /setting/alert/chains | Add escalation chain
[**add_event_source**](LMApi.md#add_event_source) | **POST** /setting/eventsources | Add event source
[**add_job_monitor**](LMApi.md#add_job_monitor) | **POST** /setting/batchjobs | Add JobMonitor
[**add_log_alert_group**](LMApi.md#add_log_alert_group) | **POST** /logpipelines | Add a new LogAlertGroup
[**add_log_alerts**](LMApi.md#add_log_alerts) | **POST** /logpipelines/processors | Add a new LogAlerts
[**add_log_query_group**](LMApi.md#add_log_query_group) | **POST** /log/logquerygroups | Create a new log query group
[**add_log_source**](LMApi.md#add_log_source) | **POST** /setting/logsources | Add log source
[**add_netscan**](LMApi.md#add_netscan) | **POST** /setting/netscans | Add a new netscan
[**add_oid**](LMApi.md#add_oid) | **POST** /setting/oids | Add a new OID
[**add_ops_note**](LMApi.md#add_ops_note) | **POST** /setting/opsnotes | add opsnote
[**add_property_rule**](LMApi.md#add_property_rule) | **POST** /setting/propertyrules | Add a new property rule
[**add_recipient_group**](LMApi.md#add_recipient_group) | **POST** /setting/recipientgroups | Add recipient group
[**add_remediation_source**](LMApi.md#add_remediation_source) | **POST** /setting/remediationsources | Add remediation source
[**add_report**](LMApi.md#add_report) | **POST** /report/reports | Add report
[**add_report_group**](LMApi.md#add_report_group) | **POST** /report/groups | Add report group
[**add_role**](LMApi.md#add_role) | **POST** /setting/roles | Add role
[**add_sdt**](LMApi.md#add_sdt) | **POST** /sdt/sdts | add SDT (Response may contain extra fields depending upon the type of SDT being added)
[**add_topology_source**](LMApi.md#add_topology_source) | **POST** /setting/topologysources | Add TopologySource
[**add_website**](LMApi.md#add_website) | **POST** /website/websites | Add website
[**add_website_group**](LMApi.md#add_website_group) | **POST** /website/groups | add website group
[**add_widget**](LMApi.md#add_widget) | **POST** /dashboard/widgets | Add widget
[**batch_update_collector_agent_log_levels**](LMApi.md#batch_update_collector_agent_log_levels) | **PUT** /setting/collector/collectors/{id}/agentloglevels | batch update collector agent log levels
[**calculate_sizing**](LMApi.md#calculate_sizing) | **POST** /setting/collector/sizing | Calculate collector sizing recommendations
[**collect_device_config_source_config**](LMApi.md#collect_device_config_source_config) | **POST** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/configCollection | collect a config for a device
[**create_log_partition**](LMApi.md#create_log_partition) | **POST** /log/partitions | Create a new log partition
[**create_tracked_query_group**](LMApi.md#create_tracked_query_group) | **POST** /trackedquerygroups | Create tracked query group
[**delete_access_group**](LMApi.md#delete_access_group) | **DELETE** /setting/accessgroup/{id} | Delete access group
[**delete_action_chain_by_id**](LMApi.md#delete_action_chain_by_id) | **DELETE** /setting/action/chains/{id} | delete action chain 
[**delete_action_rule_by_id**](LMApi.md#delete_action_rule_by_id) | **DELETE** /setting/action/rules/{id} | delete action rule
[**delete_admin_by_id**](LMApi.md#delete_admin_by_id) | **DELETE** /setting/admins/{id} | delete user
[**delete_alert_rule_by_id**](LMApi.md#delete_alert_rule_by_id) | **DELETE** /setting/alert/rules/{id} | delete alert rule
[**delete_api_token_by_id**](LMApi.md#delete_api_token_by_id) | **DELETE** /setting/admins/{adminId}/apitokens/{apitokenId} | Delete API token
[**delete_applies_to_function_by_id**](LMApi.md#delete_applies_to_function_by_id) | **DELETE** /setting/functions/{id} | Delete applies to function
[**delete_collector_by_id**](LMApi.md#delete_collector_by_id) | **DELETE** /setting/collector/collectors/{id} | delete collector
[**delete_collector_group_by_id**](LMApi.md#delete_collector_group_by_id) | **DELETE** /setting/collector/groups/{id} | Delete collector group
[**delete_config_source_by_id**](LMApi.md#delete_config_source_by_id) | **DELETE** /setting/configsources/{id} | Delete config source by ID
[**delete_dashboard_by_id**](LMApi.md#delete_dashboard_by_id) | **DELETE** /dashboard/dashboards/{id} | delete dashboard
[**delete_dashboard_group_by_id**](LMApi.md#delete_dashboard_group_by_id) | **DELETE** /dashboard/groups/{id} | delete dashboard group
[**delete_datasource_by_id**](LMApi.md#delete_datasource_by_id) | **DELETE** /setting/datasources/{id} | Delete datasource
[**delete_device_by_id**](LMApi.md#delete_device_by_id) | **DELETE** /device/devices/{id} | delete a device
[**delete_device_datasource_instance_by_id**](LMApi.md#delete_device_datasource_instance_by_id) | **DELETE** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | delete a device instance
[**delete_device_group_by_id**](LMApi.md#delete_device_group_by_id) | **DELETE** /device/groups/{id} | delete device group
[**delete_device_group_cluster_alert_conf_by_id**](LMApi.md#delete_device_group_cluster_alert_conf_by_id) | **DELETE** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Delete cluster alert configuration
[**delete_device_group_property_by_name**](LMApi.md#delete_device_group_property_by_name) | **DELETE** /device/groups/{gid}/properties/{name} | Delete device group property
[**delete_device_property_by_name**](LMApi.md#delete_device_property_by_name) | **DELETE** /device/devices/{deviceId}/properties/{name} | Delete device property
[**delete_diagnostic_source_by_id**](LMApi.md#delete_diagnostic_source_by_id) | **DELETE** /setting/diagnosticsources/{id} | Delete a diagnostic source module
[**delete_escalation_chain_by_id**](LMApi.md#delete_escalation_chain_by_id) | **DELETE** /setting/alert/chains/{id} | Delete escalation chain
[**delete_event_source_by_id**](LMApi.md#delete_event_source_by_id) | **DELETE** /setting/eventsources/{id} | Delete event source by ID
[**delete_job_monitor**](LMApi.md#delete_job_monitor) | **DELETE** /setting/batchjobs/{id} | Delete JobMonitor
[**delete_log_alert_group**](LMApi.md#delete_log_alert_group) | **DELETE** /logpipelines/{pipelineId} | Delete a specific LogAlertGroup by ID
[**delete_log_alerts_by_id**](LMApi.md#delete_log_alerts_by_id) | **DELETE** /logpipelines/processors/{processorId} | Delete a LogAlerts by ID
[**delete_log_partition_by_id**](LMApi.md#delete_log_partition_by_id) | **DELETE** /log/partitions/{id} | Delete a log partition by ID
[**delete_log_query_group**](LMApi.md#delete_log_query_group) | **DELETE** /log/logquerygroups/{id} | Delete log query group
[**delete_log_source**](LMApi.md#delete_log_source) | **DELETE** /setting/logsources/{id} | Delete log source
[**delete_netscan_by_id**](LMApi.md#delete_netscan_by_id) | **DELETE** /setting/netscans/{id} | Delete a netscan
[**delete_oid**](LMApi.md#delete_oid) | **DELETE** /setting/oids/{id} | Delete an OID
[**delete_ops_note_by_id**](LMApi.md#delete_ops_note_by_id) | **DELETE** /setting/opsnotes/{id} | delete opsnote
[**delete_property_rule**](LMApi.md#delete_property_rule) | **DELETE** /setting/propertyrules/{id} | delete a property rule
[**delete_recipient_group_by_id**](LMApi.md#delete_recipient_group_by_id) | **DELETE** /setting/recipientgroups/{id} | Delete recipient group
[**delete_remediation_source_by_id**](LMApi.md#delete_remediation_source_by_id) | **DELETE** /setting/remediationsources/{id} | Delete a remediation source module
[**delete_report_by_id**](LMApi.md#delete_report_by_id) | **DELETE** /report/reports/{id} | Delete report
[**delete_report_group_by_id**](LMApi.md#delete_report_group_by_id) | **DELETE** /report/groups/{id} | Delete report group
[**delete_role_by_id**](LMApi.md#delete_role_by_id) | **DELETE** /setting/roles/{id} | Delete role
[**delete_sdt_by_id**](LMApi.md#delete_sdt_by_id) | **DELETE** /sdt/sdts/{id} | delete SDT
[**delete_topology_source**](LMApi.md#delete_topology_source) | **DELETE** /setting/topologysources/{id} | Delete TopologySource
[**delete_tracked_query_group**](LMApi.md#delete_tracked_query_group) | **DELETE** /trackedquerygroups/{id} | Delete tracked query group
[**delete_website_by_id**](LMApi.md#delete_website_by_id) | **DELETE** /website/websites/{id} | delete website
[**delete_website_group_by_id**](LMApi.md#delete_website_group_by_id) | **DELETE** /website/groups/{id} | delete website group
[**delete_widget_by_id**](LMApi.md#delete_widget_by_id) | **DELETE** /dashboard/widgets/{id} | Delete widget
[**discover_subscriptions**](LMApi.md#discover_subscriptions) | **POST** /azure/functions/discoverSubscriptions | view subscriptions
[**escalated_alert_by_id**](LMApi.md#escalated_alert_by_id) | **POST** /alert/alerts/{id}/escalate | Escalate alert by ID
[**execute_debug_command**](LMApi.md#execute_debug_command) | **POST** /debug | Execute a Collector debug command
[**execute_diagnostics_manually**](LMApi.md#execute_diagnostics_manually) | **POST** /setting/diagnosticsources/executemanually | Trigger a diagnostic module for host.
[**execute_remediation_manually**](LMApi.md#execute_remediation_manually) | **POST** /setting/remediationsources/executemanually | Trigger a remediation module for host.
[**fetch_device_instances_data**](LMApi.md#fetch_device_instances_data) | **POST** /device/instances/datafetch | Fetch device instances data
[**fetch_report_using_task_id**](LMApi.md#fetch_report_using_task_id) | **GET** /report/reports/{id}/tasks/{taskId} | Get report for task ID
[**generate_report_by_id**](LMApi.md#generate_report_by_id) | **POST** /report/reports/{id}/executions | Run a report
[**get_access_group_by_id**](LMApi.md#get_access_group_by_id) | **GET** /setting/accessgroup/{id} | Get access group by id
[**get_access_group_list**](LMApi.md#get_access_group_list) | **GET** /setting/accessgroup | Get access group list
[**get_action_chain_by_id**](LMApi.md#get_action_chain_by_id) | **GET** /setting/action/chains/{id} | Get action chain by ID
[**get_action_chains_list**](LMApi.md#get_action_chains_list) | **GET** /setting/action/chains | Get action chains list
[**get_action_rule_by_id**](LMApi.md#get_action_rule_by_id) | **GET** /setting/action/rules/{id} | get action rule
[**get_action_rule_status_by_id**](LMApi.md#get_action_rule_status_by_id) | **GET** /setting/action/rules/{id}/status | get action rule status
[**get_action_rules_list**](LMApi.md#get_action_rules_list) | **GET** /setting/action/rules | Get action rules list
[**get_admin_by_id**](LMApi.md#get_admin_by_id) | **GET** /setting/admins/{id} | get user
[**get_admin_list**](LMApi.md#get_admin_list) | **GET** /setting/admins | get user list
[**get_alert_by_id**](LMApi.md#get_alert_by_id) | **GET** /alert/alerts/{id} | get alert
[**get_alert_list**](LMApi.md#get_alert_list) | **GET** /alert/alerts | Get alert list
[**get_alert_list_by_device_group_id**](LMApi.md#get_alert_list_by_device_group_id) | **GET** /device/groups/{id}/alerts | get device group alerts
[**get_alert_list_by_device_id**](LMApi.md#get_alert_list_by_device_id) | **GET** /device/devices/{id}/alerts | get alerts
[**get_alert_rule_by_id**](LMApi.md#get_alert_rule_by_id) | **GET** /setting/alert/rules/{id} | get alert rule by id
[**get_alert_rule_list**](LMApi.md#get_alert_rule_list) | **GET** /setting/alert/rules | get alert rule list
[**get_all_log_partitions**](LMApi.md#get_all_log_partitions) | **GET** /log/partitions | Retrieve a list of all log partitions
[**get_all_sdt_list_by_device_id**](LMApi.md#get_all_sdt_list_by_device_id) | **GET** /device/devices/{id}/sdts | get SDTs for a device
[**get_all_sdt_list_by_website_group_id**](LMApi.md#get_all_sdt_list_by_website_group_id) | **GET** /website/groups/{id}/sdts | get a list of SDTs for a website group (Response may contain extra fields depending upon the type of SDT)
[**get_api_token_list**](LMApi.md#get_api_token_list) | **GET** /setting/admins/apitokens | Get a list of API tokens across users
[**get_api_token_list_by_admin_id**](LMApi.md#get_api_token_list_by_admin_id) | **GET** /setting/admins/{adminId}/apitokens | Get API tokens for a user
[**get_applies_to_function_by_id**](LMApi.md#get_applies_to_function_by_id) | **GET** /setting/functions/{id} | Get applies to function by ID
[**get_applies_to_function_list**](LMApi.md#get_applies_to_function_list) | **GET** /setting/functions | Get applies to function list
[**get_associated_device_list_by_data_source_id**](LMApi.md#get_associated_device_list_by_data_source_id) | **GET** /setting/datasources/{id}/devices | Get devices associated with a datasource
[**get_audit_log_by_id**](LMApi.md#get_audit_log_by_id) | **GET** /setting/accesslogs/{id} | Get audit log by id
[**get_audit_log_list**](LMApi.md#get_audit_log_list) | **GET** /setting/accesslogs | Get audit logs
[**get_aws_account_id**](LMApi.md#get_aws_account_id) | **GET** /aws/accountId | Get AWS account ID
[**get_aws_external_id**](LMApi.md#get_aws_external_id) | **GET** /aws/externalId | Get AWS external ID
[**get_collector_agent_log_level_by_component**](LMApi.md#get_collector_agent_log_level_by_component) | **GET** /setting/collector/collectors/{id}/agentloglevels/{component} | get collector agent log level by component
[**get_collector_agent_log_levels**](LMApi.md#get_collector_agent_log_levels) | **GET** /setting/collector/collectors/{id}/agentloglevels | get collector agent log levels
[**get_collector_by_id**](LMApi.md#get_collector_by_id) | **GET** /setting/collector/collectors/{id} | get collector
[**get_collector_download_token_by_id**](LMApi.md#get_collector_download_token_by_id) | **GET** /setting/collector/collectors/{id}/downloadToken | get collector download token
[**get_collector_events**](LMApi.md#get_collector_events) | **GET** /setting/collector/collectors/{collectorId}/events | get collector events
[**get_collector_group_by_id**](LMApi.md#get_collector_group_by_id) | **GET** /setting/collector/groups/{id} | Get collector group
[**get_collector_group_list**](LMApi.md#get_collector_group_list) | **GET** /setting/collector/groups | Get collector group list
[**get_collector_installer**](LMApi.md#get_collector_installer) | **GET** /setting/collector/collectors/{collectorId}/installers/{osAndArch} | get collector installer
[**get_collector_list**](LMApi.md#get_collector_list) | **GET** /setting/collector/collectors | get collector list
[**get_collector_log_file_by_name**](LMApi.md#get_collector_log_file_by_name) | **GET** /setting/collector/collectors/{collectorId}/logs/{fileName} | get collector log file
[**get_collector_log_files**](LMApi.md#get_collector_log_files) | **GET** /setting/collector/collectors/{collectorId}/logs | get collector log files
[**get_collector_status_check**](LMApi.md#get_collector_status_check) | **GET** /setting/collector/collectors/{collectorId}/services/getStatusCheck | get collector status check
[**get_collector_upgrade_history**](LMApi.md#get_collector_upgrade_history) | **GET** /setting/collector/collectors/upgradeHistory | get collector upgrade history list
[**get_collector_version_list**](LMApi.md#get_collector_version_list) | **GET** /setting/collector/collectors/versions | get collector version list
[**get_collectors_by_group_id**](LMApi.md#get_collectors_by_group_id) | **GET** /setting/collector/groups/{id}/collectors | get collectors by collector group id
[**get_config_source_by_id**](LMApi.md#get_config_source_by_id) | **GET** /setting/configsources/{id} | Get config source by ID
[**get_config_source_list**](LMApi.md#get_config_source_list) | **GET** /setting/configsources | Get config source list
[**get_contract_info_by_company**](LMApi.md#get_contract_info_by_company) | **GET** /usage/contractInfo | get contract info by company
[**get_dashboard_by_id**](LMApi.md#get_dashboard_by_id) | **GET** /dashboard/dashboards/{id} | get dashboard
[**get_dashboard_group_by_id**](LMApi.md#get_dashboard_group_by_id) | **GET** /dashboard/groups/{id} | Get dashboard group by ID
[**get_dashboard_group_list**](LMApi.md#get_dashboard_group_list) | **GET** /dashboard/groups | get dashboard group list
[**get_dashboard_list**](LMApi.md#get_dashboard_list) | **GET** /dashboard/dashboards | Get dashboard list
[**get_data_source_overview_graph_by_id**](LMApi.md#get_data_source_overview_graph_by_id) | **GET** /setting/datasources/{dsId}/ographs/{id} | Get datasource overview graph by ID
[**get_data_source_overview_graph_list**](LMApi.md#get_data_source_overview_graph_list) | **GET** /setting/datasources/{dsId}/ographs | Get datasource overview graph list
[**get_datasource_by_id**](LMApi.md#get_datasource_by_id) | **GET** /setting/datasources/{id} | Get datasource by ID
[**get_datasource_list**](LMApi.md#get_datasource_list) | **GET** /setting/datasources | Get datasource list
[**get_debug_command_result**](LMApi.md#get_debug_command_result) | **GET** /debug/{id} | Get the result of a Collector debug command using sessionId
[**get_delta_devices**](LMApi.md#get_delta_devices) | **GET** /device/devices/delta/{deltaId} | Get delta devices using deltaId
[**get_delta_id_with_devices**](LMApi.md#get_delta_id_with_devices) | **GET** /device/devices/delta | Get filter matched devices with new deltaId
[**get_device_by_id**](LMApi.md#get_device_by_id) | **GET** /device/devices/{id} | get device by id
[**get_device_config_source_config_by_id**](LMApi.md#get_device_config_source_config_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config/{id} | get a config for a device
[**get_device_config_source_config_list**](LMApi.md#get_device_config_source_config_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/config | get detailed config information for the instance
[**get_device_datasource_by_id**](LMApi.md#get_device_datasource_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id} | Get device datasource
[**get_device_datasource_data_by_id**](LMApi.md#get_device_datasource_data_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/data | Get device datasource data
[**get_device_datasource_instance_alert_setting_by_id**](LMApi.md#get_device_datasource_instance_alert_setting_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | get device instance alert setting
[**get_device_datasource_instance_alert_setting_list_of_device**](LMApi.md#get_device_datasource_instance_alert_setting_list_of_device) | **GET** /device/devices/{deviceId}/alertsettings | get a list of alert settings for a device
[**get_device_datasource_instance_alert_setting_list_of_dsi**](LMApi.md#get_device_datasource_instance_alert_setting_list_of_dsi) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings | get a list of alert settings for a device datasource instance
[**get_device_datasource_instance_by_id**](LMApi.md#get_device_datasource_instance_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | get device instance
[**get_device_datasource_instance_data**](LMApi.md#get_device_datasource_instance_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/data | get device instance data
[**get_device_datasource_instance_graph_data**](LMApi.md#get_device_datasource_instance_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/graphs/{graphId}/data | get device instance graph data
[**get_device_datasource_instance_group_by_id**](LMApi.md#get_device_datasource_instance_group_by_id) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | Get device datasource instance group
[**get_device_datasource_instance_group_list**](LMApi.md#get_device_datasource_instance_group_list) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups | Get device datasource instance group list
[**get_device_datasource_instance_group_overview_graph_data**](LMApi.md#get_device_datasource_instance_group_overview_graph_data) | **GET** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/graphs/{ographId}/data | Get device instance group overview graph data
[**get_device_datasource_instance_list**](LMApi.md#get_device_datasource_instance_list) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances | get device instance list
[**get_device_datasource_instance_sdt_history**](LMApi.md#get_device_datasource_instance_sdt_history) | **GET** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id}/historysdts | get device instance SDT history
[**get_device_datasource_list**](LMApi.md#get_device_datasource_list) | **GET** /device/devices/{deviceId}/devicedatasources | Get device datasource list
[**get_device_eventsource_list**](LMApi.md#get_device_eventsource_list) | **GET** /device/devices/{deviceId}/deviceeventsources | Get device eventsource list
[**get_device_group_by_id**](LMApi.md#get_device_group_by_id) | **GET** /device/groups/{id} | get device group
[**get_device_group_cluster_alert_conf_by_id**](LMApi.md#get_device_group_cluster_alert_conf_by_id) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Get cluster alert configuration by id
[**get_device_group_cluster_alert_conf_list**](LMApi.md#get_device_group_cluster_alert_conf_list) | **GET** /device/groups/{deviceGroupId}/clusterAlertConf | get a list of cluster alert configurations for a device group
[**get_device_group_datasource_alert_setting**](LMApi.md#get_device_group_datasource_alert_setting) | **GET** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | Get device group datasource alert setting
[**get_device_group_datasource_by_id**](LMApi.md#get_device_group_datasource_by_id) | **GET** /device/groups/{deviceGroupId}/datasources/{id} | get device group datasource
[**get_device_group_datasource_list**](LMApi.md#get_device_group_datasource_list) | **GET** /device/groups/{deviceGroupId}/datasources | get device group datasource list
[**get_device_group_list**](LMApi.md#get_device_group_list) | **GET** /device/groups | get device group list
[**get_device_group_property_by_name**](LMApi.md#get_device_group_property_by_name) | **GET** /device/groups/{gid}/properties/{name} | Get device group property by name
[**get_device_group_property_list**](LMApi.md#get_device_group_property_list) | **GET** /device/groups/{gid}/properties | Get device group properties
[**get_device_group_sdt_list**](LMApi.md#get_device_group_sdt_list) | **GET** /device/groups/{id}/sdts | get device group SDTs
[**get_device_instance_graph_data_only_by_instance_id**](LMApi.md#get_device_instance_graph_data_only_by_instance_id) | **GET** /device/devicedatasourceinstances/{instanceId}/graphs/{graphId}/data | get device instance data
[**get_device_instance_list**](LMApi.md#get_device_instance_list) | **GET** /device/devices/{id}/instances | get device instance list
[**get_device_list**](LMApi.md#get_device_list) | **GET** /device/devices | Get device list
[**get_device_property_by_name**](LMApi.md#get_device_property_by_name) | **GET** /device/devices/{deviceId}/properties/{name} | Get device property by name
[**get_device_property_list**](LMApi.md#get_device_property_list) | **GET** /device/devices/{deviceId}/properties | Get device properties
[**get_diagnostic_remediation_assigned_sources**](LMApi.md#get_diagnostic_remediation_assigned_sources) | **GET** /setting/diagnosticRemediation/list | List assigned diagnostic and remediation exchange modules
[**get_diagnostic_remediation_execution_results**](LMApi.md#get_diagnostic_remediation_execution_results) | **GET** /setting/diagnosticRemediation/executionResults | Get diagnostic and remediation execution results (canonical)
[**get_diagnostic_sources_by_id**](LMApi.md#get_diagnostic_sources_by_id) | **GET** /setting/diagnosticsources/{id} | Get diagnostics sources by ID
[**get_diagnostic_sources_list**](LMApi.md#get_diagnostic_sources_list) | **GET** /setting/diagnosticsources | Get diagnostics sources list
[**get_escalation_chain_by_id**](LMApi.md#get_escalation_chain_by_id) | **GET** /setting/alert/chains/{id} | Get escalation chain by ID
[**get_escalation_chain_list**](LMApi.md#get_escalation_chain_list) | **GET** /setting/alert/chains | Get escalation chain list
[**get_event_source_by_id**](LMApi.md#get_event_source_by_id) | **GET** /setting/eventsources/{id} | Get event source by ID
[**get_event_source_list**](LMApi.md#get_event_source_list) | **GET** /setting/eventsources | Get event source list
[**get_external_api_stats**](LMApi.md#get_external_api_stats) | **GET** /apiStats/externalApis | get external api stats info
[**get_focus_cost_usage**](LMApi.md#get_focus_cost_usage) | **GET** /usage/focusCostUsage | FOCUS Cost and Usage shaped usage export
[**get_immediate_device_list_by_device_group_id**](LMApi.md#get_immediate_device_list_by_device_group_id) | **GET** /device/groups/{id}/devices | get immediate devices under group
[**get_immediate_website_list_by_website_group_id**](LMApi.md#get_immediate_website_list_by_website_group_id) | **GET** /website/groups/{id}/websites | get a list of websites for a group (Response may contain extra fields depending upon the type of check { PingCheck | WebCheck} being added)
[**get_integration_audit_logs**](LMApi.md#get_integration_audit_logs) | **GET** /setting/integrations/auditlogs | Get integration audit logs list
[**get_job_monitor_by_id**](LMApi.md#get_job_monitor_by_id) | **GET** /setting/batchjobs/{id} | Get JobMonitor by ID
[**get_job_monitor_list**](LMApi.md#get_job_monitor_list) | **GET** /setting/batchjobs | Get JobMonitor List
[**get_log_alert_group_by_id**](LMApi.md#get_log_alert_group_by_id) | **GET** /logpipelines/{pipelineId} | Retrieve a LogAlertGroup by ID
[**get_log_alert_groups_list**](LMApi.md#get_log_alert_groups_list) | **GET** /logpipelines | Retrieve all LogAlertGroups
[**get_log_alerts**](LMApi.md#get_log_alerts) | **GET** /logpipelines/processors | Retrieve all LogAlerts
[**get_log_alerts_by_id**](LMApi.md#get_log_alerts_by_id) | **GET** /logpipelines/processors/{processorId} | Retrieve a LogAlerts by ID
[**get_log_queries_by_group_id**](LMApi.md#get_log_queries_by_group_id) | **GET** /log/logquerygroups/{id}/logqueries | Get log queries by group ID
[**get_log_query_group_by_id**](LMApi.md#get_log_query_group_by_id) | **GET** /log/logquerygroups/{id} | Get log query group by ID
[**get_log_query_group_list**](LMApi.md#get_log_query_group_list) | **GET** /log/logquerygroups | Get log query group list
[**get_log_query_group_list_by_group_type**](LMApi.md#get_log_query_group_list_by_group_type) | **GET** /log/logquerygroups/grouptype/{groupType} | Get log query groups by groupType
[**get_log_source_by_id**](LMApi.md#get_log_source_by_id) | **GET** /setting/logsources/{id} | Get log source
[**get_log_source_list**](LMApi.md#get_log_source_list) | **GET** /setting/logsources | Get log source list
[**get_metrics_summary**](LMApi.md#get_metrics_summary) | **GET** /metrics/summary | get metrics usage with company settings summary
[**get_metrics_usage**](LMApi.md#get_metrics_usage) | **GET** /metrics/usage | Get metrics usage
[**get_netflow_endpoint_list**](LMApi.md#get_netflow_endpoint_list) | **GET** /device/devices/{id}/endpoints | get netflow endpoints
[**get_netflow_flow_list**](LMApi.md#get_netflow_flow_list) | **GET** /device/devices/{id}/flows | get netflow flows
[**get_netflow_port_list**](LMApi.md#get_netflow_port_list) | **GET** /device/devices/{id}/ports | get netflow ports
[**get_netscan_by_id**](LMApi.md#get_netscan_by_id) | **GET** /setting/netscans/{id} | Get netscan by ID
[**get_netscan_list**](LMApi.md#get_netscan_list) | **GET** /setting/netscans | Get netscan list
[**get_oid_by_id**](LMApi.md#get_oid_by_id) | **GET** /setting/oids/{id} | Get OID by ID
[**get_oid_list**](LMApi.md#get_oid_list) | **GET** /setting/oids | Get OID&#x27;s list
[**get_ops_note_by_id**](LMApi.md#get_ops_note_by_id) | **GET** /setting/opsnotes/{id} | get opsnote by id
[**get_ops_note_list**](LMApi.md#get_ops_note_list) | **GET** /setting/opsnotes | get opsnote list
[**get_partition_by_id**](LMApi.md#get_partition_by_id) | **GET** /log/partitions/{id} | Retrieve details of a specific log partition
[**get_property_rules_by_id**](LMApi.md#get_property_rules_by_id) | **GET** /setting/propertyrules/{id} | Get property rules by id
[**get_property_rules_list**](LMApi.md#get_property_rules_list) | **GET** /setting/propertyrules | Get property rules list
[**get_recipient_group_by_id**](LMApi.md#get_recipient_group_by_id) | **GET** /setting/recipientgroups/{id} | Get recipient group by id
[**get_recipient_group_list**](LMApi.md#get_recipient_group_list) | **GET** /setting/recipientgroups | Get recipient group list
[**get_recommendation_by_id**](LMApi.md#get_recommendation_by_id) | **GET** /cost-optimization/recommendations/{id} | Get recommendation by ID
[**get_recommendation_categories_list**](LMApi.md#get_recommendation_categories_list) | **GET** /cost-optimization/recommendations/categories | Get recommendation category list
[**get_recommendations_list**](LMApi.md#get_recommendations_list) | **GET** /cost-optimization/recommendations | Get recommendation list
[**get_remediation_sources_by_id**](LMApi.md#get_remediation_sources_by_id) | **GET** /setting/remediationsources/{id} | Get remediation sources by ID
[**get_remediation_sources_list**](LMApi.md#get_remediation_sources_list) | **GET** /setting/remediationsources | Get remediation sources list
[**get_report_by_id**](LMApi.md#get_report_by_id) | **GET** /report/reports/{id} | Get report by ID
[**get_report_group_by_id**](LMApi.md#get_report_group_by_id) | **GET** /report/groups/{id} | Get report group by id
[**get_report_group_list**](LMApi.md#get_report_group_list) | **GET** /report/groups | Get report group list
[**get_report_list**](LMApi.md#get_report_list) | **GET** /report/reports | Get report list
[**get_retention_list**](LMApi.md#get_retention_list) | **GET** /log/partitions/retentions | Retrieve the list of log retentions
[**get_role_by_id**](LMApi.md#get_role_by_id) | **GET** /setting/roles/{id} | Get role by ID
[**get_role_list**](LMApi.md#get_role_list) | **GET** /setting/roles | Get role list
[**get_sdt_by_id**](LMApi.md#get_sdt_by_id) | **GET** /sdt/sdts/{id} | get SDT by id (Response may contain extra fields depending upon the type of SDT of given id)
[**get_sdt_history_by_device_data_source_id**](LMApi.md#get_sdt_history_by_device_data_source_id) | **GET** /device/devices/{deviceId}/devicedatasources/{id}/historysdts | Get SDT history for the device dataSource
[**get_sdt_history_by_device_group_id**](LMApi.md#get_sdt_history_by_device_group_id) | **GET** /device/groups/{id}/historysdts | get SDT history for the group
[**get_sdt_history_by_device_id**](LMApi.md#get_sdt_history_by_device_id) | **GET** /device/devices/{id}/historysdts | get SDT history for the device
[**get_sdt_history_by_website_group_id**](LMApi.md#get_sdt_history_by_website_group_id) | **GET** /website/groups/{id}/historysdts | get SDT history for the website group (Response may contain extra fields depending upon the type of SDT)
[**get_sdt_history_by_website_id**](LMApi.md#get_sdt_history_by_website_id) | **GET** /website/websites/{id}/historysdts | get SDT history for the website (Response may contain extra fields depending upon the type of SDT)
[**get_sdt_list**](LMApi.md#get_sdt_list) | **GET** /sdt/sdts | get SDT list
[**get_site_monitor_check_point_list**](LMApi.md#get_site_monitor_check_point_list) | **GET** /website/smcheckpoints | Get website checkpoint list
[**get_top_talkers_graph**](LMApi.md#get_top_talkers_graph) | **GET** /device/devices/{id}/topTalkersGraph | get top talkers graph
[**get_topology_source_by_id**](LMApi.md#get_topology_source_by_id) | **GET** /setting/topologysources/{id} | Get TopologySource by id
[**get_topology_source_list**](LMApi.md#get_topology_source_list) | **GET** /setting/topologysources | Get TopologySource List
[**get_tracked_query_group_by_id**](LMApi.md#get_tracked_query_group_by_id) | **GET** /trackedquerygroups/{id} | Get tracked query group by ID
[**get_tracked_query_group_list**](LMApi.md#get_tracked_query_group_list) | **GET** /trackedquerygroups | Get tracked query group list
[**get_unmonitored_device_list**](LMApi.md#get_unmonitored_device_list) | **GET** /device/unmonitoreddevices | Get unmonitored device list
[**get_update_reason_list_by_config_source_id**](LMApi.md#get_update_reason_list_by_config_source_id) | **GET** /setting/configsources/{id}/updatereasons | Get update history for a configSource
[**get_update_reason_list_by_data_source_id**](LMApi.md#get_update_reason_list_by_data_source_id) | **GET** /setting/datasources/{id}/updatereasons | Get update history for a datasource
[**get_v4_metadata**](LMApi.md#get_v4_metadata) | **GET** /setting/logicmodules/metadata | get metadata
[**get_website_alert_list_by_website_id**](LMApi.md#get_website_alert_list_by_website_id) | **GET** /website/websites/{id}/alerts | get alerts for a website
[**get_website_by_id**](LMApi.md#get_website_by_id) | **GET** /website/websites/{id} | get website by id
[**get_website_checkpoint_data_by_id**](LMApi.md#get_website_checkpoint_data_by_id) | **GET** /website/websites/{srvId}/checkpoints/{checkId}/data | get data for a website checkpoint
[**get_website_data_by_graph_name**](LMApi.md#get_website_data_by_graph_name) | **GET** /website/websites/{id}/graphs/{graphName}/data | get website data by graph name
[**get_website_graph_data**](LMApi.md#get_website_graph_data) | **GET** /website/websites/{websiteId}/checkpoints/{checkpointId}/graphs/{graphName}/data | Get website graph data
[**get_website_group_by_id**](LMApi.md#get_website_group_by_id) | **GET** /website/groups/{id} | get website group
[**get_website_group_list**](LMApi.md#get_website_group_list) | **GET** /website/groups | get website group list
[**get_website_list**](LMApi.md#get_website_list) | **GET** /website/websites | get website list
[**get_website_property_list_by_website_id**](LMApi.md#get_website_property_list_by_website_id) | **GET** /website/websites/{id}/properties | get a list of properties for a website
[**get_website_sdt_list_by_website_id**](LMApi.md#get_website_sdt_list_by_website_id) | **GET** /website/websites/{id}/sdts | get a list of SDTs for a website
[**get_widget_by_id**](LMApi.md#get_widget_by_id) | **GET** /dashboard/widgets/{id} | Get widget by ID
[**get_widget_data_by_id**](LMApi.md#get_widget_data_by_id) | **GET** /dashboard/widgets/{id}/data | get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
[**get_widget_list**](LMApi.md#get_widget_list) | **GET** /dashboard/widgets | Get widget list
[**get_widget_list_by_dashboard_id**](LMApi.md#get_widget_list_by_dashboard_id) | **GET** /dashboard/dashboards/{id}/widgets | get widget list by DashboardId
[**import_applies_to_function_json**](LMApi.md#import_applies_to_function_json) | **POST** /setting/functions/importjson | Import AppliesTo function via json
[**import_batch_job**](LMApi.md#import_batch_job) | **POST** /setting/batchjobs/importxml | Import batch job via XML
[**import_config_source**](LMApi.md#import_config_source) | **POST** /setting/configsources/importxml | Import config source via XML
[**import_config_source_json**](LMApi.md#import_config_source_json) | **POST** /setting/configsources/importjson | Import ConfigSource via json
[**import_data_source**](LMApi.md#import_data_source) | **POST** /setting/datasources/importxml | Import datasource via XML
[**import_data_source_json**](LMApi.md#import_data_source_json) | **POST** /setting/datasources/importjson | Import DataSource via json
[**import_diagnostic_source_json**](LMApi.md#import_diagnostic_source_json) | **POST** /setting/diagnosticsources/importjson | Import DiagnosticSource via json
[**import_event_source**](LMApi.md#import_event_source) | **POST** /setting/eventsources/importxml | Import event source via XML
[**import_event_source_json**](LMApi.md#import_event_source_json) | **POST** /setting/eventsources/importjson | Import EventSource via json
[**import_job_monitor_json**](LMApi.md#import_job_monitor_json) | **POST** /setting/batchjobs/importjson | Import batch JobMonitor via json
[**import_log_query_groups**](LMApi.md#import_log_query_groups) | **POST** /log/logquerygroups/import | Import log query groups and queries (best-effort)
[**import_log_source_json**](LMApi.md#import_log_source_json) | **POST** /setting/logsources/importjson | Import LogSource via json
[**import_oid_json**](LMApi.md#import_oid_json) | **POST** /setting/oids/importjson | Import OID via json
[**import_property_source_json**](LMApi.md#import_property_source_json) | **POST** /setting/propertyrules/importjson | Import PropertySource via json
[**import_topology_source_json**](LMApi.md#import_topology_source_json) | **POST** /setting/topologysources/importjson | Import TopologySource via json
[**map_un_map_module_to_access_group**](LMApi.md#map_un_map_module_to_access_group) | **POST** /setting/accessgroup/mapunmap/modules | Create a mapping of access group &amp; module
[**move_log_queries**](LMApi.md#move_log_queries) | **POST** /log/logquerygroups/{id}/move | Move log queries to another group
[**partition_action**](LMApi.md#partition_action) | **POST** /log/partitions/{id}/{action} | Perform an action on a specified log partition
[**patch_access_group**](LMApi.md#patch_access_group) | **PATCH** /setting/accessgroup/{id} | Update access group
[**patch_action_chain_by_id**](LMApi.md#patch_action_chain_by_id) | **PATCH** /setting/action/chains/{id} | update action chain
[**patch_action_rule_by_id**](LMApi.md#patch_action_rule_by_id) | **PATCH** /setting/action/rules/{id} | update action rule
[**patch_action_rule_status_by_id**](LMApi.md#patch_action_rule_status_by_id) | **PATCH** /setting/action/rules/{id}/status | enable/disable action rule
[**patch_admin_by_id**](LMApi.md#patch_admin_by_id) | **PATCH** /setting/admins/{id} | update user
[**patch_alert_rule_by_id**](LMApi.md#patch_alert_rule_by_id) | **PATCH** /setting/alert/rules/{id} | update alert rule
[**patch_api_token_by_admin_id**](LMApi.md#patch_api_token_by_admin_id) | **PATCH** /setting/admins/{adminId}/apitokens/{apitokenId} | Update API tokens for a user
[**patch_applies_to_function**](LMApi.md#patch_applies_to_function) | **PATCH** /setting/functions/{id} | Update applies to function
[**patch_collector_by_id**](LMApi.md#patch_collector_by_id) | **PATCH** /setting/collector/collectors/{id} | update collector
[**patch_collector_group_by_id**](LMApi.md#patch_collector_group_by_id) | **PATCH** /setting/collector/groups/{id} | Update collector group
[**patch_config_source_by_id**](LMApi.md#patch_config_source_by_id) | **PATCH** /setting/configsources/{id} | Update config source by ID
[**patch_dashboard_by_id**](LMApi.md#patch_dashboard_by_id) | **PATCH** /dashboard/dashboards/{id} | update dashboard
[**patch_dashboard_group_by_id**](LMApi.md#patch_dashboard_group_by_id) | **PATCH** /dashboard/groups/{id} | update dashboard group
[**patch_datasource_by_id**](LMApi.md#patch_datasource_by_id) | **PATCH** /setting/datasources/{id} | Update datasource
[**patch_default_dashboard**](LMApi.md#patch_default_dashboard) | **PATCH** /setting/userdata/{id} | Update default dashboard
[**patch_device**](LMApi.md#patch_device) | **PATCH** /device/devices/{id} | update a device (Request schema may change depending upon the type of uptime device being updated)
[**patch_device_datasource_instance_alert_setting_by_id**](LMApi.md#patch_device_datasource_instance_alert_setting_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**patch_device_datasource_instance_by_id**](LMApi.md#patch_device_datasource_instance_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**patch_device_datasource_instance_group_by_id**](LMApi.md#patch_device_datasource_instance_group_by_id) | **PATCH** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | Update device datasource instance group
[**patch_device_group_by_id**](LMApi.md#patch_device_group_by_id) | **PATCH** /device/groups/{id} | update device group
[**patch_device_group_cluster_alert_conf_by_id**](LMApi.md#patch_device_group_cluster_alert_conf_by_id) | **PATCH** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**patch_device_group_datasource_alert_setting**](LMApi.md#patch_device_group_datasource_alert_setting) | **PATCH** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | Update device group datasource alert setting
[**patch_device_group_datasource_by_id**](LMApi.md#patch_device_group_datasource_by_id) | **PATCH** /device/groups/{deviceGroupId}/datasources/{id} | update device group datasource
[**patch_device_group_property_by_name**](LMApi.md#patch_device_group_property_by_name) | **PATCH** /device/groups/{gid}/properties/{name} | Update device group property
[**patch_device_property_by_name**](LMApi.md#patch_device_property_by_name) | **PATCH** /device/devices/{deviceId}/properties/{name} | Update device property
[**patch_diagnostic_source_by_id**](LMApi.md#patch_diagnostic_source_by_id) | **PATCH** /setting/diagnosticsources/{id} | Update a diagnostics source
[**patch_escalation_chain_by_id**](LMApi.md#patch_escalation_chain_by_id) | **PATCH** /setting/alert/chains/{id} | Update escalation chain
[**patch_event_source_by_id**](LMApi.md#patch_event_source_by_id) | **PATCH** /setting/eventsources/{id} | Update event source by ID
[**patch_job_monitor**](LMApi.md#patch_job_monitor) | **PATCH** /setting/batchjobs/{id} | Update JobMonitor
[**patch_log_alert_group**](LMApi.md#patch_log_alert_group) | **PATCH** /logpipelines/{pipelineId} | Update a specific LogAlertGroup by its ID
[**patch_log_alerts**](LMApi.md#patch_log_alerts) | **PATCH** /logpipelines/processors/{processorId} | Update a LogAlerts by ID
[**patch_log_partition**](LMApi.md#patch_log_partition) | **PATCH** /log/partitions/{id} | Update an existing log partition
[**patch_log_query_group**](LMApi.md#patch_log_query_group) | **PATCH** /log/logquerygroups/{id} | Update log query group
[**patch_log_source**](LMApi.md#patch_log_source) | **PATCH** /setting/logsources/{id} | Update log source
[**patch_netscan**](LMApi.md#patch_netscan) | **PATCH** /setting/netscans/{id} | Update a netscan
[**patch_oid**](LMApi.md#patch_oid) | **PATCH** /setting/oids/{id} | Update an OID
[**patch_ops_note_by_id**](LMApi.md#patch_ops_note_by_id) | **PATCH** /setting/opsnotes/{id} | update opsnote
[**patch_property_rule**](LMApi.md#patch_property_rule) | **PATCH** /setting/propertyrules/{id} | update a property rule
[**patch_recipient_group_by_id**](LMApi.md#patch_recipient_group_by_id) | **PATCH** /setting/recipientgroups/{id} | Update recipient group
[**patch_remediation_source_by_id**](LMApi.md#patch_remediation_source_by_id) | **PATCH** /setting/remediationsources/{id} | Update a remediation source
[**patch_report_by_id**](LMApi.md#patch_report_by_id) | **PATCH** /report/reports/{id} | Update report
[**patch_report_group_by_id**](LMApi.md#patch_report_group_by_id) | **PATCH** /report/groups/{id} | Update report group
[**patch_role_by_id**](LMApi.md#patch_role_by_id) | **PATCH** /setting/roles/{id} | Update role
[**patch_sdt_by_id**](LMApi.md#patch_sdt_by_id) | **PATCH** /sdt/sdts/{id} | update SDT (Response may contain extra fields depending upon the type of SDT being updated)
[**patch_topology_source**](LMApi.md#patch_topology_source) | **PATCH** /setting/topologysources/{id} | Update TopologySource
[**patch_tracked_query_group**](LMApi.md#patch_tracked_query_group) | **PATCH** /trackedquerygroups/{id} | Update tracked query group
[**patch_website_by_id**](LMApi.md#patch_website_by_id) | **PATCH** /website/websites/{id} | update website
[**patch_website_group_by_id**](LMApi.md#patch_website_group_by_id) | **PATCH** /website/groups/{id} | update website group
[**patch_widget_by_id**](LMApi.md#patch_widget_by_id) | **PATCH** /dashboard/widgets/{id} | Update widget
[**restart_collector_by_id**](LMApi.md#restart_collector_by_id) | **POST** /setting/collector/collectors/{collectorId}/services/restart | restart collector
[**schedule_auto_discovery_by_device_id**](LMApi.md#schedule_auto_discovery_by_device_id) | **POST** /device/devices/{id}/scheduleAutoDiscovery | schedule active discovery for a device
[**test_aws_account**](LMApi.md#test_aws_account) | **POST** /aws/functions/testAccount | Test AWS account
[**test_azure_account**](LMApi.md#test_azure_account) | **POST** /azure/functions/testAccount | test Azure account
[**test_gcp_account**](LMApi.md#test_gcp_account) | **POST** /gcp/functions/testAccount | test GCP account
[**test_saa_s_account**](LMApi.md#test_saa_s_account) | **POST** /saas/functions/testAccount | Test SaaS account
[**trigger_collector_status_check**](LMApi.md#trigger_collector_status_check) | **POST** /setting/collector/collectors/{collectorId}/services/triggerStatusCheck | trigger collector status check
[**update_access_group**](LMApi.md#update_access_group) | **PUT** /setting/accessgroup/{id} | Update access group
[**update_action_chain_by_id**](LMApi.md#update_action_chain_by_id) | **PUT** /setting/action/chains/{id} | update action chain
[**update_action_rule_by_id**](LMApi.md#update_action_rule_by_id) | **PUT** /setting/action/rules/{id} | update action rule
[**update_action_rule_status_by_id**](LMApi.md#update_action_rule_status_by_id) | **PUT** /setting/action/rules/{id}/status | enable/disable action rule
[**update_admin_by_id**](LMApi.md#update_admin_by_id) | **PUT** /setting/admins/{id} | update user
[**update_alert_rule_by_id**](LMApi.md#update_alert_rule_by_id) | **PUT** /setting/alert/rules/{id} | update alert rule
[**update_api_token_by_admin_id**](LMApi.md#update_api_token_by_admin_id) | **PUT** /setting/admins/{adminId}/apitokens/{apitokenId} | Update API tokens for a user
[**update_applies_to_function**](LMApi.md#update_applies_to_function) | **PUT** /setting/functions/{id} | Update applies to function
[**update_collector_by_id**](LMApi.md#update_collector_by_id) | **PUT** /setting/collector/collectors/{id} | update collector
[**update_collector_group_by_id**](LMApi.md#update_collector_group_by_id) | **PUT** /setting/collector/groups/{id} | Update collector group
[**update_config_source_by_id**](LMApi.md#update_config_source_by_id) | **PUT** /setting/configsources/{id} | Update config source by ID
[**update_dashboard_by_id**](LMApi.md#update_dashboard_by_id) | **PUT** /dashboard/dashboards/{id} | update dashboard
[**update_dashboard_group_by_id**](LMApi.md#update_dashboard_group_by_id) | **PUT** /dashboard/groups/{id} | update dashboard group
[**update_datasource_by_id**](LMApi.md#update_datasource_by_id) | **PUT** /setting/datasources/{id} | Update datasource
[**update_default_dashboard**](LMApi.md#update_default_dashboard) | **PUT** /setting/userdata/{id} | Update default dashboard
[**update_device**](LMApi.md#update_device) | **PUT** /device/devices/{id} | update a device (Request schema may change depending upon the type of uptime device being updated)
[**update_device_datasource_instance_alert_setting_by_id**](LMApi.md#update_device_datasource_instance_alert_setting_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{instanceId}/alertsettings/{id} | update device instance alert setting
[**update_device_datasource_instance_by_id**](LMApi.md#update_device_datasource_instance_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{hdsId}/instances/{id} | update device instance
[**update_device_datasource_instance_group_by_id**](LMApi.md#update_device_datasource_instance_group_by_id) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{id} | Update device datasource instance group
[**update_device_group_by_id**](LMApi.md#update_device_group_by_id) | **PUT** /device/groups/{id} | update device group
[**update_device_group_cluster_alert_conf_by_id**](LMApi.md#update_device_group_cluster_alert_conf_by_id) | **PUT** /device/groups/{deviceGroupId}/clusterAlertConf/{id} | Update cluster alert configuration
[**update_device_group_datasource_alert_setting**](LMApi.md#update_device_group_datasource_alert_setting) | **PUT** /device/groups/{deviceGroupId}/datasources/{dsId}/alertsettings | Update device group datasource alert setting
[**update_device_group_datasource_by_id**](LMApi.md#update_device_group_datasource_by_id) | **PUT** /device/groups/{deviceGroupId}/datasources/{id} | update device group datasource
[**update_device_group_property_by_name**](LMApi.md#update_device_group_property_by_name) | **PUT** /device/groups/{gid}/properties/{name} | Update device group property
[**update_device_property_by_name**](LMApi.md#update_device_property_by_name) | **PUT** /device/devices/{deviceId}/properties/{name} | Update device property
[**update_diagnostic_source_by_id**](LMApi.md#update_diagnostic_source_by_id) | **PUT** /setting/diagnosticsources/{id} | Update a diagnostics source
[**update_disable_log_alerts**](LMApi.md#update_disable_log_alerts) | **PUT** /logpipelines/processors/{processorId}/{action} | Enable or disable a LogAlerts by ID
[**update_escalation_chain_by_id**](LMApi.md#update_escalation_chain_by_id) | **PUT** /setting/alert/chains/{id} | Update escalation chain
[**update_event_source_by_id**](LMApi.md#update_event_source_by_id) | **PUT** /setting/eventsources/{id} | Update event source by ID
[**update_instance_group_alert_threshold**](LMApi.md#update_instance_group_alert_threshold) | **PUT** /device/devices/{deviceId}/devicedatasources/{deviceDsId}/groups/{dsigId}/datapoints/{dpId}/alertconfig | Update instance group alert threshold
[**update_job_monitor**](LMApi.md#update_job_monitor) | **PUT** /setting/batchjobs/{id} | Update JobMonitor
[**update_log_alert_group**](LMApi.md#update_log_alert_group) | **PUT** /logpipelines/{pipelineId} | Update a specific LogAlertGroup by its ID
[**update_log_alerts**](LMApi.md#update_log_alerts) | **PUT** /logpipelines/processors/{processorId} | Update a LogAlerts by ID
[**update_log_partition**](LMApi.md#update_log_partition) | **PUT** /log/partitions/{id} | Update an existing log partition
[**update_log_query_group**](LMApi.md#update_log_query_group) | **PUT** /log/logquerygroups/{id} | Update log query group
[**update_log_source**](LMApi.md#update_log_source) | **PUT** /setting/logsources/{id} | Update log source
[**update_netscan**](LMApi.md#update_netscan) | **PUT** /setting/netscans/{id} | Update a netscan
[**update_oid**](LMApi.md#update_oid) | **PUT** /setting/oids/{id} | Update an OID
[**update_ops_note_by_id**](LMApi.md#update_ops_note_by_id) | **PUT** /setting/opsnotes/{id} | update opsnote
[**update_property_rule**](LMApi.md#update_property_rule) | **PUT** /setting/propertyrules/{id} | update a property rule
[**update_recipient_group_by_id**](LMApi.md#update_recipient_group_by_id) | **PUT** /setting/recipientgroups/{id} | Update recipient group
[**update_remediation_source_by_id**](LMApi.md#update_remediation_source_by_id) | **PUT** /setting/remediationsources/{id} | Update a remediation source
[**update_report_by_id**](LMApi.md#update_report_by_id) | **PUT** /report/reports/{id} | Update report
[**update_report_group_by_id**](LMApi.md#update_report_group_by_id) | **PUT** /report/groups/{id} | Update report group
[**update_role_by_id**](LMApi.md#update_role_by_id) | **PUT** /setting/roles/{id} | Update role
[**update_sdt_by_id**](LMApi.md#update_sdt_by_id) | **PUT** /sdt/sdts/{id} | update SDT (Response may contain extra fields depending upon the type of SDT being updated)
[**update_topology_source**](LMApi.md#update_topology_source) | **PUT** /setting/topologysources/{id} | Update TopologySource
[**update_tracked_query_group**](LMApi.md#update_tracked_query_group) | **PUT** /trackedquerygroups/{id} | Update tracked query group
[**update_website_by_id**](LMApi.md#update_website_by_id) | **PUT** /website/websites/{id} | update website
[**update_website_group_by_id**](LMApi.md#update_website_group_by_id) | **PUT** /website/groups/{id} | update website group
[**update_widget_by_id**](LMApi.md#update_widget_by_id) | **PUT** /dashboard/widgets/{id} | Update widget
[**verify_aws_billing_permissions**](LMApi.md#verify_aws_billing_permissions) | **POST** /aws/functions/verifyBillingPermissions | Verify AWS Billing Permissions
[**verify_storage_accounts_permissions**](LMApi.md#verify_storage_accounts_permissions) | **POST** /azure/functions/verifyStorageAccountsPermissions | view storage accounts

# **ack_alert_by_id**
> object ack_alert_by_id(body, id)

Acknowledge alert by ID

Acknowledge the alert with the given ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Acknowledge alert by ID
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

# **add_action_chain**
> ActionChain add_action_chain(body)

Add action chain

Create a new action chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ActionChain() # ActionChain | 

try:
    # Add action chain
    api_response = api_instance.add_action_chain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_action_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionChain**](ActionChain.md)|  | 

### Return type

[**ActionChain**](ActionChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_action_rule**
> ActionRule add_action_rule(body)

Add Action Rule

Add a new action rule

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.ActionRule() # ActionRule | 

try:
    # Add Action Rule
    api_response = api_instance.add_action_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_action_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionRule**](ActionRule.md)|  | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_admin**
> Admin add_admin(body)

add user

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

Add alert note

Add a note to the alert with the given ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add alert note
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

Add API tokens for a user

Add new API tokens for a specific user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
type = 'type_example' # str |  (optional)

try:
    # Add API tokens for a user
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
 **type** | **str**|  | [optional] 

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

Add applies to function

Create a new applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add applies to function
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

Add collector group

Create a new collector group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add collector group
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

Add a new config source

Create a new config source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add a new config source
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
recursive = true # bool |  (optional)

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
 **recursive** | **bool**|  | [optional] 

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

Add datasource

Adds a new datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
create_graph = true # bool |  (optional)

try:
    # Add datasource
    api_response = api_instance.add_datasource_by_id(body=body, create_graph=create_graph)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataSource**](DataSource.md)|  | [optional] 
 **create_graph** | **bool**|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device**
> Device add_device(body, end=end, netflow_filter=netflow_filter, start=start, add_from_wizard=add_from_wizard, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)

add a new device (Request schema may change depending upon the type of uptime device being added)

add a new device (Request schema may change depending upon the type of uptime device being added)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
add_from_wizard = true # bool |  (optional)
need_stc_grp_and_sorted_cp = true # bool |  (optional)

try:
    # add a new device (Request schema may change depending upon the type of uptime device being added)
    api_response = api_instance.add_device(body, end=end, netflow_filter=netflow_filter, start=start, add_from_wizard=add_from_wizard, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Device**](Device.md)|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **add_from_wizard** | **bool**|  | [optional] 
 **need_stc_grp_and_sorted_cp** | **bool**|  | [optional] 

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
> DeviceDataSourceInstanceGroup add_device_datasource_instance_group(device_ds_id, device_id, body)

Add device datasource instance group

Add a new device datasource instance group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # Add device datasource instance group
    api_response = api_instance.add_device_datasource_instance_group(device_ds_id, device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_device_datasource_instance_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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

Add device group property

Add a new property to a specific device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add device group property
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

Add device property

Add a new property to a specific device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add device property
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

# **add_diagnostic_source**
> DiagnosticsSource add_diagnostic_source(body=body)

Add diagnostics source

Adds a new diagnostics source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DiagnosticsSource() # DiagnosticsSource |  (optional)

try:
    # Add diagnostics source
    api_response = api_instance.add_diagnostic_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_diagnostic_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiagnosticsSource**](DiagnosticsSource.md)|  | [optional] 

### Return type

[**DiagnosticsSource**](DiagnosticsSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dns_mapping**
> RestDNSMappingV3 add_dns_mapping(body=body)

Add DNS mapping

Add a new DNS mapping

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add DNS mapping
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

Add escalation chain

Create a new escalation chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add escalation chain
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

Add event source

Adds a new event source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add event source
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

Create a new JobMonitor

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **add_log_alert_group**
> RestLogPipelineV3 add_log_alert_group(body)

Add a new LogAlertGroup

Handles the addition of a new LogAlertGroup.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestLogPipelineV3() # RestLogPipelineV3 | 

try:
    # Add a new LogAlertGroup
    api_response = api_instance.add_log_alert_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_log_alert_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestLogPipelineV3**](RestLogPipelineV3.md)|  | 

### Return type

[**RestLogPipelineV3**](RestLogPipelineV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_log_alerts**
> RestLogPipelineProcessorV3 add_log_alerts(body)

Add a new LogAlerts

Handles the addition of a new LogAlerts.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestLogPipelineProcessorV3() # RestLogPipelineProcessorV3 | 

try:
    # Add a new LogAlerts
    api_response = api_instance.add_log_alerts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_log_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)|  | 

### Return type

[**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_log_query_group**
> LogQueryGroup add_log_query_group(body)

Create a new log query group

Add a log query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.LogQueryGroup() # LogQueryGroup | 

try:
    # Create a new log query group
    api_response = api_instance.add_log_query_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_log_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogQueryGroup**](LogQueryGroup.md)|  | 

### Return type

[**LogQueryGroup**](LogQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_log_source**
> LogSource add_log_source(body=body)

Add log source

Adds a new log source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add log source
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

Add a new netscan

Create a new netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add a new netscan
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

Add a new OID

Create a new OID and add it to the system

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add a new OID
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

Add a new property rule

Creates a new property rule in the system

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add a new property rule
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

Add recipient group

Add a new recipient group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add recipient group
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

# **add_remediation_source**
> RemediationSource add_remediation_source(body=body)

Add remediation source

Adds a new remediation source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RemediationSource() # RemediationSource |  (optional)

try:
    # Add remediation source
    api_response = api_instance.add_remediation_source(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->add_remediation_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemediationSource**](RemediationSource.md)|  | [optional] 

### Return type

[**RemediationSource**](RemediationSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_report**
> ReportBase add_report(body)

Add report

Create a new report

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add report
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

Add report group

Add a new report group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add report group
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

Add role

Create a new role

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add role
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

Add website

Add website. Request structure may vary based on the check type {PingCheck | WebCheck model}. Use the respective model in SDK.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add website
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

Add widget

Adds a new widget. Based on widget type, the request and response may contain additional attributes. Please refer to the models corresponding to specific widget types at the bottom of this page for detailed attributes.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Add widget
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

# **batch_update_collector_agent_log_levels**
> list[RestAgentLogLevelV3] batch_update_collector_agent_log_levels(id, body=body)

batch update collector agent log levels

batch update collector agent log levels for multiple components

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = [logicmonitor_sdk.RestAgentLogLevelV3()] # list[RestAgentLogLevelV3] |  (optional)

try:
    # batch update collector agent log levels
    api_response = api_instance.batch_update_collector_agent_log_levels(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->batch_update_collector_agent_log_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**list[RestAgentLogLevelV3]**](RestAgentLogLevelV3.md)|  | [optional] 

### Return type

[**list[RestAgentLogLevelV3]**](RestAgentLogLevelV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_sizing**
> RestCollectorSizingResponseV3 calculate_sizing(body, fields=fields)

Calculate collector sizing recommendations

Analyzes workload requirements (devices, logs, NetFlow) and recommends optimal collector size and count for each workload type. Supports three independent collector pools: polling collectors for device monitoring, logs collectors for log ingestion, and NetFlow collectors for flow data processing.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RestCollectorSizingRequestV3() # RestCollectorSizingRequestV3 | Sizing request with workload specifications
fields = 'fields_example' # str | Optional comma-separated list of fields to include in response (optional)

try:
    # Calculate collector sizing recommendations
    api_response = api_instance.calculate_sizing(body, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->calculate_sizing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestCollectorSizingRequestV3**](RestCollectorSizingRequestV3.md)| Sizing request with workload specifications | 
 **fields** | **str**| Optional comma-separated list of fields to include in response | [optional] 

### Return type

[**RestCollectorSizingResponseV3**](RestCollectorSizingResponseV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_device_config_source_config**
> object collect_device_config_source_config(instance_id, device_id, hds_id)

collect a config for a device

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
instance_id = 56 # int | 
device_id = 56 # int | 
hds_id = 56 # int | 

try:
    # collect a config for a device
    api_response = api_instance.collect_device_config_source_config(instance_id, device_id, hds_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->collect_device_config_source_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_log_partition**
> LogPartition create_log_partition(body=body)

Create a new log partition

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

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracked_query_group**
> TrackedQueryGroup create_tracked_query_group(body=body)

Create tracked query group

Create a new tracked query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.TrackedQueryGroup() # TrackedQueryGroup |  (optional)

try:
    # Create tracked query group
    api_response = api_instance.create_tracked_query_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->create_tracked_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrackedQueryGroup**](TrackedQueryGroup.md)|  | [optional] 

### Return type

[**TrackedQueryGroup**](TrackedQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_group**
> object delete_access_group(id)

Delete access group

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

# **delete_action_chain_by_id**
> object delete_action_chain_by_id(id)

delete action chain 

delete action chain by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # delete action chain 
    api_response = api_instance.delete_action_chain_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_action_chain_by_id: %s\n" % e)
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

# **delete_action_rule_by_id**
> object delete_action_rule_by_id(id)

delete action rule

delete action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # delete action rule
    api_response = api_instance.delete_action_rule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_action_rule_by_id: %s\n" % e)
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

Delete API token

Delete a specific API token by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete API token
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

Delete applies to function

Delete a specific applies to function by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
ignore_reference = true # bool |  (optional)

try:
    # Delete applies to function
    api_response = api_instance.delete_applies_to_function_by_id(id, ignore_reference=ignore_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_applies_to_function_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **ignore_reference** | **bool**|  | [optional] 

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

Delete collector group

Delete a specific collector group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete collector group
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

Delete config source by ID

Delete a config source based on the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete config source by ID
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
allow_non_empty_group = true # bool |  (optional)

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
 **allow_non_empty_group** | **bool**|  | [optional] 

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

Delete datasource

Deletes a datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete datasource
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
> object delete_device_by_id(id, end=end, netflow_filter=netflow_filter, start=start, delete_hard=delete_hard)

delete a device

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
delete_hard = true # bool |  (optional)

try:
    # delete a device
    api_response = api_instance.delete_device_by_id(id, end=end, netflow_filter=netflow_filter, start=start, delete_hard=delete_hard)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **delete_hard** | **bool**|  | [optional] 

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
delete_children = true # bool |  (optional)
delete_hard = true # bool |  (optional)

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
 **delete_children** | **bool**|  | [optional] 
 **delete_hard** | **bool**|  | [optional] 

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

Delete device group property

Delete a specific property of a device group by its name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete device group property
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

Delete device property

Delete a specific property of a device by its name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete device property
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

# **delete_diagnostic_source_by_id**
> object delete_diagnostic_source_by_id(id)

Delete a diagnostic source module

Deletes a diagnostic source module by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete a diagnostic source module
    api_response = api_instance.delete_diagnostic_source_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_diagnostic_source_by_id: %s\n" % e)
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

# **delete_escalation_chain_by_id**
> object delete_escalation_chain_by_id(id)

Delete escalation chain

Delete a specific escalation chain by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete escalation chain
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

Delete event source by ID

Deletes an event source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete event source by ID
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

Delete a specific JobMonitor by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **delete_log_alert_group**
> object delete_log_alert_group(pipeline_id)

Delete a specific LogAlertGroup by ID

Handles the deletion of a specific LogAlertGroup by it's ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
pipeline_id = 56 # int | 

try:
    # Delete a specific LogAlertGroup by ID
    api_response = api_instance.delete_log_alert_group(pipeline_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_log_alert_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_alerts_by_id**
> object delete_log_alerts_by_id(processor_id)

Delete a LogAlerts by ID

Deletes the specified LogAlerts using its unique ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
processor_id = 56 # int | 

try:
    # Delete a LogAlerts by ID
    api_response = api_instance.delete_log_alerts_by_id(processor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_log_alerts_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_partition_by_id**
> object delete_log_partition_by_id(id)

Delete a log partition by ID

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
id = 56 # int | 

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
 **id** | **int**|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_query_group**
> object delete_log_query_group(id)

Delete log query group

Delete log query group by ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete log query group
    api_response = api_instance.delete_log_query_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_log_query_group: %s\n" % e)
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

# **delete_log_source**
> object delete_log_source(id)

Delete log source

Deletes an existing log source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete log source
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

Delete a netscan

Delete a specific netscan by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete a netscan
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

Delete an OID

Delete an existing OID from the system

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete an OID
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

Delete a property rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Delete recipient group

Delete a specific recipient group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete recipient group
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

# **delete_remediation_source_by_id**
> object delete_remediation_source_by_id(id)

Delete a remediation source module

Deletes a remediation source module by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete a remediation source module
    api_response = api_instance.delete_remediation_source_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_remediation_source_by_id: %s\n" % e)
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

Delete report

Delete a specific report by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete report
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

Delete report group

Delete a specific report group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete report group
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

Delete role

Delete a specific role by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete role
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

# **delete_tracked_query_group**
> object delete_tracked_query_group(id)

Delete tracked query group

Delete a tracked query group by ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete tracked query group
    api_response = api_instance.delete_tracked_query_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->delete_tracked_query_group: %s\n" % e)
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

# **delete_website_by_id**
> object delete_website_by_id(id)

delete website

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
delete_children = 56 # int |  (optional)

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
 **delete_children** | **int**|  | [optional] 

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

Delete widget

Deletes a widget by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Delete widget
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

Escalate alert by ID

Escalate the alert with the given ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Escalate alert by ID
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
collector_id = 56 # int |  (optional)

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
 **collector_id** | **int**|  | [optional] 

### Return type

[**Debug**](Debug.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_diagnostics_manually**
> DiagnosticsSourceExecution execute_diagnostics_manually(body=body)

Trigger a diagnostic module for host.

Trigger a diagnostic module for host. Set includeOutput=true to wait for completion and return script output.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.DiagnosticsSourceExecution() # DiagnosticsSourceExecution |  (optional)

try:
    # Trigger a diagnostic module for host.
    api_response = api_instance.execute_diagnostics_manually(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->execute_diagnostics_manually: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiagnosticsSourceExecution**](DiagnosticsSourceExecution.md)|  | [optional] 

### Return type

[**DiagnosticsSourceExecution**](DiagnosticsSourceExecution.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_remediation_manually**
> RemediationSourceExecution execute_remediation_manually(body=body)

Trigger a remediation module for host.

Trigger a remediation module for host. Set includeOutput=true to wait for completion and return script output.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = logicmonitor_sdk.RemediationSourceExecution() # RemediationSourceExecution |  (optional)

try:
    # Trigger a remediation module for host.
    api_response = api_instance.execute_remediation_manually(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->execute_remediation_manually: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemediationSourceExecution**](RemediationSourceExecution.md)|  | [optional] 

### Return type

[**RemediationSourceExecution**](RemediationSourceExecution.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_device_instances_data**
> DeviceInstanceDataPaginationResponse fetch_device_instances_data(body, period=period, start=start, end=end, aggregate=aggregate)

Fetch device instances data

Retrieve a paginated list of data for device instances

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
period = 1.2 # float |  (optional)
start = 789 # int |  (optional)
end = 789 # int |  (optional)
aggregate = 'aggregate_example' # str | The aggregate option (optional)

try:
    # Fetch device instances data
    api_response = api_instance.fetch_device_instances_data(body, period=period, start=start, end=end, aggregate=aggregate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->fetch_device_instances_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceInstances**](DeviceInstances.md)|  | 
 **period** | **float**|  | [optional] 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **aggregate** | **str**| The aggregate option | [optional] 

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

Get report for task ID

Fetch the report associated with a specific task ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get report for task ID
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

Run a report

Generate a report based on the given report ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Run a report
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

# **get_action_chain_by_id**
> ActionChain get_action_chain_by_id(id)

Get action chain by ID

Retrieve details of a specific action chain using its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get action chain by ID
    api_response = api_instance.get_action_chain_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_action_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ActionChain**](ActionChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_chains_list**
> ActionChainPaginationResponse get_action_chains_list()

Get action chains list

Retrieves a list of action chains

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get action chains list
    api_response = api_instance.get_action_chains_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_action_chains_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActionChainPaginationResponse**](ActionChainPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_rule_by_id**
> ActionRule get_action_rule_by_id(id)

get action rule

get action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # get action rule
    api_response = api_instance.get_action_rule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_action_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_rule_status_by_id**
> ActionRuleStatus get_action_rule_status_by_id(id)

get action rule status

get action rule status by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # get action rule status
    api_response = api_instance.get_action_rule_status_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_action_rule_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ActionRuleStatus**](ActionRuleStatus.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_rules_list**
> ActionRulePaginationResponse get_action_rules_list()

Get action rules list

Retrieves a list of action rules

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get action rules list
    api_response = api_instance.get_action_rules_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_action_rules_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActionRulePaginationResponse**](ActionRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_by_id**
> Admin get_admin_by_id(id, fields=fields)

get user

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

get alert by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
need_message = true # bool |  (optional)
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
 **need_message** | **bool**|  | [optional] 
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

Get alert list

Retrieve the list of alerts

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get alert list
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
need_message = true # bool |  (optional)
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
 **need_message** | **bool**|  | [optional] 
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
> AlertPaginationResponse get_alert_list_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)

get alerts

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
need_message = true # bool |  (optional)
custom_columns = 'custom_columns_example' # str |  (optional)
bound = 'bound_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get alerts
    api_response = api_instance.get_alert_list_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, need_message=need_message, custom_columns=custom_columns, bound=bound, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_alert_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **need_message** | **bool**|  | [optional] 
 **custom_columns** | **str**|  | [optional] 
 **bound** | **str**|  | [optional] 
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
> SDTPaginationResponse get_all_sdt_list_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)

get SDTs for a device

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDTs for a device
    api_response = api_instance.get_all_sdt_list_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_all_sdt_list_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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

Get a list of API tokens across users

Retrieve a paginated list of API tokens for all users

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get a list of API tokens across users
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

Get API tokens for a user

Retrieve a paginated list of API tokens for a specific user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get API tokens for a user
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

Get applies to function by ID

Retrieve a specific applies to function using its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get applies to function by ID
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

Get applies to function list

Retrieve a paginated list of functions that apply

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get applies to function list
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

Get devices associated with a datasource

Retrieves the list of devices associated with a specific datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get devices associated with a datasource
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

Retrieve a specific audit log by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Retrieve a paginated list of audit logs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Retrieve the AWS account ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Retrieve the AWS external ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **get_collector_agent_log_level_by_component**
> RestAgentLogLevelV3 get_collector_agent_log_level_by_component(id, component)

get collector agent log level by component

get collector agent log level by component

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
component = 'component_example' # str | 

try:
    # get collector agent log level by component
    api_response = api_instance.get_collector_agent_log_level_by_component(id, component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_agent_log_level_by_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **component** | **str**|  | 

### Return type

[**RestAgentLogLevelV3**](RestAgentLogLevelV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_agent_log_levels**
> RestAgentLogLevelV3 get_collector_agent_log_levels(id)

get collector agent log levels

get collector agent log levels

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # get collector agent log levels
    api_response = api_instance.get_collector_agent_log_levels(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_agent_log_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestAgentLogLevelV3**](RestAgentLogLevelV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_by_id**
> Collector get_collector_by_id(id, fields=fields)

get collector

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

# **get_collector_download_token_by_id**
> RestCollectorDownloadTokenV3 get_collector_download_token_by_id(id)

get collector download token

get collector download token – a short-lived token used to authorize downloading the collector installer

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | The collector ID

try:
    # get collector download token
    api_response = api_instance.get_collector_download_token_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_download_token_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The collector ID | 

### Return type

[**RestCollectorDownloadTokenV3**](RestCollectorDownloadTokenV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_events**
> RestCollectorEventV3 get_collector_events(collector_id)

get collector events

get collector events

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

try:
    # get collector events
    api_response = api_instance.get_collector_events(collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**|  | 

### Return type

[**RestCollectorEventV3**](RestCollectorEventV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_by_id**
> CollectorGroup get_collector_group_by_id(id, fields=fields)

Get collector group

Retrieve details of a specific collector group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get collector group
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

Get collector group list

Retrieve a paginated list of collector groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get collector group list
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
> str get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea, arch_type=arch_type)

get collector installer

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
monitor_others = true # bool |  (optional)
collector_size = 'collector_size_example' # str | The size of the Collector you'd like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory), extra large (requires 16GB memory), double extra large (requires 32GB memory). Requires collector version 22.180 or higher. Defaults to small (optional)
use_ea = true # bool | If true, the latest EA Collector version will be used. Defaults to false (optional)
arch_type = 'arch_type_example' # str | The architecture of the collector installer. Options are x64 (default) or arm64 (optional)

try:
    # get collector installer
    api_response = api_instance.get_collector_installer(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea, arch_type=arch_type)
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
 **monitor_others** | **bool**|  | [optional] 
 **collector_size** | **str**| The size of the Collector you&#x27;d like to install. Options are nano, small (requires 2GB memory), medium (requires 4GB memory), large (requires 8GB memory), extra large (requires 16GB memory), double extra large (requires 32GB memory). Requires collector version 22.180 or higher. Defaults to small | [optional] 
 **use_ea** | **bool**| If true, the latest EA Collector version will be used. Defaults to false | [optional] 
 **arch_type** | **str**| The architecture of the collector installer. Options are x64 (default) or arm64 | [optional] 

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

# **get_collector_log_file_by_name**
> RestCollectorLogFileV3 get_collector_log_file_by_name(collector_id, file_name, format=format)

get collector log file

get collector log file

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | The collector ID
file_name = 'file_name_example' # str | The name of the log file to retrieve (e.g. 30.wrapper.log.zip)
format = 'format_example' # str | Response format – Use 'json' (default) to get file metadata, or 'zip' to download the file as a binary attachment (optional)

try:
    # get collector log file
    api_response = api_instance.get_collector_log_file_by_name(collector_id, file_name, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_log_file_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**| The collector ID | 
 **file_name** | **str**| The name of the log file to retrieve (e.g. 30.wrapper.log.zip) | 
 **format** | **str**| Response format – Use &#x27;json&#x27; (default) to get file metadata, or &#x27;zip&#x27; to download the file as a binary attachment | [optional] 

### Return type

[**RestCollectorLogFileV3**](RestCollectorLogFileV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_log_files**
> CollectorLogFilePaginationResponse get_collector_log_files(collector_id, format=format)

get collector log files

get collector log files, list or zip archive

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | The collector ID
format = 'format_example' # str | Response format – Use 'json' (default) to list log files, or 'zip' to download all log files as a zip archive (optional)

try:
    # get collector log files
    api_response = api_instance.get_collector_log_files(collector_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_log_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**| The collector ID | 
 **format** | **str**| Response format – Use &#x27;json&#x27; (default) to list log files, or &#x27;zip&#x27; to download all log files as a zip archive | [optional] 

### Return type

[**CollectorLogFilePaginationResponse**](CollectorLogFilePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_status_check**
> RestCollectorStatusV3 get_collector_status_check(collector_id)

get collector status check

get collector status check

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | The collector ID

try:
    # get collector status check
    api_response = api_instance.get_collector_status_check(collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_status_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**| The collector ID | 

### Return type

[**RestCollectorStatusV3**](RestCollectorStatusV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_upgrade_history**
> CollectorUpgradeHistoryPaginationResponse get_collector_upgrade_history()

get collector upgrade history list

get collector upgrade history list

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # get collector upgrade history list
    api_response = api_instance.get_collector_upgrade_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collector_upgrade_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectorUpgradeHistoryPaginationResponse**](CollectorUpgradeHistoryPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_version_list**
> CollectorVersionPaginationResponse get_collector_version_list(fields=fields, size=size, offset=offset, filter=filter)

get collector version list

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

# **get_collectors_by_group_id**
> CollectorPaginationResponse get_collectors_by_group_id(id)

get collectors by collector group id

get collectors by collector group id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 56 # int | The collector group ID

try:
    # get collectors by collector group id
    api_response = api_instance.get_collectors_by_group_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_collectors_by_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The collector group ID | 

### Return type

[**CollectorPaginationResponse**](CollectorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_source_by_id**
> ConfigSource get_config_source_by_id(id, format=format)

Get config source by ID

Retrieve a config source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get config source by ID
    api_response = api_instance.get_config_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_config_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

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

Get config source list

Retrieve a list of config sources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get config source list
    api_response = api_instance.get_config_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_config_source_list: %s\n" % e)
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
template = true # bool |  (optional)
format = 'format_example' # str |  (optional)
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
 **template** | **bool**|  | [optional] 
 **format** | **str**|  | [optional] 
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

Get dashboard group by ID

Retrieves a dashboard group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
template = true # bool |  (optional)
format = 'format_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # Get dashboard group by ID
    api_response = api_instance.get_dashboard_group_by_id(id, template=template, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_dashboard_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **template** | **bool**|  | [optional] 
 **format** | **str**|  | [optional] 
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

Get dashboard list

Retrieves a list of dashboards

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get dashboard list
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

Get datasource overview graph by ID

Retrieves a datasource overview graph based on the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get datasource overview graph by ID
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

Get datasource overview graph list

Retrieves the list of datasource overview graphs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get datasource overview graph list
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

Get datasource by ID

Retrieves a datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # Get datasource by ID
    api_response = api_instance.get_datasource_by_id(id, format=format, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 
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

Get datasource list

Retrieves a list of datasources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get datasource list
    api_response = api_instance.get_datasource_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_datasource_list: %s\n" % e)
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
collector_id = 56 # int |  (optional)

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
 **collector_id** | **int**|  | [optional] 

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
> Device get_device_by_id(id, end=end, netflow_filter=netflow_filter, start=start, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp, fields=fields)

get device by id

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
need_stc_grp_and_sorted_cp = true # bool |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get device by id
    api_response = api_instance.get_device_by_id(id, end=end, netflow_filter=netflow_filter, start=start, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **need_stc_grp_and_sorted_cp** | **bool**|  | [optional] 
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
> DeviceDataSourceInstanceConfig get_device_config_source_config_by_id(instance_id, device_id, hds_id, id, format=format, start_epoch=start_epoch, fields=fields)

get a config for a device

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
instance_id = 56 # int | 
device_id = 56 # int | 
hds_id = 56 # int | 
id = 'id_example' # str | 
format = 'format_example' # str |  (optional)
start_epoch = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # get a config for a device
    api_response = api_instance.get_device_config_source_config_by_id(instance_id, device_id, hds_id, id, format=format, start_epoch=start_epoch, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **str**|  | 
 **format** | **str**|  | [optional] 
 **start_epoch** | **int**|  | [optional] 
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
> DeviceDatasourceInstanceConfigPaginationResponse get_device_config_source_config_list(instance_id, device_id, hds_id, fields=fields, size=size, offset=offset, filter=filter)

get detailed config information for the instance

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
instance_id = 56 # int | 
device_id = 56 # int | 
hds_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get detailed config information for the instance
    api_response = api_instance.get_device_config_source_config_list(instance_id, device_id, hds_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_config_source_config_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
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

Get device datasource

Retrieve a specific device datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device datasource
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

Get device datasource data

Retrieve data for a specific device datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
period = 1.2 # float |  (optional)
start = 789 # int |  (optional)
end = 789 # int |  (optional)
datapoints = 'datapoints_example' # str |  (optional)
format = 'format_example' # str |  (optional)
aggregate = 'aggregate_example' # str | The aggregate option (optional)

try:
    # Get device datasource data
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
 **period** | **float**|  | [optional] 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 
 **aggregate** | **str**| The aggregate option | [optional] 

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
> DeviceDataSourceInstanceAlertSettingPaginationResponse get_device_datasource_instance_alert_setting_list_of_device(device_id, end=end, netflow_filter=netflow_filter, start=start, size=size, offset=offset)

get a list of alert settings for a device

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # get a list of alert settings for a device
    api_response = api_instance.get_device_datasource_instance_alert_setting_list_of_device(device_id, end=end, netflow_filter=netflow_filter, start=start, size=size, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_alert_setting_list_of_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
period = 1.2 # float |  (optional)
start = 789 # int |  (optional)
end = 789 # int |  (optional)
datapoints = 'datapoints_example' # str |  (optional)
format = 'format_example' # str |  (optional)

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
 **period** | **float**|  | [optional] 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 

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
> DeviceDataSourceInstanceGroup get_device_datasource_instance_group_by_id(device_ds_id, device_id, id, fields=fields)

Get device datasource instance group

Retrieve a specific device datasource instance group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
id = 56 # int | 
fields = 'fields_example' # str |  (optional)

try:
    # Get device datasource instance group
    api_response = api_instance.get_device_datasource_instance_group_by_id(device_ds_id, device_id, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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
> DeviceDatasourceInstanceGroupPaginationResponse get_device_datasource_instance_group_list(device_ds_id, device_id, fields=fields, size=size, offset=offset, filter=filter)

Get device datasource instance group list

Retrieve a paginated list of device datasource instance groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get device datasource instance group list
    api_response = api_instance.get_device_datasource_instance_group_list(device_ds_id, device_id, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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
> GraphPlot get_device_datasource_instance_group_overview_graph_data(device_ds_id, device_id, dsig_id, ograph_id, start=start, end=end, format=format)

Get device instance group overview graph data

Retrieve graph data for the overview of a device instance group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
dsig_id = 56 # int | 
ograph_id = 56 # int | 
start = 789 # int |  (optional)
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # Get device instance group overview graph data
    api_response = api_instance.get_device_datasource_instance_group_overview_graph_data(device_ds_id, device_id, dsig_id, ograph_id, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_datasource_instance_group_overview_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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

Get device datasource list

Retrieve a paginated list of device datasources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device datasource list
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

# **get_device_eventsource_list**
> RestDeviceEventsourcePaginationResponse get_device_eventsource_list(device_id)

Get device eventsource list

Retrieve a paginated list of device eventsources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

try:
    # Get device eventsource list
    api_response = api_instance.get_device_eventsource_list(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_eventsource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 

### Return type

[**RestDeviceEventsourcePaginationResponse**](RestDeviceEventsourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> DeviceGroup get_device_group_by_id(id, fields=fields)

get device group

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

Get device group datasource alert setting

Retrieve the alert setting for a specific device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device group datasource alert setting
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
include_disabled_data_source_without_instance = true # bool |  (optional)
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
 **include_disabled_data_source_without_instance** | **bool**|  | [optional] 
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

Get device group property by name

Retrieve a specific device group property by its name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device group property by name
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

Get device group properties

Retrieve a paginated list of properties for a specific device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device group properties
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
> DeviceDatasourceInstancePaginationResponse get_device_instance_list(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)

get device instance list

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get device instance list
    api_response = api_instance.get_device_instance_list(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
> DevicePaginationResponse get_device_list(end=end, netflow_filter=netflow_filter, start=start, include_deleted_resources=include_deleted_resources, fields=fields, size=size, offset=offset, filter=filter)

Get device list

Retrieve a paginated list of devices

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
include_deleted_resources = true # bool |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get device list
    api_response = api_instance.get_device_list(end=end, netflow_filter=netflow_filter, start=start, include_deleted_resources=include_deleted_resources, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_device_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **include_deleted_resources** | **bool**|  | [optional] 
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

Get device property by name

Retrieve a specific device property by its name

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device property by name
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

Get device properties

Retrieve a paginated list of properties for a specific device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get device properties
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

# **get_diagnostic_remediation_assigned_sources**
> DiagnosticRemediationAssignedSource get_diagnostic_remediation_assigned_sources(resource_id=resource_id, alert_id=alert_id, module_type=module_type)

List assigned diagnostic and remediation exchange modules

Returns id, type, name, description, appliesTo, and group. Supply resourceId or alertId (optional moduleType). Use standard v3 list params: filter (e.g. filter=name~Playbook), sort, fields, size, offset, query.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
resource_id = 56 # int |  (optional)
alert_id = 'alert_id_example' # str |  (optional)
module_type = 'module_type_example' # str |  (optional)

try:
    # List assigned diagnostic and remediation exchange modules
    api_response = api_instance.get_diagnostic_remediation_assigned_sources(resource_id=resource_id, alert_id=alert_id, module_type=module_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_diagnostic_remediation_assigned_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **int**|  | [optional] 
 **alert_id** | **str**|  | [optional] 
 **module_type** | **str**|  | [optional] 

### Return type

[**DiagnosticRemediationAssignedSource**](DiagnosticRemediationAssignedSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_remediation_execution_results**
> AdrOutputList get_diagnostic_remediation_execution_results(alert_id=alert_id, host_id=host_id, module_type=module_type, diagnostic_source_id=diagnostic_source_id, diagnostic_source_name=diagnostic_source_name, remediation_source_id=remediation_source_id, remediation_source_name=remediation_source_name, start_time_ms=start_time_ms, end_time_ms=end_time_ms, per_page_count=per_page_count, page_offset_count=page_offset_count, cursor=cursor, remediation_cursor=remediation_cursor)

Get diagnostic and remediation execution results (canonical)

Requires exactly one of query alertId or hostId (resource / device id). Optional moduleType: diagnostic, remediation, or both (default when omitted). Alert: set both startTimeMs and endTimeMs (epoch milliseconds) for history in that window; otherwise latest in the alert window. Device: without both times, at most one latest row; with both times, history with paging (module id or name required per side). Cursors are not supported when moduleType is both.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
alert_id = 'alert_id_example' # str |  (optional)
host_id = 56 # int |  (optional)
module_type = 'module_type_example' # str |  (optional)
diagnostic_source_id = 56 # int |  (optional)
diagnostic_source_name = 'diagnostic_source_name_example' # str |  (optional)
remediation_source_id = 56 # int |  (optional)
remediation_source_name = 'remediation_source_name_example' # str |  (optional)
start_time_ms = 789 # int |  (optional)
end_time_ms = 789 # int |  (optional)
per_page_count = 56 # int |  (optional)
page_offset_count = 56 # int |  (optional)
cursor = 'cursor_example' # str |  (optional)
remediation_cursor = 'remediation_cursor_example' # str |  (optional)

try:
    # Get diagnostic and remediation execution results (canonical)
    api_response = api_instance.get_diagnostic_remediation_execution_results(alert_id=alert_id, host_id=host_id, module_type=module_type, diagnostic_source_id=diagnostic_source_id, diagnostic_source_name=diagnostic_source_name, remediation_source_id=remediation_source_id, remediation_source_name=remediation_source_name, start_time_ms=start_time_ms, end_time_ms=end_time_ms, per_page_count=per_page_count, page_offset_count=page_offset_count, cursor=cursor, remediation_cursor=remediation_cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_diagnostic_remediation_execution_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | [optional] 
 **host_id** | **int**|  | [optional] 
 **module_type** | **str**|  | [optional] 
 **diagnostic_source_id** | **int**|  | [optional] 
 **diagnostic_source_name** | **str**|  | [optional] 
 **remediation_source_id** | **int**|  | [optional] 
 **remediation_source_name** | **str**|  | [optional] 
 **start_time_ms** | **int**|  | [optional] 
 **end_time_ms** | **int**|  | [optional] 
 **per_page_count** | **int**|  | [optional] 
 **page_offset_count** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **remediation_cursor** | **str**|  | [optional] 

### Return type

[**AdrOutputList**](AdrOutputList.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_sources_by_id**
> DiagnosticsSource get_diagnostic_sources_by_id(id, format=format)

Get diagnostics sources by ID

Retrieves a diagnostics source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get diagnostics sources by ID
    api_response = api_instance.get_diagnostic_sources_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_diagnostic_sources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**DiagnosticsSource**](DiagnosticsSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostic_sources_list**
> DiagnosticsourcePaginationResponse get_diagnostic_sources_list()

Get diagnostics sources list

Retrieves a list of diagnostics sources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get diagnostics sources list
    api_response = api_instance.get_diagnostic_sources_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_diagnostic_sources_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsourcePaginationResponse**](DiagnosticsourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_escalation_chain_by_id**
> EscalatingChain get_escalation_chain_by_id(id, fields=fields)

Get escalation chain by ID

Retrieve details of a specific escalation chain by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get escalation chain by ID
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

Get escalation chain list

Retrieve a paginated list of escalation chains

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get escalation chain list
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

Get event source by ID

Retrieves an event source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get event source by ID
    api_response = api_instance.get_event_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_event_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

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

Get event source list

Retrieves the list of event sources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get event source list
    api_response = api_instance.get_event_source_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_event_source_list: %s\n" % e)
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

# **get_focus_cost_usage**
> get_focus_cost_usage(feature=feature, dimension_key=dimension_key, start_time=start_time, end_time=end_time, at=at, metric_qualifier=metric_qualifier, usage_breakdown_type=usage_breakdown_type, usage_breakdown_units=usage_breakdown_units, sku=sku, tenant_ids=tenant_ids, size=size, offset=offset)

FOCUS Cost and Usage shaped usage export

Returns usage rows aligned with FOCUS v1.3 Cost and Usage column identifiers, sourced from Usage Reporting Service (same contract as usage top contributors).

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
feature = 'feature_example' # str |  (optional)
dimension_key = 'dimension_key_example' # str |  (optional)
start_time = 789 # int |  (optional)
end_time = 789 # int |  (optional)
at = 789 # int |  (optional)
metric_qualifier = 'metric_qualifier_example' # str |  (optional)
usage_breakdown_type = 'usage_breakdown_type_example' # str |  (optional)
usage_breakdown_units = 'usage_breakdown_units_example' # str |  (optional)
sku = 'sku_example' # str |  (optional)
tenant_ids = ['tenant_ids_example'] # list[str] |  (optional)
size = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # FOCUS Cost and Usage shaped usage export
    api_instance.get_focus_cost_usage(feature=feature, dimension_key=dimension_key, start_time=start_time, end_time=end_time, at=at, metric_qualifier=metric_qualifier, usage_breakdown_type=usage_breakdown_type, usage_breakdown_units=usage_breakdown_units, sku=sku, tenant_ids=tenant_ids, size=size, offset=offset)
except ApiException as e:
    print("Exception when calling LMApi->get_focus_cost_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | **str**|  | [optional] 
 **dimension_key** | **str**|  | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **at** | **int**|  | [optional] 
 **metric_qualifier** | **str**|  | [optional] 
 **usage_breakdown_type** | **str**|  | [optional] 
 **usage_breakdown_units** | **str**|  | [optional] 
 **sku** | **str**|  | [optional] 
 **tenant_ids** | [**list[str]**](str.md)|  | [optional] 
 **size** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_device_list_by_device_group_id**
> DevicePaginationResponse get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get immediate devices under group

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

Get integration audit logs list

Retrieves the list of integration audit logs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get integration audit logs list
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

Get JobMonitor by ID

Retrieve a specific JobMonitor using its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get JobMonitor by ID
    api_response = api_instance.get_job_monitor_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_job_monitor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

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

Retrieve a paginated list of Job Monitors

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get JobMonitor List
    api_response = api_instance.get_job_monitor_list(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_job_monitor_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

[**BatchJobPaginationResponse**](BatchJobPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_alert_group_by_id**
> RestLogPipelineV3 get_log_alert_group_by_id(pipeline_id)

Retrieve a LogAlertGroup by ID

Handles the retrieval of a specific LogAlertGroup by its ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
pipeline_id = 56 # int | 

try:
    # Retrieve a LogAlertGroup by ID
    api_response = api_instance.get_log_alert_group_by_id(pipeline_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_alert_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **int**|  | 

### Return type

[**RestLogPipelineV3**](RestLogPipelineV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_alert_groups_list**
> PipelinePaginationResponse get_log_alert_groups_list()

Retrieve all LogAlertGroups

Handles the retrieval of all LogAlertGroups.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Retrieve all LogAlertGroups
    api_response = api_instance.get_log_alert_groups_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_alert_groups_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelinePaginationResponse**](PipelinePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_alerts**
> PipelineProcessorPaginationResponse get_log_alerts()

Retrieve all LogAlerts

Handles the retrieval of all LogAlerts.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Retrieve all LogAlerts
    api_response = api_instance.get_log_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelineProcessorPaginationResponse**](PipelineProcessorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_alerts_by_id**
> RestLogPipelineProcessorV3 get_log_alerts_by_id(processor_id)

Retrieve a LogAlerts by ID

Handles the retrieval of a specific LogAlerts by ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
processor_id = 56 # int | 

try:
    # Retrieve a LogAlerts by ID
    api_response = api_instance.get_log_alerts_by_id(processor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_alerts_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_id** | **int**|  | 

### Return type

[**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_queries_by_group_id**
> object get_log_queries_by_group_id(id)

Get log queries by group ID

Fetch log queries belonging to a log query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get log queries by group ID
    api_response = api_instance.get_log_queries_by_group_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_queries_by_group_id: %s\n" % e)
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

# **get_log_query_group_by_id**
> LogQueryGroup get_log_query_group_by_id(id)

Get log query group by ID

Fetch a log query group by ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get log query group by ID
    api_response = api_instance.get_log_query_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_query_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**LogQueryGroup**](LogQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_query_group_list**
> LogQueryGroupPaginationResponse get_log_query_group_list()

Get log query group list

Get all log query groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get log query group list
    api_response = api_instance.get_log_query_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_query_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogQueryGroupPaginationResponse**](LogQueryGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_query_group_list_by_group_type**
> LogQueryGroupPaginationResponse get_log_query_group_list_by_group_type(group_type, all_groups=all_groups)

Get log query groups by groupType

Returns log query groups filtered by the provided groupType. If allGroups=true, returns all groups (subject to permissions); otherwise returns groups for the current user.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
group_type = 'group_type_example' # str | 
all_groups = true # bool |  (optional)

try:
    # Get log query groups by groupType
    api_response = api_instance.get_log_query_group_list_by_group_type(group_type, all_groups=all_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_query_group_list_by_group_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_type** | **str**|  | 
 **all_groups** | **bool**|  | [optional] 

### Return type

[**LogQueryGroupPaginationResponse**](LogQueryGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_source_by_id**
> LogSource get_log_source_by_id(id, format=format)

Get log source

Retrieves a specific log source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get log source
    api_response = api_instance.get_log_source_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **format** | **str**|  | [optional] 

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

Get log source list

Retrieves a list of log sources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get log source list
    api_response = api_instance.get_log_source_list(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_log_source_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

[**LogSourcePaginationResponse**](LogSourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_summary**
> CompanyMetricsSummary get_metrics_summary()

get metrics usage with company settings summary

get metrics usage with company settings summary

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # get metrics usage with company settings summary
    api_response = api_instance.get_metrics_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_metrics_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompanyMetricsSummary**](CompanyMetricsSummary.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_usage**
> Usage get_metrics_usage()

Get metrics usage

Retrieve the metrics usage information

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get metrics usage
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
> EndpointPaginationResponse get_netflow_endpoint_list(id, end=end, netflow_filter=netflow_filter, start=start, port=port, fields=fields, size=size, offset=offset, filter=filter)

get netflow endpoints

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
port = 'port_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow endpoints
    api_response = api_instance.get_netflow_endpoint_list(id, end=end, netflow_filter=netflow_filter, start=start, port=port, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_endpoint_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
> FlowRecordPaginationResponse get_netflow_flow_list(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)

get netflow flows

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow flows
    api_response = api_instance.get_netflow_flow_list(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_flow_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
> PortPaginationResponse get_netflow_port_list(id, end=end, netflow_filter=netflow_filter, start=start, ip=ip, fields=fields, size=size, offset=offset, filter=filter)

get netflow ports

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
ip = 'ip_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get netflow ports
    api_response = api_instance.get_netflow_port_list(id, end=end, netflow_filter=netflow_filter, start=start, ip=ip, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_netflow_port_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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

Get netscan by ID

Retrieve a specific netscan by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get netscan by ID
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

Get netscan list

Retrieve a list of netscans

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get netscan list
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

Get OID by ID

Retrieve the OID details by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get OID by ID
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

Get OID's list

Retrieve the list of OIDs

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get OID's list
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
id = 56 # int | 

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
 **id** | **int**|  | 

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

Get property rules by id

Fetches a property rule by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get property rules by id
    api_response = api_instance.get_property_rules_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_property_rules_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

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

Get property rules list

Fetches a list of property rules

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get property rules list
    api_response = api_instance.get_property_rules_list(format=format, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_property_rules_list: %s\n" % e)
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

[**PropertyRulePaginationResponse**](PropertyRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipient_group_by_id**
> RecipientGroup get_recipient_group_by_id(id)

Get recipient group by id

Retrieve a specific recipient group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get recipient group by id
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

Get recipient group list

Retrieve a paginated list of recipient groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get recipient group list
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

# **get_recommendation_by_id**
> RestCloudRecommendationV3 get_recommendation_by_id(id, fields=fields)

Get recommendation by ID

Retrieves a recommendation by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
id = 'id_example' # str | an alphanumeric identifier composed of the recommendation's database ID, the associated resource ID, and the recommendation type, delimited with hyphens, e.g. 123-456-EBS_UNATTACHED
fields = 'fields_example' # str |  (optional)

try:
    # Get recommendation by ID
    api_response = api_instance.get_recommendation_by_id(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recommendation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| an alphanumeric identifier composed of the recommendation&#x27;s database ID, the associated resource ID, and the recommendation type, delimited with hyphens, e.g. 123-456-EBS_UNATTACHED | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestCloudRecommendationV3**](RestCloudRecommendationV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendation_categories_list**
> RestCloudRecommendationCategoryV3 get_recommendation_categories_list(fields=fields, size=size, offset=offset, filter=filter)

Get recommendation category list

Retrieves the list of recommendation categories

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get recommendation category list
    api_response = api_instance.get_recommendation_categories_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recommendation_categories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestCloudRecommendationCategoryV3**](RestCloudRecommendationCategoryV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommendations_list**
> RestCloudRecommendationV3 get_recommendations_list(fields=fields, size=size, offset=offset, filter=filter)

Get recommendation list

Retrieves a list of recommendations

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
size = 50 # int | The number of recommendations to return. Max permitted value is 500 (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str | Filtering is available with the : (equals) operator for recommendationStatus and recommendationCategory. Only one value at a time is supported for recommendationCategory, but multiple recommendationStatuses may be filtered on with the | (OR) operator. Also, only the , (AND) relation is supported when combining multiple filters (optional)

try:
    # Get recommendation list
    api_response = api_instance.get_recommendations_list(fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_recommendations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**| The number of recommendations to return. Max permitted value is 500 | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**| Filtering is available with the : (equals) operator for recommendationStatus and recommendationCategory. Only one value at a time is supported for recommendationCategory, but multiple recommendationStatuses may be filtered on with the | (OR) operator. Also, only the , (AND) relation is supported when combining multiple filters | [optional] 

### Return type

[**RestCloudRecommendationV3**](RestCloudRecommendationV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remediation_sources_by_id**
> RemediationSource get_remediation_sources_by_id(id, format=format)

Get remediation sources by ID

Retrieves a remediation source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
format = 'format_example' # str |  (optional)

try:
    # Get remediation sources by ID
    api_response = api_instance.get_remediation_sources_by_id(id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_remediation_sources_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **format** | **str**|  | [optional] 

### Return type

[**RemediationSource**](RemediationSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remediation_sources_list**
> RemediationSourcePaginationResponse get_remediation_sources_list()

Get remediation sources list

Retrieves a list of remediation sources

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get remediation sources list
    api_response = api_instance.get_remediation_sources_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_remediation_sources_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RemediationSourcePaginationResponse**](RemediationSourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_id**
> ReportBase get_report_by_id(id, fields=fields)

Get report by ID

Retrieve the details of a specific report by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get report by ID
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

Get report group by id

Retrieve a specific report group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get report group by id
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

Get report group list

Retrieve a paginated list of report groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get report group list
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
> ReportPaginationResponse get_report_list(show_next_gen_reports=show_next_gen_reports, fields=fields, size=size, offset=offset, filter=filter)

Get report list

Retrieve a paginated list of reports

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
show_next_gen_reports = true # bool |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get report list
    api_response = api_instance.get_report_list(show_next_gen_reports=show_next_gen_reports, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_report_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_next_gen_reports** | **bool**|  | [optional] 
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

Get role by ID

Retrieve details of a specific role by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get role by ID
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

Get role list

Retrieve a paginated list of roles

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
exclude_admin = true # bool |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get role list
    api_response = api_instance.get_role_list(exclude_admin=exclude_admin, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_role_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_admin** | **bool**|  | [optional] 
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

Get SDT history for the device dataSource

Retrieve the SDT (Service Disruption Time) history for a specific device dataSource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get SDT history for the device dataSource
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
> DeviceSDTHistoryPaginationResponse get_sdt_history_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)

get SDT history for the device

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # get SDT history for the device
    api_response = api_instance.get_sdt_history_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_sdt_history_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
> SiteMonitorCheckPointPaginationResponse get_site_monitor_check_point_list(type=type, fields=fields, size=size, offset=offset, filter=filter)

Get website checkpoint list

Retrieves the list of website checkpoints

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
type = 'type_example' # str | Type of checkpoint to filter. If not specified, returns website legacy checkpoints. (optional)
fields = 'fields_example' # str |  (optional)
size = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)
filter = 'filter_example' # str |  (optional)

try:
    # Get website checkpoint list
    api_response = api_instance.get_site_monitor_check_point_list(type=type, fields=fields, size=size, offset=offset, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_site_monitor_check_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of checkpoint to filter. If not specified, returns website legacy checkpoints. | [optional] 
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
> GraphPlot get_top_talkers_graph(id, end=end, netflow_filter=netflow_filter, start=start, format=format, keyword=keyword)

get top talkers graph

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
format = 'format_example' # str |  (optional)
keyword = 'keyword_example' # str |  (optional)

try:
    # get top talkers graph
    api_response = api_instance.get_top_talkers_graph(id, end=end, netflow_filter=netflow_filter, start=start, format=format, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_top_talkers_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
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
format = 'format_example' # str |  (optional)

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
 **format** | **str**|  | [optional] 

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

# **get_tracked_query_group_by_id**
> TrackedQueryGroup get_tracked_query_group_by_id(id)

Get tracked query group by ID

Fetch a tracked query group by ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get tracked query group by ID
    api_response = api_instance.get_tracked_query_group_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_tracked_query_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TrackedQueryGroup**](TrackedQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracked_query_group_list**
> TrackQueryGroupPaginationResponse get_tracked_query_group_list()

Get tracked query group list

Get all tracked query groups

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get tracked query group list
    api_response = api_instance.get_tracked_query_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_tracked_query_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrackQueryGroupPaginationResponse**](TrackQueryGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmonitored_device_list**
> UnmonitoredDevicePaginationResponse get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)

Get unmonitored device list

Retrieve a paginated list of unmonitored devices

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get unmonitored device list
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

Get update history for a configSource

Retrieve the list of update reasons/history for a specific configSource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get update history for a configSource
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

Get update history for a datasource

Retrieves the update history for a specific datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get update history for a datasource
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
need_message = true # bool |  (optional)
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
 **need_message** | **bool**|  | [optional] 
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
format = 'format_example' # str |  (optional)

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
 **format** | **str**|  | [optional] 

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
period = 1.2 # float |  (optional)
start = 789 # int |  (optional)
end = 789 # int |  (optional)
datapoints = 'datapoints_example' # str |  (optional)
format = 'format_example' # str |  (optional)
aggregate = 'aggregate_example' # str | the aggregate option (optional)

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
 **period** | **float**|  | [optional] 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] 
 **aggregate** | **str**| the aggregate option | [optional] 

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
start = 789 # int |  (optional)
end = 789 # int |  (optional)
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

# **get_website_graph_data**
> GraphPlot get_website_graph_data(checkpoint_id, website_id, graph_name, end=end, start=start, format=format)

Get website graph data

Retrieves the graph data for a website

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
checkpoint_id = 56 # int | 
website_id = 56 # int | 
graph_name = 'graph_name_example' # str | 
end = 789 # int |  (optional)
start = 789 # int |  (optional)
format = 'format_example' # str |  (optional)

try:
    # Get website graph data
    api_response = api_instance.get_website_graph_data(checkpoint_id, website_id, graph_name, end=end, start=start, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_website_graph_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkpoint_id** | **int**|  | 
 **website_id** | **int**|  | 
 **graph_name** | **str**|  | 
 **end** | **int**|  | [optional] 
 **start** | **int**|  | [optional] 
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

Get widget by ID

Retrieves a widget by its ID. Based on widget type, the response may contain additional attributes. Please refer to the models corresponding to specific widget types at the bottom of this page for detailed attributes.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get widget by ID
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
> WidgetData get_widget_data_by_id(id, end=end, format=format, start=start)

get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)

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
end = 789 # int |  (optional)
format = 'format_example' # str |  (optional)
start = 789 # int |  (optional)

try:
    # get widget data (Based upon widget type the response may contain additional attributes. Please refer models corresponding to specific widget type at the bottom of this page to check the attributes)
    api_response = api_instance.get_widget_data_by_id(id, end=end, format=format, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->get_widget_data_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 

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

Get widget list

Retrieves a list of widgets. Based on widget type, the response may contain additional attributes. Please refer to the models corresponding to specific widget types at the bottom of this page for detailed attributes.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Get widget list
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

# **import_applies_to_function_json**
> AppliesToFunction import_applies_to_function_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import AppliesTo function via json

Import a AppliesTo function using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import AppliesTo function via json
    api_response = api_instance.import_applies_to_function_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_applies_to_function_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**AppliesToFunction**](AppliesToFunction.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_batch_job**
> object import_batch_job(file)

Import batch job via XML

Import a batch job using XML data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Import batch job via XML
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

Import config source via XML

Import configuration source data from an XML file

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Import config source via XML
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

# **import_config_source_json**
> ConfigSource import_config_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import ConfigSource via json

Import a ConfigSource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import ConfigSource via json
    api_response = api_instance.import_config_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_config_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ConfigSource**](ConfigSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data_source**
> object import_data_source(file)

Import datasource via XML

Imports a datasource from an XML file

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Import datasource via XML
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

# **import_data_source_json**
> DataSource import_data_source_json(file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import DataSource via json

Import a DataSource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import DataSource via json
    api_response = api_instance.import_data_source_json(file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_data_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_diagnostic_source_json**
> RestDiagnosticSourceV4 import_diagnostic_source_json(file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import DiagnosticSource via json

Import a DiagnosticSource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import DiagnosticSource via json
    api_response = api_instance.import_diagnostic_source_json(file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_diagnostic_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RestDiagnosticSourceV4**](RestDiagnosticSourceV4.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_event_source**
> object import_event_source(file)

Import event source via XML

Imports an event source from an XML file

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Import event source via XML
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

# **import_event_source_json**
> EventSource import_event_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import EventSource via json

Import a EventSource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import EventSource via json
    api_response = api_instance.import_event_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_event_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**EventSource**](EventSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_job_monitor_json**
> BatchJob import_job_monitor_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import batch JobMonitor via json

Import a JobMonitor using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import batch JobMonitor via json
    api_response = api_instance.import_job_monitor_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_job_monitor_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**BatchJob**](BatchJob.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_log_query_groups**
> list[RestLogQueryGroupImportResult] import_log_query_groups(body=body, group_type=group_type)

Import log query groups and queries (best-effort)

Validates the payload, then persists every query that passes validation and returns per-item status with reasons for any unimported entries. HTTP 200 when all imported, 207 on partial success, 500 on fatal error.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
body = [logicmonitor_sdk.RestLogQueryGroupValidationRequestItemV4()] # list[RestLogQueryGroupValidationRequestItemV4] |  (optional)
group_type = 'group_type_example' # str |  (optional)

try:
    # Import log query groups and queries (best-effort)
    api_response = api_instance.import_log_query_groups(body=body, group_type=group_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_log_query_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RestLogQueryGroupValidationRequestItemV4]**](RestLogQueryGroupValidationRequestItemV4.md)|  | [optional] 
 **group_type** | **str**|  | [optional] 

### Return type

[**list[RestLogQueryGroupImportResult]**](RestLogQueryGroupImportResult.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_log_source_json**
> LogSource import_log_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import LogSource via json

Import a LogSource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import LogSource via json
    api_response = api_instance.import_log_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_log_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**LogSource**](LogSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_oid_json**
> RestOidV3 import_oid_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import OID via json

Import a OID using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import OID via json
    api_response = api_instance.import_oid_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_oid_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RestOidV3**](RestOidV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_property_source_json**
> PropertyRule import_property_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import PropertySource via json

Import a PropertySource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import PropertySource via json
    api_response = api_instance.import_property_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_property_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**PropertyRule**](PropertyRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_topology_source_json**
> TopologySource import_topology_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)

Import TopologySource via json

Import a TopologySource using json data

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
file = 'file_example' # str |  (optional)
handle_conflict = 'handle_conflict_example' # str |  (optional)
fields_to_preserve = ['fields_to_preserve_example'] # list[str] |  (optional)

try:
    # Import TopologySource via json
    api_response = api_instance.import_topology_source_json(file=file, handle_conflict=handle_conflict, fields_to_preserve=fields_to_preserve)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->import_topology_source_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **handle_conflict** | **str**|  | [optional] 
 **fields_to_preserve** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TopologySource**](TopologySource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_un_map_module_to_access_group**
> RestMapModuleV3 map_un_map_module_to_access_group(body=body)

Create a mapping of access group & module

Map a module to an access group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **move_log_queries**
> object move_log_queries(id, body)

Move log queries to another group

Move one or more log queries into a different log query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = ['body_example'] # list[str] | 

try:
    # Move log queries to another group
    api_response = api_instance.move_log_queries(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->move_log_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**list[str]**](str.md)|  | 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partition_action**
> LogPartition partition_action(id, action)

Perform an action on a specified log partition

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
id = 56 # int | 
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
 **id** | **int**|  | 
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

# **patch_action_chain_by_id**
> ActionChain patch_action_chain_by_id(id, body)

update action chain

update action chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionChain() # ActionChain | 

try:
    # update action chain
    api_response = api_instance.patch_action_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_action_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionChain**](ActionChain.md)|  | 

### Return type

[**ActionChain**](ActionChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_action_rule_by_id**
> ActionRule patch_action_rule_by_id(id, body)

update action rule

update action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionRule() # ActionRule | 

try:
    # update action rule
    api_response = api_instance.patch_action_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_action_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionRule**](ActionRule.md)|  | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_action_rule_status_by_id**
> ActionRuleStatus patch_action_rule_status_by_id(id, body)

enable/disable action rule

enable/disable action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionRuleStatus() # ActionRuleStatus | 

try:
    # enable/disable action rule
    api_response = api_instance.patch_action_rule_status_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_action_rule_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionRuleStatus**](ActionRuleStatus.md)|  | 

### Return type

[**ActionRuleStatus**](ActionRuleStatus.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_admin_by_id**
> Admin patch_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)

update user

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
change_password = true # bool |  (optional)
validation_only = true # bool |  (optional)

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
 **change_password** | **bool**|  | [optional] 
 **validation_only** | **bool**|  | [optional] 

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

Update API tokens for a user

Update the API tokens for a specific user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update API tokens for a user
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

Update applies to function

Update an existing applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
ignore_reference = true # bool |  (optional)

try:
    # Update applies to function
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
 **ignore_reference** | **bool**|  | [optional] 

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
auto_balance_monitored_devices = true # bool |  (optional)
force_update_failed_over_devices = true # bool |  (optional)
op_type = 'op_type_example' # str |  (optional)

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
 **auto_balance_monitored_devices** | **bool**|  | [optional] 
 **force_update_failed_over_devices** | **bool**|  | [optional] 
 **op_type** | **str**|  | [optional] 

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

Update collector group

Update the details of a specific collector group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
auto_balance_monitored_devices = true # bool |  (optional)
force_update_failed_over_devices = true # bool |  (optional)
op_type = 'op_type_example' # str |  (optional)

try:
    # Update collector group
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
 **auto_balance_monitored_devices** | **bool**|  | [optional] 
 **force_update_failed_over_devices** | **bool**|  | [optional] 
 **op_type** | **str**|  | [optional] 

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

Update config source by ID

Update the config source details based on the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update config source by ID
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
overwrite_group_fields = true # bool |  (optional)

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
 **overwrite_group_fields** | **bool**|  | [optional] 

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

Update datasource

Updates a datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
force_unique_identifier = true # bool |  (optional)
force_restricted_change_key = 'force_restricted_change_key_example' # str |  (optional)

try:
    # Update datasource
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
 **force_unique_identifier** | **bool**|  | [optional] 
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

Update default dashboard

Update the default dashboard settings for a user or group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update default dashboard
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
> Device patch_device(id, body, end=end, netflow_filter=netflow_filter, start=start, op_type=op_type, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)

update a device (Request schema may change depending upon the type of uptime device being updated)

update a device (Request schema may change depending upon the type of uptime device being updated)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
op_type = 'op_type_example' # str |  (optional)
need_stc_grp_and_sorted_cp = true # bool |  (optional)

try:
    # update a device (Request schema may change depending upon the type of uptime device being updated)
    api_response = api_instance.patch_device(id, body, end=end, netflow_filter=netflow_filter, start=start, op_type=op_type, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **op_type** | **str**|  | [optional] 
 **need_stc_grp_and_sorted_cp** | **bool**|  | [optional] 

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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup patch_device_datasource_instance_group_by_id(device_ds_id, device_id, id, body)

Update device datasource instance group

Update a specific device datasource instance group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # Update device datasource instance group
    api_response = api_instance.patch_device_datasource_instance_group_by_id(device_ds_id, device_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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

Update device group datasource alert setting

Update the alert setting for a specific device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device group datasource alert setting
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

Update device group property

Update a specific property of a device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device group property
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

Update device property

Update a specific property of a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device property
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

# **patch_diagnostic_source_by_id**
> DiagnosticsSource patch_diagnostic_source_by_id(id, body=body, reason=reason)

Update a diagnostics source

Updates a diagnostics source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.DiagnosticsSource() # DiagnosticsSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update a diagnostics source
    api_response = api_instance.patch_diagnostic_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_diagnostic_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DiagnosticsSource**](DiagnosticsSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**DiagnosticsSource**](DiagnosticsSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_escalation_chain_by_id**
> EscalatingChain patch_escalation_chain_by_id(id, body)

Update escalation chain

Update the details of a specific escalation chain by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update escalation chain
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

Update event source by ID

Updates the event source with the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update event source by ID
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

Update an existing JobMonitor by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **patch_log_alert_group**
> RestLogPipelineV3 patch_log_alert_group(pipeline_id, body)

Update a specific LogAlertGroup by its ID

Handles the update of a specific LogAlertGroup by its ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
pipeline_id = 56 # int | 
body = logicmonitor_sdk.RestLogPipelineV3() # RestLogPipelineV3 | 

try:
    # Update a specific LogAlertGroup by its ID
    api_response = api_instance.patch_log_alert_group(pipeline_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_alert_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **int**|  | 
 **body** | [**RestLogPipelineV3**](RestLogPipelineV3.md)|  | 

### Return type

[**RestLogPipelineV3**](RestLogPipelineV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_alerts**
> RestLogPipelineProcessorV3 patch_log_alerts(processor_id, body)

Update a LogAlerts by ID

Handles the update of a specific LogAlerts by ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
processor_id = 56 # int | 
body = logicmonitor_sdk.RestLogPipelineProcessorV3() # RestLogPipelineProcessorV3 | 

try:
    # Update a LogAlerts by ID
    api_response = api_instance.patch_log_alerts(processor_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_id** | **int**|  | 
 **body** | [**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)|  | 

### Return type

[**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_partition**
> LogPartition patch_log_partition(id, body=body)

Update an existing log partition

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
id = 'id_example' # str | 
body = logicmonitor_sdk.LogPartition() # LogPartition |  (optional)

try:
    # Update an existing log partition
    api_response = api_instance.patch_log_partition(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**LogPartition**](LogPartition.md)|  | [optional] 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_query_group**
> LogQueryGroup patch_log_query_group(id, body)

Update log query group

Modify an existing log query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.LogQueryGroup() # LogQueryGroup | 

try:
    # Update log query group
    api_response = api_instance.patch_log_query_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_log_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**LogQueryGroup**](LogQueryGroup.md)|  | 

### Return type

[**LogQueryGroup**](LogQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_log_source**
> LogSource patch_log_source(id, body=body, reason=reason)

Update log source

Updates an existing log source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update log source
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

Update a netscan

Update an existing netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update a netscan
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

Update an OID

Update the details of an existing OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update an OID
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

Update a property rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Update recipient group

Update a specific recipient group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update recipient group
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

# **patch_remediation_source_by_id**
> RemediationSource patch_remediation_source_by_id(id, body=body, reason=reason)

Update a remediation source

Updates a remediation source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.RemediationSource() # RemediationSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update a remediation source
    api_response = api_instance.patch_remediation_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_remediation_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RemediationSource**](RemediationSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**RemediationSource**](RemediationSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_report_by_id**
> ReportBase patch_report_by_id(id, body)

Update report

Update the details of a specific report by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update report
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

Update report group

Update a specific report group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update report group
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

Update role

Update the details of a specific role by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update role
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

# **patch_tracked_query_group**
> TrackedQueryGroup patch_tracked_query_group(id, body=body)

Update tracked query group

Update an existing tracked query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.TrackedQueryGroup() # TrackedQueryGroup |  (optional)

try:
    # Update tracked query group
    api_response = api_instance.patch_tracked_query_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->patch_tracked_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**TrackedQueryGroup**](TrackedQueryGroup.md)|  | [optional] 

### Return type

[**TrackedQueryGroup**](TrackedQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_website_by_id**
> Website patch_website_by_id(id, body, op_type=op_type)

update website

Update website. Request structure may vary based on the check type {PingCheck | WebCheck model}. Use the respective model in SDK.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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

Update widget

Updates a widget. Based on widget type, the request and response may contain additional attributes. Please refer to the models corresponding to specific widget types at the bottom of this page for detailed attributes.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update widget
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

# **restart_collector_by_id**
> int restart_collector_by_id(collector_id, body=body)

restart collector

restart collector

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | The collector ID
body = logicmonitor_sdk.RestRestartCollectorV3() # RestRestartCollectorV3 | Optional configuration overrides to apply before restarting. All fields default to empty string if omitted. (optional)

try:
    # restart collector
    api_response = api_instance.restart_collector_by_id(collector_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->restart_collector_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**| The collector ID | 
 **body** | [**RestRestartCollectorV3**](RestRestartCollectorV3.md)| Optional configuration overrides to apply before restarting. All fields default to empty string if omitted. | [optional] 

### Return type

**int**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_auto_discovery_by_device_id**
> object schedule_auto_discovery_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start)

schedule active discovery for a device

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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)

try:
    # schedule active discovery for a device
    api_response = api_instance.schedule_auto_discovery_by_device_id(id, end=end, netflow_filter=netflow_filter, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->schedule_auto_discovery_by_device_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 

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

Test AWS account

Test the connection or status of an AWS account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Test AWS account
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

Test SaaS account

Test the connection or status of a SaaS account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Test SaaS account
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

# **trigger_collector_status_check**
> str trigger_collector_status_check(collector_id)

trigger collector status check

trigger collector status check

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
collector_id = 56 # int | The collector ID

try:
    # trigger collector status check
    api_response = api_instance.trigger_collector_status_check(collector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->trigger_collector_status_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**| The collector ID | 

### Return type

**str**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_group**
> AccessGroup update_access_group(id, body)

Update access group

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

# **update_action_chain_by_id**
> ActionChain update_action_chain_by_id(id, body)

update action chain

update action chain

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionChain() # ActionChain | 

try:
    # update action chain
    api_response = api_instance.update_action_chain_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_action_chain_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionChain**](ActionChain.md)|  | 

### Return type

[**ActionChain**](ActionChain.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_action_rule_by_id**
> ActionRule update_action_rule_by_id(id, body)

update action rule

update action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionRule() # ActionRule | 

try:
    # update action rule
    api_response = api_instance.update_action_rule_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_action_rule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionRule**](ActionRule.md)|  | 

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_action_rule_status_by_id**
> ActionRuleStatus update_action_rule_status_by_id(id, body)

enable/disable action rule

enable/disable action rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.ActionRuleStatus() # ActionRuleStatus | 

try:
    # enable/disable action rule
    api_response = api_instance.update_action_rule_status_by_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_action_rule_status_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**ActionRuleStatus**](ActionRuleStatus.md)|  | 

### Return type

[**ActionRuleStatus**](ActionRuleStatus.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_by_id**
> Admin update_admin_by_id(id, body, change_password=change_password, validation_only=validation_only)

update user

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
change_password = true # bool |  (optional)
validation_only = true # bool |  (optional)

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
 **change_password** | **bool**|  | [optional] 
 **validation_only** | **bool**|  | [optional] 

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

Update API tokens for a user

Update the API tokens for a specific user

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update API tokens for a user
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

Update applies to function

Update an existing applies to function

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
ignore_reference = true # bool |  (optional)

try:
    # Update applies to function
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
 **ignore_reference** | **bool**|  | [optional] 

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
auto_balance_monitored_devices = true # bool |  (optional)
force_update_failed_over_devices = true # bool |  (optional)
op_type = 'op_type_example' # str |  (optional)

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
 **auto_balance_monitored_devices** | **bool**|  | [optional] 
 **force_update_failed_over_devices** | **bool**|  | [optional] 
 **op_type** | **str**|  | [optional] 

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

Update collector group

Update the details of a specific collector group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
auto_balance_monitored_devices = true # bool |  (optional)
force_update_failed_over_devices = true # bool |  (optional)
op_type = 'op_type_example' # str |  (optional)

try:
    # Update collector group
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
 **auto_balance_monitored_devices** | **bool**|  | [optional] 
 **force_update_failed_over_devices** | **bool**|  | [optional] 
 **op_type** | **str**|  | [optional] 

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

Update config source by ID

Update the config source details based on the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update config source by ID
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
overwrite_group_fields = true # bool |  (optional)

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
 **overwrite_group_fields** | **bool**|  | [optional] 

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

Update datasource

Updates a datasource by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
force_unique_identifier = true # bool |  (optional)
force_restricted_change_key = 'force_restricted_change_key_example' # str |  (optional)

try:
    # Update datasource
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
 **force_unique_identifier** | **bool**|  | [optional] 
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

Update default dashboard

Update the default dashboard settings for a user or group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update default dashboard
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
> Device update_device(id, body, end=end, netflow_filter=netflow_filter, start=start, op_type=op_type, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)

update a device (Request schema may change depending upon the type of uptime device being updated)

update a device (Request schema may change depending upon the type of uptime device being updated)

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
end = 789 # int |  (optional)
netflow_filter = 'netflow_filter_example' # str |  (optional)
start = 789 # int |  (optional)
op_type = 'op_type_example' # str |  (optional)
need_stc_grp_and_sorted_cp = true # bool |  (optional)

try:
    # update a device (Request schema may change depending upon the type of uptime device being updated)
    api_response = api_instance.update_device(id, body, end=end, netflow_filter=netflow_filter, start=start, op_type=op_type, need_stc_grp_and_sorted_cp=need_stc_grp_and_sorted_cp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**Device**](Device.md)|  | 
 **end** | **int**|  | [optional] 
 **netflow_filter** | **str**|  | [optional] 
 **start** | **int**|  | [optional] 
 **op_type** | **str**|  | [optional] 
 **need_stc_grp_and_sorted_cp** | **bool**|  | [optional] 

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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

### Return type

[**DeviceDataSourceInstance**](DeviceDataSourceInstance.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_group_by_id**
> DeviceDataSourceInstanceGroup update_device_datasource_instance_group_by_id(device_ds_id, device_id, id, body)

Update device datasource instance group

Update a specific device datasource instance group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
id = 56 # int | 
body = logicmonitor_sdk.DeviceDataSourceInstanceGroup() # DeviceDataSourceInstanceGroup | 

try:
    # Update device datasource instance group
    api_response = api_instance.update_device_datasource_instance_group_by_id(device_ds_id, device_id, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_device_datasource_instance_group_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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

Update device group datasource alert setting

Update the alert setting for a specific device group datasource

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device group datasource alert setting
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

Update device group property

Update a specific property of a device group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device group property
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

Update device property

Update a specific property of a device

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update device property
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

# **update_diagnostic_source_by_id**
> DiagnosticsSource update_diagnostic_source_by_id(id, body=body, reason=reason)

Update a diagnostics source

Updates a diagnostics source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.DiagnosticsSource() # DiagnosticsSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update a diagnostics source
    api_response = api_instance.update_diagnostic_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_diagnostic_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DiagnosticsSource**](DiagnosticsSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**DiagnosticsSource**](DiagnosticsSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_disable_log_alerts**
> object update_disable_log_alerts(processor_id, action, body=body)

Enable or disable a LogAlerts by ID

Updates the state of a LogAlerts by ID. The action must be either 'enable' or 'disable'.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
processor_id = 56 # int | 
action = 'action_example' # str | 
body = logicmonitor_sdk.DisableProcessorPayload() # DisableProcessorPayload |  (optional)

try:
    # Enable or disable a LogAlerts by ID
    api_response = api_instance.update_disable_log_alerts(processor_id, action, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_disable_log_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_id** | **int**|  | 
 **action** | **str**|  | 
 **body** | [**DisableProcessorPayload**](DisableProcessorPayload.md)|  | [optional] 

### Return type

**object**

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_escalation_chain_by_id**
> EscalatingChain update_escalation_chain_by_id(id, body)

Update escalation chain

Update the details of a specific escalation chain by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update escalation chain
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

Update event source by ID

Updates the event source with the provided ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update event source by ID
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
> object update_instance_group_alert_threshold(device_ds_id, device_id, dsig_id, dp_id, body=body)

Update instance group alert threshold

Update the alert threshold for an instance group. Setting the threshold at the default group is not allowed.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
device_ds_id = 56 # int | The device-datasource ID you'd like to add an instance group for
device_id = 56 # int | 
dsig_id = 56 # int | 
dp_id = 56 # int | 
body = logicmonitor_sdk.RestDeviceInstanceGroupAlertConfigV3() # RestDeviceInstanceGroupAlertConfigV3 |  (optional)

try:
    # Update instance group alert threshold
    api_response = api_instance.update_instance_group_alert_threshold(device_ds_id, device_id, dsig_id, dp_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_instance_group_alert_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_ds_id** | **int**| The device-datasource ID you&#x27;d like to add an instance group for | 
 **device_id** | **int**|  | 
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

Update an existing JobMonitor by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

# **update_log_alert_group**
> RestLogPipelineV3 update_log_alert_group(pipeline_id, body)

Update a specific LogAlertGroup by its ID

Handles the update of a specific LogAlertGroup by its ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
pipeline_id = 56 # int | 
body = logicmonitor_sdk.RestLogPipelineV3() # RestLogPipelineV3 | 

try:
    # Update a specific LogAlertGroup by its ID
    api_response = api_instance.update_log_alert_group(pipeline_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_alert_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **int**|  | 
 **body** | [**RestLogPipelineV3**](RestLogPipelineV3.md)|  | 

### Return type

[**RestLogPipelineV3**](RestLogPipelineV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_alerts**
> RestLogPipelineProcessorV3 update_log_alerts(processor_id, body)

Update a LogAlerts by ID

Handles the update of a specific LogAlerts by ID.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class test
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))
processor_id = 56 # int | 
body = logicmonitor_sdk.RestLogPipelineProcessorV3() # RestLogPipelineProcessorV3 | 

try:
    # Update a LogAlerts by ID
    api_response = api_instance.update_log_alerts(processor_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processor_id** | **int**|  | 
 **body** | [**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)|  | 

### Return type

[**RestLogPipelineProcessorV3**](RestLogPipelineProcessorV3.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_partition**
> LogPartition update_log_partition(id, body=body)

Update an existing log partition

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
id = 'id_example' # str | 
body = logicmonitor_sdk.LogPartition() # LogPartition |  (optional)

try:
    # Update an existing log partition
    api_response = api_instance.update_log_partition(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_partition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**LogPartition**](LogPartition.md)|  | [optional] 

### Return type

[**LogPartition**](LogPartition.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_query_group**
> LogQueryGroup update_log_query_group(id, body)

Update log query group

Modify an existing log query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.LogQueryGroup() # LogQueryGroup | 

try:
    # Update log query group
    api_response = api_instance.update_log_query_group(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_log_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**LogQueryGroup**](LogQueryGroup.md)|  | 

### Return type

[**LogQueryGroup**](LogQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_log_source**
> LogSource update_log_source(id, body=body, reason=reason)

Update log source

Updates an existing log source

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update log source
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

Update a netscan

Update an existing netscan

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update a netscan
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

Update an OID

Update the details of an existing OID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update an OID
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

Update a property rule by id

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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

Update recipient group

Update a specific recipient group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update recipient group
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

# **update_remediation_source_by_id**
> RemediationSource update_remediation_source_by_id(id, body=body, reason=reason)

Update a remediation source

Updates a remediation source by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.RemediationSource() # RemediationSource |  (optional)
reason = 'reason_example' # str |  (optional)

try:
    # Update a remediation source
    api_response = api_instance.update_remediation_source_by_id(id, body=body, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_remediation_source_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RemediationSource**](RemediationSource.md)|  | [optional] 
 **reason** | **str**|  | [optional] 

### Return type

[**RemediationSource**](RemediationSource.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_report_by_id**
> ReportBase update_report_by_id(id, body)

Update report

Update the details of a specific report by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update report
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

Update report group

Update a specific report group by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update report group
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

Update role

Update the details of a specific role by its ID

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update role
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

# **update_tracked_query_group**
> TrackedQueryGroup update_tracked_query_group(id, body=body)

Update tracked query group

Update an existing tracked query group

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
body = logicmonitor_sdk.TrackedQueryGroup() # TrackedQueryGroup |  (optional)

try:
    # Update tracked query group
    api_response = api_instance.update_tracked_query_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->update_tracked_query_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**TrackedQueryGroup**](TrackedQueryGroup.md)|  | [optional] 

### Return type

[**TrackedQueryGroup**](TrackedQueryGroup.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_website_by_id**
> Website update_website_by_id(id, body, op_type=op_type)

update website

Update website. Request structure may vary based on the check type {PingCheck | WebCheck model}. Use the respective model in SDK.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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
op_type = 'op_type_example' # str |  (optional)

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
 **op_type** | **str**|  | [optional] 

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

Update widget

Updates a widget. Based on widget type, the request and response may contain additional attributes. Please refer to the models corresponding to specific widget types at the bottom of this page for detailed attributes.

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Update widget
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

Verify AWS Billing Permissions

Verify the billing permissions of an AWS account

### Example
```python
from __future__ import print_function
import time
import logicmonitor_sdk
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
    # Verify AWS Billing Permissions
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

