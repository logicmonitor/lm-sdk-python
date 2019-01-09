# logicmonitor.DefaultApi

All URIs are relative to *https://localhost/santaba/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
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

ack alert by id



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertAck**](RestAlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ack_collector_down_alert_by_id**
> RestNullObjectResponse ack_collector_down_alert_by_id(id, body)

ack collector down alert



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestAckCollectorDown**](RestAckCollectorDown.md)|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_admin**
> RestAdminResponse add_admin(body)

add admin



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

# **add_alert_note_by_id**
> RestNullObjectResponse add_alert_note_by_id(body, id)

add alert note



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertAck**](RestAlertAck.md)|  | 
 **id** | **str**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_alert_rule**
> RestAlertRuleResponse add_alert_rule(body)

add alert rule



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

# **add_api_token_by_admin_id**
> RestApiTokenResponse add_api_token_by_admin_id(admin_id, body)

add apiToken by admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **body** | [**RestAPIToken**](RestAPIToken.md)|  | 

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_collector**
> RestCollectorResponse add_collector(body)

add collector



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

# **add_collector_group**
> RestCollectorGroupResponse add_collector_group(body)

add collector group



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

# **add_dashboard**
> RestDashboardV1Response add_dashboard(body)

add dashboard



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

# **add_dashboard_group**
> RestDashboardGroupResponse add_dashboard_group(body)

add dashboard group



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

# **add_device**
> RestDeviceResponse add_device(body, add_from_wizard=add_from_wizard)

add a new device



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
 **add_from_wizard** | **bool**|  | [optional] [default to false]

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance**
> RestDeviceDataSourceInstanceResponse add_device_datasource_instance(device_id, hds_id, body)

