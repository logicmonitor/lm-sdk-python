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
from logicmonitor_sdk.models.report_base import ReportBase  # noqa: F401,E501

class HostGroupInventoryReport(ReportBase):
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
        'sorted_by': 'str',
        'host_groups': 'str',
        'include_sub_groups': 'bool',
        'properties': 'list[str]'
    }
    if hasattr(ReportBase, "swagger_types"):
        swagger_types.update(ReportBase.swagger_types)

    attribute_map = {
        'sorted_by': 'sortedBy',
        'host_groups': 'hostGroups',
        'include_sub_groups': 'includeSubGroups',
        'properties': 'properties'
    }
    if hasattr(ReportBase, "attribute_map"):
        attribute_map.update(ReportBase.attribute_map)

    def __init__(self, sorted_by=None, host_groups=None, include_sub_groups=None, properties=None, *args, **kwargs):  # noqa: E501
        """HostGroupInventoryReport - a model defined in Swagger"""  # noqa: E501
        self._sorted_by = None
        self._host_groups = None
        self._include_sub_groups = None
        self._properties = None
        self.discriminator = None
        if sorted_by is not None:
            self.sorted_by = sorted_by
        if host_groups is not None:
            self.host_groups = host_groups
        if include_sub_groups is not None:
            self.include_sub_groups = include_sub_groups
        self.properties = properties
        ReportBase.__init__(self, *args, **kwargs)

    @property
    def sorted_by(self):
        """Gets the sorted_by of this HostGroupInventoryReport.  # noqa: E501


        :return: The sorted_by of this HostGroupInventoryReport.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this HostGroupInventoryReport.


        :param sorted_by: The sorted_by of this HostGroupInventoryReport.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

    @property
    def host_groups(self):
        """Gets the host_groups of this HostGroupInventoryReport.  # noqa: E501


        :return: The host_groups of this HostGroupInventoryReport.  # noqa: E501
        :rtype: str
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, host_groups):
        """Sets the host_groups of this HostGroupInventoryReport.


        :param host_groups: The host_groups of this HostGroupInventoryReport.  # noqa: E501
        :type: str
        """

        self._host_groups = host_groups

    @property
    def include_sub_groups(self):
        """Gets the include_sub_groups of this HostGroupInventoryReport.  # noqa: E501


        :return: The include_sub_groups of this HostGroupInventoryReport.  # noqa: E501
        :rtype: bool
        """
        return self._include_sub_groups

    @include_sub_groups.setter
    def include_sub_groups(self, include_sub_groups):
        """Sets the include_sub_groups of this HostGroupInventoryReport.


        :param include_sub_groups: The include_sub_groups of this HostGroupInventoryReport.  # noqa: E501
        :type: bool
        """

        self._include_sub_groups = include_sub_groups

    @property
    def properties(self):
        """Gets the properties of this HostGroupInventoryReport.  # noqa: E501


        :return: The properties of this HostGroupInventoryReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this HostGroupInventoryReport.


        :param properties: The properties of this HostGroupInventoryReport.  # noqa: E501
        :type: list[str]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if issubclass(HostGroupInventoryReport, dict):
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
        if not isinstance(other, HostGroupInventoryReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
