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

from logicmonitor_sdk.models.custom_graph import CustomGraph  # noqa: F401,E501
from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501


class CustomGraphWidget(Widget):
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
        'dashboard_id': 'int',
        'description': 'str',
        'id': 'int',
        'interval': 'int',
        'last_updated_by': 'str',
        'last_updated_on': 'int',
        'name': 'str',
        'theme': 'str',
        'timescale': 'str',
        'type': 'str',
        'user_permission': 'str',
        'graph_info': 'CustomGraph'
    }

    attribute_map = {
        'dashboard_id': 'dashboardId',
        'description': 'description',
        'id': 'id',
        'interval': 'interval',
        'last_updated_by': 'lastUpdatedBy',
        'last_updated_on': 'lastUpdatedOn',
        'name': 'name',
        'theme': 'theme',
        'timescale': 'timescale',
        'type': 'type',
        'user_permission': 'userPermission',
        'graph_info': 'graphInfo'
    }

    def __init__(self, dashboard_id=None, description=None, id=None, interval=None, last_updated_by=None, last_updated_on=None, name=None, theme=None, timescale=None, type=None, user_permission=None, graph_info=None):  # noqa: E501
        """CustomGraphWidget - a model defined in Swagger"""  # noqa: E501

        self._dashboard_id = None
        self._description = None
        self._id = None
        self._interval = None
        self._last_updated_by = None
        self._last_updated_on = None
        self._name = None
        self._theme = None
        self._timescale = None
        self._type = None
        self._user_permission = None
        self._graph_info = None
        self.discriminator = None

        self.dashboard_id = dashboard_id
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        self.name = name
        if theme is not None:
            self.theme = theme
        if timescale is not None:
            self.timescale = timescale
        self.type = type
        if user_permission is not None:
            self.user_permission = user_permission
        if graph_info is not None:
            self.graph_info = graph_info

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this CustomGraphWidget.  # noqa: E501

        The id of the dashboard the widget belongs to  # noqa: E501

        :return: The dashboard_id of this CustomGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this CustomGraphWidget.

        The id of the dashboard the widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this CustomGraphWidget.  # noqa: E501
        :type: int
        """
        if dashboard_id is None:
            raise ValueError("Invalid value for `dashboard_id`, must not be `None`")  # noqa: E501

        self._dashboard_id = dashboard_id

    @property
    def description(self):
        """Gets the description of this CustomGraphWidget.  # noqa: E501

        The description of the widget  # noqa: E501

        :return: The description of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomGraphWidget.

        The description of the widget  # noqa: E501

        :param description: The description of this CustomGraphWidget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this CustomGraphWidget.  # noqa: E501

        The Id of the widget  # noqa: E501

        :return: The id of this CustomGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomGraphWidget.

        The Id of the widget  # noqa: E501

        :param id: The id of this CustomGraphWidget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this CustomGraphWidget.  # noqa: E501

        The refresh interval of the widget, in minutes  # noqa: E501

        :return: The interval of this CustomGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CustomGraphWidget.

        The refresh interval of the widget, in minutes  # noqa: E501

        :param interval: The interval of this CustomGraphWidget.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this CustomGraphWidget.  # noqa: E501

        The user that last updated the widget  # noqa: E501

        :return: The last_updated_by of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this CustomGraphWidget.

        The user that last updated the widget  # noqa: E501

        :param last_updated_by: The last_updated_by of this CustomGraphWidget.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this CustomGraphWidget.  # noqa: E501

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :return: The last_updated_on of this CustomGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this CustomGraphWidget.

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :param last_updated_on: The last_updated_on of this CustomGraphWidget.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def name(self):
        """Gets the name of this CustomGraphWidget.  # noqa: E501

        The name of the widget  # noqa: E501

        :return: The name of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomGraphWidget.

        The name of the widget  # noqa: E501

        :param name: The name of this CustomGraphWidget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def theme(self):
        """Gets the theme of this CustomGraphWidget.  # noqa: E501

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :return: The theme of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this CustomGraphWidget.

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :param theme: The theme of this CustomGraphWidget.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def timescale(self):
        """Gets the timescale of this CustomGraphWidget.  # noqa: E501

        The default timescale of the widget  # noqa: E501

        :return: The timescale of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._timescale

    @timescale.setter
    def timescale(self, timescale):
        """Sets the timescale of this CustomGraphWidget.

        The default timescale of the widget  # noqa: E501

        :param timescale: The timescale of this CustomGraphWidget.  # noqa: E501
        :type: str
        """

        self._timescale = timescale

    @property
    def type(self):
        """Gets the type of this CustomGraphWidget.  # noqa: E501

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :return: The type of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomGraphWidget.

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :param type: The type of this CustomGraphWidget.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_permission(self):
        """Gets the user_permission of this CustomGraphWidget.  # noqa: E501

        The permission level of the user who last modified the widget  # noqa: E501

        :return: The user_permission of this CustomGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this CustomGraphWidget.

        The permission level of the user who last modified the widget  # noqa: E501

        :param user_permission: The user_permission of this CustomGraphWidget.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def graph_info(self):
        """Gets the graph_info of this CustomGraphWidget.  # noqa: E501


        :return: The graph_info of this CustomGraphWidget.  # noqa: E501
        :rtype: CustomGraph
        """
        return self._graph_info

    @graph_info.setter
    def graph_info(self, graph_info):
        """Sets the graph_info of this CustomGraphWidget.


        :param graph_info: The graph_info of this CustomGraphWidget.  # noqa: E501
        :type: CustomGraph
        """

        self._graph_info = graph_info

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
        if issubclass(CustomGraphWidget, dict):
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
        if not isinstance(other, CustomGraphWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
