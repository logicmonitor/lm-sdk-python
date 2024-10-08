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
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501

class GraphPlot(WidgetData):
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
        'missinglines': 'list[str]',
        'time_scale': 'str',
        'instances': 'list[int]',
        'timestamps': 'list[int]',
        'min_value': 'object',
        'start_time': 'int',
        'id': 'int',
        'rigid': 'bool',
        'lines': 'list[GraphPlotLine]',
        'height': 'int',
        'end_tz_offset': 'int',
        'base1024': 'bool',
        'ds_name': 'str',
        'max_value': 'object',
        'display_prio': 'int',
        'time_zone_id': 'str',
        'time_zone': 'str',
        'start_tz_offset': 'int',
        'x_axis_name': 'str',
        'width': 'int',
        'name': 'str',
        'vertical_label': 'str',
        'step': 'int',
        'end_time': 'int',
        'scopes': 'list[GraphOpsNoteScope]',
        'base': 'int',
        'export_file_name': 'str'
    }
    if hasattr(WidgetData, "swagger_types"):
        swagger_types.update(WidgetData.swagger_types)

    attribute_map = {
        'missinglines': 'missinglines',
        'time_scale': 'timeScale',
        'instances': 'instances',
        'timestamps': 'timestamps',
        'min_value': 'minValue',
        'start_time': 'startTime',
        'id': 'id',
        'rigid': 'rigid',
        'lines': 'lines',
        'height': 'height',
        'end_tz_offset': 'endTZOffset',
        'base1024': 'base1024',
        'ds_name': 'dsName',
        'max_value': 'maxValue',
        'display_prio': 'displayPrio',
        'time_zone_id': 'timeZoneId',
        'time_zone': 'timeZone',
        'start_tz_offset': 'startTZOffset',
        'x_axis_name': 'xAxisName',
        'width': 'width',
        'name': 'name',
        'vertical_label': 'verticalLabel',
        'step': 'step',
        'end_time': 'endTime',
        'scopes': 'scopes',
        'base': 'base',
        'export_file_name': 'exportFileName'
    }
    if hasattr(WidgetData, "attribute_map"):
        attribute_map.update(WidgetData.attribute_map)

    def __init__(self, missinglines=None, time_scale=None, instances=None, timestamps=None, min_value=None, start_time=None, id=None, rigid=None, lines=None, height=None, end_tz_offset=None, base1024=None, ds_name=None, max_value=None, display_prio=None, time_zone_id=None, time_zone=None, start_tz_offset=None, x_axis_name=None, width=None, name=None, vertical_label=None, step=None, end_time=None, scopes=None, base=None, export_file_name=None, *args, **kwargs):  # noqa: E501
        """GraphPlot - a model defined in Swagger"""  # noqa: E501
        self._missinglines = None
        self._time_scale = None
        self._instances = None
        self._timestamps = None
        self._min_value = None
        self._start_time = None
        self._id = None
        self._rigid = None
        self._lines = None
        self._height = None
        self._end_tz_offset = None
        self._base1024 = None
        self._ds_name = None
        self._max_value = None
        self._display_prio = None
        self._time_zone_id = None
        self._time_zone = None
        self._start_tz_offset = None
        self._x_axis_name = None
        self._width = None
        self._name = None
        self._vertical_label = None
        self._step = None
        self._end_time = None
        self._scopes = None
        self._base = None
        self._export_file_name = None
        self.discriminator = None
        if missinglines is not None:
            self.missinglines = missinglines
        if time_scale is not None:
            self.time_scale = time_scale
        if instances is not None:
            self.instances = instances
        if timestamps is not None:
            self.timestamps = timestamps
        if min_value is not None:
            self.min_value = min_value
        if start_time is not None:
            self.start_time = start_time
        if id is not None:
            self.id = id
        if rigid is not None:
            self.rigid = rigid
        if lines is not None:
            self.lines = lines
        if height is not None:
            self.height = height
        if end_tz_offset is not None:
            self.end_tz_offset = end_tz_offset
        if base1024 is not None:
            self.base1024 = base1024
        if ds_name is not None:
            self.ds_name = ds_name
        if max_value is not None:
            self.max_value = max_value
        if display_prio is not None:
            self.display_prio = display_prio
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if time_zone is not None:
            self.time_zone = time_zone
        if start_tz_offset is not None:
            self.start_tz_offset = start_tz_offset
        if x_axis_name is not None:
            self.x_axis_name = x_axis_name
        if width is not None:
            self.width = width
        if name is not None:
            self.name = name
        if vertical_label is not None:
            self.vertical_label = vertical_label
        if step is not None:
            self.step = step
        if end_time is not None:
            self.end_time = end_time
        if scopes is not None:
            self.scopes = scopes
        if base is not None:
            self.base = base
        if export_file_name is not None:
            self.export_file_name = export_file_name
        WidgetData.__init__(self, *args, **kwargs)

    @property
    def missinglines(self):
        """Gets the missinglines of this GraphPlot.  # noqa: E501

        The Missing lines of the graph  # noqa: E501

        :return: The missinglines of this GraphPlot.  # noqa: E501
        :rtype: list[str]
        """
        return self._missinglines

    @missinglines.setter
    def missinglines(self, missinglines):
        """Sets the missinglines of this GraphPlot.

        The Missing lines of the graph  # noqa: E501

        :param missinglines: The missinglines of this GraphPlot.  # noqa: E501
        :type: list[str]
        """

        self._missinglines = missinglines

    @property
    def time_scale(self):
        """Gets the time_scale of this GraphPlot.  # noqa: E501

        The specified timescale for the graph  # noqa: E501

        :return: The time_scale of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._time_scale

    @time_scale.setter
    def time_scale(self, time_scale):
        """Sets the time_scale of this GraphPlot.

        The specified timescale for the graph  # noqa: E501

        :param time_scale: The time_scale of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._time_scale = time_scale

    @property
    def instances(self):
        """Gets the instances of this GraphPlot.  # noqa: E501

        The matched instances of graph  # noqa: E501

        :return: The instances of this GraphPlot.  # noqa: E501
        :rtype: list[int]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this GraphPlot.

        The matched instances of graph  # noqa: E501

        :param instances: The instances of this GraphPlot.  # noqa: E501
        :type: list[int]
        """

        self._instances = instances

    @property
    def timestamps(self):
        """Gets the timestamps of this GraphPlot.  # noqa: E501

        The timestamps of the graph  # noqa: E501

        :return: The timestamps of this GraphPlot.  # noqa: E501
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this GraphPlot.

        The timestamps of the graph  # noqa: E501

        :param timestamps: The timestamps of this GraphPlot.  # noqa: E501
        :type: list[int]
        """

        self._timestamps = timestamps

    @property
    def min_value(self):
        """Gets the min_value of this GraphPlot.  # noqa: E501

        Specifies the minimum value of the graph  # noqa: E501

        :return: The min_value of this GraphPlot.  # noqa: E501
        :rtype: object
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this GraphPlot.

        Specifies the minimum value of the graph  # noqa: E501

        :param min_value: The min_value of this GraphPlot.  # noqa: E501
        :type: object
        """

        self._min_value = min_value

    @property
    def start_time(self):
        """Gets the start_time of this GraphPlot.  # noqa: E501

        Specifies the start-time of the graph  # noqa: E501

        :return: The start_time of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GraphPlot.

        Specifies the start-time of the graph  # noqa: E501

        :param start_time: The start_time of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def id(self):
        """Gets the id of this GraphPlot.  # noqa: E501

        The Id of the graph  # noqa: E501

        :return: The id of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GraphPlot.

        The Id of the graph  # noqa: E501

        :param id: The id of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rigid(self):
        """Gets the rigid of this GraphPlot.  # noqa: E501

        true | false Specifies if the graph is rigid or not  # noqa: E501

        :return: The rigid of this GraphPlot.  # noqa: E501
        :rtype: bool
        """
        return self._rigid

    @rigid.setter
    def rigid(self, rigid):
        """Sets the rigid of this GraphPlot.

        true | false Specifies if the graph is rigid or not  # noqa: E501

        :param rigid: The rigid of this GraphPlot.  # noqa: E501
        :type: bool
        """

        self._rigid = rigid

    @property
    def lines(self):
        """Gets the lines of this GraphPlot.  # noqa: E501

        The properties of the graph and graph lines  # noqa: E501

        :return: The lines of this GraphPlot.  # noqa: E501
        :rtype: list[GraphPlotLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this GraphPlot.

        The properties of the graph and graph lines  # noqa: E501

        :param lines: The lines of this GraphPlot.  # noqa: E501
        :type: list[GraphPlotLine]
        """

        self._lines = lines

    @property
    def height(self):
        """Gets the height of this GraphPlot.  # noqa: E501

        Specifies the height of graph  # noqa: E501

        :return: The height of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GraphPlot.

        Specifies the height of graph  # noqa: E501

        :param height: The height of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def end_tz_offset(self):
        """Gets the end_tz_offset of this GraphPlot.  # noqa: E501

        Specifies the end TimeZone Offset of the graph  # noqa: E501

        :return: The end_tz_offset of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._end_tz_offset

    @end_tz_offset.setter
    def end_tz_offset(self, end_tz_offset):
        """Sets the end_tz_offset of this GraphPlot.

        Specifies the end TimeZone Offset of the graph  # noqa: E501

        :param end_tz_offset: The end_tz_offset of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._end_tz_offset = end_tz_offset

    @property
    def base1024(self):
        """Gets the base1024 of this GraphPlot.  # noqa: E501

        true | false Changes base scale from 1000 to 1024 if value is set to true  # noqa: E501

        :return: The base1024 of this GraphPlot.  # noqa: E501
        :rtype: bool
        """
        return self._base1024

    @base1024.setter
    def base1024(self, base1024):
        """Sets the base1024 of this GraphPlot.

        true | false Changes base scale from 1000 to 1024 if value is set to true  # noqa: E501

        :param base1024: The base1024 of this GraphPlot.  # noqa: E501
        :type: bool
        """

        self._base1024 = base1024

    @property
    def ds_name(self):
        """Gets the ds_name of this GraphPlot.  # noqa: E501

        The name of the DataSource to be used to plot the graph  # noqa: E501

        :return: The ds_name of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._ds_name

    @ds_name.setter
    def ds_name(self, ds_name):
        """Sets the ds_name of this GraphPlot.

        The name of the DataSource to be used to plot the graph  # noqa: E501

        :param ds_name: The ds_name of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._ds_name = ds_name

    @property
    def max_value(self):
        """Gets the max_value of this GraphPlot.  # noqa: E501

        Specifies the maximum value of the graph  # noqa: E501

        :return: The max_value of this GraphPlot.  # noqa: E501
        :rtype: object
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this GraphPlot.

        Specifies the maximum value of the graph  # noqa: E501

        :param max_value: The max_value of this GraphPlot.  # noqa: E501
        :type: object
        """

        self._max_value = max_value

    @property
    def display_prio(self):
        """Gets the display_prio of this GraphPlot.  # noqa: E501

        The display priority of the graph in your LogicMonitor portal  # noqa: E501

        :return: The display_prio of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._display_prio

    @display_prio.setter
    def display_prio(self, display_prio):
        """Sets the display_prio of this GraphPlot.

        The display priority of the graph in your LogicMonitor portal  # noqa: E501

        :param display_prio: The display_prio of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._display_prio = display_prio

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this GraphPlot.  # noqa: E501

        The Id of selected Time Zone  # noqa: E501

        :return: The time_zone_id of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this GraphPlot.

        The Id of selected Time Zone  # noqa: E501

        :param time_zone_id: The time_zone_id of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._time_zone_id = time_zone_id

    @property
    def time_zone(self):
        """Gets the time_zone of this GraphPlot.  # noqa: E501

        The selected timezone for the graph  # noqa: E501

        :return: The time_zone of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this GraphPlot.

        The selected timezone for the graph  # noqa: E501

        :param time_zone: The time_zone of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def start_tz_offset(self):
        """Gets the start_tz_offset of this GraphPlot.  # noqa: E501

        Specifies the start TimeZone Offset of the graph  # noqa: E501

        :return: The start_tz_offset of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._start_tz_offset

    @start_tz_offset.setter
    def start_tz_offset(self, start_tz_offset):
        """Sets the start_tz_offset of this GraphPlot.

        Specifies the start TimeZone Offset of the graph  # noqa: E501

        :param start_tz_offset: The start_tz_offset of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._start_tz_offset = start_tz_offset

    @property
    def x_axis_name(self):
        """Gets the x_axis_name of this GraphPlot.  # noqa: E501

        The label that will be displayed along the X axis  # noqa: E501

        :return: The x_axis_name of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._x_axis_name

    @x_axis_name.setter
    def x_axis_name(self, x_axis_name):
        """Sets the x_axis_name of this GraphPlot.

        The label that will be displayed along the X axis  # noqa: E501

        :param x_axis_name: The x_axis_name of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._x_axis_name = x_axis_name

    @property
    def width(self):
        """Gets the width of this GraphPlot.  # noqa: E501

        Specifies the width of graph  # noqa: E501

        :return: The width of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this GraphPlot.

        Specifies the width of graph  # noqa: E501

        :param width: The width of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def name(self):
        """Gets the name of this GraphPlot.  # noqa: E501

        The Name of the Graph  # noqa: E501

        :return: The name of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GraphPlot.

        The Name of the Graph  # noqa: E501

        :param name: The name of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vertical_label(self):
        """Gets the vertical_label of this GraphPlot.  # noqa: E501

        The label that will be displayed along the y axis (Vertical Label)  # noqa: E501

        :return: The vertical_label of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, vertical_label):
        """Sets the vertical_label of this GraphPlot.

        The label that will be displayed along the y axis (Vertical Label)  # noqa: E501

        :param vertical_label: The vertical_label of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._vertical_label = vertical_label

    @property
    def step(self):
        """Gets the step of this GraphPlot.  # noqa: E501

        The Step of the graph  # noqa: E501

        :return: The step of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this GraphPlot.

        The Step of the graph  # noqa: E501

        :param step: The step of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._step = step

    @property
    def end_time(self):
        """Gets the end_time of this GraphPlot.  # noqa: E501

        Specifies the end-time of the graph  # noqa: E501

        :return: The end_time of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GraphPlot.

        Specifies the end-time of the graph  # noqa: E501

        :param end_time: The end_time of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def scopes(self):
        """Gets the scopes of this GraphPlot.  # noqa: E501

        Scopes: use this field to find match opsnote  # noqa: E501

        :return: The scopes of this GraphPlot.  # noqa: E501
        :rtype: list[GraphOpsNoteScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this GraphPlot.

        Scopes: use this field to find match opsnote  # noqa: E501

        :param scopes: The scopes of this GraphPlot.  # noqa: E501
        :type: list[GraphOpsNoteScope]
        """

        self._scopes = scopes

    @property
    def base(self):
        """Gets the base of this GraphPlot.  # noqa: E501

        The Base of the graph  # noqa: E501

        :return: The base of this GraphPlot.  # noqa: E501
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this GraphPlot.

        The Base of the graph  # noqa: E501

        :param base: The base of this GraphPlot.  # noqa: E501
        :type: int
        """

        self._base = base

    @property
    def export_file_name(self):
        """Gets the export_file_name of this GraphPlot.  # noqa: E501

        The export file name  # noqa: E501

        :return: The export_file_name of this GraphPlot.  # noqa: E501
        :rtype: str
        """
        return self._export_file_name

    @export_file_name.setter
    def export_file_name(self, export_file_name):
        """Sets the export_file_name of this GraphPlot.

        The export file name  # noqa: E501

        :param export_file_name: The export_file_name of this GraphPlot.  # noqa: E501
        :type: str
        """

        self._export_file_name = export_file_name

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
        if issubclass(GraphPlot, dict):
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
        if not isinstance(other, GraphPlot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
