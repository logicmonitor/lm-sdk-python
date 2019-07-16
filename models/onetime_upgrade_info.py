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


class OnetimeUpgradeInfo(object):
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
        'created_by': 'str',
        'description': 'str',
        'end_epoch': 'int',
        'level': 'str',
        'major_version': 'int',
        'minor_version': 'int',
        'start_epoch': 'int',
        'timezone': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'description': 'description',
        'end_epoch': 'endEpoch',
        'level': 'level',
        'major_version': 'majorVersion',
        'minor_version': 'minorVersion',
        'start_epoch': 'startEpoch',
        'timezone': 'timezone',
        'type': 'type'
    }

    def __init__(self, created_by=None, description=None, end_epoch=None, level=None, major_version=None, minor_version=None, start_epoch=None, timezone=None, type=None):  # noqa: E501
        """OnetimeUpgradeInfo - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._description = None
        self._end_epoch = None
        self._level = None
        self._major_version = None
        self._minor_version = None
        self._start_epoch = None
        self._timezone = None
        self._type = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if end_epoch is not None:
            self.end_epoch = end_epoch
        if level is not None:
            self.level = level
        self.major_version = major_version
        self.minor_version = minor_version
        self.start_epoch = start_epoch
        if timezone is not None:
            self.timezone = timezone
        if type is not None:
            self.type = type

    @property
    def created_by(self):
        """Gets the created_by of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The created_by of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OnetimeUpgradeInfo.


        :param created_by: The created_by of this OnetimeUpgradeInfo.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The description of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OnetimeUpgradeInfo.


        :param description: The description of this OnetimeUpgradeInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_epoch(self):
        """Gets the end_epoch of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The end_epoch of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_epoch

    @end_epoch.setter
    def end_epoch(self, end_epoch):
        """Sets the end_epoch of this OnetimeUpgradeInfo.


        :param end_epoch: The end_epoch of this OnetimeUpgradeInfo.  # noqa: E501
        :type: int
        """

        self._end_epoch = end_epoch

    @property
    def level(self):
        """Gets the level of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The level of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this OnetimeUpgradeInfo.


        :param level: The level of this OnetimeUpgradeInfo.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def major_version(self):
        """Gets the major_version of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The major_version of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this OnetimeUpgradeInfo.


        :param major_version: The major_version of this OnetimeUpgradeInfo.  # noqa: E501
        :type: int
        """
        if major_version is None:
            raise ValueError("Invalid value for `major_version`, must not be `None`")  # noqa: E501

        self._major_version = major_version

    @property
    def minor_version(self):
        """Gets the minor_version of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The minor_version of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """Sets the minor_version of this OnetimeUpgradeInfo.


        :param minor_version: The minor_version of this OnetimeUpgradeInfo.  # noqa: E501
        :type: int
        """
        if minor_version is None:
            raise ValueError("Invalid value for `minor_version`, must not be `None`")  # noqa: E501

        self._minor_version = minor_version

    @property
    def start_epoch(self):
        """Gets the start_epoch of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The start_epoch of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_epoch

    @start_epoch.setter
    def start_epoch(self, start_epoch):
        """Sets the start_epoch of this OnetimeUpgradeInfo.


        :param start_epoch: The start_epoch of this OnetimeUpgradeInfo.  # noqa: E501
        :type: int
        """
        if start_epoch is None:
            raise ValueError("Invalid value for `start_epoch`, must not be `None`")  # noqa: E501

        self._start_epoch = start_epoch

    @property
    def timezone(self):
        """Gets the timezone of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The timezone of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this OnetimeUpgradeInfo.


        :param timezone: The timezone of this OnetimeUpgradeInfo.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this OnetimeUpgradeInfo.  # noqa: E501


        :return: The type of this OnetimeUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OnetimeUpgradeInfo.


        :param type: The type of this OnetimeUpgradeInfo.  # noqa: E501
        :type: str
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
        if issubclass(OnetimeUpgradeInfo, dict):
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
        if not isinstance(other, OnetimeUpgradeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
