# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NetflowPort(object):
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
        'percent_usage': 'float',
        'port': 'int',
        'data_type': 'str',
        'usage': 'float',
        'description': 'str'
    }

    attribute_map = {
        'percent_usage': 'percentUsage',
        'port': 'port',
        'data_type': 'dataType',
        'usage': 'usage',
        'description': 'description'
    }

    def __init__(self, percent_usage=None, port=None, data_type=None, usage=None, description=None):  # noqa: E501
        """NetflowPort - a model defined in Swagger"""  # noqa: E501

        self._percent_usage = None
        self._port = None
        self._data_type = None
        self._usage = None
        self._description = None
        self.discriminator = None

        if percent_usage is not None:
            self.percent_usage = percent_usage
        if port is not None:
            self.port = port
        if data_type is not None:
            self.data_type = data_type
        if usage is not None:
            self.usage = usage
        if description is not None:
            self.description = description

    @property
    def percent_usage(self):
        """Gets the percent_usage of this NetflowPort.  # noqa: E501


        :return: The percent_usage of this NetflowPort.  # noqa: E501
        :rtype: float
        """
        return self._percent_usage

    @percent_usage.setter
    def percent_usage(self, percent_usage):
        """Sets the percent_usage of this NetflowPort.


        :param percent_usage: The percent_usage of this NetflowPort.  # noqa: E501
        :type: float
        """

        self._percent_usage = percent_usage

    @property
    def port(self):
        """Gets the port of this NetflowPort.  # noqa: E501


        :return: The port of this NetflowPort.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NetflowPort.


        :param port: The port of this NetflowPort.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def data_type(self):
        """Gets the data_type of this NetflowPort.  # noqa: E501


        :return: The data_type of this NetflowPort.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this NetflowPort.


        :param data_type: The data_type of this NetflowPort.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def usage(self):
        """Gets the usage of this NetflowPort.  # noqa: E501


        :return: The usage of this NetflowPort.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this NetflowPort.


        :param usage: The usage of this NetflowPort.  # noqa: E501
        :type: float
        """

        self._usage = usage

    @property
    def description(self):
        """Gets the description of this NetflowPort.  # noqa: E501


        :return: The description of this NetflowPort.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetflowPort.


        :param description: The description of this NetflowPort.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(NetflowPort, dict):
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
        if not isinstance(other, NetflowPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
