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


class OpsNoteTagBase(object):
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
        'update_on_in_sec': 'int',
        'created_on_in_sec': 'int',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'update_on_in_sec': 'updateOnInSec',
        'created_on_in_sec': 'createdOnInSec',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, update_on_in_sec=None, created_on_in_sec=None, name=None, id=None):  # noqa: E501
        """OpsNoteTagBase - a model defined in Swagger"""  # noqa: E501

        self._update_on_in_sec = None
        self._created_on_in_sec = None
        self._name = None
        self._id = None
        self.discriminator = None

        if update_on_in_sec is not None:
            self.update_on_in_sec = update_on_in_sec
        if created_on_in_sec is not None:
            self.created_on_in_sec = created_on_in_sec
        self.name = name
        if id is not None:
            self.id = id

    @property
    def update_on_in_sec(self):
        """Gets the update_on_in_sec of this OpsNoteTagBase.  # noqa: E501


        :return: The update_on_in_sec of this OpsNoteTagBase.  # noqa: E501
        :rtype: int
        """
        return self._update_on_in_sec

    @update_on_in_sec.setter
    def update_on_in_sec(self, update_on_in_sec):
        """Sets the update_on_in_sec of this OpsNoteTagBase.


        :param update_on_in_sec: The update_on_in_sec of this OpsNoteTagBase.  # noqa: E501
        :type: int
        """

        self._update_on_in_sec = update_on_in_sec

    @property
    def created_on_in_sec(self):
        """Gets the created_on_in_sec of this OpsNoteTagBase.  # noqa: E501


        :return: The created_on_in_sec of this OpsNoteTagBase.  # noqa: E501
        :rtype: int
        """
        return self._created_on_in_sec

    @created_on_in_sec.setter
    def created_on_in_sec(self, created_on_in_sec):
        """Sets the created_on_in_sec of this OpsNoteTagBase.


        :param created_on_in_sec: The created_on_in_sec of this OpsNoteTagBase.  # noqa: E501
        :type: int
        """

        self._created_on_in_sec = created_on_in_sec

    @property
    def name(self):
        """Gets the name of this OpsNoteTagBase.  # noqa: E501

        release  # noqa: E501

        :return: The name of this OpsNoteTagBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpsNoteTagBase.

        release  # noqa: E501

        :param name: The name of this OpsNoteTagBase.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this OpsNoteTagBase.  # noqa: E501


        :return: The id of this OpsNoteTagBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpsNoteTagBase.


        :param id: The id of this OpsNoteTagBase.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(OpsNoteTagBase, dict):
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
        if not isinstance(other, OpsNoteTagBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
