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


class AutoDiscoveryFilter(object):
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
        'attribute': 'str',
        'comment': 'str',
        'operation': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attribute': 'attribute',
        'comment': 'comment',
        'operation': 'operation',
        'value': 'value'
    }

    def __init__(self, attribute=None, comment=None, operation=None, value=None):  # noqa: E501
        """AutoDiscoveryFilter - a model defined in Swagger"""  # noqa: E501

        self._attribute = None
        self._comment = None
        self._operation = None
        self._value = None
        self.discriminator = None

        self.attribute = attribute
        if comment is not None:
            self.comment = comment
        self.operation = operation
        if value is not None:
            self.value = value

    @property
    def attribute(self):
        """Gets the attribute of this AutoDiscoveryFilter.  # noqa: E501


        :return: The attribute of this AutoDiscoveryFilter.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this AutoDiscoveryFilter.


        :param attribute: The attribute of this AutoDiscoveryFilter.  # noqa: E501
        :type: str
        """
        if attribute is None:
            raise ValueError("Invalid value for `attribute`, must not be `None`")  # noqa: E501

        self._attribute = attribute

    @property
    def comment(self):
        """Gets the comment of this AutoDiscoveryFilter.  # noqa: E501


        :return: The comment of this AutoDiscoveryFilter.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AutoDiscoveryFilter.


        :param comment: The comment of this AutoDiscoveryFilter.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def operation(self):
        """Gets the operation of this AutoDiscoveryFilter.  # noqa: E501


        :return: The operation of this AutoDiscoveryFilter.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AutoDiscoveryFilter.


        :param operation: The operation of this AutoDiscoveryFilter.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def value(self):
        """Gets the value of this AutoDiscoveryFilter.  # noqa: E501


        :return: The value of this AutoDiscoveryFilter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AutoDiscoveryFilter.


        :param value: The value of this AutoDiscoveryFilter.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(AutoDiscoveryFilter, dict):
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
        if not isinstance(other, AutoDiscoveryFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
