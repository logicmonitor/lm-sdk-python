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

from logicmonitor_sdk.models.netflow_data_base import NetflowDataBase  # noqa: F401,E501
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class NetflowGroupWidgetData(WidgetData):
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
        'total': 'int',
        'items': 'list[NetflowDataBase]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'total': 'total',
        'items': 'items'
    }

    def __init__(self, type=None, title=None, total=None, items=None):  # noqa: E501
        """NetflowGroupWidgetData - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._total = None
        self._items = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if total is not None:
            self.total = total
        if items is not None:
            self.items = items

    @property
    def type(self):
        """Gets the type of this NetflowGroupWidgetData.  # noqa: E501

        The widget data type. The values can be noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :return: The type of this NetflowGroupWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetflowGroupWidgetData.

        The widget data type. The values can be noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :param type: The type of this NetflowGroupWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this NetflowGroupWidgetData.  # noqa: E501

        The widget title  # noqa: E501

        :return: The title of this NetflowGroupWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NetflowGroupWidgetData.

        The widget title  # noqa: E501

        :param title: The title of this NetflowGroupWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def total(self):
        """Gets the total of this NetflowGroupWidgetData.  # noqa: E501


        :return: The total of this NetflowGroupWidgetData.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NetflowGroupWidgetData.


        :param total: The total of this NetflowGroupWidgetData.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def items(self):
        """Gets the items of this NetflowGroupWidgetData.  # noqa: E501


        :return: The items of this NetflowGroupWidgetData.  # noqa: E501
        :rtype: list[NetflowDataBase]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NetflowGroupWidgetData.


        :param items: The items of this NetflowGroupWidgetData.  # noqa: E501
        :type: list[NetflowDataBase]
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
        if issubclass(NetflowGroupWidgetData, dict):
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
        if not isinstance(other, NetflowGroupWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
