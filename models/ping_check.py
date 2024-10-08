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
from logicmonitor_sdk.models.website import Website  # noqa: F401,E501

class PingCheck(Website):
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
        'percent_pkts_not_receive_in_time': 'int',
        'count': 'int',
        'host': 'str',
        'timeout_in_ms_pkts_not_receive': 'int'
    }
    if hasattr(Website, "swagger_types"):
        swagger_types.update(Website.swagger_types)

    attribute_map = {
        'percent_pkts_not_receive_in_time': 'percentPktsNotReceiveInTime',
        'count': 'count',
        'host': 'host',
        'timeout_in_ms_pkts_not_receive': 'timeoutInMSPktsNotReceive'
    }
    if hasattr(Website, "attribute_map"):
        attribute_map.update(Website.attribute_map)

    def __init__(self, percent_pkts_not_receive_in_time=None, count=None, host=None, timeout_in_ms_pkts_not_receive=None, *args, **kwargs):  # noqa: E501
        """PingCheck - a model defined in Swagger"""  # noqa: E501
        self._percent_pkts_not_receive_in_time = None
        self._count = None
        self._host = None
        self._timeout_in_ms_pkts_not_receive = None
        self.discriminator = None
        if percent_pkts_not_receive_in_time is not None:
            self.percent_pkts_not_receive_in_time = percent_pkts_not_receive_in_time
        if count is not None:
            self.count = count
        self.host = host
        if timeout_in_ms_pkts_not_receive is not None:
            self.timeout_in_ms_pkts_not_receive = timeout_in_ms_pkts_not_receive
        Website.__init__(self, *args, **kwargs)

    @property
    def percent_pkts_not_receive_in_time(self):
        """Gets the percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501

        The percentage of packets that should be returned in the time period specified by timeoutInMSPktsNotReceive for each ping check  # noqa: E501

        :return: The percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._percent_pkts_not_receive_in_time

    @percent_pkts_not_receive_in_time.setter
    def percent_pkts_not_receive_in_time(self, percent_pkts_not_receive_in_time):
        """Sets the percent_pkts_not_receive_in_time of this PingCheck.

        The percentage of packets that should be returned in the time period specified by timeoutInMSPktsNotReceive for each ping check  # noqa: E501

        :param percent_pkts_not_receive_in_time: The percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501
        :type: int
        """

        self._percent_pkts_not_receive_in_time = percent_pkts_not_receive_in_time

    @property
    def count(self):
        """Gets the count of this PingCheck.  # noqa: E501

        The number of packets to send  # noqa: E501

        :return: The count of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PingCheck.

        The number of packets to send  # noqa: E501

        :param count: The count of this PingCheck.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def host(self):
        """Gets the host of this PingCheck.  # noqa: E501

        The URL to check, without the scheme or protocol (e.g http or https) E.g. if the URL is \"http://www.google.com, then the host=\"www.google.com\"  # noqa: E501

        :return: The host of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this PingCheck.

        The URL to check, without the scheme or protocol (e.g http or https) E.g. if the URL is \"http://www.google.com, then the host=\"www.google.com\"  # noqa: E501

        :param host: The host of this PingCheck.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def timeout_in_ms_pkts_not_receive(self):
        """Gets the timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501

        The time period that the percentage of packets specified by percentPktsNotReceiveInTime must be returned in for each ping check  # noqa: E501

        :return: The timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._timeout_in_ms_pkts_not_receive

    @timeout_in_ms_pkts_not_receive.setter
    def timeout_in_ms_pkts_not_receive(self, timeout_in_ms_pkts_not_receive):
        """Sets the timeout_in_ms_pkts_not_receive of this PingCheck.

        The time period that the percentage of packets specified by percentPktsNotReceiveInTime must be returned in for each ping check  # noqa: E501

        :param timeout_in_ms_pkts_not_receive: The timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501
        :type: int
        """

        self._timeout_in_ms_pkts_not_receive = timeout_in_ms_pkts_not_receive

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
        if issubclass(PingCheck, dict):
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
        if not isinstance(other, PingCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
