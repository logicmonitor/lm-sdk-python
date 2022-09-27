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


class ScriptERIDiscoveryAttributeV3(object):
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
        'win_script': 'str',
        'groovy_script': 'str',
        'name': 'str',
        'type': 'str',
        'linux_cmdline': 'str',
        'linux_script': 'str',
        'win_cmdline': 'str'
    }

    attribute_map = {
        'win_script': 'winScript',
        'groovy_script': 'groovyScript',
        'name': 'name',
        'type': 'type',
        'linux_cmdline': 'linuxCmdline',
        'linux_script': 'linuxScript',
        'win_cmdline': 'winCmdline'
    }

    def __init__(self, win_script=None, groovy_script=None, name=None, type=None, linux_cmdline=None, linux_script=None, win_cmdline=None):  # noqa: E501
        """ScriptERIDiscoveryAttributeV3 - a model defined in Swagger"""  # noqa: E501

        self._win_script = None
        self._groovy_script = None
        self._name = None
        self._type = None
        self._linux_cmdline = None
        self._linux_script = None
        self._win_cmdline = None
        self.discriminator = None

        if win_script is not None:
            self.win_script = win_script
        if groovy_script is not None:
            self.groovy_script = groovy_script
        self.name = name
        if type is not None:
            self.type = type
        if linux_cmdline is not None:
            self.linux_cmdline = linux_cmdline
        if linux_script is not None:
            self.linux_script = linux_script
        if win_cmdline is not None:
            self.win_cmdline = win_cmdline

    @property
    def win_script(self):
        """Gets the win_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        windows script  # noqa: E501

        :return: The win_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._win_script

    @win_script.setter
    def win_script(self, win_script):
        """Sets the win_script of this ScriptERIDiscoveryAttributeV3.

        windows script  # noqa: E501

        :param win_script: The win_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._win_script = win_script

    @property
    def groovy_script(self):
        """Gets the groovy_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        groovy script   # noqa: E501

        :return: The groovy_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._groovy_script

    @groovy_script.setter
    def groovy_script(self, groovy_script):
        """Sets the groovy_script of this ScriptERIDiscoveryAttributeV3.

        groovy script   # noqa: E501

        :param groovy_script: The groovy_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._groovy_script = groovy_script

    @property
    def name(self):
        """Gets the name of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        ERI detection name  # noqa: E501

        :return: The name of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScriptERIDiscoveryAttributeV3.

        ERI detection name  # noqa: E501

        :param name: The name of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        script type  # noqa: E501

        :return: The type of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScriptERIDiscoveryAttributeV3.

        script type  # noqa: E501

        :param type: The type of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def linux_cmdline(self):
        """Gets the linux_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        linux script command line  # noqa: E501

        :return: The linux_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._linux_cmdline

    @linux_cmdline.setter
    def linux_cmdline(self, linux_cmdline):
        """Sets the linux_cmdline of this ScriptERIDiscoveryAttributeV3.

        linux script command line  # noqa: E501

        :param linux_cmdline: The linux_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._linux_cmdline = linux_cmdline

    @property
    def linux_script(self):
        """Gets the linux_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        linux script file  # noqa: E501

        :return: The linux_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._linux_script

    @linux_script.setter
    def linux_script(self, linux_script):
        """Sets the linux_script of this ScriptERIDiscoveryAttributeV3.

        linux script file  # noqa: E501

        :param linux_script: The linux_script of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._linux_script = linux_script

    @property
    def win_cmdline(self):
        """Gets the win_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501

        windows script command line  # noqa: E501

        :return: The win_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._win_cmdline

    @win_cmdline.setter
    def win_cmdline(self, win_cmdline):
        """Sets the win_cmdline of this ScriptERIDiscoveryAttributeV3.

        windows script command line  # noqa: E501

        :param win_cmdline: The win_cmdline of this ScriptERIDiscoveryAttributeV3.  # noqa: E501
        :type: str
        """

        self._win_cmdline = win_cmdline

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
        if issubclass(ScriptERIDiscoveryAttributeV3, dict):
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
        if not isinstance(other, ScriptERIDiscoveryAttributeV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other