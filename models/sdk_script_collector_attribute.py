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

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class SDKScriptCollectorAttribute(CollectorAttribute):
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
        'groovy_script': 'str',
        'sdk_version': 'str',
        'sdk_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'groovy_script': 'groovyScript',
        'sdk_version': 'sdkVersion',
        'sdk_name': 'sdkName'
    }

    def __init__(self, name=None, groovy_script=None, sdk_version=None, sdk_name=None):  # noqa: E501
        """SDKScriptCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._groovy_script = None
        self._sdk_version = None
        self._sdk_name = None
        self.discriminator = None

        self.name = name
        self.groovy_script = groovy_script
        self.sdk_version = sdk_version
        self.sdk_name = sdk_name

    @property
    def name(self):
        """Gets the name of this SDKScriptCollectorAttribute.  # noqa: E501


        :return: The name of this SDKScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SDKScriptCollectorAttribute.


        :param name: The name of this SDKScriptCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def groovy_script(self):
        """Gets the groovy_script of this SDKScriptCollectorAttribute.  # noqa: E501


        :return: The groovy_script of this SDKScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._groovy_script

    @groovy_script.setter
    def groovy_script(self, groovy_script):
        """Sets the groovy_script of this SDKScriptCollectorAttribute.


        :param groovy_script: The groovy_script of this SDKScriptCollectorAttribute.  # noqa: E501
        :type: str
        """
        if groovy_script is None:
            raise ValueError("Invalid value for `groovy_script`, must not be `None`")  # noqa: E501

        self._groovy_script = groovy_script

    @property
    def sdk_version(self):
        """Gets the sdk_version of this SDKScriptCollectorAttribute.  # noqa: E501


        :return: The sdk_version of this SDKScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        """Sets the sdk_version of this SDKScriptCollectorAttribute.


        :param sdk_version: The sdk_version of this SDKScriptCollectorAttribute.  # noqa: E501
        :type: str
        """
        if sdk_version is None:
            raise ValueError("Invalid value for `sdk_version`, must not be `None`")  # noqa: E501

        self._sdk_version = sdk_version

    @property
    def sdk_name(self):
        """Gets the sdk_name of this SDKScriptCollectorAttribute.  # noqa: E501


        :return: The sdk_name of this SDKScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._sdk_name

    @sdk_name.setter
    def sdk_name(self, sdk_name):
        """Sets the sdk_name of this SDKScriptCollectorAttribute.


        :param sdk_name: The sdk_name of this SDKScriptCollectorAttribute.  # noqa: E501
        :type: str
        """
        if sdk_name is None:
            raise ValueError("Invalid value for `sdk_name`, must not be `None`")  # noqa: E501

        self._sdk_name = sdk_name

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
        if issubclass(SDKScriptCollectorAttribute, dict):
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
        if not isinstance(other, SDKScriptCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
