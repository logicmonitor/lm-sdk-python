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

from logicmonitor_sdk.models.pie_chart_info import PieChartInfo  # noqa: F401,E501
from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501


class PieChartWidget(Widget):
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
        'last_updated_by': 'str',
        'user_permission': 'str',
        'dashboard_id': 'int',
        'name': 'str',
        'description': 'str',
        'last_updated_on': 'int',
        'theme': 'str',
        'interval': 'int',
        'id': 'int',
        'type': 'str',
        'timescale': 'str',
        'pie_chart_info': 'PieChartInfo'
    }

    attribute_map = {
        'last_updated_by': 'lastUpdatedBy',
        'user_permission': 'userPermission',
        'dashboard_id': 'dashboardId',
        'name': 'name',
        'description': 'description',
        'last_updated_on': 'lastUpdatedOn',
        'theme': 'theme',
        'interval': 'interval',
        'id': 'id',
        'type': 'type',
        'timescale': 'timescale',
        'pie_chart_info': 'pieChartInfo'
    }

    def __init__(self, last_updated_by=None, user_permission=None, dashboard_id=None, name=None, description=None, last_updated_on=None, theme=None, interval=None, id=None, type=None, timescale=None, pie_chart_info=None):  # noqa: E501
        """PieChartWidget - a model defined in Swagger"""  # noqa: E501

        self._last_updated_by = None
        self._user_permission = None
        self._dashboard_id = None
        self._name = None
        self._description = None
        self._last_updated_on = None
        self._theme = None
        self._interval = None
        self._id = None
        self._type = None
        self._timescale = None
        self._pie_chart_info = None
        self.discriminator = None

        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if user_permission is not None:
            self.user_permission = user_permission
        self.dashboard_id = dashboard_id
        self.name = name
        if description is not None:
            self.description = description
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        if theme is not None:
            self.theme = theme
        if interval is not None:
            self.interval = interval
        if id is not None:
            self.id = id
        self.type = type
        if timescale is not None:
            self.timescale = timescale
        self.pie_chart_info = pie_chart_info

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this PieChartWidget.  # noqa: E501

        The user that last updated the widget  # noqa: E501

        :return: The last_updated_by of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this PieChartWidget.

        The user that last updated the widget  # noqa: E501

        :param last_updated_by: The last_updated_by of this PieChartWidget.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def user_permission(self):
        """Gets the user_permission of this PieChartWidget.  # noqa: E501

        The permission level of the user who last modified the widget  # noqa: E501

        :return: The user_permission of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this PieChartWidget.

        The permission level of the user who last modified the widget  # noqa: E501

        :param user_permission: The user_permission of this PieChartWidget.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this PieChartWidget.  # noqa: E501

        The id of the dashboard the widget belongs to  # noqa: E501

        :return: The dashboard_id of this PieChartWidget.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this PieChartWidget.

        The id of the dashboard the widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this PieChartWidget.  # noqa: E501
        :type: int
        """
        if dashboard_id is None:
            raise ValueError("Invalid value for `dashboard_id`, must not be `None`")  # noqa: E501

        self._dashboard_id = dashboard_id

    @property
    def name(self):
        """Gets the name of this PieChartWidget.  # noqa: E501

        The name of the widget  # noqa: E501

        :return: The name of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PieChartWidget.

        The name of the widget  # noqa: E501

        :param name: The name of this PieChartWidget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this PieChartWidget.  # noqa: E501

        The description of the widget  # noqa: E501

        :return: The description of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PieChartWidget.

        The description of the widget  # noqa: E501

        :param description: The description of this PieChartWidget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this PieChartWidget.  # noqa: E501

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :return: The last_updated_on of this PieChartWidget.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this PieChartWidget.

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :param last_updated_on: The last_updated_on of this PieChartWidget.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def theme(self):
        """Gets the theme of this PieChartWidget.  # noqa: E501

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :return: The theme of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this PieChartWidget.

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :param theme: The theme of this PieChartWidget.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def interval(self):
        """Gets the interval of this PieChartWidget.  # noqa: E501

        The refresh interval of the widget, in minutes  # noqa: E501

        :return: The interval of this PieChartWidget.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PieChartWidget.

        The refresh interval of the widget, in minutes  # noqa: E501

        :param interval: The interval of this PieChartWidget.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def id(self):
        """Gets the id of this PieChartWidget.  # noqa: E501

        The Id of the widget  # noqa: E501

        :return: The id of this PieChartWidget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PieChartWidget.

        The Id of the widget  # noqa: E501

        :param id: The id of this PieChartWidget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this PieChartWidget.  # noqa: E501

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA | savedMap  # noqa: E501

        :return: The type of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PieChartWidget.

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA | savedMap  # noqa: E501

        :param type: The type of this PieChartWidget.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def timescale(self):
        """Gets the timescale of this PieChartWidget.  # noqa: E501

        The default timescale of the widget  # noqa: E501

        :return: The timescale of this PieChartWidget.  # noqa: E501
        :rtype: str
        """
        return self._timescale

    @timescale.setter
    def timescale(self, timescale):
        """Sets the timescale of this PieChartWidget.

        The default timescale of the widget  # noqa: E501

        :param timescale: The timescale of this PieChartWidget.  # noqa: E501
        :type: str
        """

        self._timescale = timescale

    @property
    def pie_chart_info(self):
        """Gets the pie_chart_info of this PieChartWidget.  # noqa: E501


        :return: The pie_chart_info of this PieChartWidget.  # noqa: E501
        :rtype: PieChartInfo
        """
        return self._pie_chart_info

    @pie_chart_info.setter
    def pie_chart_info(self, pie_chart_info):
        """Sets the pie_chart_info of this PieChartWidget.


        :param pie_chart_info: The pie_chart_info of this PieChartWidget.  # noqa: E501
        :type: PieChartInfo
        """
        if pie_chart_info is None:
            raise ValueError("Invalid value for `pie_chart_info`, must not be `None`")  # noqa: E501

        self._pie_chart_info = pie_chart_info

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
        if issubclass(PieChartWidget, dict):
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
        if not isinstance(other, PieChartWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
