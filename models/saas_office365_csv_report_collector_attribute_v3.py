# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class SaasOffice365CsvReportCollectorAttributeV3(CollectorAttribute):
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
        'name': 'str',
        'period': 'int',
        'report_name': 'str',
        'instance_column_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'period': 'period',
        'report_name': 'reportName',
        'instance_column_name': 'instanceColumnName'
    }

    def __init__(self, name=None, period=None, report_name=None, instance_column_name=None):  # noqa: E501
        """SaasOffice365CsvReportCollectorAttributeV3 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._period = None
        self._report_name = None
        self._instance_column_name = None
        self.discriminator = None

        self.name = name
        if period is not None:
            self.period = period
        self.report_name = report_name
        if instance_column_name is not None:
            self.instance_column_name = instance_column_name

    @property
    def name(self):
        """Gets the name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501

        data collector's name  # noqa: E501

        :return: The name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaasOffice365CsvReportCollectorAttributeV3.

        data collector's name  # noqa: E501

        :param name: The name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def period(self):
        """Gets the period of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501


        :return: The period of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this SaasOffice365CsvReportCollectorAttributeV3.


        :param period: The period of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def report_name(self):
        """Gets the report_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501


        :return: The report_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this SaasOffice365CsvReportCollectorAttributeV3.


        :param report_name: The report_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :type: str
        """
        if report_name is None:
            raise ValueError("Invalid value for `report_name`, must not be `None`")  # noqa: E501

        self._report_name = report_name

    @property
    def instance_column_name(self):
        """Gets the instance_column_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501


        :return: The instance_column_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :rtype: str
        """
        return self._instance_column_name

    @instance_column_name.setter
    def instance_column_name(self, instance_column_name):
        """Sets the instance_column_name of this SaasOffice365CsvReportCollectorAttributeV3.


        :param instance_column_name: The instance_column_name of this SaasOffice365CsvReportCollectorAttributeV3.  # noqa: E501
        :type: str
        """

        self._instance_column_name = instance_column_name

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
        if issubclass(SaasOffice365CsvReportCollectorAttributeV3, dict):
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
        if not isinstance(other, SaasOffice365CsvReportCollectorAttributeV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other