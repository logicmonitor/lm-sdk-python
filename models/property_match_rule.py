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


class PropertyMatchRule(object):
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
        'underscore': 'bool',
        'case_insensitive': 'bool'
    }

    attribute_map = {
        'underscore': 'underscore',
        'case_insensitive': 'caseInsensitive'
    }

    def __init__(self, underscore=None, case_insensitive=None):  # noqa: E501
        """PropertyMatchRule - a model defined in Swagger"""  # noqa: E501

        self._underscore = None
        self._case_insensitive = None
        self.discriminator = None

        if underscore is not None:
            self.underscore = underscore
        if case_insensitive is not None:
            self.case_insensitive = case_insensitive

    @property
    def underscore(self):
        """Gets the underscore of this PropertyMatchRule.  # noqa: E501


        :return: The underscore of this PropertyMatchRule.  # noqa: E501
        :rtype: bool
        """
        return self._underscore

    @underscore.setter
    def underscore(self, underscore):
        """Sets the underscore of this PropertyMatchRule.


        :param underscore: The underscore of this PropertyMatchRule.  # noqa: E501
        :type: bool
        """

        self._underscore = underscore

    @property
    def case_insensitive(self):
        """Gets the case_insensitive of this PropertyMatchRule.  # noqa: E501


        :return: The case_insensitive of this PropertyMatchRule.  # noqa: E501
        :rtype: bool
        """
        return self._case_insensitive

    @case_insensitive.setter
    def case_insensitive(self, case_insensitive):
        """Sets the case_insensitive of this PropertyMatchRule.


        :param case_insensitive: The case_insensitive of this PropertyMatchRule.  # noqa: E501
        :type: bool
        """

        self._case_insensitive = case_insensitive

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
        if issubclass(PropertyMatchRule, dict):
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
        if not isinstance(other, PropertyMatchRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
