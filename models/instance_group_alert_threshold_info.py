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

class InstanceGroupAlertThresholdInfo(object):
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
        'enable_anomaly_alert_generation': 'str',
        'alert_for_no_data': 'int',
        'enable_anomaly_alert_suppression': 'str',
        'group_id': 'int',
        'alert_clear_transition_interval': 'int',
        'alert_enabled': 'bool',
        'alert_expr': 'str',
        'alert_transition_interval': 'int'
    }

    attribute_map = {
        'enable_anomaly_alert_generation': 'enableAnomalyAlertGeneration',
        'alert_for_no_data': 'alertForNoData',
        'enable_anomaly_alert_suppression': 'enableAnomalyAlertSuppression',
        'group_id': 'groupId',
        'alert_clear_transition_interval': 'alertClearTransitionInterval',
        'alert_enabled': 'alertEnabled',
        'alert_expr': 'alertExpr',
        'alert_transition_interval': 'alertTransitionInterval'
    }

    def __init__(self, enable_anomaly_alert_generation=None, alert_for_no_data=None, enable_anomaly_alert_suppression=None, group_id=None, alert_clear_transition_interval=None, alert_enabled=None, alert_expr=None, alert_transition_interval=None):  # noqa: E501
        """InstanceGroupAlertThresholdInfo - a model defined in Swagger"""  # noqa: E501
        self._enable_anomaly_alert_generation = None
        self._alert_for_no_data = None
        self._enable_anomaly_alert_suppression = None
        self._group_id = None
        self._alert_clear_transition_interval = None
        self._alert_enabled = None
        self._alert_expr = None
        self._alert_transition_interval = None
        self.discriminator = None
        if enable_anomaly_alert_generation is not None:
            self.enable_anomaly_alert_generation = enable_anomaly_alert_generation
        if alert_for_no_data is not None:
            self.alert_for_no_data = alert_for_no_data
        if enable_anomaly_alert_suppression is not None:
            self.enable_anomaly_alert_suppression = enable_anomaly_alert_suppression
        if group_id is not None:
            self.group_id = group_id
        if alert_clear_transition_interval is not None:
            self.alert_clear_transition_interval = alert_clear_transition_interval
        if alert_enabled is not None:
            self.alert_enabled = alert_enabled
        if alert_expr is not None:
            self.alert_expr = alert_expr
        if alert_transition_interval is not None:
            self.alert_transition_interval = alert_transition_interval

    @property
    def enable_anomaly_alert_generation(self):
        """Gets the enable_anomaly_alert_generation of this InstanceGroupAlertThresholdInfo.  # noqa: E501

        enable anomaly alert generation  # noqa: E501

        :return: The enable_anomaly_alert_generation of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_generation

    @enable_anomaly_alert_generation.setter
    def enable_anomaly_alert_generation(self, enable_anomaly_alert_generation):
        """Sets the enable_anomaly_alert_generation of this InstanceGroupAlertThresholdInfo.

        enable anomaly alert generation  # noqa: E501

        :param enable_anomaly_alert_generation: The enable_anomaly_alert_generation of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_generation = enable_anomaly_alert_generation

    @property
    def alert_for_no_data(self):
        """Gets the alert_for_no_data of this InstanceGroupAlertThresholdInfo.  # noqa: E501

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 ( 1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :return: The alert_for_no_data of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: int
        """
        return self._alert_for_no_data

    @alert_for_no_data.setter
    def alert_for_no_data(self, alert_for_no_data):
        """Sets the alert_for_no_data of this InstanceGroupAlertThresholdInfo.

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 ( 1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :param alert_for_no_data: The alert_for_no_data of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: int
        """

        self._alert_for_no_data = alert_for_no_data

    @property
    def enable_anomaly_alert_suppression(self):
        """Gets the enable_anomaly_alert_suppression of this InstanceGroupAlertThresholdInfo.  # noqa: E501

        enable anomaly alert suppression  # noqa: E501

        :return: The enable_anomaly_alert_suppression of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_suppression

    @enable_anomaly_alert_suppression.setter
    def enable_anomaly_alert_suppression(self, enable_anomaly_alert_suppression):
        """Sets the enable_anomaly_alert_suppression of this InstanceGroupAlertThresholdInfo.

        enable anomaly alert suppression  # noqa: E501

        :param enable_anomaly_alert_suppression: The enable_anomaly_alert_suppression of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_suppression = enable_anomaly_alert_suppression

    @property
    def group_id(self):
        """Gets the group_id of this InstanceGroupAlertThresholdInfo.  # noqa: E501


        :return: The group_id of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InstanceGroupAlertThresholdInfo.


        :param group_id: The group_id of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def alert_clear_transition_interval(self):
        """Gets the alert_clear_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :return: The alert_clear_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: int
        """
        return self._alert_clear_transition_interval

    @alert_clear_transition_interval.setter
    def alert_clear_transition_interval(self, alert_clear_transition_interval):
        """Sets the alert_clear_transition_interval of this InstanceGroupAlertThresholdInfo.

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :param alert_clear_transition_interval: The alert_clear_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: int
        """

        self._alert_clear_transition_interval = alert_clear_transition_interval

    @property
    def alert_enabled(self):
        """Gets the alert_enabled of this InstanceGroupAlertThresholdInfo.  # noqa: E501


        :return: The alert_enabled of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        """Sets the alert_enabled of this InstanceGroupAlertThresholdInfo.


        :param alert_enabled: The alert_enabled of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: bool
        """

        self._alert_enabled = alert_enabled

    @property
    def alert_expr(self):
        """Gets the alert_expr of this InstanceGroupAlertThresholdInfo.  # noqa: E501


        :return: The alert_expr of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """Sets the alert_expr of this InstanceGroupAlertThresholdInfo.


        :param alert_expr: The alert_expr of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: str
        """

        self._alert_expr = alert_expr

    @property
    def alert_transition_interval(self):
        """Gets the alert_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :return: The alert_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :rtype: int
        """
        return self._alert_transition_interval

    @alert_transition_interval.setter
    def alert_transition_interval(self, alert_transition_interval):
        """Sets the alert_transition_interval of this InstanceGroupAlertThresholdInfo.

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :param alert_transition_interval: The alert_transition_interval of this InstanceGroupAlertThresholdInfo.  # noqa: E501
        :type: int
        """

        self._alert_transition_interval = alert_transition_interval

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
        if issubclass(InstanceGroupAlertThresholdInfo, dict):
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
        if not isinstance(other, InstanceGroupAlertThresholdInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
