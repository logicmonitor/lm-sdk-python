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

class AlertFilters(object):
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
        'datapoints_filter_mode': 'str',
        'is_ignore_sdt_alerts': 'bool',
        'datapoint_filters': 'list[DatapointFilterItem]'
    }

    attribute_map = {
        'datapoints_filter_mode': 'datapointsFilterMode',
        'is_ignore_sdt_alerts': 'isIgnoreSdtAlerts',
        'datapoint_filters': 'datapointFilters'
    }

    def __init__(self, datapoints_filter_mode=None, is_ignore_sdt_alerts=None, datapoint_filters=None):  # noqa: E501
        """AlertFilters - a model defined in Swagger"""  # noqa: E501
        self._datapoints_filter_mode = None
        self._is_ignore_sdt_alerts = None
        self._datapoint_filters = None
        self.discriminator = None
        if datapoints_filter_mode is not None:
            self.datapoints_filter_mode = datapoints_filter_mode
        if is_ignore_sdt_alerts is not None:
            self.is_ignore_sdt_alerts = is_ignore_sdt_alerts
        if datapoint_filters is not None:
            self.datapoint_filters = datapoint_filters

    @property
    def datapoints_filter_mode(self):
        """Gets the datapoints_filter_mode of this AlertFilters.  # noqa: E501


        :return: The datapoints_filter_mode of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._datapoints_filter_mode

    @datapoints_filter_mode.setter
    def datapoints_filter_mode(self, datapoints_filter_mode):
        """Sets the datapoints_filter_mode of this AlertFilters.


        :param datapoints_filter_mode: The datapoints_filter_mode of this AlertFilters.  # noqa: E501
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]  # noqa: E501
        if datapoints_filter_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `datapoints_filter_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(datapoints_filter_mode, allowed_values)
            )

        self._datapoints_filter_mode = datapoints_filter_mode

    @property
    def is_ignore_sdt_alerts(self):
        """Gets the is_ignore_sdt_alerts of this AlertFilters.  # noqa: E501


        :return: The is_ignore_sdt_alerts of this AlertFilters.  # noqa: E501
        :rtype: bool
        """
        return self._is_ignore_sdt_alerts

    @is_ignore_sdt_alerts.setter
    def is_ignore_sdt_alerts(self, is_ignore_sdt_alerts):
        """Sets the is_ignore_sdt_alerts of this AlertFilters.


        :param is_ignore_sdt_alerts: The is_ignore_sdt_alerts of this AlertFilters.  # noqa: E501
        :type: bool
        """

        self._is_ignore_sdt_alerts = is_ignore_sdt_alerts

    @property
    def datapoint_filters(self):
        """Gets the datapoint_filters of this AlertFilters.  # noqa: E501


        :return: The datapoint_filters of this AlertFilters.  # noqa: E501
        :rtype: list[DatapointFilterItem]
        """
        return self._datapoint_filters

    @datapoint_filters.setter
    def datapoint_filters(self, datapoint_filters):
        """Sets the datapoint_filters of this AlertFilters.


        :param datapoint_filters: The datapoint_filters of this AlertFilters.  # noqa: E501
        :type: list[DatapointFilterItem]
        """

        self._datapoint_filters = datapoint_filters

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
        if issubclass(AlertFilters, dict):
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
        if not isinstance(other, AlertFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
