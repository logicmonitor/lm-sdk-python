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

class GraphVirtualDataPoint(object):
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
        'rpn': 'str',
        'name': 'str'
    }

    attribute_map = {
        'rpn': 'rpn',
        'name': 'name'
    }

    def __init__(self, rpn=None, name=None):  # noqa: E501
        """GraphVirtualDataPoint - a model defined in Swagger"""  # noqa: E501
        self._rpn = None
        self._name = None
        self.discriminator = None
        if rpn is not None:
            self.rpn = rpn
        if name is not None:
            self.name = name

    @property
    def rpn(self):
        """Gets the rpn of this GraphVirtualDataPoint.  # noqa: E501

        The graph virtual data point rpn expression  # noqa: E501

        :return: The rpn of this GraphVirtualDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._rpn

    @rpn.setter
    def rpn(self, rpn):
        """Sets the rpn of this GraphVirtualDataPoint.

        The graph virtual data point rpn expression  # noqa: E501

        :param rpn: The rpn of this GraphVirtualDataPoint.  # noqa: E501
        :type: str
        """

        self._rpn = rpn

    @property
    def name(self):
        """Gets the name of this GraphVirtualDataPoint.  # noqa: E501

        The graph virtual data point name  # noqa: E501

        :return: The name of this GraphVirtualDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GraphVirtualDataPoint.

        The graph virtual data point name  # noqa: E501

        :param name: The name of this GraphVirtualDataPoint.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GraphVirtualDataPoint, dict):
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
        if not isinstance(other, GraphVirtualDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
