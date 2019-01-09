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


class TableWidgetInstanceCell(object):
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
        'validation_status_code': 'int',
        'data_point_name': 'str',
        'instance_id': 'int',
        'data_point_id': 'int',
        'instance_name': 'str'
    }

    attribute_map = {
        'validation_status_code': 'validationStatusCode',
        'data_point_name': 'dataPointName',
        'instance_id': 'instanceId',
        'data_point_id': 'dataPointId',
        'instance_name': 'instanceName'
    }

    def __init__(self, validation_status_code=None, data_point_name=None, instance_id=None, data_point_id=None, instance_name=None):  # noqa: E501
        """TableWidgetInstanceCell - a model defined in Swagger"""  # noqa: E501

        self._validation_status_code = None
        self._data_point_name = None
        self._instance_id = None
        self._data_point_id = None
        self._instance_name = None
        self.discriminator = None

        if validation_status_code is not None:
            self.validation_status_code = validation_status_code
        if data_point_name is not None:
            self.data_point_name = data_point_name
        self.instance_id = instance_id
        if data_point_id is not None:
            self.data_point_id = data_point_id
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def validation_status_code(self):
        """Gets the validation_status_code of this TableWidgetInstanceCell.  # noqa: E501


        :return: The validation_status_code of this TableWidgetInstanceCell.  # noqa: E501
        :rtype: int
        """
        return self._validation_status_code

    @validation_status_code.setter
    def validation_status_code(self, validation_status_code):
        """Sets the validation_status_code of this TableWidgetInstanceCell.


        :param validation_status_code: The validation_status_code of this TableWidgetInstanceCell.  # noqa: E501
        :type: int
        """

        self._validation_status_code = validation_status_code

    @property
    def data_point_name(self):
        """Gets the data_point_name of this TableWidgetInstanceCell.  # noqa: E501


        :return: The data_point_name of this TableWidgetInstanceCell.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this TableWidgetInstanceCell.


        :param data_point_name: The data_point_name of this TableWidgetInstanceCell.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def instance_id(self):
        """Gets the instance_id of this TableWidgetInstanceCell.  # noqa: E501


        :return: The instance_id of this TableWidgetInstanceCell.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this TableWidgetInstanceCell.


        :param instance_id: The instance_id of this TableWidgetInstanceCell.  # noqa: E501
        :type: int
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def data_point_id(self):
        """Gets the data_point_id of this TableWidgetInstanceCell.  # noqa: E501


        :return: The data_point_id of this TableWidgetInstanceCell.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this TableWidgetInstanceCell.


        :param data_point_id: The data_point_id of this TableWidgetInstanceCell.  # noqa: E501
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def instance_name(self):
        """Gets the instance_name of this TableWidgetInstanceCell.  # noqa: E501


        :return: The instance_name of this TableWidgetInstanceCell.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this TableWidgetInstanceCell.


        :param instance_name: The instance_name of this TableWidgetInstanceCell.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

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
        if issubclass(TableWidgetInstanceCell, dict):
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
        if not isinstance(other, TableWidgetInstanceCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
