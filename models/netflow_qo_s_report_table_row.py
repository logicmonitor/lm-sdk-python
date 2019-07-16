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

from logicmonitor_sdk.models.netflow_data_base import NetflowDataBase  # noqa: F401,E501


class NetflowQoSReportTableRow(NetflowDataBase):
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
        'data_type': 'str',
        'received': 'float',
        'sent': 'float',
        'type': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'received': 'received',
        'sent': 'sent',
        'type': 'type'
    }

    def __init__(self, data_type=None, received=None, sent=None, type=None):  # noqa: E501
        """NetflowQoSReportTableRow - a model defined in Swagger"""  # noqa: E501

        self._data_type = None
        self._received = None
        self._sent = None
        self._type = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if received is not None:
            self.received = received
        if sent is not None:
            self.sent = sent
        if type is not None:
            self.type = type

    @property
    def data_type(self):
        """Gets the data_type of this NetflowQoSReportTableRow.  # noqa: E501


        :return: The data_type of this NetflowQoSReportTableRow.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this NetflowQoSReportTableRow.


        :param data_type: The data_type of this NetflowQoSReportTableRow.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def received(self):
        """Gets the received of this NetflowQoSReportTableRow.  # noqa: E501


        :return: The received of this NetflowQoSReportTableRow.  # noqa: E501
        :rtype: float
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this NetflowQoSReportTableRow.


        :param received: The received of this NetflowQoSReportTableRow.  # noqa: E501
        :type: float
        """

        self._received = received

    @property
    def sent(self):
        """Gets the sent of this NetflowQoSReportTableRow.  # noqa: E501


        :return: The sent of this NetflowQoSReportTableRow.  # noqa: E501
        :rtype: float
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this NetflowQoSReportTableRow.


        :param sent: The sent of this NetflowQoSReportTableRow.  # noqa: E501
        :type: float
        """

        self._sent = sent

    @property
    def type(self):
        """Gets the type of this NetflowQoSReportTableRow.  # noqa: E501


        :return: The type of this NetflowQoSReportTableRow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetflowQoSReportTableRow.


        :param type: The type of this NetflowQoSReportTableRow.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(NetflowQoSReportTableRow, dict):
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
        if not isinstance(other, NetflowQoSReportTableRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
