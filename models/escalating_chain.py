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

class EscalatingChain(object):
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
        'in_alerting': 'bool',
        'throttling_alerts': 'int',
        'enable_throttling': 'bool',
        'destinations': 'list[Chain]',
        'name': 'str',
        'description': 'str',
        'id': 'int',
        'cc_destinations': 'list[Recipient]',
        'throttling_period': 'int'
    }

    attribute_map = {
        'in_alerting': 'inAlerting',
        'throttling_alerts': 'throttlingAlerts',
        'enable_throttling': 'enableThrottling',
        'destinations': 'destinations',
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'cc_destinations': 'ccDestinations',
        'throttling_period': 'throttlingPeriod'
    }

    def __init__(self, in_alerting=None, throttling_alerts=None, enable_throttling=None, destinations=None, name=None, description=None, id=None, cc_destinations=None, throttling_period=None):  # noqa: E501
        """EscalatingChain - a model defined in Swagger"""  # noqa: E501
        self._in_alerting = None
        self._throttling_alerts = None
        self._enable_throttling = None
        self._destinations = None
        self._name = None
        self._description = None
        self._id = None
        self._cc_destinations = None
        self._throttling_period = None
        self.discriminator = None
        if in_alerting is not None:
            self.in_alerting = in_alerting
        if throttling_alerts is not None:
            self.throttling_alerts = throttling_alerts
        if enable_throttling is not None:
            self.enable_throttling = enable_throttling
        self.destinations = destinations
        self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if cc_destinations is not None:
            self.cc_destinations = cc_destinations
        if throttling_period is not None:
            self.throttling_period = throttling_period

    @property
    def in_alerting(self):
        """Gets the in_alerting of this EscalatingChain.  # noqa: E501

        Whether or not chain in alerting  # noqa: E501

        :return: The in_alerting of this EscalatingChain.  # noqa: E501
        :rtype: bool
        """
        return self._in_alerting

    @in_alerting.setter
    def in_alerting(self, in_alerting):
        """Sets the in_alerting of this EscalatingChain.

        Whether or not chain in alerting  # noqa: E501

        :param in_alerting: The in_alerting of this EscalatingChain.  # noqa: E501
        :type: bool
        """

        self._in_alerting = in_alerting

    @property
    def throttling_alerts(self):
        """Gets the throttling_alerts of this EscalatingChain.  # noqa: E501

        Maximum number of alerts can be sent during a throttle period  # noqa: E501

        :return: The throttling_alerts of this EscalatingChain.  # noqa: E501
        :rtype: int
        """
        return self._throttling_alerts

    @throttling_alerts.setter
    def throttling_alerts(self, throttling_alerts):
        """Sets the throttling_alerts of this EscalatingChain.

        Maximum number of alerts can be sent during a throttle period  # noqa: E501

        :param throttling_alerts: The throttling_alerts of this EscalatingChain.  # noqa: E501
        :type: int
        """

        self._throttling_alerts = throttling_alerts

    @property
    def enable_throttling(self):
        """Gets the enable_throttling of this EscalatingChain.  # noqa: E501

        If throttle needs to be enabled then true if not then false.  # noqa: E501

        :return: The enable_throttling of this EscalatingChain.  # noqa: E501
        :rtype: bool
        """
        return self._enable_throttling

    @enable_throttling.setter
    def enable_throttling(self, enable_throttling):
        """Sets the enable_throttling of this EscalatingChain.

        If throttle needs to be enabled then true if not then false.  # noqa: E501

        :param enable_throttling: The enable_throttling of this EscalatingChain.  # noqa: E501
        :type: bool
        """

        self._enable_throttling = enable_throttling

    @property
    def destinations(self):
        """Gets the destinations of this EscalatingChain.  # noqa: E501

        The chain destinations  # noqa: E501

        :return: The destinations of this EscalatingChain.  # noqa: E501
        :rtype: list[Chain]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this EscalatingChain.

        The chain destinations  # noqa: E501

        :param destinations: The destinations of this EscalatingChain.  # noqa: E501
        :type: list[Chain]
        """
        if destinations is None:
            raise ValueError("Invalid value for `destinations`, must not be `None`")  # noqa: E501

        self._destinations = destinations

    @property
    def name(self):
        """Gets the name of this EscalatingChain.  # noqa: E501

        The chain name  # noqa: E501

        :return: The name of this EscalatingChain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EscalatingChain.

        The chain name  # noqa: E501

        :param name: The name of this EscalatingChain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this EscalatingChain.  # noqa: E501

        The description for chain  # noqa: E501

        :return: The description of this EscalatingChain.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EscalatingChain.

        The description for chain  # noqa: E501

        :param description: The description of this EscalatingChain.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this EscalatingChain.  # noqa: E501

        The Id of the chain  # noqa: E501

        :return: The id of this EscalatingChain.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EscalatingChain.

        The Id of the chain  # noqa: E501

        :param id: The id of this EscalatingChain.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cc_destinations(self):
        """Gets the cc_destinations of this EscalatingChain.  # noqa: E501

        The chain's cc destinations  # noqa: E501

        :return: The cc_destinations of this EscalatingChain.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._cc_destinations

    @cc_destinations.setter
    def cc_destinations(self, cc_destinations):
        """Sets the cc_destinations of this EscalatingChain.

        The chain's cc destinations  # noqa: E501

        :param cc_destinations: The cc_destinations of this EscalatingChain.  # noqa: E501
        :type: list[Recipient]
        """

        self._cc_destinations = cc_destinations

    @property
    def throttling_period(self):
        """Gets the throttling_period of this EscalatingChain.  # noqa: E501

        The throttle period  # noqa: E501

        :return: The throttling_period of this EscalatingChain.  # noqa: E501
        :rtype: int
        """
        return self._throttling_period

    @throttling_period.setter
    def throttling_period(self, throttling_period):
        """Sets the throttling_period of this EscalatingChain.

        The throttle period  # noqa: E501

        :param throttling_period: The throttling_period of this EscalatingChain.  # noqa: E501
        :type: int
        """

        self._throttling_period = throttling_period

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
        if issubclass(EscalatingChain, dict):
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
        if not isinstance(other, EscalatingChain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
