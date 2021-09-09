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

from logicmonitor_sdk.models.item_data import ItemData  # noqa: F401,E501
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class NOCWidgetData(WidgetData):
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
        'type': 'str',
        'title': 'str',
        'ack_checked': 'bool',
        'sdt_checked': 'bool',
        'items': 'list[ItemData]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'ack_checked': 'ackChecked',
        'sdt_checked': 'sdtChecked',
        'items': 'items'
    }

    def __init__(self, type=None, title=None, ack_checked=None, sdt_checked=None, items=None):  # noqa: E501
        """NOCWidgetData - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._ack_checked = None
        self._sdt_checked = None
        self._items = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if ack_checked is not None:
            self.ack_checked = ack_checked
        if sdt_checked is not None:
            self.sdt_checked = sdt_checked
        if items is not None:
            self.items = items

    @property
    def type(self):
        """Gets the type of this NOCWidgetData.  # noqa: E501


        :return: The type of this NOCWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NOCWidgetData.


        :param type: The type of this NOCWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this NOCWidgetData.  # noqa: E501


        :return: The title of this NOCWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NOCWidgetData.


        :param title: The title of this NOCWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def ack_checked(self):
        """Gets the ack_checked of this NOCWidgetData.  # noqa: E501


        :return: The ack_checked of this NOCWidgetData.  # noqa: E501
        :rtype: bool
        """
        return self._ack_checked

    @ack_checked.setter
    def ack_checked(self, ack_checked):
        """Sets the ack_checked of this NOCWidgetData.


        :param ack_checked: The ack_checked of this NOCWidgetData.  # noqa: E501
        :type: bool
        """

        self._ack_checked = ack_checked

    @property
    def sdt_checked(self):
        """Gets the sdt_checked of this NOCWidgetData.  # noqa: E501


        :return: The sdt_checked of this NOCWidgetData.  # noqa: E501
        :rtype: bool
        """
        return self._sdt_checked

    @sdt_checked.setter
    def sdt_checked(self, sdt_checked):
        """Sets the sdt_checked of this NOCWidgetData.


        :param sdt_checked: The sdt_checked of this NOCWidgetData.  # noqa: E501
        :type: bool
        """

        self._sdt_checked = sdt_checked

    @property
    def items(self):
        """Gets the items of this NOCWidgetData.  # noqa: E501


        :return: The items of this NOCWidgetData.  # noqa: E501
        :rtype: list[ItemData]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NOCWidgetData.


        :param items: The items of this NOCWidgetData.  # noqa: E501
        :type: list[ItemData]
        """

        self._items = items

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
        if issubclass(NOCWidgetData, dict):
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
        if not isinstance(other, NOCWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
