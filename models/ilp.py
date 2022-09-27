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


class ILP(object):
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
        'wmi_name': 'str',
        'lm_name': 'str'
    }

    attribute_map = {
        'wmi_name': 'wmiName',
        'lm_name': 'lmName'
    }

    def __init__(self, wmi_name=None, lm_name=None):  # noqa: E501
        """ILP - a model defined in Swagger"""  # noqa: E501

        self._wmi_name = None
        self._lm_name = None
        self.discriminator = None

        self.wmi_name = wmi_name
        self.lm_name = lm_name

    @property
    def wmi_name(self):
        """Gets the wmi_name of this ILP.  # noqa: E501


        :return: The wmi_name of this ILP.  # noqa: E501
        :rtype: str
        """
        return self._wmi_name

    @wmi_name.setter
    def wmi_name(self, wmi_name):
        """Sets the wmi_name of this ILP.


        :param wmi_name: The wmi_name of this ILP.  # noqa: E501
        :type: str
        """
        if wmi_name is None:
            raise ValueError("Invalid value for `wmi_name`, must not be `None`")  # noqa: E501

        self._wmi_name = wmi_name

    @property
    def lm_name(self):
        """Gets the lm_name of this ILP.  # noqa: E501


        :return: The lm_name of this ILP.  # noqa: E501
        :rtype: str
        """
        return self._lm_name

    @lm_name.setter
    def lm_name(self, lm_name):
        """Sets the lm_name of this ILP.


        :param lm_name: The lm_name of this ILP.  # noqa: E501
        :type: str
        """
        if lm_name is None:
            raise ValueError("Invalid value for `lm_name`, must not be `None`")  # noqa: E501

        self._lm_name = lm_name

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
        if issubclass(ILP, dict):
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
        if not isinstance(other, ILP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