add device instance 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **body** | [**RestDeviceDataSourceInstance**](RestDeviceDataSourceInstance.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_datasource_instance_group**
> RestDeviceDataSourceInstanceGroupResponse add_device_datasource_instance_group(device_id, device_ds_id, body)

add device datasource instance group 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **body** | [**RestDeviceDataSourceInstanceGroup**](RestDeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_group**
> RestDeviceGroupResponse add_device_group(body)

add device group



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

# **add_device_group_property**
> RestPropertyResponse add_device_group_property(gid, body)

add device group property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**|  | 
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_device_property**
> RestPropertyResponse add_device_property(device_id, body)

add device property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> RestRoleResponse add_role(body)

add role



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

# **add_service_group**
> RestServiceGroupResponse add_service_group(body)

add service group



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

# **delete_admin_by_id**
> RestNullObjectResponse delete_admin_by_id(id)

delete admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_by_id**
> RestAlertRuleResponse delete_alert_rule_by_id(id)

delete alert rule



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token_by_id**
> RestApiTokenResponse delete_api_token_by_id(admin_id, apitoken_id)

delete apiToken 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_by_id**
> RestCollectorResponse delete_collector_by_id(id)

delete collector



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collector_group_by_id**
> RestCollectorGroupResponse delete_collector_group_by_id(id)

delete collector group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_by_id**
> RestNullObjectResponse delete_dashboard_by_id(id)

delete dashboard



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard_group_by_id**
> RestNullObjectResponse delete_dashboard_group_by_id(id)

delete dashboard group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> RestNullObjectResponse delete_device(id)

delete a device



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_by_id**
> RestNullObjectResponse delete_device_group_by_id(id, delete_children=delete_children)

delete device group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **bool**|  | [optional] [default to false]

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_group_property_by_name**
> RestNullObjectResponse delete_device_group_property_by_name(gid, name)

delete device group property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**|  | 
 **name** | **str**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_property_by_name**
> RestNullObjectResponse delete_device_property_by_name(device_id, name)

delete device  property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_by_id**
> RestRoleResponse delete_role_by_id(id)

delete role



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_group_by_id**
> RestNullObjectResponse delete_service_group_by_id(id, delete_children=delete_children)

delete service group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_children** | **int**|  | [optional] [default to 0]

### Return type

[**RestNullObjectResponse**](RestNullObjectResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_by_id**
> RestAdminResponse get_admin_by_id(id, fields=fields)

get admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestAdminResponse**](RestAdminResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_list**
> RestAdminPaginationResponse get_admin_list(fields=fields, size=size, offset=offset, filter=filter)

get admin list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestAdminPaginationResponse**](RestAdminPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_by_id**
> RestAlertResponse get_alert_by_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields)

get alert



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**RestAlertResponse**](RestAlertResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list**
> RestAlertPaginationResponse get_alert_list(need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)

get alert list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_group_id**
> RestAlertPaginationResponse get_alert_list_by_device_group_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)

get device group alerts



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_list_by_device_id**
> RestAlertPaginationResponse get_alert_list_by_device_id(id, need_message=need_message, custom_columns=custom_columns, fields=fields, size=size, offset=offset, search_id=search_id, filter=filter)

get alerts



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **need_message** | **bool**|  | [optional] [default to false]
 **custom_columns** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **search_id** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**RestAlertPaginationResponse**](RestAlertPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_by_id**
> RestAlertRuleResponse get_alert_rule_by_id(id, fields=fields)

get alert rule by id



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rule_list**
> RestAlertRulePaginationResponse get_alert_rule_list(fields=fields, size=size, offset=offset, filter=filter)

get alert rule list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestAlertRulePaginationResponse**](RestAlertRulePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token_list_by_admin_id**
> RestApiTokenPaginationResponse get_api_token_list_by_admin_id(admin_id, fields=fields, size=size, offset=offset, filter=filter)

get apiToken by admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestApiTokenPaginationResponse**](RestApiTokenPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_by_id**
> RestCollectorResponse get_collector_by_id(id, fields=fields)

get collector



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_by_id**
> RestCollectorGroupResponse get_collector_group_by_id(id, fields=fields)

get collector group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_group_list**
> RestCollectorGroupPaginationResponse get_collector_group_list(fields=fields, size=size, offset=offset, filter=filter)

get collector group list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestCollectorGroupPaginationResponse**](RestCollectorGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collector_list**
> RestCollectorPaginationResponse get_collector_list(fields=fields, size=size, offset=offset, filter=filter)

get collector list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestCollectorPaginationResponse**](RestCollectorPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_by_id**
> RestDashboardV1Response get_dashboard_by_id(id, fields=fields)

get dashboard



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDashboardV1Response**](RestDashboardV1Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_by_id**
> RestDashboardGroupResponse get_dashboard_group_by_id(id, fields=fields)

get dashboard group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDashboardGroupResponse**](RestDashboardGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_group_list**
> RestDashboardGroupPaginationResponse get_dashboard_group_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard group list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDashboardGroupPaginationResponse**](RestDashboardGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dashboard_list**
> RestDashboardV1PaginationResponse get_dashboard_list(fields=fields, size=size, offset=offset, filter=filter)

get dashboard list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDashboardV1PaginationResponse**](RestDashboardV1PaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_by_id**
> RestDeviceResponse get_device_by_id(id, fields=fields)

get device by id



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_by_id**
> RestDeviceDatasourceResponse get_device_datasource_by_id(device_id, id, fields=fields)

get device datasource 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceDatasourceResponse**](RestDeviceDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_data_by_id**
> RestDeviceDatasourceDataResponse get_device_datasource_data_by_id(device_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get device datasource data 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**RestDeviceDatasourceDataResponse**](RestDeviceDatasourceDataResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_alert_setting_by_id**
> RestDeviceDataSourceInstanceAlertSettingResponse get_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, fields=fields)

get device instance alert setting



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceDataSourceInstanceAlertSettingResponse**](RestDeviceDataSourceInstanceAlertSettingResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_by_id**
> RestDeviceDataSourceInstanceResponse get_device_datasource_instance_by_id(device_id, hds_id, id, fields=fields)

get device instance 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_data**
> RestDeviceDataSourceInstanceDataResponse get_device_datasource_instance_data(device_id, hds_id, id, period=period, start=start, end=end, datapoints=datapoints, format=format)

get device instance data



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **period** | **float**|  | [optional] [default to 1]
 **start** | **int**|  | [optional] [default to 0]
 **end** | **int**|  | [optional] [default to 0]
 **datapoints** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to json]

