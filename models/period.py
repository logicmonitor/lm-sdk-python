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

class Period(object):
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
        'week_days': 'list[int]',
        'timezone': 'str',
        'start_minutes': 'int',
        'end_minutes': 'int'
    }

    attribute_map = {
        'week_days': 'weekDays',
        'timezone': 'timezone',
        'start_minutes': 'startMinutes',
        'end_minutes': 'endMinutes'
    }

    def __init__(self, week_days=None, timezone=None, start_minutes=None, end_minutes=None):  # noqa: E501
        """Period - a model defined in Swagger"""  # noqa: E501
        self._week_days = None
        self._timezone = None
        self._start_minutes = None
        self._end_minutes = None
        self.discriminator = None
        self.week_days = week_days
        self.timezone = timezone
        self.start_minutes = start_minutes
        self.end_minutes = end_minutes

    @property
    def week_days(self):
        """Gets the week_days of this Period.  # noqa: E501

        The list of week day of this period  # noqa: E501

        :return: The week_days of this Period.  # noqa: E501
        :rtype: list[int]
        """
        return self._week_days

    @week_days.setter
    def week_days(self, week_days):
        """Sets the week_days of this Period.

        The list of week day of this period  # noqa: E501

        :param week_days: The week_days of this Period.  # noqa: E501
        :type: list[int]
        """
        if week_days is None:
            raise ValueError("Invalid value for `week_days`, must not be `None`")  # noqa: E501

        self._week_days = week_days

    @property
    def timezone(self):
        """Gets the timezone of this Period.  # noqa: E501

        The timezone for this period  # noqa: E501

        :return: The timezone of this Period.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Period.

        The timezone for this period  # noqa: E501

        :param timezone: The timezone of this Period.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

    @property
    def start_minutes(self):
        """Gets the start_minutes of this Period.  # noqa: E501

        The start minute of this period  # noqa: E501

        :return: The start_minutes of this Period.  # noqa: E501
        :rtype: int
        """
        return self._start_minutes

    @start_minutes.setter
    def start_minutes(self, start_minutes):
        """Sets the start_minutes of this Period.

        The start minute of this period  # noqa: E501

        :param start_minutes: The start_minutes of this Period.  # noqa: E501
        :type: int
        """
        if start_minutes is None:
            raise ValueError("Invalid value for `start_minutes`, must not be `None`")  # noqa: E501

        self._start_minutes = start_minutes

    @property
    def end_minutes(self):
        """Gets the end_minutes of this Period.  # noqa: E501

        The end minute of this period  # noqa: E501

        :return: The end_minutes of this Period.  # noqa: E501
        :rtype: int
        """
        return self._end_minutes

    @end_minutes.setter
    def end_minutes(self, end_minutes):
        """Sets the end_minutes of this Period.

        The end minute of this period  # noqa: E501

        :param end_minutes: The end_minutes of this Period.  # noqa: E501
        :type: int
        """
        if end_minutes is None:
            raise ValueError("Invalid value for `end_minutes`, must not be `None`")  # noqa: E501

        self._end_minutes = end_minutes

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
        if issubclass(Period, dict):
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
        if not isinstance(other, Period):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
