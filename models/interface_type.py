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


class InterfaceType(object):
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
        'if_position': 'str',
        'if_id': 'int'
    }

    attribute_map = {
        'if_position': 'ifPosition',
        'if_id': 'ifId'
    }

    def __init__(self, if_position=None, if_id=None):  # noqa: E501
        """InterfaceType - a model defined in Swagger"""  # noqa: E501

        self._if_position = None
        self._if_id = None
        self.discriminator = None

        if if_position is not None:
            self.if_position = if_position
        if if_id is not None:
            self.if_id = if_id

    @property
    def if_position(self):
        """Gets the if_position of this InterfaceType.  # noqa: E501


        :return: The if_position of this InterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._if_position

    @if_position.setter
    def if_position(self, if_position):
        """Sets the if_position of this InterfaceType.


        :param if_position: The if_position of this InterfaceType.  # noqa: E501
        :type: str
        """

        self._if_position = if_position

    @property
    def if_id(self):
        """Gets the if_id of this InterfaceType.  # noqa: E501


        :return: The if_id of this InterfaceType.  # noqa: E501
        :rtype: int
        """
        return self._if_id

    @if_id.setter
    def if_id(self, if_id):
        """Sets the if_id of this InterfaceType.


        :param if_id: The if_id of this InterfaceType.  # noqa: E501
        :type: int
        """

        self._if_id = if_id

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
        if issubclass(InterfaceType, dict):
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
        if not isinstance(other, InterfaceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
