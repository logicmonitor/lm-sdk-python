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


class Debug(object):
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
        'output': 'str',
        'cmdline': 'str',
        'cmd_context': 'str',
        'session_id': 'str'
    }

    attribute_map = {
        'output': 'output',
        'cmdline': 'cmdline',
        'cmd_context': 'cmdContext',
        'session_id': 'sessionId'
    }

    def __init__(self, output=None, cmdline=None, cmd_context=None, session_id=None):  # noqa: E501
        """Debug - a model defined in Swagger"""  # noqa: E501

        self._output = None
        self._cmdline = None
        self._cmd_context = None
        self._session_id = None
        self.discriminator = None

        if output is not None:
            self.output = output
        if cmdline is not None:
            self.cmdline = cmdline
        if cmd_context is not None:
            self.cmd_context = cmd_context
        if session_id is not None:
            self.session_id = session_id

    @property
    def output(self):
        """Gets the output of this Debug.  # noqa: E501

        The value of the debug command  # noqa: E501

        :return: The output of this Debug.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Debug.

        The value of the debug command  # noqa: E501

        :param output: The output of this Debug.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def cmdline(self):
        """Gets the cmdline of this Debug.  # noqa: E501

        The debug command to execute  # noqa: E501

        :return: The cmdline of this Debug.  # noqa: E501
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        """Sets the cmdline of this Debug.

        The debug command to execute  # noqa: E501

        :param cmdline: The cmdline of this Debug.  # noqa: E501
        :type: str
        """

        self._cmdline = cmdline

    @property
    def cmd_context(self):
        """Gets the cmd_context of this Debug.  # noqa: E501

        The session prefix name  # noqa: E501

        :return: The cmd_context of this Debug.  # noqa: E501
        :rtype: str
        """
        return self._cmd_context

    @cmd_context.setter
    def cmd_context(self, cmd_context):
        """Sets the cmd_context of this Debug.

        The session prefix name  # noqa: E501

        :param cmd_context: The cmd_context of this Debug.  # noqa: E501
        :type: str
        """

        self._cmd_context = cmd_context

    @property
    def session_id(self):
        """Gets the session_id of this Debug.  # noqa: E501

        The session id  # noqa: E501

        :return: The session_id of this Debug.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this Debug.

        The session id  # noqa: E501

        :param session_id: The session_id of this Debug.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

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
        if issubclass(Debug, dict):
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
        if not isinstance(other, Debug):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
