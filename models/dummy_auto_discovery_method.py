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
from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501

class DummyAutoDiscoveryMethod(AutoDiscoveryMethod):
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
        'generate_count': 'int',
        'get_generate_count2': 'int',
        'max_number': 'int'
    }
    if hasattr(AutoDiscoveryMethod, "swagger_types"):
        swagger_types.update(AutoDiscoveryMethod.swagger_types)

    attribute_map = {
        'generate_count': 'generateCount',
        'get_generate_count2': 'getGenerateCount2',
        'max_number': 'maxNumber'
    }
    if hasattr(AutoDiscoveryMethod, "attribute_map"):
        attribute_map.update(AutoDiscoveryMethod.attribute_map)

    def __init__(self, generate_count=None, get_generate_count2=None, max_number=None, *args, **kwargs):  # noqa: E501
        """DummyAutoDiscoveryMethod - a model defined in Swagger"""  # noqa: E501
        self._generate_count = None
        self._get_generate_count2 = None
        self._max_number = None
        self.discriminator = None
        self.generate_count = generate_count
        self.get_generate_count2 = get_generate_count2
        self.max_number = max_number
        AutoDiscoveryMethod.__init__(self, *args, **kwargs)

    @property
    def generate_count(self):
        """Gets the generate_count of this DummyAutoDiscoveryMethod.  # noqa: E501


        :return: The generate_count of this DummyAutoDiscoveryMethod.  # noqa: E501
        :rtype: int
        """
        return self._generate_count

    @generate_count.setter
    def generate_count(self, generate_count):
        """Sets the generate_count of this DummyAutoDiscoveryMethod.


        :param generate_count: The generate_count of this DummyAutoDiscoveryMethod.  # noqa: E501
        :type: int
        """
        if generate_count is None:
            raise ValueError("Invalid value for `generate_count`, must not be `None`")  # noqa: E501

        self._generate_count = generate_count

    @property
    def get_generate_count2(self):
        """Gets the get_generate_count2 of this DummyAutoDiscoveryMethod.  # noqa: E501


        :return: The get_generate_count2 of this DummyAutoDiscoveryMethod.  # noqa: E501
        :rtype: int
        """
        return self._get_generate_count2

    @get_generate_count2.setter
    def get_generate_count2(self, get_generate_count2):
        """Sets the get_generate_count2 of this DummyAutoDiscoveryMethod.


        :param get_generate_count2: The get_generate_count2 of this DummyAutoDiscoveryMethod.  # noqa: E501
        :type: int
        """
        if get_generate_count2 is None:
            raise ValueError("Invalid value for `get_generate_count2`, must not be `None`")  # noqa: E501

        self._get_generate_count2 = get_generate_count2

    @property
    def max_number(self):
        """Gets the max_number of this DummyAutoDiscoveryMethod.  # noqa: E501


        :return: The max_number of this DummyAutoDiscoveryMethod.  # noqa: E501
        :rtype: int
        """
        return self._max_number

    @max_number.setter
    def max_number(self, max_number):
        """Sets the max_number of this DummyAutoDiscoveryMethod.


        :param max_number: The max_number of this DummyAutoDiscoveryMethod.  # noqa: E501
        :type: int
        """
        if max_number is None:
            raise ValueError("Invalid value for `max_number`, must not be `None`")  # noqa: E501

        self._max_number = max_number

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
        if issubclass(DummyAutoDiscoveryMethod, dict):
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
        if not isinstance(other, DummyAutoDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
