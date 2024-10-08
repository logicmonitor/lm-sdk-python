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

class ColorThreshold(object):
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
        'level': 'int',
        'threshold': 'float',
        'relation': 'str'
    }

    attribute_map = {
        'level': 'level',
        'threshold': 'threshold',
        'relation': 'relation'
    }

    def __init__(self, level=None, threshold=None, relation=None):  # noqa: E501
        """ColorThreshold - a model defined in Swagger"""  # noqa: E501
        self._level = None
        self._threshold = None
        self._relation = None
        self.discriminator = None
        self.level = level
        self.threshold = threshold
        self.relation = relation

    @property
    def level(self):
        """Gets the level of this ColorThreshold.  # noqa: E501


        :return: The level of this ColorThreshold.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ColorThreshold.


        :param level: The level of this ColorThreshold.  # noqa: E501
        :type: int
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def threshold(self):
        """Gets the threshold of this ColorThreshold.  # noqa: E501


        :return: The threshold of this ColorThreshold.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ColorThreshold.


        :param threshold: The threshold of this ColorThreshold.  # noqa: E501
        :type: float
        """
        if threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

    @property
    def relation(self):
        """Gets the relation of this ColorThreshold.  # noqa: E501


        :return: The relation of this ColorThreshold.  # noqa: E501
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this ColorThreshold.


        :param relation: The relation of this ColorThreshold.  # noqa: E501
        :type: str
        """
        if relation is None:
            raise ValueError("Invalid value for `relation`, must not be `None`")  # noqa: E501

        self._relation = relation

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
        if issubclass(ColorThreshold, dict):
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
        if not isinstance(other, ColorThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
