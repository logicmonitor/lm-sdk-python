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

from logicmonitor_sdk.models.glob_match_toggle import GlobMatchToggle  # noqa: F401,E501
from logicmonitor_sdk.models.graph_display import GraphDisplay  # noqa: F401,E501


class CustomFlexibleVirtualDataSourceEx(object):
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
        'custom_graph_id': 'int',
        'instance_name': 'GlobMatchToggle',
        'display': 'GraphDisplay',
        'aggregate_function': 'str',
        'device_display_name': 'GlobMatchToggle',
        'data_point_name': 'str',
        'data_source_id': 'int',
        'data_point_id': 'int',
        'data_source_full_name': 'str',
        'consolidate_function': 'str',
        'name': 'str',
        'id': 'int',
        'device_group_full_path': 'GlobMatchToggle'
    }

    attribute_map = {
        'custom_graph_id': 'customGraphId',
        'instance_name': 'instanceName',
        'display': 'display',
        'aggregate_function': 'aggregateFunction',
        'device_display_name': 'deviceDisplayName',
        'data_point_name': 'dataPointName',
        'data_source_id': 'dataSourceId',
        'data_point_id': 'dataPointId',
        'data_source_full_name': 'dataSourceFullName',
        'consolidate_function': 'consolidateFunction',
        'name': 'name',
        'id': 'id',
        'device_group_full_path': 'deviceGroupFullPath'
    }

    def __init__(self, custom_graph_id=None, instance_name=None, display=None, aggregate_function=None, device_display_name=None, data_point_name=None, data_source_id=None, data_point_id=None, data_source_full_name=None, consolidate_function=None, name=None, id=None, device_group_full_path=None):  # noqa: E501
        """CustomFlexibleVirtualDataSourceEx - a model defined in Swagger"""  # noqa: E501

        self._custom_graph_id = None
        self._instance_name = None
        self._display = None
        self._aggregate_function = None
        self._device_display_name = None
        self._data_point_name = None
        self._data_source_id = None
        self._data_point_id = None
        self._data_source_full_name = None
        self._consolidate_function = None
        self._name = None
        self._id = None
        self._device_group_full_path = None
        self.discriminator = None

        if custom_graph_id is not None:
            self.custom_graph_id = custom_graph_id
        self.instance_name = instance_name
        self.display = display
        if aggregate_function is not None:
            self.aggregate_function = aggregate_function
        self.device_display_name = device_display_name
        if data_point_name is not None:
            self.data_point_name = data_point_name
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if data_point_id is not None:
            self.data_point_id = data_point_id
        if data_source_full_name is not None:
            self.data_source_full_name = data_source_full_name
        if consolidate_function is not None:
            self.consolidate_function = consolidate_function
        self.name = name
        if id is not None:
            self.id = id
        self.device_group_full_path = device_group_full_path

    @property
    def custom_graph_id(self):
        """Gets the custom_graph_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The custom_graph_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: int
        """
        return self._custom_graph_id

    @custom_graph_id.setter
    def custom_graph_id(self, custom_graph_id):
        """Sets the custom_graph_id of this CustomFlexibleVirtualDataSourceEx.


        :param custom_graph_id: The custom_graph_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: int
        """

        self._custom_graph_id = custom_graph_id

    @property
    def instance_name(self):
        """Gets the instance_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The instance_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: GlobMatchToggle
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this CustomFlexibleVirtualDataSourceEx.


        :param instance_name: The instance_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: GlobMatchToggle
        """
        if instance_name is None:
            raise ValueError("Invalid value for `instance_name`, must not be `None`")  # noqa: E501

        self._instance_name = instance_name

    @property
    def display(self):
        """Gets the display of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The display of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: GraphDisplay
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this CustomFlexibleVirtualDataSourceEx.


        :param display: The display of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: GraphDisplay
        """
        if display is None:
            raise ValueError("Invalid value for `display`, must not be `None`")  # noqa: E501

        self._display = display

    @property
    def aggregate_function(self):
        """Gets the aggregate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The aggregate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_function

    @aggregate_function.setter
    def aggregate_function(self, aggregate_function):
        """Sets the aggregate_function of this CustomFlexibleVirtualDataSourceEx.


        :param aggregate_function: The aggregate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: str
        """

        self._aggregate_function = aggregate_function

    @property
    def device_display_name(self):
        """Gets the device_display_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The device_display_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: GlobMatchToggle
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this CustomFlexibleVirtualDataSourceEx.


        :param device_display_name: The device_display_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: GlobMatchToggle
        """
        if device_display_name is None:
            raise ValueError("Invalid value for `device_display_name`, must not be `None`")  # noqa: E501

        self._device_display_name = device_display_name

    @property
    def data_point_name(self):
        """Gets the data_point_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The data_point_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this CustomFlexibleVirtualDataSourceEx.


        :param data_point_name: The data_point_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def data_source_id(self):
        """Gets the data_source_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The data_source_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this CustomFlexibleVirtualDataSourceEx.


        :param data_source_id: The data_source_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: int
        """

        self._data_source_id = data_source_id

    @property
    def data_point_id(self):
        """Gets the data_point_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The data_point_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this CustomFlexibleVirtualDataSourceEx.


        :param data_point_id: The data_point_id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def data_source_full_name(self):
        """Gets the data_source_full_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The data_source_full_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: str
        """
        return self._data_source_full_name

    @data_source_full_name.setter
    def data_source_full_name(self, data_source_full_name):
        """Sets the data_source_full_name of this CustomFlexibleVirtualDataSourceEx.


        :param data_source_full_name: The data_source_full_name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: str
        """

        self._data_source_full_name = data_source_full_name

    @property
    def consolidate_function(self):
        """Gets the consolidate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The consolidate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: str
        """
        return self._consolidate_function

    @consolidate_function.setter
    def consolidate_function(self, consolidate_function):
        """Sets the consolidate_function of this CustomFlexibleVirtualDataSourceEx.


        :param consolidate_function: The consolidate_function of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: str
        """

        self._consolidate_function = consolidate_function

    @property
    def name(self):
        """Gets the name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomFlexibleVirtualDataSourceEx.


        :param name: The name of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomFlexibleVirtualDataSourceEx.


        :param id: The id of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device_group_full_path(self):
        """Gets the device_group_full_path of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501


        :return: The device_group_full_path of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :rtype: GlobMatchToggle
        """
        return self._device_group_full_path

    @device_group_full_path.setter
    def device_group_full_path(self, device_group_full_path):
        """Sets the device_group_full_path of this CustomFlexibleVirtualDataSourceEx.


        :param device_group_full_path: The device_group_full_path of this CustomFlexibleVirtualDataSourceEx.  # noqa: E501
        :type: GlobMatchToggle
        """
        if device_group_full_path is None:
            raise ValueError("Invalid value for `device_group_full_path`, must not be `None`")  # noqa: E501

        self._device_group_full_path = device_group_full_path

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
        if issubclass(CustomFlexibleVirtualDataSourceEx, dict):
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
        if not isinstance(other, CustomFlexibleVirtualDataSourceEx):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
