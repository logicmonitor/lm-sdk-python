# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class TCPCollectorAttribute(CollectorAttribute):
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
        'name': 'str',
        'payload': 'str',
        'port': 'str',
        'encoding': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'name': 'name',
        'payload': 'payload',
        'port': 'port',
        'encoding': 'encoding',
        'timeout': 'timeout'
    }

    def __init__(self, name=None, payload=None, port=None, encoding=None, timeout=None):  # noqa: E501
        """TCPCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._payload = None
        self._port = None
        self._encoding = None
        self._timeout = None
        self.discriminator = None

        self.name = name
        if payload is not None:
            self.payload = payload
        if port is not None:
            self.port = port
        if encoding is not None:
            self.encoding = encoding
        if timeout is not None:
            self.timeout = timeout

    @property
    def name(self):
        """Gets the name of this TCPCollectorAttribute.  # noqa: E501

        data collector's name  # noqa: E501

        :return: The name of this TCPCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TCPCollectorAttribute.

        data collector's name  # noqa: E501

        :param name: The name of this TCPCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def payload(self):
        """Gets the payload of this TCPCollectorAttribute.  # noqa: E501


        :return: The payload of this TCPCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this TCPCollectorAttribute.


        :param payload: The payload of this TCPCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def port(self):
        """Gets the port of this TCPCollectorAttribute.  # noqa: E501


        :return: The port of this TCPCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TCPCollectorAttribute.


        :param port: The port of this TCPCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def encoding(self):
        """Gets the encoding of this TCPCollectorAttribute.  # noqa: E501


        :return: The encoding of this TCPCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this TCPCollectorAttribute.


        :param encoding: The encoding of this TCPCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def timeout(self):
        """Gets the timeout of this TCPCollectorAttribute.  # noqa: E501


        :return: The timeout of this TCPCollectorAttribute.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this TCPCollectorAttribute.


        :param timeout: The timeout of this TCPCollectorAttribute.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(TCPCollectorAttribute, dict):
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
        if not isinstance(other, TCPCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
