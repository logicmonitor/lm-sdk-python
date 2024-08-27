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

class RestLogSourceFilterV3(object):
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
        'include': 'str',
        'comment': 'str',
        'attribute': 'str',
        'value': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'include': 'include',
        'comment': 'comment',
        'attribute': 'attribute',
        'value': 'value',
        'operator': 'operator'
    }

    def __init__(self, include=None, comment=None, attribute=None, value=None, operator=None):  # noqa: E501
        """RestLogSourceFilterV3 - a model defined in Swagger"""  # noqa: E501
        self._include = None
        self._comment = None
        self._attribute = None
        self._value = None
        self._operator = None
        self.discriminator = None
        if include is not None:
            self.include = include
        if comment is not None:
            self.comment = comment
        if attribute is not None:
            self.attribute = attribute
        if value is not None:
            self.value = value
        if operator is not None:
            self.operator = operator

    @property
    def include(self):
        """Gets the include of this RestLogSourceFilterV3.  # noqa: E501


        :return: The include of this RestLogSourceFilterV3.  # noqa: E501
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this RestLogSourceFilterV3.


        :param include: The include of this RestLogSourceFilterV3.  # noqa: E501
        :type: str
        """

        self._include = include

    @property
    def comment(self):
        """Gets the comment of this RestLogSourceFilterV3.  # noqa: E501


        :return: The comment of this RestLogSourceFilterV3.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this RestLogSourceFilterV3.


        :param comment: The comment of this RestLogSourceFilterV3.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def attribute(self):
        """Gets the attribute of this RestLogSourceFilterV3.  # noqa: E501


        :return: The attribute of this RestLogSourceFilterV3.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this RestLogSourceFilterV3.


        :param attribute: The attribute of this RestLogSourceFilterV3.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def value(self):
        """Gets the value of this RestLogSourceFilterV3.  # noqa: E501


        :return: The value of this RestLogSourceFilterV3.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RestLogSourceFilterV3.


        :param value: The value of this RestLogSourceFilterV3.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def operator(self):
        """Gets the operator of this RestLogSourceFilterV3.  # noqa: E501


        :return: The operator of this RestLogSourceFilterV3.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this RestLogSourceFilterV3.


        :param operator: The operator of this RestLogSourceFilterV3.  # noqa: E501
        :type: str
        """

        self._operator = operator

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
        if issubclass(RestLogSourceFilterV3, dict):
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
        if not isinstance(other, RestLogSourceFilterV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
