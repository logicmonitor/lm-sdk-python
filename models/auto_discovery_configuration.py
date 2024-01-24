# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. <br> <br> Note: <ul> <li> For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. </li> <li> Both underscore and camelCase are supported if parameters are encapsulated within the body. </li> <li> Only camelCase is supported if parameters are encapsulated within the body and also if the user is passing raw JSON as REQUEST parameter. However, the RESPONSE parameters always contain an underscore. For example, you can use testLocation or test_location in the REQUEST parameter. But the RESPONSE parameter will always be test_location. </li> <li> The fields parameter only supports camelCase. </li> </ul>  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.auto_discovery_filter import AutoDiscoveryFilter  # noqa: F401,E501
from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501


class AutoDiscoveryConfiguration(object):
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
        'persistent_instance': 'bool',
        'schedule_interval': 'int',
        'delete_inactive_instance': 'bool',
        'method': 'AutoDiscoveryMethod',
        'instance_auto_group_method': 'str',
        'instance_auto_group_method_params': 'str',
        'filters': 'list[AutoDiscoveryFilter]',
        'disable_instance': 'bool'
    }

    attribute_map = {
        'persistent_instance': 'persistentInstance',
        'schedule_interval': 'scheduleInterval',
        'delete_inactive_instance': 'deleteInactiveInstance',
        'method': 'method',
        'instance_auto_group_method': 'instanceAutoGroupMethod',
        'instance_auto_group_method_params': 'instanceAutoGroupMethodParams',
        'filters': 'filters',
        'disable_instance': 'disableInstance'
    }

    def __init__(self, persistent_instance=None, schedule_interval=None, delete_inactive_instance=None, method=None, instance_auto_group_method=None, instance_auto_group_method_params=None, filters=None, disable_instance=None):  # noqa: E501
        """AutoDiscoveryConfiguration - a model defined in Swagger"""  # noqa: E501

        self._persistent_instance = None
        self._schedule_interval = None
        self._delete_inactive_instance = None
        self._method = None
        self._instance_auto_group_method = None
        self._instance_auto_group_method_params = None
        self._filters = None
        self._disable_instance = None
        self.discriminator = None

        if persistent_instance is not None:
            self.persistent_instance = persistent_instance
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if delete_inactive_instance is not None:
            self.delete_inactive_instance = delete_inactive_instance
        self.method = method
        if instance_auto_group_method is not None:
            self.instance_auto_group_method = instance_auto_group_method
        if instance_auto_group_method_params is not None:
            self.instance_auto_group_method_params = instance_auto_group_method_params
        if filters is not None:
            self.filters = filters
        if disable_instance is not None:
            self.disable_instance = disable_instance

    @property
    def persistent_instance(self):
        """Gets the persistent_instance of this AutoDiscoveryConfiguration.  # noqa: E501

        Persist discovered instance  # noqa: E501

        :return: The persistent_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._persistent_instance

    @persistent_instance.setter
    def persistent_instance(self, persistent_instance):
        """Sets the persistent_instance of this AutoDiscoveryConfiguration.

        Persist discovered instance  # noqa: E501

        :param persistent_instance: The persistent_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: bool
        """

        self._persistent_instance = persistent_instance

    @property
    def schedule_interval(self):
        """Gets the schedule_interval of this AutoDiscoveryConfiguration.  # noqa: E501

        Auto discovery schedule interval in minutes. 0 means host or data source changed. The values can be 0|15|60|1440  # noqa: E501

        :return: The schedule_interval of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        """Sets the schedule_interval of this AutoDiscoveryConfiguration.

        Auto discovery schedule interval in minutes. 0 means host or data source changed. The values can be 0|15|60|1440  # noqa: E501

        :param schedule_interval: The schedule_interval of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: int
        """

        self._schedule_interval = schedule_interval

    @property
    def delete_inactive_instance(self):
        """Gets the delete_inactive_instance of this AutoDiscoveryConfiguration.  # noqa: E501

        Delete inactive instance  # noqa: E501

        :return: The delete_inactive_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._delete_inactive_instance

    @delete_inactive_instance.setter
    def delete_inactive_instance(self, delete_inactive_instance):
        """Sets the delete_inactive_instance of this AutoDiscoveryConfiguration.

        Delete inactive instance  # noqa: E501

        :param delete_inactive_instance: The delete_inactive_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: bool
        """

        self._delete_inactive_instance = delete_inactive_instance

    @property
    def method(self):
        """Gets the method of this AutoDiscoveryConfiguration.  # noqa: E501

        Method used to do auto discovery instance  # noqa: E501

        :return: The method of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: AutoDiscoveryMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AutoDiscoveryConfiguration.

        Method used to do auto discovery instance  # noqa: E501

        :param method: The method of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: AutoDiscoveryMethod
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def instance_auto_group_method(self):
        """Gets the instance_auto_group_method of this AutoDiscoveryConfiguration.  # noqa: E501

        Auto group method. The values can be none|netscaler|netscalerservicegroup|regex|esx|ilp  # noqa: E501

        :return: The instance_auto_group_method of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instance_auto_group_method

    @instance_auto_group_method.setter
    def instance_auto_group_method(self, instance_auto_group_method):
        """Sets the instance_auto_group_method of this AutoDiscoveryConfiguration.

        Auto group method. The values can be none|netscaler|netscalerservicegroup|regex|esx|ilp  # noqa: E501

        :param instance_auto_group_method: The instance_auto_group_method of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: str
        """

        self._instance_auto_group_method = instance_auto_group_method

    @property
    def instance_auto_group_method_params(self):
        """Gets the instance_auto_group_method_params of this AutoDiscoveryConfiguration.  # noqa: E501

        Auto group method's parameters  # noqa: E501

        :return: The instance_auto_group_method_params of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instance_auto_group_method_params

    @instance_auto_group_method_params.setter
    def instance_auto_group_method_params(self, instance_auto_group_method_params):
        """Sets the instance_auto_group_method_params of this AutoDiscoveryConfiguration.

        Auto group method's parameters  # noqa: E501

        :param instance_auto_group_method_params: The instance_auto_group_method_params of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: str
        """

        self._instance_auto_group_method_params = instance_auto_group_method_params

    @property
    def filters(self):
        """Gets the filters of this AutoDiscoveryConfiguration.  # noqa: E501


        :return: The filters of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: list[AutoDiscoveryFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AutoDiscoveryConfiguration.


        :param filters: The filters of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: list[AutoDiscoveryFilter]
        """

        self._filters = filters

    @property
    def disable_instance(self):
        """Gets the disable_instance of this AutoDiscoveryConfiguration.  # noqa: E501

        Disable discovered instance  # noqa: E501

        :return: The disable_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._disable_instance

    @disable_instance.setter
    def disable_instance(self, disable_instance):
        """Sets the disable_instance of this AutoDiscoveryConfiguration.

        Disable discovered instance  # noqa: E501

        :param disable_instance: The disable_instance of this AutoDiscoveryConfiguration.  # noqa: E501
        :type: bool
        """

        self._disable_instance = disable_instance

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
        if issubclass(AutoDiscoveryConfiguration, dict):
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
        if not isinstance(other, AutoDiscoveryConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
