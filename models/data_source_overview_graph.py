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

class DataSourceOverviewGraph(object):
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
        'base1024': 'bool',
        'time_scale': 'str',
        'max_value': 'object',
        'display_prio': 'int',
        'aggregated': 'bool',
        'title': 'str',
        'virtual_data_points': 'list[GraphVirtualDataPoint]',
        'min_value': 'object',
        'name': 'str',
        'width': 'int',
        'data_points': 'list[OverviewGraphDataPoint]',
        'vertical_label': 'str',
        'id': 'int',
        'rigid': 'bool',
        'lines': 'list[GraphLine]',
        'height': 'int'
    }

    attribute_map = {
        'base1024': 'base1024',
        'time_scale': 'timeScale',
        'max_value': 'maxValue',
        'display_prio': 'displayPrio',
        'aggregated': 'aggregated',
        'title': 'title',
        'virtual_data_points': 'virtualDataPoints',
        'min_value': 'minValue',
        'name': 'name',
        'width': 'width',
        'data_points': 'dataPoints',
        'vertical_label': 'verticalLabel',
        'id': 'id',
        'rigid': 'rigid',
        'lines': 'lines',
        'height': 'height'
    }

    def __init__(self, base1024=None, time_scale=None, max_value=None, display_prio=None, aggregated=None, title=None, virtual_data_points=None, min_value=None, name=None, width=None, data_points=None, vertical_label=None, id=None, rigid=None, lines=None, height=None):  # noqa: E501
        """DataSourceOverviewGraph - a model defined in Swagger"""  # noqa: E501
        self._base1024 = None
        self._time_scale = None
        self._max_value = None
        self._display_prio = None
        self._aggregated = None
        self._title = None
        self._virtual_data_points = None
        self._min_value = None
        self._name = None
        self._width = None
        self._data_points = None
        self._vertical_label = None
        self._id = None
        self._rigid = None
        self._lines = None
        self._height = None
        self.discriminator = None
        if base1024 is not None:
            self.base1024 = base1024
        if time_scale is not None:
            self.time_scale = time_scale
        if max_value is not None:
            self.max_value = max_value
        if display_prio is not None:
            self.display_prio = display_prio
        if aggregated is not None:
            self.aggregated = aggregated
        if title is not None:
            self.title = title
        if virtual_data_points is not None:
            self.virtual_data_points = virtual_data_points
        if min_value is not None:
            self.min_value = min_value
        if name is not None:
            self.name = name
        if width is not None:
            self.width = width
        if data_points is not None:
            self.data_points = data_points
        if vertical_label is not None:
            self.vertical_label = vertical_label
        if id is not None:
            self.id = id
        if rigid is not None:
            self.rigid = rigid
        if lines is not None:
            self.lines = lines
        if height is not None:
            self.height = height

    @property
    def base1024(self):
        """Gets the base1024 of this DataSourceOverviewGraph.  # noqa: E501

        base1024 graph or not  # noqa: E501

        :return: The base1024 of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: bool
        """
        return self._base1024

    @base1024.setter
    def base1024(self, base1024):
        """Sets the base1024 of this DataSourceOverviewGraph.

        base1024 graph or not  # noqa: E501

        :param base1024: The base1024 of this DataSourceOverviewGraph.  # noqa: E501
        :type: bool
        """

        self._base1024 = base1024

    @property
    def time_scale(self):
        """Gets the time_scale of this DataSourceOverviewGraph.  # noqa: E501

        The graph time scale.  The values can be 1hour|2hour|5hour|day|yesterday|week|lastweek|month|3month|year  # noqa: E501

        :return: The time_scale of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: str
        """
        return self._time_scale

    @time_scale.setter
    def time_scale(self, time_scale):
        """Sets the time_scale of this DataSourceOverviewGraph.

        The graph time scale.  The values can be 1hour|2hour|5hour|day|yesterday|week|lastweek|month|3month|year  # noqa: E501

        :param time_scale: The time_scale of this DataSourceOverviewGraph.  # noqa: E501
        :type: str
        """

        self._time_scale = time_scale

    @property
    def max_value(self):
        """Gets the max_value of this DataSourceOverviewGraph.  # noqa: E501

        The graph max value  # noqa: E501

        :return: The max_value of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: object
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this DataSourceOverviewGraph.

        The graph max value  # noqa: E501

        :param max_value: The max_value of this DataSourceOverviewGraph.  # noqa: E501
        :type: object
        """

        self._max_value = max_value

    @property
    def display_prio(self):
        """Gets the display_prio of this DataSourceOverviewGraph.  # noqa: E501

        The graph display priority  # noqa: E501

        :return: The display_prio of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: int
        """
        return self._display_prio

    @display_prio.setter
    def display_prio(self, display_prio):
        """Sets the display_prio of this DataSourceOverviewGraph.

        The graph display priority  # noqa: E501

        :param display_prio: The display_prio of this DataSourceOverviewGraph.  # noqa: E501
        :type: int
        """

        self._display_prio = display_prio

    @property
    def aggregated(self):
        """Gets the aggregated of this DataSourceOverviewGraph.  # noqa: E501

        Whether the overview graph is aggregated  # noqa: E501

        :return: The aggregated of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: bool
        """
        return self._aggregated

    @aggregated.setter
    def aggregated(self, aggregated):
        """Sets the aggregated of this DataSourceOverviewGraph.

        Whether the overview graph is aggregated  # noqa: E501

        :param aggregated: The aggregated of this DataSourceOverviewGraph.  # noqa: E501
        :type: bool
        """

        self._aggregated = aggregated

    @property
    def title(self):
        """Gets the title of this DataSourceOverviewGraph.  # noqa: E501

        The graph title  # noqa: E501

        :return: The title of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DataSourceOverviewGraph.

        The graph title  # noqa: E501

        :param title: The title of this DataSourceOverviewGraph.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def virtual_data_points(self):
        """Gets the virtual_data_points of this DataSourceOverviewGraph.  # noqa: E501

        The virtual data point list  # noqa: E501

        :return: The virtual_data_points of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: list[GraphVirtualDataPoint]
        """
        return self._virtual_data_points

    @virtual_data_points.setter
    def virtual_data_points(self, virtual_data_points):
        """Sets the virtual_data_points of this DataSourceOverviewGraph.

        The virtual data point list  # noqa: E501

        :param virtual_data_points: The virtual_data_points of this DataSourceOverviewGraph.  # noqa: E501
        :type: list[GraphVirtualDataPoint]
        """

        self._virtual_data_points = virtual_data_points

    @property
    def min_value(self):
        """Gets the min_value of this DataSourceOverviewGraph.  # noqa: E501

        The graph min value  # noqa: E501

        :return: The min_value of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: object
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this DataSourceOverviewGraph.

        The graph min value  # noqa: E501

        :param min_value: The min_value of this DataSourceOverviewGraph.  # noqa: E501
        :type: object
        """

        self._min_value = min_value

    @property
    def name(self):
        """Gets the name of this DataSourceOverviewGraph.  # noqa: E501

        The graph name  # noqa: E501

        :return: The name of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataSourceOverviewGraph.

        The graph name  # noqa: E501

        :param name: The name of this DataSourceOverviewGraph.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def width(self):
        """Gets the width of this DataSourceOverviewGraph.  # noqa: E501

        The graph width  # noqa: E501

        :return: The width of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DataSourceOverviewGraph.

        The graph width  # noqa: E501

        :param width: The width of this DataSourceOverviewGraph.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def data_points(self):
        """Gets the data_points of this DataSourceOverviewGraph.  # noqa: E501

        The graph data point list  # noqa: E501

        :return: The data_points of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: list[OverviewGraphDataPoint]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this DataSourceOverviewGraph.

        The graph data point list  # noqa: E501

        :param data_points: The data_points of this DataSourceOverviewGraph.  # noqa: E501
        :type: list[OverviewGraphDataPoint]
        """

        self._data_points = data_points

    @property
    def vertical_label(self):
        """Gets the vertical_label of this DataSourceOverviewGraph.  # noqa: E501

        The graph vertical label  # noqa: E501

        :return: The vertical_label of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: str
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, vertical_label):
        """Sets the vertical_label of this DataSourceOverviewGraph.

        The graph vertical label  # noqa: E501

        :param vertical_label: The vertical_label of this DataSourceOverviewGraph.  # noqa: E501
        :type: str
        """

        self._vertical_label = vertical_label

    @property
    def id(self):
        """Gets the id of this DataSourceOverviewGraph.  # noqa: E501

        The graph Id  # noqa: E501

        :return: The id of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSourceOverviewGraph.

        The graph Id  # noqa: E501

        :param id: The id of this DataSourceOverviewGraph.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rigid(self):
        """Gets the rigid of this DataSourceOverviewGraph.  # noqa: E501

        The rigid. The values can be true|false  # noqa: E501

        :return: The rigid of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: bool
        """
        return self._rigid

    @rigid.setter
    def rigid(self, rigid):
        """Sets the rigid of this DataSourceOverviewGraph.

        The rigid. The values can be true|false  # noqa: E501

        :param rigid: The rigid of this DataSourceOverviewGraph.  # noqa: E501
        :type: bool
        """

        self._rigid = rigid

    @property
    def lines(self):
        """Gets the lines of this DataSourceOverviewGraph.  # noqa: E501

        The graph lines  # noqa: E501

        :return: The lines of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: list[GraphLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this DataSourceOverviewGraph.

        The graph lines  # noqa: E501

        :param lines: The lines of this DataSourceOverviewGraph.  # noqa: E501
        :type: list[GraphLine]
        """

        self._lines = lines

    @property
    def height(self):
        """Gets the height of this DataSourceOverviewGraph.  # noqa: E501

        The graph height  # noqa: E501

        :return: The height of this DataSourceOverviewGraph.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DataSourceOverviewGraph.

        The graph height  # noqa: E501

        :param height: The height of this DataSourceOverviewGraph.  # noqa: E501
        :type: int
        """

        self._height = height

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
        if issubclass(DataSourceOverviewGraph, dict):
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
        if not isinstance(other, DataSourceOverviewGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
