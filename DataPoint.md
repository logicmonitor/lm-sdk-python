# DataPoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_for_no_data** | **int** | The triggered alert level if we cannot collect data for this datapoint. The values can be 0-4 (0:unused alert, 1:alert ok, 2:warn alert, 2:error alert, 4:critical alert) | [optional] 
**post_processor_method** | **str** | The post processor method for the data value. Currently support complex expression and groovy. | [optional] 
**post_processor_param** | **str** | The post processor parameter, e.g. dataPoint1*2 | [optional] 
**max_digits** | **int** | The max digits of the data value | [optional] 
**raw_data_field_name** | **str** | The name of the raw data field name used to fetch value, e.g. avgrtt, output | [optional] 
**description** | **str** | The datapoint description | [optional] 
**alert_clear_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before the alert will be cleared | [optional] 
**user_param3** | **str** | The third user parameter will be used to fetch the datapoint value.  | [optional] 
**user_param2** | **str** | The second user parameter will be used to fetch the datapoint value. e.g. jmx attribute name | [optional] 
**type** | **int** | The data metric type. The values can be 0-7 (0:unknown, 1:counter, 2:gauge, 3:derive, 5:status, 6:compute, 7:counter32, 8:counter64) | [optional] 
**data_source_id** | **int** | The datasource id | [optional] 
**min_value** | **str** | The minimum value of the datapoint value range | [optional] 
**alert_body** | **str** | The customized alert message body define.  Empty string mean we will use the define in default template | [optional] 
**origin_id** | **str** | Portable id for origin tracking | [optional] 
**user_param1** | **str** | The first user parameter will be used to fetch the datapoint value. e.g. snmp oid | [optional] 
**alert_subject** | **str** | The customized alert message subject define. Empty string mean we will use the define in default template | [optional] 
**id** | **int** | The datapoint id | [optional] 
**alert_transition_interval** | **int** | The count that the alert must exist for this many poll cycles before it will be triggered | [optional] 
**enable_anomaly_alert_suppression** | **str** | Expression of anomaly detection setting, split by comma 0 means off,  1 means on, -1 means invalid 1,0,1 &#x3D;   warn : ON     error: OFF   critical: ON Empty value on this parameter means : 0,0,0 | [optional] 
**max_value** | **str** | The max value of the datapoint value range | [optional] 
**data_type** | **int** | The data value type. The values can be 1-8 (1:boolean, 2:byte, 3:short, 4:int, 5:long, 6:float, 7:double, 8:ulong) | [optional] 
**critical_ad_adv_setting** | **str** | Enable anomaly detection advance setting for CRITICAL severity | [optional] 
**alert_expr_note** | **str** | alert expression note | [optional] 
**ad_adv_setting_enabled** | **bool** | The AD advance setting enable flag | [optional] 
**error_ad_adv_setting** | **str** | Enable anomaly detection advance setting for ERROR severity | [optional] 
**warn_ad_adv_setting** | **str** | Enable anomaly detection advance setting for WARN severity | [optional] 
**name** | **str** | The datapoint name | 
**alert_expr** | **str** | The alert threshold define for the datapoint. e.g. &#39;&gt; 60 80 90&#39; mean it will:  trigger warn alert if value &gt; 60 trigger error alert if value &gt; 80 trigger critical alert if value &gt; 90 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


