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

class AlertRule(object):
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
        'datapoint': 'str',
        'instance': 'str',
        'devices': 'list[str]',
        'escalating_chain_id': 'int',
        'resource_properties': 'list[DeviceProperty]',
        'send_anomaly_suppressed_alert': 'bool',
        'priority': 'int',
        'suppress_alert_ack_sdt': 'bool',
        'datasource': 'str',
        'suppress_alert_clear': 'bool',
        'name': 'str',
        'id': 'int',
        'level_str': 'str',
        'device_groups': 'list[str]',
        'escalating_chain': 'object',
        'escalation_interval': 'int'
    }

    attribute_map = {
        'datapoint': 'datapoint',
        'instance': 'instance',
        'devices': 'devices',
        'escalating_chain_id': 'escalatingChainId',
        'resource_properties': 'resourceProperties',
        'send_anomaly_suppressed_alert': 'sendAnomalySuppressedAlert',
        'priority': 'priority',
        'suppress_alert_ack_sdt': 'suppressAlertAckSdt',
        'datasource': 'datasource',
        'suppress_alert_clear': 'suppressAlertClear',
        'name': 'name',
        'id': 'id',
        'level_str': 'levelStr',
        'device_groups': 'deviceGroups',
        'escalating_chain': 'escalatingChain',
        'escalation_interval': 'escalationInterval'
    }

    def __init__(self, datapoint=None, instance=None, devices=None, escalating_chain_id=None, resource_properties=None, send_anomaly_suppressed_alert=None, priority=None, suppress_alert_ack_sdt=None, datasource=None, suppress_alert_clear=None, name=None, id=None, level_str=None, device_groups=None, escalating_chain=None, escalation_interval=None):  # noqa: E501
        """AlertRule - a model defined in Swagger"""  # noqa: E501
        self._datapoint = None
        self._instance = None
        self._devices = None
        self._escalating_chain_id = None
        self._resource_properties = None
        self._send_anomaly_suppressed_alert = None
        self._priority = None
        self._suppress_alert_ack_sdt = None
        self._datasource = None
        self._suppress_alert_clear = None
        self._name = None
        self._id = None
        self._level_str = None
        self._device_groups = None
        self._escalating_chain = None
        self._escalation_interval = None
        self.discriminator = None
        if datapoint is not None:
            self.datapoint = datapoint
        if instance is not None:
            self.instance = instance
        if devices is not None:
            self.devices = devices
        self.escalating_chain_id = escalating_chain_id
        if resource_properties is not None:
            self.resource_properties = resource_properties
        self.send_anomaly_suppressed_alert = send_anomaly_suppressed_alert
        self.priority = priority
        if suppress_alert_ack_sdt is not None:
            self.suppress_alert_ack_sdt = suppress_alert_ack_sdt
        if datasource is not None:
            self.datasource = datasource
        if suppress_alert_clear is not None:
            self.suppress_alert_clear = suppress_alert_clear
        self.name = name
        if id is not None:
            self.id = id
        if level_str is not None:
            self.level_str = level_str
        if device_groups is not None:
            self.device_groups = device_groups
        if escalating_chain is not None:
            self.escalating_chain = escalating_chain
        if escalation_interval is not None:
            self.escalation_interval = escalation_interval

    @property
    def datapoint(self):
        """Gets the datapoint of this AlertRule.  # noqa: E501

        The datapoint for which the alert rule is configured to match  # noqa: E501

        :return: The datapoint of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._datapoint

    @datapoint.setter
    def datapoint(self, datapoint):
        """Sets the datapoint of this AlertRule.

        The datapoint for which the alert rule is configured to match  # noqa: E501

        :param datapoint: The datapoint of this AlertRule.  # noqa: E501
        :type: str
        """

        self._datapoint = datapoint

    @property
    def instance(self):
        """Gets the instance of this AlertRule.  # noqa: E501

        The instance for which the alert rule is configured to match  # noqa: E501

        :return: The instance of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this AlertRule.

        The instance for which the alert rule is configured to match  # noqa: E501

        :param instance: The instance of this AlertRule.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def devices(self):
        """Gets the devices of this AlertRule.  # noqa: E501

        The device names and service names for which the alert rule is configured to match  # noqa: E501

        :return: The devices of this AlertRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this AlertRule.

        The device names and service names for which the alert rule is configured to match  # noqa: E501

        :param devices: The devices of this AlertRule.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def escalating_chain_id(self):
        """Gets the escalating_chain_id of this AlertRule.  # noqa: E501

        The id of the escalation chain associated with the alert rule  # noqa: E501

        :return: The escalating_chain_id of this AlertRule.  # noqa: E501
        :rtype: int
        """
        return self._escalating_chain_id

    @escalating_chain_id.setter
    def escalating_chain_id(self, escalating_chain_id):
        """Sets the escalating_chain_id of this AlertRule.

        The id of the escalation chain associated with the alert rule  # noqa: E501

        :param escalating_chain_id: The escalating_chain_id of this AlertRule.  # noqa: E501
        :type: int
        """
        if escalating_chain_id is None:
            raise ValueError("Invalid value for `escalating_chain_id`, must not be `None`")  # noqa: E501

        self._escalating_chain_id = escalating_chain_id

    @property
    def resource_properties(self):
        """Gets the resource_properties of this AlertRule.  # noqa: E501

        The resource property filters list  # noqa: E501

        :return: The resource_properties of this AlertRule.  # noqa: E501
        :rtype: list[DeviceProperty]
        """
        return self._resource_properties

    @resource_properties.setter
    def resource_properties(self, resource_properties):
        """Sets the resource_properties of this AlertRule.

        The resource property filters list  # noqa: E501

        :param resource_properties: The resource_properties of this AlertRule.  # noqa: E501
        :type: list[DeviceProperty]
        """

        self._resource_properties = resource_properties

    @property
    def send_anomaly_suppressed_alert(self):
        """Gets the send_anomaly_suppressed_alert of this AlertRule.  # noqa: E501

        Whether or not send anomaly suppressed alert  # noqa: E501

        :return: The send_anomaly_suppressed_alert of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._send_anomaly_suppressed_alert

    @send_anomaly_suppressed_alert.setter
    def send_anomaly_suppressed_alert(self, send_anomaly_suppressed_alert):
        """Sets the send_anomaly_suppressed_alert of this AlertRule.

        Whether or not send anomaly suppressed alert  # noqa: E501

        :param send_anomaly_suppressed_alert: The send_anomaly_suppressed_alert of this AlertRule.  # noqa: E501
        :type: bool
        """
        if send_anomaly_suppressed_alert is None:
            raise ValueError("Invalid value for `send_anomaly_suppressed_alert`, must not be `None`")  # noqa: E501

        self._send_anomaly_suppressed_alert = send_anomaly_suppressed_alert

    @property
    def priority(self):
        """Gets the priority of this AlertRule.  # noqa: E501

        The priority associated with the alert rule  # noqa: E501

        :return: The priority of this AlertRule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AlertRule.

        The priority associated with the alert rule  # noqa: E501

        :param priority: The priority of this AlertRule.  # noqa: E501
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def suppress_alert_ack_sdt(self):
        """Gets the suppress_alert_ack_sdt of this AlertRule.  # noqa: E501

        Whether or not status notifications for acknowledgements and SDTs should be sent to the alert rule  # noqa: E501

        :return: The suppress_alert_ack_sdt of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_alert_ack_sdt

    @suppress_alert_ack_sdt.setter
    def suppress_alert_ack_sdt(self, suppress_alert_ack_sdt):
        """Sets the suppress_alert_ack_sdt of this AlertRule.

        Whether or not status notifications for acknowledgements and SDTs should be sent to the alert rule  # noqa: E501

        :param suppress_alert_ack_sdt: The suppress_alert_ack_sdt of this AlertRule.  # noqa: E501
        :type: bool
        """

        self._suppress_alert_ack_sdt = suppress_alert_ack_sdt

    @property
    def datasource(self):
        """Gets the datasource of this AlertRule.  # noqa: E501

        The datasource for which the alert rule is configured to match  # noqa: E501

        :return: The datasource of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this AlertRule.

        The datasource for which the alert rule is configured to match  # noqa: E501

        :param datasource: The datasource of this AlertRule.  # noqa: E501
        :type: str
        """

        self._datasource = datasource

    @property
    def suppress_alert_clear(self):
        """Gets the suppress_alert_clear of this AlertRule.  # noqa: E501

        Whether or not alert clear notifications should be sent to the alert rule  # noqa: E501

        :return: The suppress_alert_clear of this AlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_alert_clear

    @suppress_alert_clear.setter
    def suppress_alert_clear(self, suppress_alert_clear):
        """Sets the suppress_alert_clear of this AlertRule.

        Whether or not alert clear notifications should be sent to the alert rule  # noqa: E501

        :param suppress_alert_clear: The suppress_alert_clear of this AlertRule.  # noqa: E501
        :type: bool
        """

        self._suppress_alert_clear = suppress_alert_clear

    @property
    def name(self):
        """Gets the name of this AlertRule.  # noqa: E501

        The name of the alert rule  # noqa: E501

        :return: The name of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertRule.

        The name of the alert rule  # noqa: E501

        :param name: The name of this AlertRule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this AlertRule.  # noqa: E501

        The Id of the alert rule  # noqa: E501

        :return: The id of this AlertRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRule.

        The Id of the alert rule  # noqa: E501

        :param id: The id of this AlertRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def level_str(self):
        """Gets the level_str of this AlertRule.  # noqa: E501

        The alert severity levels for which the alert rule is configured to match.  The values can be All|Warn|Error|Critical  # noqa: E501

        :return: The level_str of this AlertRule.  # noqa: E501
        :rtype: str
        """
        return self._level_str

    @level_str.setter
    def level_str(self, level_str):
        """Sets the level_str of this AlertRule.

        The alert severity levels for which the alert rule is configured to match.  The values can be All|Warn|Error|Critical  # noqa: E501

        :param level_str: The level_str of this AlertRule.  # noqa: E501
        :type: str
        """

        self._level_str = level_str

    @property
    def device_groups(self):
        """Gets the device_groups of this AlertRule.  # noqa: E501

        The device groups and service groups for which the alert rule is configured to match  # noqa: E501

        :return: The device_groups of this AlertRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_groups

    @device_groups.setter
    def device_groups(self, device_groups):
        """Sets the device_groups of this AlertRule.

        The device groups and service groups for which the alert rule is configured to match  # noqa: E501

        :param device_groups: The device_groups of this AlertRule.  # noqa: E501
        :type: list[str]
        """

        self._device_groups = device_groups

    @property
    def escalating_chain(self):
        """Gets the escalating_chain of this AlertRule.  # noqa: E501

        The escalation chain associated with the alert rule  # noqa: E501

        :return: The escalating_chain of this AlertRule.  # noqa: E501
        :rtype: object
        """
        return self._escalating_chain

    @escalating_chain.setter
    def escalating_chain(self, escalating_chain):
        """Sets the escalating_chain of this AlertRule.

        The escalation chain associated with the alert rule  # noqa: E501

        :param escalating_chain: The escalating_chain of this AlertRule.  # noqa: E501
        :type: object
        """

        self._escalating_chain = escalating_chain

    @property
    def escalation_interval(self):
        """Gets the escalation_interval of this AlertRule.  # noqa: E501

        The escalation interval associated with the alert rule, in minutes  # noqa: E501

        :return: The escalation_interval of this AlertRule.  # noqa: E501
        :rtype: int
        """
        return self._escalation_interval

    @escalation_interval.setter
    def escalation_interval(self, escalation_interval):
        """Sets the escalation_interval of this AlertRule.

        The escalation interval associated with the alert rule, in minutes  # noqa: E501

        :param escalation_interval: The escalation_interval of this AlertRule.  # noqa: E501
        :type: int
        """

        self._escalation_interval = escalation_interval

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
        if issubclass(AlertRule, dict):
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
        if not isinstance(other, AlertRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
