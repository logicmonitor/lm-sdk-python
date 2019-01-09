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


class Privilege(object):
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
        'object_name': 'str',
        'sub_operation': 'str',
        'operation': 'str',
        'object_id': 'str',
        'object_type': 'str'
    }

    attribute_map = {
        'object_name': 'objectName',
        'sub_operation': 'subOperation',
        'operation': 'operation',
        'object_id': 'objectId',
        'object_type': 'objectType'
    }

    def __init__(self, object_name=None, sub_operation=None, operation=None, object_id=None, object_type=None):  # noqa: E501
        """Privilege - a model defined in Swagger"""  # noqa: E501

        self._object_name = None
        self._sub_operation = None
        self._operation = None
        self._object_id = None
        self._object_type = None
        self.discriminator = None

        if object_name is not None:
            self.object_name = object_name
        if sub_operation is not None:
            self.sub_operation = sub_operation
        self.operation = operation
        self.object_id = object_id
        self.object_type = object_type

    @property
    def object_name(self):
        """Gets the object_name of this Privilege.  # noqa: E501


        :return: The object_name of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this Privilege.


        :param object_name: The object_name of this Privilege.  # noqa: E501
        :type: str
        """

        self._object_name = object_name

    @property
    def sub_operation(self):
        """Gets the sub_operation of this Privilege.  # noqa: E501


        :return: The sub_operation of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._sub_operation

    @sub_operation.setter
    def sub_operation(self, sub_operation):
        """Sets the sub_operation of this Privilege.


        :param sub_operation: The sub_operation of this Privilege.  # noqa: E501
        :type: str
        """

        self._sub_operation = sub_operation

    @property
    def operation(self):
        """Gets the operation of this Privilege.  # noqa: E501


        :return: The operation of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this Privilege.


        :param operation: The operation of this Privilege.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def object_id(self):
        """Gets the object_id of this Privilege.  # noqa: E501


        :return: The object_id of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this Privilege.


        :param object_id: The object_id of this Privilege.  # noqa: E501
        :type: str
        """
        if object_id is None:
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this Privilege.  # noqa: E501


        :return: The object_type of this Privilege.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this Privilege.


        :param object_type: The object_type of this Privilege.  # noqa: E501
        :type: str
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501

        self._object_type = object_type

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
        if issubclass(Privilege, dict):
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
        if not isinstance(other, Privilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
