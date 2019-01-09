# DeviceDataSourceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stop_monitoring** | **bool** | Whether or not monitoring is disabled for the instance | [optional] 
**device_data_source_id** | **int** | The id of the unique device-datasource the instance is associated with | [optional] 
**display_name** | **str** | The instance alias. This is the descriptive name of the instance, and should be unique for the device/datasource combination | 
**wild_value2** | **str** | Only used for two dimensional active discovery. When used, during Active Discovery runs, the token ##WILDVALUE## is replaces with the value of ALIAS and the token ##WILDVALUE2## is replaced with the value of the second part alias. This value must be unique for the device/datasource/WILDVALUE combination | [optional] 
**group_id** | **int** | The id of the instance group associated with the datasource instance | [optional] 
**description** | **str** | The description of the datasource instance | [optional] 
**disable_alerting** | **bool** | Whether or not alerting is disabled for the instance | [optional] 
**device_id** | **int** | The id of the device the datasource instance is associated with | [optional] 
**device_display_name** | **str** | The display name of the device the datasource instance is associated with | [optional] 
**system_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any instance level system properties assigned to the instance | [optional] 
**auto_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any instance level auto properties assigned to the instance | [optional] 
**data_source_id** | **int** | The id of the datasource definition that the instance represents | [optional] 
**group_name** | **str** | The name of the instance group associated with the datasource instance | [optional] 
**custom_properties** | [**list[NameAndValue]**](NameAndValue.md) | Any instance level properties assigned to the instance | [optional] 
**lock_description** | **bool** | Whether or not Active Discovery is enabled, and thus whether or not the instance description is editable | [optional] 
**name** | **str** | The name of the datasource instance, in the format of: datasourceName-instanceAlias | [optional] 
**id** | **int** | The Id of the datasource instance | [optional] 
**wild_value** | **str** | The variable part of the instance, used to query data from a device. For example, variable part of the SNMP OID tree. This value must be unique for the device/datasource combination, unless two-dimensional active discovery is used | 
**data_source_type** | **str** | The type of LogicModule, e.g. DS (datasource) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


