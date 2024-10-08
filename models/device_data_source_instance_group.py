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

class DeviceDataSourceInstanceGroup(object):
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
        'device_data_source_id': 'int',
        'name': 'str',
        'description': 'str',
        'create_on': 'int',
        'id': 'int',
        'device_id': 'int',
        'device_display_name': 'str'
    }

    attribute_map = {
        'device_data_source_id': 'deviceDataSourceId',
        'name': 'name',
        'description': 'description',
        'create_on': 'createOn',
        'id': 'id',
        'device_id': 'deviceId',
        'device_display_name': 'deviceDisplayName'
    }

    def __init__(self, device_data_source_id=None, name=None, description=None, create_on=None, id=None, device_id=None, device_display_name=None):  # noqa: E501
        """DeviceDataSourceInstanceGroup - a model defined in Swagger"""  # noqa: E501
        self._device_data_source_id = None
        self._name = None
        self._description = None
        self._create_on = None
        self._id = None
        self._device_id = None
        self._device_display_name = None
        self.discriminator = None
        if device_data_source_id is not None:
            self.device_data_source_id = device_data_source_id
        self.name = name
        if description is not None:
            self.description = description
        if create_on is not None:
            self.create_on = create_on
        if id is not None:
            self.id = id
        if device_id is not None:
            self.device_id = device_id
        if device_display_name is not None:
            self.device_display_name = device_display_name

    @property
    def device_data_source_id(self):
        """Gets the device_data_source_id of this DeviceDataSourceInstanceGroup.  # noqa: E501

        The device datasource id  # noqa: E501

        :return: The device_data_source_id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: int
        """
        return self._device_data_source_id

    @device_data_source_id.setter
    def device_data_source_id(self, device_data_source_id):
        """Sets the device_data_source_id of this DeviceDataSourceInstanceGroup.

        The device datasource id  # noqa: E501

        :param device_data_source_id: The device_data_source_id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: int
        """

        self._device_data_source_id = device_data_source_id

    @property
    def name(self):
        """Gets the name of this DeviceDataSourceInstanceGroup.  # noqa: E501

        Name of the datasource instance group  # noqa: E501

        :return: The name of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceDataSourceInstanceGroup.

        Name of the datasource instance group  # noqa: E501

        :param name: The name of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DeviceDataSourceInstanceGroup.  # noqa: E501

        The description of the datasource instance group  # noqa: E501

        :return: The description of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceDataSourceInstanceGroup.

        The description of the datasource instance group  # noqa: E501

        :param description: The description of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def create_on(self):
        """Gets the create_on of this DeviceDataSourceInstanceGroup.  # noqa: E501

        Time when the group was created.  # noqa: E501

        :return: The create_on of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: int
        """
        return self._create_on

    @create_on.setter
    def create_on(self, create_on):
        """Sets the create_on of this DeviceDataSourceInstanceGroup.

        Time when the group was created.  # noqa: E501

        :param create_on: The create_on of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: int
        """

        self._create_on = create_on

    @property
    def id(self):
        """Gets the id of this DeviceDataSourceInstanceGroup.  # noqa: E501

        The instance group id  # noqa: E501

        :return: The id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceDataSourceInstanceGroup.

        The instance group id  # noqa: E501

        :param id: The id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device_id(self):
        """Gets the device_id of this DeviceDataSourceInstanceGroup.  # noqa: E501

        The id of associated device  # noqa: E501

        :return: The device_id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceDataSourceInstanceGroup.

        The id of associated device  # noqa: E501

        :param device_id: The device_id of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_display_name(self):
        """Gets the device_display_name of this DeviceDataSourceInstanceGroup.  # noqa: E501

        The display name of the device  # noqa: E501

        :return: The device_display_name of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this DeviceDataSourceInstanceGroup.

        The display name of the device  # noqa: E501

        :param device_display_name: The device_display_name of this DeviceDataSourceInstanceGroup.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

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
        if issubclass(DeviceDataSourceInstanceGroup, dict):
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
        if not isinstance(other, DeviceDataSourceInstanceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
