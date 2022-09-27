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

from logicmonitor_sdk.models.pie_chart_data import PieChartData  # noqa: F401,E501
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class PieChartWidgetData(WidgetData):
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
        'max_slices_can_be_shown': 'int',
        'data': 'list[PieChartData]',
        'hide_zero_percent_slices': 'bool',
        'group_remaining_as_others': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'max_slices_can_be_shown': 'maxSlicesCanBeShown',
        'data': 'data',
        'hide_zero_percent_slices': 'hideZeroPercentSlices',
        'group_remaining_as_others': 'groupRemainingAsOthers'
    }

    def __init__(self, type=None, title=None, max_slices_can_be_shown=None, data=None, hide_zero_percent_slices=None, group_remaining_as_others=None):  # noqa: E501
        """PieChartWidgetData - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._max_slices_can_be_shown = None
        self._data = None
        self._hide_zero_percent_slices = None
        self._group_remaining_as_others = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if max_slices_can_be_shown is not None:
            self.max_slices_can_be_shown = max_slices_can_be_shown
        if data is not None:
            self.data = data
        if hide_zero_percent_slices is not None:
            self.hide_zero_percent_slices = hide_zero_percent_slices
        if group_remaining_as_others is not None:
            self.group_remaining_as_others = group_remaining_as_others

    @property
    def type(self):
        """Gets the type of this PieChartWidgetData.  # noqa: E501

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :return: The type of this PieChartWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PieChartWidgetData.

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :param type: The type of this PieChartWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this PieChartWidgetData.  # noqa: E501

        the widget title  # noqa: E501

        :return: The title of this PieChartWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PieChartWidgetData.

        the widget title  # noqa: E501

        :param title: The title of this PieChartWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def max_slices_can_be_shown(self):
        """Gets the max_slices_can_be_shown of this PieChartWidgetData.  # noqa: E501


        :return: The max_slices_can_be_shown of this PieChartWidgetData.  # noqa: E501
        :rtype: int
        """
        return self._max_slices_can_be_shown

    @max_slices_can_be_shown.setter
    def max_slices_can_be_shown(self, max_slices_can_be_shown):
        """Sets the max_slices_can_be_shown of this PieChartWidgetData.


        :param max_slices_can_be_shown: The max_slices_can_be_shown of this PieChartWidgetData.  # noqa: E501
        :type: int
        """

        self._max_slices_can_be_shown = max_slices_can_be_shown

    @property
    def data(self):
        """Gets the data of this PieChartWidgetData.  # noqa: E501


        :return: The data of this PieChartWidgetData.  # noqa: E501
        :rtype: list[PieChartData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PieChartWidgetData.


        :param data: The data of this PieChartWidgetData.  # noqa: E501
        :type: list[PieChartData]
        """

        self._data = data

    @property
    def hide_zero_percent_slices(self):
        """Gets the hide_zero_percent_slices of this PieChartWidgetData.  # noqa: E501


        :return: The hide_zero_percent_slices of this PieChartWidgetData.  # noqa: E501
        :rtype: bool
        """
        return self._hide_zero_percent_slices

    @hide_zero_percent_slices.setter
    def hide_zero_percent_slices(self, hide_zero_percent_slices):
        """Sets the hide_zero_percent_slices of this PieChartWidgetData.


        :param hide_zero_percent_slices: The hide_zero_percent_slices of this PieChartWidgetData.  # noqa: E501
        :type: bool
        """

        self._hide_zero_percent_slices = hide_zero_percent_slices

    @property
    def group_remaining_as_others(self):
        """Gets the group_remaining_as_others of this PieChartWidgetData.  # noqa: E501


        :return: The group_remaining_as_others of this PieChartWidgetData.  # noqa: E501
        :rtype: bool
        """
        return self._group_remaining_as_others

    @group_remaining_as_others.setter
    def group_remaining_as_others(self, group_remaining_as_others):
        """Sets the group_remaining_as_others of this PieChartWidgetData.


        :param group_remaining_as_others: The group_remaining_as_others of this PieChartWidgetData.  # noqa: E501
        :type: bool
        """

        self._group_remaining_as_others = group_remaining_as_others

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
        if issubclass(PieChartWidgetData, dict):
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
        if not isinstance(other, PieChartWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
