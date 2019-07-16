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

from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class WebsiteSLAWidgetData(WidgetData):
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
        'title': 'str',
        'type': 'str',
        'availability': 'float',
        'color_level': 'int'
    }

    attribute_map = {
        'title': 'title',
        'type': 'type',
        'availability': 'availability',
        'color_level': 'colorLevel'
    }

    def __init__(self, title=None, type=None, availability=None, color_level=None):  # noqa: E501
        """WebsiteSLAWidgetData - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._type = None
        self._availability = None
        self._color_level = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if availability is not None:
            self.availability = availability
        if color_level is not None:
            self.color_level = color_level

    @property
    def title(self):
        """Gets the title of this WebsiteSLAWidgetData.  # noqa: E501


        :return: The title of this WebsiteSLAWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WebsiteSLAWidgetData.


        :param title: The title of this WebsiteSLAWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this WebsiteSLAWidgetData.  # noqa: E501


        :return: The type of this WebsiteSLAWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebsiteSLAWidgetData.


        :param type: The type of this WebsiteSLAWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def availability(self):
        """Gets the availability of this WebsiteSLAWidgetData.  # noqa: E501


        :return: The availability of this WebsiteSLAWidgetData.  # noqa: E501
        :rtype: float
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this WebsiteSLAWidgetData.


        :param availability: The availability of this WebsiteSLAWidgetData.  # noqa: E501
        :type: float
        """

        self._availability = availability

    @property
    def color_level(self):
        """Gets the color_level of this WebsiteSLAWidgetData.  # noqa: E501


        :return: The color_level of this WebsiteSLAWidgetData.  # noqa: E501
        :rtype: int
        """
        return self._color_level

    @color_level.setter
    def color_level(self, color_level):
        """Sets the color_level of this WebsiteSLAWidgetData.


        :param color_level: The color_level of this WebsiteSLAWidgetData.  # noqa: E501
        :type: int
        """

        self._color_level = color_level

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
        if issubclass(WebsiteSLAWidgetData, dict):
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
        if not isinstance(other, WebsiteSLAWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
