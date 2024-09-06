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

class ReportGroup(object):
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
        'matched_report_count': 'int',
        'user_permission': 'str',
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'reports_count': 'int'
    }

    attribute_map = {
        'matched_report_count': 'matchedReportCount',
        'user_permission': 'userPermission',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'reports_count': 'reportsCount'
    }

    def __init__(self, matched_report_count=None, user_permission=None, name=None, description=None, id=None, reports_count=None):  # noqa: E501
        """ReportGroup - a model defined in Swagger"""  # noqa: E501
        self._matched_report_count = None
        self._user_permission = None
        self._name = None
        self._description = None
        self._id = None
        self._reports_count = None
        self.discriminator = None
        if matched_report_count is not None:
            self.matched_report_count = matched_report_count
        if user_permission is not None:
            self.user_permission = user_permission
        self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if reports_count is not None:
            self.reports_count = reports_count

    @property
    def matched_report_count(self):
        """Gets the matched_report_count of this ReportGroup.  # noqa: E501

        The matched reports count of this group  # noqa: E501

        :return: The matched_report_count of this ReportGroup.  # noqa: E501
        :rtype: int
        """
        return self._matched_report_count

    @matched_report_count.setter
    def matched_report_count(self, matched_report_count):
        """Sets the matched_report_count of this ReportGroup.

        The matched reports count of this group  # noqa: E501

        :param matched_report_count: The matched_report_count of this ReportGroup.  # noqa: E501
        :type: int
        """

        self._matched_report_count = matched_report_count

    @property
    def user_permission(self):
        """Gets the user_permission of this ReportGroup.  # noqa: E501

        The user permission on the report group  # noqa: E501

        :return: The user_permission of this ReportGroup.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this ReportGroup.

        The user permission on the report group  # noqa: E501

        :param user_permission: The user_permission of this ReportGroup.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def name(self):
        """Gets the name of this ReportGroup.  # noqa: E501

        The report group name  # noqa: E501

        :return: The name of this ReportGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportGroup.

        The report group name  # noqa: E501

        :param name: The name of this ReportGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReportGroup.  # noqa: E501

        The report group description  # noqa: E501

        :return: The description of this ReportGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportGroup.

        The report group description  # noqa: E501

        :param description: The description of this ReportGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this ReportGroup.  # noqa: E501

        The report group id  # noqa: E501

        :return: The id of this ReportGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReportGroup.

        The report group id  # noqa: E501

        :param id: The id of this ReportGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reports_count(self):
        """Gets the reports_count of this ReportGroup.  # noqa: E501

        The reports count of this group  # noqa: E501

        :return: The reports_count of this ReportGroup.  # noqa: E501
        :rtype: int
        """
        return self._reports_count

    @reports_count.setter
    def reports_count(self, reports_count):
        """Sets the reports_count of this ReportGroup.

        The reports count of this group  # noqa: E501

        :param reports_count: The reports_count of this ReportGroup.  # noqa: E501
        :type: int
        """

        self._reports_count = reports_count

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
        if issubclass(ReportGroup, dict):
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
        if not isinstance(other, ReportGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
