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
from logicmonitor_sdk.models.event_source import EventSource  # noqa: F401,E501

class LogFileEventSource(EventSource):
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
        'log_files': 'list[LogFile]'
    }
    if hasattr(EventSource, "swagger_types"):
        swagger_types.update(EventSource.swagger_types)

    attribute_map = {
        'log_files': 'logFiles'
    }
    if hasattr(EventSource, "attribute_map"):
        attribute_map.update(EventSource.attribute_map)

    def __init__(self, log_files=None, *args, **kwargs):  # noqa: E501
        """LogFileEventSource - a model defined in Swagger"""  # noqa: E501
        self._log_files = None
        self.discriminator = None
        if log_files is not None:
            self.log_files = log_files
        EventSource.__init__(self, *args, **kwargs)

    @property
    def log_files(self):
        """Gets the log_files of this LogFileEventSource.  # noqa: E501

        log files  # noqa: E501

        :return: The log_files of this LogFileEventSource.  # noqa: E501
        :rtype: list[LogFile]
        """
        return self._log_files

    @log_files.setter
    def log_files(self, log_files):
        """Sets the log_files of this LogFileEventSource.

        log files  # noqa: E501

        :param log_files: The log_files of this LogFileEventSource.  # noqa: E501
        :type: list[LogFile]
        """

        self._log_files = log_files

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
        if issubclass(LogFileEventSource, dict):
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
        if not isinstance(other, LogFileEventSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
