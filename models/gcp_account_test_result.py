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

class GcpAccountTestResult(object):
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
        'no_permission_services': 'list[str]',
        'detail_link': 'str',
        'non_permission_errors': 'list[str]'
    }

    attribute_map = {
        'no_permission_services': 'noPermissionServices',
        'detail_link': 'detailLink',
        'non_permission_errors': 'nonPermissionErrors'
    }

    def __init__(self, no_permission_services=None, detail_link=None, non_permission_errors=None):  # noqa: E501
        """GcpAccountTestResult - a model defined in Swagger"""  # noqa: E501
        self._no_permission_services = None
        self._detail_link = None
        self._non_permission_errors = None
        self.discriminator = None
        if no_permission_services is not None:
            self.no_permission_services = no_permission_services
        if detail_link is not None:
            self.detail_link = detail_link
        if non_permission_errors is not None:
            self.non_permission_errors = non_permission_errors

    @property
    def no_permission_services(self):
        """Gets the no_permission_services of this GcpAccountTestResult.  # noqa: E501


        :return: The no_permission_services of this GcpAccountTestResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._no_permission_services

    @no_permission_services.setter
    def no_permission_services(self, no_permission_services):
        """Sets the no_permission_services of this GcpAccountTestResult.


        :param no_permission_services: The no_permission_services of this GcpAccountTestResult.  # noqa: E501
        :type: list[str]
        """

        self._no_permission_services = no_permission_services

    @property
    def detail_link(self):
        """Gets the detail_link of this GcpAccountTestResult.  # noqa: E501


        :return: The detail_link of this GcpAccountTestResult.  # noqa: E501
        :rtype: str
        """
        return self._detail_link

    @detail_link.setter
    def detail_link(self, detail_link):
        """Sets the detail_link of this GcpAccountTestResult.


        :param detail_link: The detail_link of this GcpAccountTestResult.  # noqa: E501
        :type: str
        """

        self._detail_link = detail_link

    @property
    def non_permission_errors(self):
        """Gets the non_permission_errors of this GcpAccountTestResult.  # noqa: E501


        :return: The non_permission_errors of this GcpAccountTestResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._non_permission_errors

    @non_permission_errors.setter
    def non_permission_errors(self, non_permission_errors):
        """Sets the non_permission_errors of this GcpAccountTestResult.


        :param non_permission_errors: The non_permission_errors of this GcpAccountTestResult.  # noqa: E501
        :type: list[str]
        """

        self._non_permission_errors = non_permission_errors

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
        if issubclass(GcpAccountTestResult, dict):
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
        if not isinstance(other, GcpAccountTestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
