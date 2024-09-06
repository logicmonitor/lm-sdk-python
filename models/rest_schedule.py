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

class RestSchedule(object):
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
        'cron': 'str',
        'recipients': 'list[str]',
        'timezone': 'str',
        'type': 'str',
        'notify': 'bool'
    }

    attribute_map = {
        'cron': 'cron',
        'recipients': 'recipients',
        'timezone': 'timezone',
        'type': 'type',
        'notify': 'notify'
    }

    def __init__(self, cron=None, recipients=None, timezone=None, type=None, notify=None):  # noqa: E501
        """RestSchedule - a model defined in Swagger"""  # noqa: E501
        self._cron = None
        self._recipients = None
        self._timezone = None
        self._type = None
        self._notify = None
        self.discriminator = None
        if cron is not None:
            self.cron = cron
        if recipients is not None:
            self.recipients = recipients
        if timezone is not None:
            self.timezone = timezone
        if type is not None:
            self.type = type
        if notify is not None:
            self.notify = notify

    @property
    def cron(self):
        """Gets the cron of this RestSchedule.  # noqa: E501

        The cron schedule for when the scan should be run  # noqa: E501

        :return: The cron of this RestSchedule.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this RestSchedule.

        The cron schedule for when the scan should be run  # noqa: E501

        :param cron: The cron of this RestSchedule.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def recipients(self):
        """Gets the recipients of this RestSchedule.  # noqa: E501

        The recipients that should receive the notification of the scan finish  # noqa: E501

        :return: The recipients of this RestSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this RestSchedule.

        The recipients that should receive the notification of the scan finish  # noqa: E501

        :param recipients: The recipients of this RestSchedule.  # noqa: E501
        :type: list[str]
        """

        self._recipients = recipients

    @property
    def timezone(self):
        """Gets the timezone of this RestSchedule.  # noqa: E501

        The timezone for the schedule  # noqa: E501

        :return: The timezone of this RestSchedule.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this RestSchedule.

        The timezone for the schedule  # noqa: E501

        :param timezone: The timezone of this RestSchedule.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this RestSchedule.  # noqa: E501

        The type of schedule. The values can be manual (no schedule)|hourly|daily|weekly|monthly  # noqa: E501

        :return: The type of this RestSchedule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestSchedule.

        The type of schedule. The values can be manual (no schedule)|hourly|daily|weekly|monthly  # noqa: E501

        :param type: The type of this RestSchedule.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def notify(self):
        """Gets the notify of this RestSchedule.  # noqa: E501

        Whether or not an email should be sent when the scan finishes  # noqa: E501

        :return: The notify of this RestSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this RestSchedule.

        Whether or not an email should be sent when the scan finishes  # noqa: E501

        :param notify: The notify of this RestSchedule.  # noqa: E501
        :type: bool
        """

        self._notify = notify

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
        if issubclass(RestSchedule, dict):
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
        if not isinstance(other, RestSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
