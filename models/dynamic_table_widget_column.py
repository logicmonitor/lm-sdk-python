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

class DynamicTableWidgetColumn(object):
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
        'rpn': 'str',
        'data_point_name': 'str',
        'display_type': 'str',
        'min_value': 'float',
        'data_point_id': 'int',
        'unit_label': 'str',
        'max_value': 'float',
        'color_thresholds': 'list[ColorThreshold]',
        'column_name': 'str',
        'enable_forecast': 'bool',
        'rounding_decimal': 'int'
    }

    attribute_map = {
        'rpn': 'rpn',
        'data_point_name': 'dataPointName',
        'display_type': 'displayType',
        'min_value': 'minValue',
        'data_point_id': 'dataPointId',
        'unit_label': 'unitLabel',
        'max_value': 'maxValue',
        'color_thresholds': 'colorThresholds',
        'column_name': 'columnName',
        'enable_forecast': 'enableForecast',
        'rounding_decimal': 'roundingDecimal'
    }

    def __init__(self, rpn=None, data_point_name=None, display_type=None, min_value=None, data_point_id=None, unit_label=None, max_value=None, color_thresholds=None, column_name=None, enable_forecast=None, rounding_decimal=None):  # noqa: E501
        """DynamicTableWidgetColumn - a model defined in Swagger"""  # noqa: E501
        self._rpn = None
        self._data_point_name = None
        self._display_type = None
        self._min_value = None
        self._data_point_id = None
        self._unit_label = None
        self._max_value = None
        self._color_thresholds = None
        self._column_name = None
        self._enable_forecast = None
        self._rounding_decimal = None
        self.discriminator = None
        if rpn is not None:
            self.rpn = rpn
        if data_point_name is not None:
            self.data_point_name = data_point_name
        if display_type is not None:
            self.display_type = display_type
        if min_value is not None:
            self.min_value = min_value
        self.data_point_id = data_point_id
        if unit_label is not None:
            self.unit_label = unit_label
        if max_value is not None:
            self.max_value = max_value
        if color_thresholds is not None:
            self.color_thresholds = color_thresholds
        self.column_name = column_name
        if enable_forecast is not None:
            self.enable_forecast = enable_forecast
        if rounding_decimal is not None:
            self.rounding_decimal = rounding_decimal

    @property
    def rpn(self):
        """Gets the rpn of this DynamicTableWidgetColumn.  # noqa: E501

        The expression in this field will be performed on the datapoint. The Column name should be referenced as the datapoint  # noqa: E501

        :return: The rpn of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: str
        """
        return self._rpn

    @rpn.setter
    def rpn(self, rpn):
        """Sets the rpn of this DynamicTableWidgetColumn.

        The expression in this field will be performed on the datapoint. The Column name should be referenced as the datapoint  # noqa: E501

        :param rpn: The rpn of this DynamicTableWidgetColumn.  # noqa: E501
        :type: str
        """

        self._rpn = rpn

    @property
    def data_point_name(self):
        """Gets the data_point_name of this DynamicTableWidgetColumn.  # noqa: E501

        The name of the datapoint  # noqa: E501

        :return: The data_point_name of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this DynamicTableWidgetColumn.

        The name of the datapoint  # noqa: E501

        :param data_point_name: The data_point_name of this DynamicTableWidgetColumn.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def display_type(self):
        """Gets the display_type of this DynamicTableWidgetColumn.  # noqa: E501

        The display type, it includes three options: raw|percent|colorBar  # noqa: E501

        :return: The display_type of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this DynamicTableWidgetColumn.

        The display type, it includes three options: raw|percent|colorBar  # noqa: E501

        :param display_type: The display_type of this DynamicTableWidgetColumn.  # noqa: E501
        :type: str
        """

        self._display_type = display_type

    @property
    def min_value(self):
        """Gets the min_value of this DynamicTableWidgetColumn.  # noqa: E501

        The minimum value of the table widget  # noqa: E501

        :return: The min_value of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this DynamicTableWidgetColumn.

        The minimum value of the table widget  # noqa: E501

        :param min_value: The min_value of this DynamicTableWidgetColumn.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def data_point_id(self):
        """Gets the data_point_id of this DynamicTableWidgetColumn.  # noqa: E501

        The id of the datapoint  # noqa: E501

        :return: The data_point_id of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this DynamicTableWidgetColumn.

        The id of the datapoint  # noqa: E501

        :param data_point_id: The data_point_id of this DynamicTableWidgetColumn.  # noqa: E501
        :type: int
        """
        if data_point_id is None:
            raise ValueError("Invalid value for `data_point_id`, must not be `None`")  # noqa: E501

        self._data_point_id = data_point_id

    @property
    def unit_label(self):
        """Gets the unit_label of this DynamicTableWidgetColumn.  # noqa: E501

        The unit label  # noqa: E501

        :return: The unit_label of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: str
        """
        return self._unit_label

    @unit_label.setter
    def unit_label(self, unit_label):
        """Sets the unit_label of this DynamicTableWidgetColumn.

        The unit label  # noqa: E501

        :param unit_label: The unit_label of this DynamicTableWidgetColumn.  # noqa: E501
        :type: str
        """

        self._unit_label = unit_label

    @property
    def max_value(self):
        """Gets the max_value of this DynamicTableWidgetColumn.  # noqa: E501

        The maximum value of the table widget  # noqa: E501

        :return: The max_value of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this DynamicTableWidgetColumn.

        The maximum value of the table widget  # noqa: E501

        :param max_value: The max_value of this DynamicTableWidgetColumn.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def color_thresholds(self):
        """Gets the color_thresholds of this DynamicTableWidgetColumn.  # noqa: E501

        The threshold of color changes  # noqa: E501

        :return: The color_thresholds of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: list[ColorThreshold]
        """
        return self._color_thresholds

    @color_thresholds.setter
    def color_thresholds(self, color_thresholds):
        """Sets the color_thresholds of this DynamicTableWidgetColumn.

        The threshold of color changes  # noqa: E501

        :param color_thresholds: The color_thresholds of this DynamicTableWidgetColumn.  # noqa: E501
        :type: list[ColorThreshold]
        """

        self._color_thresholds = color_thresholds

    @property
    def column_name(self):
        """Gets the column_name of this DynamicTableWidgetColumn.  # noqa: E501

        The name for the column  # noqa: E501

        :return: The column_name of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this DynamicTableWidgetColumn.

        The name for the column  # noqa: E501

        :param column_name: The column_name of this DynamicTableWidgetColumn.  # noqa: E501
        :type: str
        """
        if column_name is None:
            raise ValueError("Invalid value for `column_name`, must not be `None`")  # noqa: E501

        self._column_name = column_name

    @property
    def enable_forecast(self):
        """Gets the enable_forecast of this DynamicTableWidgetColumn.  # noqa: E501

        Whether or not forecasting is enabled  # noqa: E501

        :return: The enable_forecast of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: bool
        """
        return self._enable_forecast

    @enable_forecast.setter
    def enable_forecast(self, enable_forecast):
        """Sets the enable_forecast of this DynamicTableWidgetColumn.

        Whether or not forecasting is enabled  # noqa: E501

        :param enable_forecast: The enable_forecast of this DynamicTableWidgetColumn.  # noqa: E501
        :type: bool
        """

        self._enable_forecast = enable_forecast

    @property
    def rounding_decimal(self):
        """Gets the rounding_decimal of this DynamicTableWidgetColumn.  # noqa: E501

        The number of decimal points to round the value to. Options are 0, 1 and 2  # noqa: E501

        :return: The rounding_decimal of this DynamicTableWidgetColumn.  # noqa: E501
        :rtype: int
        """
        return self._rounding_decimal

    @rounding_decimal.setter
    def rounding_decimal(self, rounding_decimal):
        """Sets the rounding_decimal of this DynamicTableWidgetColumn.

        The number of decimal points to round the value to. Options are 0, 1 and 2  # noqa: E501

        :param rounding_decimal: The rounding_decimal of this DynamicTableWidgetColumn.  # noqa: E501
        :type: int
        """

        self._rounding_decimal = rounding_decimal

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
        if issubclass(DynamicTableWidgetColumn, dict):
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
        if not isinstance(other, DynamicTableWidgetColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
