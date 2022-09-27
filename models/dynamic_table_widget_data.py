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

from logicmonitor_sdk.models.column_header import ColumnHeader  # noqa: F401,E501
from logicmonitor_sdk.models.row_data import RowData  # noqa: F401,E501
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class DynamicTableWidgetData(WidgetData):
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
        'column_headers': 'list[ColumnHeader]',
        'rows': 'list[RowData]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'column_headers': 'columnHeaders',
        'rows': 'rows'
    }

    def __init__(self, type=None, title=None, column_headers=None, rows=None):  # noqa: E501
        """DynamicTableWidgetData - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._column_headers = None
        self._rows = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if column_headers is not None:
            self.column_headers = column_headers
        if rows is not None:
            self.rows = rows

    @property
    def type(self):
        """Gets the type of this DynamicTableWidgetData.  # noqa: E501

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :return: The type of this DynamicTableWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicTableWidgetData.

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :param type: The type of this DynamicTableWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this DynamicTableWidgetData.  # noqa: E501

        the widget title  # noqa: E501

        :return: The title of this DynamicTableWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DynamicTableWidgetData.

        the widget title  # noqa: E501

        :param title: The title of this DynamicTableWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def column_headers(self):
        """Gets the column_headers of this DynamicTableWidgetData.  # noqa: E501


        :return: The column_headers of this DynamicTableWidgetData.  # noqa: E501
        :rtype: list[ColumnHeader]
        """
        return self._column_headers

    @column_headers.setter
    def column_headers(self, column_headers):
        """Sets the column_headers of this DynamicTableWidgetData.


        :param column_headers: The column_headers of this DynamicTableWidgetData.  # noqa: E501
        :type: list[ColumnHeader]
        """

        self._column_headers = column_headers

    @property
    def rows(self):
        """Gets the rows of this DynamicTableWidgetData.  # noqa: E501


        :return: The rows of this DynamicTableWidgetData.  # noqa: E501
        :rtype: list[RowData]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DynamicTableWidgetData.


        :param rows: The rows of this DynamicTableWidgetData.  # noqa: E501
        :type: list[RowData]
        """

        self._rows = rows

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
        if issubclass(DynamicTableWidgetData, dict):
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
        if not isinstance(other, DynamicTableWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
