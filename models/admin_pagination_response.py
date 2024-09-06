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

class AdminPaginationResponse(object):
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
        'total': 'int',
        'search_id': 'str',
        'items': 'list[Admin]'
    }

    attribute_map = {
        'total': 'total',
        'search_id': 'searchId',
        'items': 'items'
    }

    def __init__(self, total=None, search_id=None, items=None):  # noqa: E501
        """AdminPaginationResponse - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._search_id = None
        self._items = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if search_id is not None:
            self.search_id = search_id
        if items is not None:
            self.items = items

    @property
    def total(self):
        """Gets the total of this AdminPaginationResponse.  # noqa: E501


        :return: The total of this AdminPaginationResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AdminPaginationResponse.


        :param total: The total of this AdminPaginationResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def search_id(self):
        """Gets the search_id of this AdminPaginationResponse.  # noqa: E501


        :return: The search_id of this AdminPaginationResponse.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this AdminPaginationResponse.


        :param search_id: The search_id of this AdminPaginationResponse.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def items(self):
        """Gets the items of this AdminPaginationResponse.  # noqa: E501


        :return: The items of this AdminPaginationResponse.  # noqa: E501
        :rtype: list[Admin]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AdminPaginationResponse.


        :param items: The items of this AdminPaginationResponse.  # noqa: E501
        :type: list[Admin]
        """

        self._items = items

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
        if issubclass(AdminPaginationResponse, dict):
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
        if not isinstance(other, AdminPaginationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
