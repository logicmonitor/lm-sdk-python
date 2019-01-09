# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.name_and_value import NameAndValue  # noqa: F401,E501


class DeviceDataSourceInstance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'stop_monitoring': 'bool',
        'device_data_source_id': 'int',
        'display_name': 'str',
        'wild_value2': 'str',
        'group_id': 'int',
        'description': 'str',
        'disable_alerting': 'bool',
        'device_id': 'int',
        'device_display_name': 'str',
        'system_properties': 'list[NameAndValue]',
        'auto_properties': 'list[NameAndValue]',
        'data_source_id': 'int',
        'group_name': 'str',
        'custom_properties': 'list[NameAndValue]',
        'lock_description': 'bool',
        'name': 'str',
        'id': 'int',
        'wild_value': 'str',
        'data_source_type': 'str'
    }

    attribute_map = {
        'stop_monitoring': 'stopMonitoring',
        'device_data_source_id': 'deviceDataSourceId',
        'display_name': 'displayName',
        'wild_value2': 'wildValue2',
        'group_id': 'groupId',
        'description': 'description',
        'disable_alerting': 'disableAlerting',
        'device_id': 'deviceId',
        'device_display_name': 'deviceDisplayName',
        'system_properties': 'systemProperties',
        'auto_properties': 'autoProperties',
        'data_source_id': 'dataSourceId',
        'group_name': 'groupName',
        'custom_properties': 'customProperties',
        'lock_description': 'lockDescription',
        'name': 'name',
        'id': 'id',
        'wild_value': 'wildValue',
        'data_source_type': 'dataSourceType'
    }

    def __init__(self, stop_monitoring=None, device_data_source_id=None, display_name=None, wild_value2=None, group_id=None, description=None, disable_alerting=None, device_id=None, device_display_name=None, system_properties=None, auto_properties=None, data_source_id=None, group_name=None, custom_properties=None, lock_description=None, name=None, id=None, wild_value=None, data_source_type=None):  # noqa: E501
        """DeviceDataSourceInstance - a model defined in Swagger"""  # noqa: E501

        self._stop_monitoring = None
        self._device_data_source_id = None
        self._display_name = None
        self._wild_value2 = None
        self._group_id = None
        self._description = None
        self._disable_alerting = None
        self._device_id = None
        self._device_display_name = None
        self._system_properties = None
        self._auto_properties = None
        self._data_source_id = None
        self._group_name = None
        self._custom_properties = None
        self._lock_description = None
        self._name = None
        self._id = None
        self._wild_value = None
        self._data_source_type = None
        self.discriminator = None

        if stop_monitoring is not None:
            self.stop_monitoring = stop_monitoring
        if device_data_source_id is not None:
            self.device_data_source_id = device_data_source_id
        self.display_name = display_name
        if wild_value2 is not None:
            self.wild_value2 = wild_value2
        if group_id is not None:
            self.group_id = group_id
        if description is not None:
            self.description = description
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        if device_id is not None:
            self.device_id = device_id
        if device_display_name is not None:
            self.device_display_name = device_display_name
        if system_properties is not None:
            self.system_properties = system_properties
        if auto_properties is not None:
            self.auto_properties = auto_properties
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if group_name is not None:
            self.group_name = group_name
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if lock_description is not None:
            self.lock_description = lock_description
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        self.wild_value = wild_value
        if data_source_type is not None:
            self.data_source_type = data_source_type

    @property
    def stop_monitoring(self):
        """Gets the stop_monitoring of this DeviceDataSourceInstance.  # noqa: E501

        Whether or not monitoring is disabled for the instance  # noqa: E501

        :return: The stop_monitoring of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: bool
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """Sets the stop_monitoring of this DeviceDataSourceInstance.

        Whether or not monitoring is disabled for the instance  # noqa: E501

        :param stop_monitoring: The stop_monitoring of this DeviceDataSourceInstance.  # noqa: E501
        :type: bool
        """

        self._stop_monitoring = stop_monitoring

    @property
    def device_data_source_id(self):
        """Gets the device_data_source_id of this DeviceDataSourceInstance.  # noqa: E501

        The id of the unique device-datasource the instance is associated with  # noqa: E501

        :return: The device_data_source_id of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: int
        """
        return self._device_data_source_id

    @device_data_source_id.setter
    def device_data_source_id(self, device_data_source_id):
        """Sets the device_data_source_id of this DeviceDataSourceInstance.

        The id of the unique device-datasource the instance is associated with  # noqa: E501

        :param device_data_source_id: The device_data_source_id of this DeviceDataSourceInstance.  # noqa: E501
        :type: int
        """

        self._device_data_source_id = device_data_source_id

    @property
    def display_name(self):
        """Gets the display_name of this DeviceDataSourceInstance.  # noqa: E501

        The instance alias. This is the descriptive name of the instance, and should be unique for the device/datasource combination  # noqa: E501

        :return: The display_name of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DeviceDataSourceInstance.

        The instance alias. This is the descriptive name of the instance, and should be unique for the device/datasource combination  # noqa: E501

        :param display_name: The display_name of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def wild_value2(self):
        """Gets the wild_value2 of this DeviceDataSourceInstance.  # noqa: E501

        Only used for two dimensional active discovery. When used, during Active Discovery runs, the token ##WILDVALUE## is replaces with the value of ALIAS and the token ##WILDVALUE2## is replaced with the value of the second part alias. This value must be unique for the device/datasource/WILDVALUE combination  # noqa: E501

        :return: The wild_value2 of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._wild_value2

    @wild_value2.setter
    def wild_value2(self, wild_value2):
        """Sets the wild_value2 of this DeviceDataSourceInstance.

        Only used for two dimensional active discovery. When used, during Active Discovery runs, the token ##WILDVALUE## is replaces with the value of ALIAS and the token ##WILDVALUE2## is replaced with the value of the second part alias. This value must be unique for the device/datasource/WILDVALUE combination  # noqa: E501

        :param wild_value2: The wild_value2 of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._wild_value2 = wild_value2

    @property
    def group_id(self):
        """Gets the group_id of this DeviceDataSourceInstance.  # noqa: E501

        The id of the instance group associated with the datasource instance  # noqa: E501

        :return: The group_id of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeviceDataSourceInstance.

        The id of the instance group associated with the datasource instance  # noqa: E501

        :param group_id: The group_id of this DeviceDataSourceInstance.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this DeviceDataSourceInstance.  # noqa: E501

        The description of the datasource instance  # noqa: E501

        :return: The description of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceDataSourceInstance.

        The description of the datasource instance  # noqa: E501

        :param description: The description of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this DeviceDataSourceInstance.  # noqa: E501

        Whether or not alerting is disabled for the instance  # noqa: E501

        :return: The disable_alerting of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this DeviceDataSourceInstance.

        Whether or not alerting is disabled for the instance  # noqa: E501

        :param disable_alerting: The disable_alerting of this DeviceDataSourceInstance.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDataSourceInstance.  # noqa: E501

        The id of the device the datasource instance is associated with  # noqa: E501

        :return: The device_id of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDataSourceInstance.

        The id of the device the datasource instance is associated with  # noqa: E501

        :param device_id: The device_id of this DeviceDataSourceInstance.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_display_name(self):
        """Gets the device_display_name of this DeviceDataSourceInstance.  # noqa: E501

        The display name of the device the datasource instance is associated with  # noqa: E501

        :return: The device_display_name of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this DeviceDataSourceInstance.

        The display name of the device the datasource instance is associated with  # noqa: E501

        :param device_display_name: The device_display_name of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

    @property
    def system_properties(self):
        """Gets the system_properties of this DeviceDataSourceInstance.  # noqa: E501

        Any instance level system properties assigned to the instance  # noqa: E501

        :return: The system_properties of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._system_properties

    @system_properties.setter
    def system_properties(self, system_properties):
        """Sets the system_properties of this DeviceDataSourceInstance.

        Any instance level system properties assigned to the instance  # noqa: E501

        :param system_properties: The system_properties of this DeviceDataSourceInstance.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._system_properties = system_properties

    @property
    def auto_properties(self):
        """Gets the auto_properties of this DeviceDataSourceInstance.  # noqa: E501

        Any instance level auto properties assigned to the instance  # noqa: E501

        :return: The auto_properties of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._auto_properties

    @auto_properties.setter
    def auto_properties(self, auto_properties):
        """Sets the auto_properties of this DeviceDataSourceInstance.

        Any instance level auto properties assigned to the instance  # noqa: E501

        :param auto_properties: The auto_properties of this DeviceDataSourceInstance.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._auto_properties = auto_properties

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DeviceDataSourceInstance.  # noqa: E501

        The id of the datasource definition that the instance represents  # noqa: E501

        :return: The data_source_id of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DeviceDataSourceInstance.

        The id of the datasource definition that the instance represents  # noqa: E501

        :param data_source_id: The data_source_id of this DeviceDataSourceInstance.  # noqa: E501
        :type: int
        """

        self._data_source_id = data_source_id

    @property
    def group_name(self):
        """Gets the group_name of this DeviceDataSourceInstance.  # noqa: E501

        The name of the instance group associated with the datasource instance  # noqa: E501

        :return: The group_name of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this DeviceDataSourceInstance.

        The name of the instance group associated with the datasource instance  # noqa: E501

        :param group_name: The group_name of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def custom_properties(self):
        """Gets the custom_properties of this DeviceDataSourceInstance.  # noqa: E501

        Any instance level properties assigned to the instance  # noqa: E501

        :return: The custom_properties of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this DeviceDataSourceInstance.

        Any instance level properties assigned to the instance  # noqa: E501

        :param custom_properties: The custom_properties of this DeviceDataSourceInstance.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._custom_properties = custom_properties

    @property
    def lock_description(self):
        """Gets the lock_description of this DeviceDataSourceInstance.  # noqa: E501

        Whether or not Active Discovery is enabled, and thus whether or not the instance description is editable  # noqa: E501

        :return: The lock_description of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: bool
        """
        return self._lock_description

    @lock_description.setter
    def lock_description(self, lock_description):
        """Sets the lock_description of this DeviceDataSourceInstance.

        Whether or not Active Discovery is enabled, and thus whether or not the instance description is editable  # noqa: E501

        :param lock_description: The lock_description of this DeviceDataSourceInstance.  # noqa: E501
        :type: bool
        """

        self._lock_description = lock_description

    @property
    def name(self):
        """Gets the name of this DeviceDataSourceInstance.  # noqa: E501

        The name of the datasource instance, in the format of: datasourceName-instanceAlias  # noqa: E501

        :return: The name of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceDataSourceInstance.

        The name of the datasource instance, in the format of: datasourceName-instanceAlias  # noqa: E501

        :param name: The name of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this DeviceDataSourceInstance.  # noqa: E501

        The Id of the datasource instance  # noqa: E501

        :return: The id of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceDataSourceInstance.

        The Id of the datasource instance  # noqa: E501

        :param id: The id of this DeviceDataSourceInstance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def wild_value(self):
        """Gets the wild_value of this DeviceDataSourceInstance.  # noqa: E501

        The variable part of the instance, used to query data from a device. For example, variable part of the SNMP OID tree. This value must be unique for the device/datasource combination, unless two-dimensional active discovery is used  # noqa: E501

        :return: The wild_value of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._wild_value

    @wild_value.setter
    def wild_value(self, wild_value):
        """Sets the wild_value of this DeviceDataSourceInstance.

        The variable part of the instance, used to query data from a device. For example, variable part of the SNMP OID tree. This value must be unique for the device/datasource combination, unless two-dimensional active discovery is used  # noqa: E501

        :param wild_value: The wild_value of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """
        if wild_value is None:
            raise ValueError("Invalid value for `wild_value`, must not be `None`")  # noqa: E501

        self._wild_value = wild_value

    @property
    def data_source_type(self):
        """Gets the data_source_type of this DeviceDataSourceInstance.  # noqa: E501

        The type of LogicModule, e.g. DS (datasource)  # noqa: E501

        :return: The data_source_type of this DeviceDataSourceInstance.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this DeviceDataSourceInstance.

        The type of LogicModule, e.g. DS (datasource)  # noqa: E501

        :param data_source_type: The data_source_type of this DeviceDataSourceInstance.  # noqa: E501
        :type: str
        """

        self._data_source_type = data_source_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceDataSourceInstance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceDataSourceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
