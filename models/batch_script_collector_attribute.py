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

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class BatchScriptCollectorAttribute(CollectorAttribute):
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
        'script_type': 'str',
        'windows_script': 'str',
        'linux_cmdline': 'str',
        'linux_script': 'str',
        'windows_cmdline': 'str'
    }

    attribute_map = {
        'name': 'name',
        'groovy_script': 'groovyScript',
        'script_type': 'scriptType',
        'windows_script': 'windowsScript',
        'linux_cmdline': 'linuxCmdline',
        'linux_script': 'linuxScript',
        'windows_cmdline': 'windowsCmdline'
    }

    def __init__(self, name=None, groovy_script=None, script_type=None, windows_script=None, linux_cmdline=None, linux_script=None, windows_cmdline=None):  # noqa: E501
        """BatchScriptCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._groovy_script = None
        self._script_type = None
        self._windows_script = None
        self._linux_cmdline = None
        self._linux_script = None
        self._windows_cmdline = None
        self.discriminator = None

        self.name = name
        if groovy_script is not None:
            self.groovy_script = groovy_script
        if script_type is not None:
            self.script_type = script_type
        if windows_script is not None:
            self.windows_script = windows_script
        if linux_cmdline is not None:
            self.linux_cmdline = linux_cmdline
        if linux_script is not None:
            self.linux_script = linux_script
        if windows_cmdline is not None:
            self.windows_cmdline = windows_cmdline

    @property
    def name(self):
        """Gets the name of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The name of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchScriptCollectorAttribute.


        :param name: The name of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def groovy_script(self):
        """Gets the groovy_script of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The groovy_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._groovy_script

    @groovy_script.setter
    def groovy_script(self, groovy_script):
        """Sets the groovy_script of this BatchScriptCollectorAttribute.


        :param groovy_script: The groovy_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._groovy_script = groovy_script

    @property
    def script_type(self):
        """Gets the script_type of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The script_type of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this BatchScriptCollectorAttribute.


        :param script_type: The script_type of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._script_type = script_type

    @property
    def windows_script(self):
        """Gets the windows_script of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The windows_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._windows_script

    @windows_script.setter
    def windows_script(self, windows_script):
        """Sets the windows_script of this BatchScriptCollectorAttribute.


        :param windows_script: The windows_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._windows_script = windows_script

    @property
    def linux_cmdline(self):
        """Gets the linux_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The linux_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._linux_cmdline

    @linux_cmdline.setter
    def linux_cmdline(self, linux_cmdline):
        """Sets the linux_cmdline of this BatchScriptCollectorAttribute.


        :param linux_cmdline: The linux_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._linux_cmdline = linux_cmdline

    @property
    def linux_script(self):
        """Gets the linux_script of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The linux_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._linux_script

    @linux_script.setter
    def linux_script(self, linux_script):
        """Sets the linux_script of this BatchScriptCollectorAttribute.


        :param linux_script: The linux_script of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._linux_script = linux_script

    @property
    def windows_cmdline(self):
        """Gets the windows_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501


        :return: The windows_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._windows_cmdline

    @windows_cmdline.setter
    def windows_cmdline(self, windows_cmdline):
        """Sets the windows_cmdline of this BatchScriptCollectorAttribute.


        :param windows_cmdline: The windows_cmdline of this BatchScriptCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._windows_cmdline = windows_cmdline

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
        if issubclass(BatchScriptCollectorAttribute, dict):
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
        if not isinstance(other, BatchScriptCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
