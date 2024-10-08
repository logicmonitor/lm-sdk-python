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
from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501

class WebsiteOverviewWidget(Widget):
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
        'website_name': 'str',
        'website_id': 'int',
        'geo_info': 'str',
        'graph': 'str'
    }
    if hasattr(Widget, "swagger_types"):
        swagger_types.update(Widget.swagger_types)

    attribute_map = {
        'website_name': 'websiteName',
        'website_id': 'websiteId',
        'geo_info': 'geoInfo',
        'graph': 'graph'
    }
    if hasattr(Widget, "attribute_map"):
        attribute_map.update(Widget.attribute_map)

    def __init__(self, website_name=None, website_id=None, geo_info=None, graph=None, *args, **kwargs):  # noqa: E501
        """WebsiteOverviewWidget - a model defined in Swagger"""  # noqa: E501
        self._website_name = None
        self._website_id = None
        self._geo_info = None
        self._graph = None
        self.discriminator = None
        if website_name is not None:
            self.website_name = website_name
        if website_id is not None:
            self.website_id = website_id
        if geo_info is not None:
            self.geo_info = geo_info
        self.graph = graph
        Widget.__init__(self, *args, **kwargs)

    @property
    def website_name(self):
        """Gets the website_name of this WebsiteOverviewWidget.  # noqa: E501


        :return: The website_name of this WebsiteOverviewWidget.  # noqa: E501
        :rtype: str
        """
        return self._website_name

    @website_name.setter
    def website_name(self, website_name):
        """Sets the website_name of this WebsiteOverviewWidget.


        :param website_name: The website_name of this WebsiteOverviewWidget.  # noqa: E501
        :type: str
        """

        self._website_name = website_name

    @property
    def website_id(self):
        """Gets the website_id of this WebsiteOverviewWidget.  # noqa: E501


        :return: The website_id of this WebsiteOverviewWidget.  # noqa: E501
        :rtype: int
        """
        return self._website_id

    @website_id.setter
    def website_id(self, website_id):
        """Sets the website_id of this WebsiteOverviewWidget.


        :param website_id: The website_id of this WebsiteOverviewWidget.  # noqa: E501
        :type: int
        """

        self._website_id = website_id

    @property
    def geo_info(self):
        """Gets the geo_info of this WebsiteOverviewWidget.  # noqa: E501


        :return: The geo_info of this WebsiteOverviewWidget.  # noqa: E501
        :rtype: str
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """Sets the geo_info of this WebsiteOverviewWidget.


        :param geo_info: The geo_info of this WebsiteOverviewWidget.  # noqa: E501
        :type: str
        """

        self._geo_info = geo_info

    @property
    def graph(self):
        """Gets the graph of this WebsiteOverviewWidget.  # noqa: E501


        :return: The graph of this WebsiteOverviewWidget.  # noqa: E501
        :rtype: str
        """
        return self._graph

    @graph.setter
    def graph(self, graph):
        """Sets the graph of this WebsiteOverviewWidget.


        :param graph: The graph of this WebsiteOverviewWidget.  # noqa: E501
        :type: str
        """
        if graph is None:
            raise ValueError("Invalid value for `graph`, must not be `None`")  # noqa: E501

        self._graph = graph

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
        if issubclass(WebsiteOverviewWidget, dict):
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
        if not isinstance(other, WebsiteOverviewWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
