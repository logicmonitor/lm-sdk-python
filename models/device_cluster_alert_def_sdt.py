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

from logicmonitor_sdk.models.sdt import SDT  # noqa: F401,E501


class DeviceClusterAlertDefSDT(SDT):
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
        'end_date_time_on_local': 'str',
        'timezone': 'str',
        'sdt_type': 'str',
        'month_day': 'int',
        'week_of_month': 'str',
        'admin': 'str',
        'end_date_time': 'int',
        'type': 'str',
        'is_effective': 'bool',
        'minute': 'int',
        'duration': 'int',
        'end_hour': 'int',
        'start_date_time': 'int',
        'hour': 'int',
        'start_date_time_on_local': 'str',
        'week_day': 'str',
        'comment': 'str',
        'id': 'str',
        'end_minute': 'int',
        'device_cluster_alert_def_id': 'int',
        'device_group_id': 'int',
        'data_source_name': 'str',
        'device_group_full_path': 'str'
    }

    attribute_map = {
        'end_date_time_on_local': 'endDateTimeOnLocal',
        'timezone': 'timezone',
        'sdt_type': 'sdtType',
        'month_day': 'monthDay',
        'week_of_month': 'weekOfMonth',
        'admin': 'admin',
        'end_date_time': 'endDateTime',
        'type': 'type',
        'is_effective': 'isEffective',
        'minute': 'minute',
        'duration': 'duration',
        'end_hour': 'endHour',
        'start_date_time': 'startDateTime',
        'hour': 'hour',
        'start_date_time_on_local': 'startDateTimeOnLocal',
        'week_day': 'weekDay',
        'comment': 'comment',
        'id': 'id',
        'end_minute': 'endMinute',
        'device_cluster_alert_def_id': 'deviceClusterAlertDefId',
        'device_group_id': 'deviceGroupId',
        'data_source_name': 'dataSourceName',
        'device_group_full_path': 'deviceGroupFullPath'
    }

    def __init__(self, end_date_time_on_local=None, timezone=None, sdt_type=None, month_day=None, week_of_month=None, admin=None, end_date_time=None, type=None, is_effective=None, minute=None, duration=None, end_hour=None, start_date_time=None, hour=None, start_date_time_on_local=None, week_day=None, comment=None, id=None, end_minute=None, device_cluster_alert_def_id=None, device_group_id=None, data_source_name=None, device_group_full_path=None):  # noqa: E501
        """DeviceClusterAlertDefSDT - a model defined in Swagger"""  # noqa: E501

        self._end_date_time_on_local = None
        self._timezone = None
        self._sdt_type = None
        self._month_day = None
        self._week_of_month = None
        self._admin = None
        self._end_date_time = None
        self._type = None
        self._is_effective = None
        self._minute = None
        self._duration = None
        self._end_hour = None
        self._start_date_time = None
        self._hour = None
        self._start_date_time_on_local = None
        self._week_day = None
        self._comment = None
        self._id = None
        self._end_minute = None
        self._device_cluster_alert_def_id = None
        self._device_group_id = None
        self._data_source_name = None
        self._device_group_full_path = None
        self.discriminator = None

        if end_date_time_on_local is not None:
            self.end_date_time_on_local = end_date_time_on_local
        if timezone is not None:
            self.timezone = timezone
        if sdt_type is not None:
            self.sdt_type = sdt_type
        if month_day is not None:
            self.month_day = month_day
        if week_of_month is not None:
            self.week_of_month = week_of_month
        if admin is not None:
            self.admin = admin
        if end_date_time is not None:
            self.end_date_time = end_date_time
        self.type = type
        if is_effective is not None:
            self.is_effective = is_effective
        if minute is not None:
            self.minute = minute
        if duration is not None:
            self.duration = duration
        if end_hour is not None:
            self.end_hour = end_hour
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if hour is not None:
            self.hour = hour
        if start_date_time_on_local is not None:
            self.start_date_time_on_local = start_date_time_on_local
        if week_day is not None:
            self.week_day = week_day
        if comment is not None:
            self.comment = comment
        if id is not None:
            self.id = id
        if end_minute is not None:
            self.end_minute = end_minute
        self.device_cluster_alert_def_id = device_cluster_alert_def_id
        if device_group_id is not None:
            self.device_group_id = device_group_id
        if data_source_name is not None:
            self.data_source_name = data_source_name
        if device_group_full_path is not None:
            self.device_group_full_path = device_group_full_path

    @property
    def end_date_time_on_local(self):
        """Gets the end_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501

        The date, time and time zone that the SDT will end at  # noqa: E501

        :return: The end_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._end_date_time_on_local

    @end_date_time_on_local.setter
    def end_date_time_on_local(self, end_date_time_on_local):
        """Sets the end_date_time_on_local of this DeviceClusterAlertDefSDT.

        The date, time and time zone that the SDT will end at  # noqa: E501

        :param end_date_time_on_local: The end_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._end_date_time_on_local = end_date_time_on_local

    @property
    def timezone(self):
        """Gets the timezone of this DeviceClusterAlertDefSDT.  # noqa: E501

        The specific timezone for SDT  # noqa: E501

        :return: The timezone of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DeviceClusterAlertDefSDT.

        The specific timezone for SDT  # noqa: E501

        :param timezone: The timezone of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def sdt_type(self):
        """Gets the sdt_type of this DeviceClusterAlertDefSDT.  # noqa: E501

        The type of sdt. The values can be oneTime|weekly|monthly|daily|monthlyByWeek  # noqa: E501

        :return: The sdt_type of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._sdt_type

    @sdt_type.setter
    def sdt_type(self, sdt_type):
        """Sets the sdt_type of this DeviceClusterAlertDefSDT.

        The type of sdt. The values can be oneTime|weekly|monthly|daily|monthlyByWeek  # noqa: E501

        :param sdt_type: The sdt_type of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._sdt_type = sdt_type

    @property
    def month_day(self):
        """Gets the month_day of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be 1 | 2....| 31. Specifies the day of the month that the SDT will be active for a monthly SDT  # noqa: E501

        :return: The month_day of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._month_day

    @month_day.setter
    def month_day(self, month_day):
        """Sets the month_day of this DeviceClusterAlertDefSDT.

        The values can be 1 | 2....| 31. Specifies the day of the month that the SDT will be active for a monthly SDT  # noqa: E501

        :param month_day: The month_day of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._month_day = month_day

    @property
    def week_of_month(self):
        """Gets the week_of_month of this DeviceClusterAlertDefSDT.  # noqa: E501

        The week of the month that the SDT will be active for a monthly SDT  # noqa: E501

        :return: The week_of_month of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._week_of_month

    @week_of_month.setter
    def week_of_month(self, week_of_month):
        """Sets the week_of_month of this DeviceClusterAlertDefSDT.

        The week of the month that the SDT will be active for a monthly SDT  # noqa: E501

        :param week_of_month: The week_of_month of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._week_of_month = week_of_month

    @property
    def admin(self):
        """Gets the admin of this DeviceClusterAlertDefSDT.  # noqa: E501

        The name of the user that created the SDT  # noqa: E501

        :return: The admin of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this DeviceClusterAlertDefSDT.

        The name of the user that created the SDT  # noqa: E501

        :param admin: The admin of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._admin = admin

    @property
    def end_date_time(self):
        """Gets the end_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501

        The epoch time, in milliseconds, that the SDT will end  # noqa: E501

        :return: The end_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this DeviceClusterAlertDefSDT.

        The epoch time, in milliseconds, that the SDT will end  # noqa: E501

        :param end_date_time: The end_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._end_date_time = end_date_time

    @property
    def type(self):
        """Gets the type of this DeviceClusterAlertDefSDT.  # noqa: E501

        The type of resource that this SDT is for. The values can be CollectorSDT | DeviceDataSourceInstanceSDT | DeviceBatchJobSDT | DeviceClusterAlertDefSDT | DeviceDataSourceInstanceGroupSDT | DeviceDataSourceSDT | DeviceEventSourceSDT | ResourceGroupSDT | ResourceSDT | WebsiteCheckpointSDT | WebsiteGroupSDT | WebsiteSDT | DeviceLogPipeLineResourceSDT  # noqa: E501

        :return: The type of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceClusterAlertDefSDT.

        The type of resource that this SDT is for. The values can be CollectorSDT | DeviceDataSourceInstanceSDT | DeviceBatchJobSDT | DeviceClusterAlertDefSDT | DeviceDataSourceInstanceGroupSDT | DeviceDataSourceSDT | DeviceEventSourceSDT | ResourceGroupSDT | ResourceSDT | WebsiteCheckpointSDT | WebsiteGroupSDT | WebsiteSDT | DeviceLogPipeLineResourceSDT  # noqa: E501

        :param type: The type of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def is_effective(self):
        """Gets the is_effective of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be true|false, where true: the SDT is currently active false: the SDT is currently inactive  # noqa: E501

        :return: The is_effective of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: bool
        """
        return self._is_effective

    @is_effective.setter
    def is_effective(self, is_effective):
        """Sets the is_effective of this DeviceClusterAlertDefSDT.

        The values can be true|false, where true: the SDT is currently active false: the SDT is currently inactive  # noqa: E501

        :param is_effective: The is_effective of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: bool
        """

        self._is_effective = is_effective

    @property
    def minute(self):
        """Gets the minute of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT should begin for a repeating SDT  # noqa: E501

        :return: The minute of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Sets the minute of this DeviceClusterAlertDefSDT.

        The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT should begin for a repeating SDT  # noqa: E501

        :param minute: The minute of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._minute = minute

    @property
    def duration(self):
        """Gets the duration of this DeviceClusterAlertDefSDT.  # noqa: E501

        The duration of the SDT in minutes  # noqa: E501

        :return: The duration of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DeviceClusterAlertDefSDT.

        The duration of the SDT in minutes  # noqa: E501

        :param duration: The duration of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def end_hour(self):
        """Gets the end_hour of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be 1 | 2....| 24. Specifies the hour that the SDT ends for a repeating SDT  # noqa: E501

        :return: The end_hour of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        """Sets the end_hour of this DeviceClusterAlertDefSDT.

        The values can be 1 | 2....| 24. Specifies the hour that the SDT ends for a repeating SDT  # noqa: E501

        :param end_hour: The end_hour of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._end_hour = end_hour

    @property
    def start_date_time(self):
        """Gets the start_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501

        The epoch time, in milliseconds, that the SDT will start  # noqa: E501

        :return: The start_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this DeviceClusterAlertDefSDT.

        The epoch time, in milliseconds, that the SDT will start  # noqa: E501

        :param start_date_time: The start_date_time of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._start_date_time = start_date_time

    @property
    def hour(self):
        """Gets the hour of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be 1 | 2....| 24. Specifies the hour that the SDT will start for a repeating SDT (daily, weekly, or monthly)  # noqa: E501

        :return: The hour of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Sets the hour of this DeviceClusterAlertDefSDT.

        The values can be 1 | 2....| 24. Specifies the hour that the SDT will start for a repeating SDT (daily, weekly, or monthly)  # noqa: E501

        :param hour: The hour of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._hour = hour

    @property
    def start_date_time_on_local(self):
        """Gets the start_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501

        The date, time and time zone that the SDT will end at  # noqa: E501

        :return: The start_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._start_date_time_on_local

    @start_date_time_on_local.setter
    def start_date_time_on_local(self, start_date_time_on_local):
        """Sets the start_date_time_on_local of this DeviceClusterAlertDefSDT.

        The date, time and time zone that the SDT will end at  # noqa: E501

        :param start_date_time_on_local: The start_date_time_on_local of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._start_date_time_on_local = start_date_time_on_local

    @property
    def week_day(self):
        """Gets the week_day of this DeviceClusterAlertDefSDT.  # noqa: E501

        The week day of sdt. The values can be SUNDAY|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY  # noqa: E501

        :return: The week_day of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        """Sets the week_day of this DeviceClusterAlertDefSDT.

        The week day of sdt. The values can be SUNDAY|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY  # noqa: E501

        :param week_day: The week_day of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._week_day = week_day

    @property
    def comment(self):
        """Gets the comment of this DeviceClusterAlertDefSDT.  # noqa: E501

        The notes associated with the SDT  # noqa: E501

        :return: The comment of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DeviceClusterAlertDefSDT.

        The notes associated with the SDT  # noqa: E501

        :param comment: The comment of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def id(self):
        """Gets the id of this DeviceClusterAlertDefSDT.  # noqa: E501

        The Id of the SDT. This value will be in the following format \"XX_##\" where XX will refer to the type of SDT and ## will refer to the number of SDTs of that type  # noqa: E501

        :return: The id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceClusterAlertDefSDT.

        The Id of the SDT. This value will be in the following format \"XX_##\" where XX will refer to the type of SDT and ## will refer to the number of SDTs of that type  # noqa: E501

        :param id: The id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def end_minute(self):
        """Gets the end_minute of this DeviceClusterAlertDefSDT.  # noqa: E501

        The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT ends for a repeating SDT  # noqa: E501

        :return: The end_minute of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._end_minute

    @end_minute.setter
    def end_minute(self, end_minute):
        """Sets the end_minute of this DeviceClusterAlertDefSDT.

        The values can be 1 | 2....| 60. Specifies the minute of the hour that the SDT ends for a repeating SDT  # noqa: E501

        :param end_minute: The end_minute of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._end_minute = end_minute

    @property
    def device_cluster_alert_def_id(self):
        """Gets the device_cluster_alert_def_id of this DeviceClusterAlertDefSDT.  # noqa: E501


        :return: The device_cluster_alert_def_id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._device_cluster_alert_def_id

    @device_cluster_alert_def_id.setter
    def device_cluster_alert_def_id(self, device_cluster_alert_def_id):
        """Sets the device_cluster_alert_def_id of this DeviceClusterAlertDefSDT.


        :param device_cluster_alert_def_id: The device_cluster_alert_def_id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """
        if device_cluster_alert_def_id is None:
            raise ValueError("Invalid value for `device_cluster_alert_def_id`, must not be `None`")  # noqa: E501

        self._device_cluster_alert_def_id = device_cluster_alert_def_id

    @property
    def device_group_id(self):
        """Gets the device_group_id of this DeviceClusterAlertDefSDT.  # noqa: E501


        :return: The device_group_id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: int
        """
        return self._device_group_id

    @device_group_id.setter
    def device_group_id(self, device_group_id):
        """Sets the device_group_id of this DeviceClusterAlertDefSDT.


        :param device_group_id: The device_group_id of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: int
        """

        self._device_group_id = device_group_id

    @property
    def data_source_name(self):
        """Gets the data_source_name of this DeviceClusterAlertDefSDT.  # noqa: E501


        :return: The data_source_name of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this DeviceClusterAlertDefSDT.


        :param data_source_name: The data_source_name of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._data_source_name = data_source_name

    @property
    def device_group_full_path(self):
        """Gets the device_group_full_path of this DeviceClusterAlertDefSDT.  # noqa: E501


        :return: The device_group_full_path of this DeviceClusterAlertDefSDT.  # noqa: E501
        :rtype: str
        """
        return self._device_group_full_path

    @device_group_full_path.setter
    def device_group_full_path(self, device_group_full_path):
        """Sets the device_group_full_path of this DeviceClusterAlertDefSDT.


        :param device_group_full_path: The device_group_full_path of this DeviceClusterAlertDefSDT.  # noqa: E501
        :type: str
        """

        self._device_group_full_path = device_group_full_path

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
        if issubclass(DeviceClusterAlertDefSDT, dict):
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
        if not isinstance(other, DeviceClusterAlertDefSDT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
