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

class GraphLine(object):
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
        'color_name': 'str',
        'data_point_name': 'str',
        'data_point_id': 'int',
        'legend': 'str',
        'is_virtual_data_point': 'bool',
        'type': 'int'
    }

    attribute_map = {
        'color_name': 'colorName',
        'data_point_name': 'dataPointName',
        'data_point_id': 'dataPointId',
        'legend': 'legend',
        'is_virtual_data_point': 'isVirtualDataPoint',
        'type': 'type'
    }

    def __init__(self, color_name=None, data_point_name=None, data_point_id=None, legend=None, is_virtual_data_point=None, type=None):  # noqa: E501
        """GraphLine - a model defined in Swagger"""  # noqa: E501
        self._color_name = None
        self._data_point_name = None
        self._data_point_id = None
        self._legend = None
        self._is_virtual_data_point = None
        self._type = None
        self.discriminator = None
        if color_name is not None:
            self.color_name = color_name
        if data_point_name is not None:
            self.data_point_name = data_point_name
        if data_point_id is not None:
            self.data_point_id = data_point_id
        if legend is not None:
            self.legend = legend
        if is_virtual_data_point is not None:
            self.is_virtual_data_point = is_virtual_data_point
        if type is not None:
            self.type = type

    @property
    def color_name(self):
        """Gets the color_name of this GraphLine.  # noqa: E501

        The graph line color name  # noqa: E501

        :return: The color_name of this GraphLine.  # noqa: E501
        :rtype: str
        """
        return self._color_name

    @color_name.setter
    def color_name(self, color_name):
        """Sets the color_name of this GraphLine.

        The graph line color name  # noqa: E501

        :param color_name: The color_name of this GraphLine.  # noqa: E501
        :type: str
        """

        self._color_name = color_name

    @property
    def data_point_name(self):
        """Gets the data_point_name of this GraphLine.  # noqa: E501

        The graph line data point name  # noqa: E501

        :return: The data_point_name of this GraphLine.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this GraphLine.

        The graph line data point name  # noqa: E501

        :param data_point_name: The data_point_name of this GraphLine.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def data_point_id(self):
        """Gets the data_point_id of this GraphLine.  # noqa: E501

        The graph line data point id  # noqa: E501

        :return: The data_point_id of this GraphLine.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this GraphLine.

        The graph line data point id  # noqa: E501

        :param data_point_id: The data_point_id of this GraphLine.  # noqa: E501
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def legend(self):
        """Gets the legend of this GraphLine.  # noqa: E501

        The graph line legend  # noqa: E501

        :return: The legend of this GraphLine.  # noqa: E501
        :rtype: str
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this GraphLine.

        The graph line legend  # noqa: E501

        :param legend: The legend of this GraphLine.  # noqa: E501
        :type: str
        """

        self._legend = legend

    @property
    def is_virtual_data_point(self):
        """Gets the is_virtual_data_point of this GraphLine.  # noqa: E501

        Whether the graph line's data point is a virtual data point  # noqa: E501

        :return: The is_virtual_data_point of this GraphLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_virtual_data_point

    @is_virtual_data_point.setter
    def is_virtual_data_point(self, is_virtual_data_point):
        """Sets the is_virtual_data_point of this GraphLine.

        Whether the graph line's data point is a virtual data point  # noqa: E501

        :param is_virtual_data_point: The is_virtual_data_point of this GraphLine.  # noqa: E501
        :type: bool
        """

        self._is_virtual_data_point = is_virtual_data_point

    @property
    def type(self):
        """Gets the type of this GraphLine.  # noqa: E501

        The graph line type.  The values can be 1|2|3|4  where,       1=line, 2=area, 3=stack, 4=column  # noqa: E501

        :return: The type of this GraphLine.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GraphLine.

        The graph line type.  The values can be 1|2|3|4  where,       1=line, 2=area, 3=stack, 4=column  # noqa: E501

        :param type: The type of this GraphLine.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if issubclass(GraphLine, dict):
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
        if not isinstance(other, GraphLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
