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

class RestResponseMetaBlock(object):
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
        'filtered_count': 'int',
        'per_page_count': 'int',
        'sort': 'str',
        'total_count': 'int',
        'page_offset_count': 'int'
    }

    attribute_map = {
        'filtered_count': 'filteredCount',
        'per_page_count': 'perPageCount',
        'sort': 'sort',
        'total_count': 'totalCount',
        'page_offset_count': 'pageOffsetCount'
    }

    def __init__(self, filtered_count=None, per_page_count=None, sort=None, total_count=None, page_offset_count=None):  # noqa: E501
        """RestResponseMetaBlock - a model defined in Swagger"""  # noqa: E501
        self._filtered_count = None
        self._per_page_count = None
        self._sort = None
        self._total_count = None
        self._page_offset_count = None
        self.discriminator = None
        if filtered_count is not None:
            self.filtered_count = filtered_count
        if per_page_count is not None:
            self.per_page_count = per_page_count
        if sort is not None:
            self.sort = sort
        if total_count is not None:
            self.total_count = total_count
        if page_offset_count is not None:
            self.page_offset_count = page_offset_count

    @property
    def filtered_count(self):
        """Gets the filtered_count of this RestResponseMetaBlock.  # noqa: E501


        :return: The filtered_count of this RestResponseMetaBlock.  # noqa: E501
        :rtype: int
        """
        return self._filtered_count

    @filtered_count.setter
    def filtered_count(self, filtered_count):
        """Sets the filtered_count of this RestResponseMetaBlock.


        :param filtered_count: The filtered_count of this RestResponseMetaBlock.  # noqa: E501
        :type: int
        """

        self._filtered_count = filtered_count

    @property
    def per_page_count(self):
        """Gets the per_page_count of this RestResponseMetaBlock.  # noqa: E501


        :return: The per_page_count of this RestResponseMetaBlock.  # noqa: E501
        :rtype: int
        """
        return self._per_page_count

    @per_page_count.setter
    def per_page_count(self, per_page_count):
        """Sets the per_page_count of this RestResponseMetaBlock.


        :param per_page_count: The per_page_count of this RestResponseMetaBlock.  # noqa: E501
        :type: int
        """

        self._per_page_count = per_page_count

    @property
    def sort(self):
        """Gets the sort of this RestResponseMetaBlock.  # noqa: E501


        :return: The sort of this RestResponseMetaBlock.  # noqa: E501
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this RestResponseMetaBlock.


        :param sort: The sort of this RestResponseMetaBlock.  # noqa: E501
        :type: str
        """

        self._sort = sort

    @property
    def total_count(self):
        """Gets the total_count of this RestResponseMetaBlock.  # noqa: E501


        :return: The total_count of this RestResponseMetaBlock.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this RestResponseMetaBlock.


        :param total_count: The total_count of this RestResponseMetaBlock.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def page_offset_count(self):
        """Gets the page_offset_count of this RestResponseMetaBlock.  # noqa: E501


        :return: The page_offset_count of this RestResponseMetaBlock.  # noqa: E501
        :rtype: int
        """
        return self._page_offset_count

    @page_offset_count.setter
    def page_offset_count(self, page_offset_count):
        """Sets the page_offset_count of this RestResponseMetaBlock.


        :param page_offset_count: The page_offset_count of this RestResponseMetaBlock.  # noqa: E501
        :type: int
        """

        self._page_offset_count = page_offset_count

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
        if issubclass(RestResponseMetaBlock, dict):
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
        if not isinstance(other, RestResponseMetaBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
