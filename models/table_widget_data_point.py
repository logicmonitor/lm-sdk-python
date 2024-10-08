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

class TableWidgetDataPoint(object):
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
        'data_source_id': 'int',
        'data_point_name': 'str',
        'data_point_id': 'int',
        'data_source_full_name': 'str',
        'is_multiple': 'bool'
    }

    attribute_map = {
        'data_source_id': 'dataSourceId',
        'data_point_name': 'dataPointName',
        'data_point_id': 'dataPointId',
        'data_source_full_name': 'dataSourceFullName',
        'is_multiple': 'isMultiple'
    }

    def __init__(self, data_source_id=None, data_point_name=None, data_point_id=None, data_source_full_name=None, is_multiple=None):  # noqa: E501
        """TableWidgetDataPoint - a model defined in Swagger"""  # noqa: E501
        self._data_source_id = None
        self._data_point_name = None
        self._data_point_id = None
        self._data_source_full_name = None
        self._is_multiple = None
        self.discriminator = None
        self.data_source_id = data_source_id
        if data_point_name is not None:
            self.data_point_name = data_point_name
        self.data_point_id = data_point_id
        if data_source_full_name is not None:
            self.data_source_full_name = data_source_full_name
        if is_multiple is not None:
            self.is_multiple = is_multiple

    @property
    def data_source_id(self):
        """Gets the data_source_id of this TableWidgetDataPoint.  # noqa: E501


        :return: The data_source_id of this TableWidgetDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this TableWidgetDataPoint.


        :param data_source_id: The data_source_id of this TableWidgetDataPoint.  # noqa: E501
        :type: int
        """
        if data_source_id is None:
            raise ValueError("Invalid value for `data_source_id`, must not be `None`")  # noqa: E501

        self._data_source_id = data_source_id

    @property
    def data_point_name(self):
        """Gets the data_point_name of this TableWidgetDataPoint.  # noqa: E501


        :return: The data_point_name of this TableWidgetDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this TableWidgetDataPoint.


        :param data_point_name: The data_point_name of this TableWidgetDataPoint.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def data_point_id(self):
        """Gets the data_point_id of this TableWidgetDataPoint.  # noqa: E501


        :return: The data_point_id of this TableWidgetDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this TableWidgetDataPoint.


        :param data_point_id: The data_point_id of this TableWidgetDataPoint.  # noqa: E501
        :type: int
        """
        if data_point_id is None:
            raise ValueError("Invalid value for `data_point_id`, must not be `None`")  # noqa: E501

        self._data_point_id = data_point_id

    @property
    def data_source_full_name(self):
        """Gets the data_source_full_name of this TableWidgetDataPoint.  # noqa: E501


        :return: The data_source_full_name of this TableWidgetDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._data_source_full_name

    @data_source_full_name.setter
    def data_source_full_name(self, data_source_full_name):
        """Sets the data_source_full_name of this TableWidgetDataPoint.


        :param data_source_full_name: The data_source_full_name of this TableWidgetDataPoint.  # noqa: E501
        :type: str
        """

        self._data_source_full_name = data_source_full_name

    @property
    def is_multiple(self):
        """Gets the is_multiple of this TableWidgetDataPoint.  # noqa: E501


        :return: The is_multiple of this TableWidgetDataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._is_multiple

    @is_multiple.setter
    def is_multiple(self, is_multiple):
        """Sets the is_multiple of this TableWidgetDataPoint.


        :param is_multiple: The is_multiple of this TableWidgetDataPoint.  # noqa: E501
        :type: bool
        """

        self._is_multiple = is_multiple

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
        if issubclass(TableWidgetDataPoint, dict):
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
        if not isinstance(other, TableWidgetDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