### Return type

[**RestDeviceDataSourceInstanceDataResponse**](RestDeviceDataSourceInstanceDataResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_graph_data**
> RestGraphPlotResponse get_device_datasource_instance_graph_data(device_id, hds_id, id, graph_id, start=start, end=end, format=format)

get device instance graph data 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_by_id**
> RestDeviceDataSourceInstanceGroupResponse get_device_datasource_instance_group_by_id(device_id, device_ds_id, id, fields=fields)

get device datasource instance group 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_instance_group_overview_graph_data**
> RestGraphPlotResponse get_device_datasource_instance_group_overview_graph_data(device_id, device_ds_id, dsig_id, ograph_id, start=start, end=end, format=format)

get device instance group overview graph data 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **dsig_id** | **int**|  | 
 **ograph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_datasource_list**
> RestDeviceDatasourcePaginationResponse get_device_datasource_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device datasource list 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDeviceDatasourcePaginationResponse**](RestDeviceDatasourcePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_by_id**
> RestDeviceGroupResponse get_device_group_by_id(id, fields=fields)

get device group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_alert_setting**
> RestDeviceGroupDatasourceAlertConfigResponse get_device_group_datasource_alert_setting(device_group_id, ds_id, fields=fields)

get device group datasource alert setting 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupDatasourceAlertConfigResponse**](RestDeviceGroupDatasourceAlertConfigResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_by_id**
> RestDeviceGroupDatasourceResponse get_device_group_datasource_by_id(device_group_id, id, fields=fields)

get device group datasource



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupDatasourceResponse**](RestDeviceGroupDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_datasource_list**
> RestDeviceGroupDatasourceResponse get_device_group_datasource_list(device_group_id, fields=fields, size=size, offset=offset, filter=filter)

get device group datasource list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupDatasourceResponse**](RestDeviceGroupDatasourceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_list**
> RestDeviceGroupPaginationResponse get_device_group_list(fields=fields, size=size, offset=offset, filter=filter)

get device group list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupPaginationResponse**](RestDeviceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_properties**
> RestPropertyPaginationResponse get_device_group_properties(gid, fields=fields, size=size, offset=offset, filter=filter)

get device group properties



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestPropertyPaginationResponse**](RestPropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_group_property_by_name**
> RestPropertyResponse get_device_group_property_by_name(gid, name, fields=fields)

get device group property by name



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_instance_graph_data_only_by_instance_id**
> RestGraphPlotResponse get_device_instance_graph_data_only_by_instance_id(instance_id, graph_id, start=start, end=end, format=format)

get device instance graphData



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**|  | 
 **graph_id** | **int**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_list**
> RestDevicePaginationResponse get_device_list(fields=fields, size=size, offset=offset, filter=filter)

get device list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDevicePaginationResponse**](RestDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_properties_list**
> RestPropertyPaginationResponse get_device_properties_list(device_id, fields=fields, size=size, offset=offset, filter=filter)

get device properties



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestPropertyPaginationResponse**](RestPropertyPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_property_by_name**
> RestPropertyResponse get_device_property_by_name(device_id, name, fields=fields)

get device property by name



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_immediate_device_list_by_device_group_id**
> RestDevicePaginationResponse get_immediate_device_list_by_device_group_id(id, fields=fields, size=size, offset=offset, filter=filter)

get immediate devices under group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestDevicePaginationResponse**](RestDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> RestRoleResponse get_role_by_id(id, fields=fields)

get role by id



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_list**
> RestRolePaginationResponse get_role_list(fields=fields, size=size, offset=offset, filter=filter)

get role list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestRolePaginationResponse**](RestRolePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_graph_data**
> RestGraphPlotResponse get_service_graph_data(service_id, checkpoint_id, graph_name, start=start, end=end, format=format)

get service graph data



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **int**|  | 
 **checkpoint_id** | **int**|  | 
 **graph_name** | **str**|  | 
 **start** | **int**|  | [optional] 
 **end** | **int**|  | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**RestGraphPlotResponse**](RestGraphPlotResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_group_by_id**
> RestServiceGroupResponse get_service_group_by_id(id, fields=fields)

get service group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**|  | [optional] 

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_group_list**
> RestServiceGroupPaginationResponse get_service_group_list(fields=fields, size=size, offset=offset, filter=filter)

get service group list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestServiceGroupPaginationResponse**](RestServiceGroupPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_monitor_check_point_list**
> RestSMCheckPointPaginationResponse get_site_monitor_check_point_list(fields=fields, size=size, offset=offset, filter=filter)

get site monitor checkpoint list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestSMCheckPointPaginationResponse**](RestSMCheckPointPaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmonitored_device_list**
> RestUnmonitoredDevicePaginationResponse get_unmonitored_device_list(fields=fields, size=size, offset=offset, filter=filter)

get unmonitored device list



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **filter** | **str**|  | [optional] 

### Return type

[**RestUnmonitoredDevicePaginationResponse**](RestUnmonitoredDevicePaginationResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_collector**
> file install_collector(collector_id, os_and_arch, collector_version=collector_version, token=token, monitor_others=monitor_others, collector_size=collector_size, use_ea=use_ea)

install collector



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collector_id** | **int**|  | 
 **os_and_arch** | **str**|  | 
 **collector_version** | **int**|  | [optional] 
 **token** | **str**|  | [optional] 
 **monitor_others** | **bool**|  | [optional] [default to true]
 **collector_size** | **str**|  | [optional] [default to medium]
 **use_ea** | **bool**|  | [optional] [default to false]

### Return type

[**file**](file.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_by_id**
> RestDeviceResponse patch_device_by_id(body, id, op_type=op_type, patch_fields=patch_fields)

patch a device



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
 **id** | **int**|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_device_group_by_id**
> RestDeviceGroupResponse patch_device_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)

patch device group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_group_by_id**
> RestServiceGroupResponse patch_service_group_by_id(id, body, op_type=op_type, patch_fields=patch_fields)

patch service group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 
 **op_type** | **str**|  | [optional] [default to refresh]
 **patch_fields** | **str**|  | [optional] 

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_auto_discovery_by_device_id**
> RestStringResponse schedule_auto_discovery_by_device_id(id)

schedule auto discovery for a host



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RestStringResponse**](RestStringResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_by_id**
> RestAdminResponse update_admin_by_id(id, body, change_password=change_password)

update admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestAdmin**](RestAdmin.md)|  | 
 **change_password** | **bool**|  | [optional] [default to false]

### Return type

[**RestAdminResponse**](RestAdminResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_rule_by_id**
> RestAlertRuleResponse update_alert_rule_by_id(body, id)

update alert rule



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestAlertRule**](RestAlertRule.md)|  | 
 **id** | **int**|  | 

### Return type

[**RestAlertRuleResponse**](RestAlertRuleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_token_by_admin_id**
> RestApiTokenResponse update_api_token_by_admin_id(admin_id, apitoken_id, body)

update apiToken by admin



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_id** | **int**|  | 
 **apitoken_id** | **int**|  | 
 **body** | [**RestAPIToken**](RestAPIToken.md)|  | 

### Return type

[**RestApiTokenResponse**](RestApiTokenResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_by_id**
> RestCollectorResponse update_collector_by_id(id, body)

update collector



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestCollector**](RestCollector.md)|  | 

### Return type

[**RestCollectorResponse**](RestCollectorResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collector_group_by_id**
> RestCollectorGroupResponse update_collector_group_by_id(id, body)

update collector group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestCollectorGroup**](RestCollectorGroup.md)|  | 

### Return type

[**RestCollectorGroupResponse**](RestCollectorGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_by_id**
> RestDashboardV1Response update_dashboard_by_id(id, body, overwrite_group_fields=overwrite_group_fields)

update dashboard



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestDashboardV1**](RestDashboardV1.md)|  | 
 **overwrite_group_fields** | **bool**|  | [optional] [default to false]

### Return type

[**RestDashboardV1Response**](RestDashboardV1Response.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard_group_by_id**
> RestDashboardGroupResponse update_dashboard_group_by_id(id, body)

update dashboard group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestDashboardGroup**](RestDashboardGroup.md)|  | 

### Return type

[**RestDashboardGroupResponse**](RestDashboardGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> RestDeviceResponse update_device(body, id, op_type=op_type)

update a device



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestDevice**](RestDevice.md)|  | 
 **id** | **int**|  | 
 **op_type** | **str**|  | [optional] [default to refresh]

### Return type

[**RestDeviceResponse**](RestDeviceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_alert_setting_by_id**
> RestDeviceDataSourceInstanceAlertSettingResponse update_device_datasource_instance_alert_setting_by_id(device_id, hds_id, instance_id, id, body)

update device instance alert setting



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **instance_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**RestDeviceDataSourceInstanceAlertSetting**](RestDeviceDataSourceInstanceAlertSetting.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceAlertSettingResponse**](RestDeviceDataSourceInstanceAlertSettingResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_by_id**
> RestDeviceDataSourceInstanceResponse update_device_datasource_instance_by_id(device_id, hds_id, id, body)

update device instance 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **hds_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**RestDeviceDataSourceInstance**](RestDeviceDataSourceInstance.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceResponse**](RestDeviceDataSourceInstanceResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_datasource_instance_group_by_id**
> RestDeviceDataSourceInstanceGroupResponse update_device_datasource_instance_group_by_id(device_id, device_ds_id, id, body)

update device datasource instance group 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **device_ds_id** | **int**|  | 
 **id** | **int**|  | 
 **body** | [**RestDeviceDataSourceInstanceGroup**](RestDeviceDataSourceInstanceGroup.md)|  | 

### Return type

[**RestDeviceDataSourceInstanceGroupResponse**](RestDeviceDataSourceInstanceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_by_id**
> RestDeviceGroupResponse update_device_group_by_id(id, body)

update device group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestDeviceGroup**](RestDeviceGroup.md)|  | 

### Return type

[**RestDeviceGroupResponse**](RestDeviceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_datasource_alert_setting**
> RestDeviceGroupDatasourceAlertConfigResponse update_device_group_datasource_alert_setting(device_group_id, ds_id, body)

update device group datasource alert setting 



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_group_id** | **int**|  | 
 **ds_id** | **int**|  | 
 **body** | [**RestDeviceGroupDataSourceAlertConfig**](RestDeviceGroupDataSourceAlertConfig.md)|  | 

### Return type

[**RestDeviceGroupDatasourceAlertConfigResponse**](RestDeviceGroupDatasourceAlertConfigResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_group_property_by_name**
> RestPropertyResponse update_device_group_property_by_name(gid, name, body)

update device group property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_property_by_name**
> RestPropertyResponse update_device_property_by_name(device_id, name, body)

update device  property



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **int**|  | 
 **name** | **str**|  | 
 **body** | [**RestProperty**](RestProperty.md)|  | 

### Return type

[**RestPropertyResponse**](RestPropertyResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_by_id**
> RestRoleResponse update_role_by_id(id, body)

update role



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestRole**](RestRole.md)|  | 

### Return type

[**RestRoleResponse**](RestRoleResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_group_by_id**
> RestServiceGroupResponse update_service_group_by_id(id, body)

update service group



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**RestServiceGroup**](RestServiceGroup.md)|  | 

### Return type

[**RestServiceGroupResponse**](RestServiceGroupResponse.md)

### Authorization

[LMv1](../README.md#LMv1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

