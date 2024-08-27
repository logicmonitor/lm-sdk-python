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

class MapItemInfo(object):
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
        'alert_status': 'str',
        'display_name': 'str',
        'formatted_location': 'str',
        'latitude': 'str',
        'description': 'str',
        'type': 'str',
        'sdt_status': 'str',
        'active_status': 'str',
        'name': 'str',
        'sub_type': 'str',
        'location': 'str',
        'id': 'int',
        'longitude': 'str'
    }

    attribute_map = {
        'alert_status': 'alertStatus',
        'display_name': 'displayName',
        'formatted_location': 'formattedLocation',
        'latitude': 'latitude',
        'description': 'description',
        'type': 'type',
        'sdt_status': 'sdtStatus',
        'active_status': 'activeStatus',
        'name': 'name',
        'sub_type': 'subType',
        'location': 'location',
        'id': 'id',
        'longitude': 'longitude'
    }

    def __init__(self, alert_status=None, display_name=None, formatted_location=None, latitude=None, description=None, type=None, sdt_status=None, active_status=None, name=None, sub_type=None, location=None, id=None, longitude=None):  # noqa: E501
        """MapItemInfo - a model defined in Swagger"""  # noqa: E501
        self._alert_status = None
        self._display_name = None
        self._formatted_location = None
        self._latitude = None
        self._description = None
        self._type = None
        self._sdt_status = None
        self._active_status = None
        self._name = None
        self._sub_type = None
        self._location = None
        self._id = None
        self._longitude = None
        self.discriminator = None
        if alert_status is not None:
            self.alert_status = alert_status
        if display_name is not None:
            self.display_name = display_name
        if formatted_location is not None:
            self.formatted_location = formatted_location
        if latitude is not None:
            self.latitude = latitude
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if sdt_status is not None:
            self.sdt_status = sdt_status
        if active_status is not None:
            self.active_status = active_status
        if name is not None:
            self.name = name
        if sub_type is not None:
            self.sub_type = sub_type
        if location is not None:
            self.location = location
        if id is not None:
            self.id = id
        if longitude is not None:
            self.longitude = longitude

    @property
    def alert_status(self):
        """Gets the alert_status of this MapItemInfo.  # noqa: E501


        :return: The alert_status of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._alert_status

    @alert_status.setter
    def alert_status(self, alert_status):
        """Sets the alert_status of this MapItemInfo.


        :param alert_status: The alert_status of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._alert_status = alert_status

    @property
    def display_name(self):
        """Gets the display_name of this MapItemInfo.  # noqa: E501


        :return: The display_name of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MapItemInfo.


        :param display_name: The display_name of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def formatted_location(self):
        """Gets the formatted_location of this MapItemInfo.  # noqa: E501


        :return: The formatted_location of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._formatted_location

    @formatted_location.setter
    def formatted_location(self, formatted_location):
        """Sets the formatted_location of this MapItemInfo.


        :param formatted_location: The formatted_location of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._formatted_location = formatted_location

    @property
    def latitude(self):
        """Gets the latitude of this MapItemInfo.  # noqa: E501


        :return: The latitude of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this MapItemInfo.


        :param latitude: The latitude of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def description(self):
        """Gets the description of this MapItemInfo.  # noqa: E501


        :return: The description of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MapItemInfo.


        :param description: The description of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this MapItemInfo.  # noqa: E501


        :return: The type of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MapItemInfo.


        :param type: The type of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def sdt_status(self):
        """Gets the sdt_status of this MapItemInfo.  # noqa: E501


        :return: The sdt_status of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._sdt_status

    @sdt_status.setter
    def sdt_status(self, sdt_status):
        """Sets the sdt_status of this MapItemInfo.


        :param sdt_status: The sdt_status of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._sdt_status = sdt_status

    @property
    def active_status(self):
        """Gets the active_status of this MapItemInfo.  # noqa: E501


        :return: The active_status of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this MapItemInfo.


        :param active_status: The active_status of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._active_status = active_status

    @property
    def name(self):
        """Gets the name of this MapItemInfo.  # noqa: E501


        :return: The name of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MapItemInfo.


        :param name: The name of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sub_type(self):
        """Gets the sub_type of this MapItemInfo.  # noqa: E501


        :return: The sub_type of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this MapItemInfo.


        :param sub_type: The sub_type of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

    @property
    def location(self):
        """Gets the location of this MapItemInfo.  # noqa: E501


        :return: The location of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this MapItemInfo.


        :param location: The location of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def id(self):
        """Gets the id of this MapItemInfo.  # noqa: E501


        :return: The id of this MapItemInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MapItemInfo.


        :param id: The id of this MapItemInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def longitude(self):
        """Gets the longitude of this MapItemInfo.  # noqa: E501


        :return: The longitude of this MapItemInfo.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this MapItemInfo.


        :param longitude: The longitude of this MapItemInfo.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

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
        if issubclass(MapItemInfo, dict):
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
        if not isinstance(other, MapItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
