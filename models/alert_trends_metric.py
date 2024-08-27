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

class AlertTrendsMetric(object):
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
        'item_type': 'str',
        'item_val': 'str'
    }

    attribute_map = {
        'item_type': 'itemType',
        'item_val': 'itemVal'
    }

    def __init__(self, item_type=None, item_val=None):  # noqa: E501
        """AlertTrendsMetric - a model defined in Swagger"""  # noqa: E501
        self._item_type = None
        self._item_val = None
        self.discriminator = None
        self.item_type = item_type
        self.item_val = item_val

    @property
    def item_type(self):
        """Gets the item_type of this AlertTrendsMetric.  # noqa: E501


        :return: The item_type of this AlertTrendsMetric.  # noqa: E501
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this AlertTrendsMetric.


        :param item_type: The item_type of this AlertTrendsMetric.  # noqa: E501
        :type: str
        """
        if item_type is None:
            raise ValueError("Invalid value for `item_type`, must not be `None`")  # noqa: E501

        self._item_type = item_type

    @property
    def item_val(self):
        """Gets the item_val of this AlertTrendsMetric.  # noqa: E501


        :return: The item_val of this AlertTrendsMetric.  # noqa: E501
        :rtype: str
        """
        return self._item_val

    @item_val.setter
    def item_val(self, item_val):
        """Sets the item_val of this AlertTrendsMetric.


        :param item_val: The item_val of this AlertTrendsMetric.  # noqa: E501
        :type: str
        """
        if item_val is None:
            raise ValueError("Invalid value for `item_val`, must not be `None`")  # noqa: E501

        self._item_val = item_val

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
        if issubclass(AlertTrendsMetric, dict):
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
        if not isinstance(other, AlertTrendsMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
