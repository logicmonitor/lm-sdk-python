# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.dynamic_column import DynamicColumn  # noqa: F401,E501
from logicmonitor_sdk.models.report_base import ReportBase  # noqa: F401,E501
from logicmonitor_sdk.models.report_recipient import ReportRecipient  # noqa: F401,E501


class AlertThresholdReport(ReportBase):
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
        'custom_report_type_id': 'int',
        'custom_report_type_name': 'str',
        'delivery': 'str',
        'description': 'str',
        'enable_view_as_other_user': 'bool',
        'format': 'str',
        'group_id': 'int',
        'id': 'int',
        'last_generate_on': 'int',
        'last_generate_pages': 'int',
        'last_generate_size': 'int',
        'lastmodify_user_id': 'int',
        'lastmodify_user_name': 'str',
        'name': 'str',
        'recipients': 'list[ReportRecipient]',
        'report_link_num': 'int',
        'schedule': 'str',
        'schedule_timezone': 'str',
        'type': 'str',
        'user_permission': 'str',
        'columns': 'list[DynamicColumn]',
        'data_point': 'str',
        'data_source_instance_name': 'str',
        'device_display_name': 'str',
        'exclude_global': 'object',
        'group_full_path': 'str',
        'sorted_by': 'str'
    }

    attribute_map = {
        'custom_report_type_id': 'customReportTypeId',
        'custom_report_type_name': 'customReportTypeName',
        'delivery': 'delivery',
        'description': 'description',
        'enable_view_as_other_user': 'enableViewAsOtherUser',
        'format': 'format',
        'group_id': 'groupId',
        'id': 'id',
        'last_generate_on': 'lastGenerateOn',
        'last_generate_pages': 'lastGeneratePages',
        'last_generate_size': 'lastGenerateSize',
        'lastmodify_user_id': 'lastmodifyUserId',
        'lastmodify_user_name': 'lastmodifyUserName',
        'name': 'name',
        'recipients': 'recipients',
        'report_link_num': 'reportLinkNum',
        'schedule': 'schedule',
        'schedule_timezone': 'scheduleTimezone',
        'type': 'type',
        'user_permission': 'userPermission',
        'columns': 'columns',
        'data_point': 'dataPoint',
        'data_source_instance_name': 'dataSourceInstanceName',
        'device_display_name': 'deviceDisplayName',
        'exclude_global': 'excludeGlobal',
        'group_full_path': 'groupFullPath',
        'sorted_by': 'sortedBy'
    }

    def __init__(self, custom_report_type_id=None, custom_report_type_name=None, delivery=None, description=None, enable_view_as_other_user=None, format=None, group_id=None, id=None, last_generate_on=None, last_generate_pages=None, last_generate_size=None, lastmodify_user_id=None, lastmodify_user_name=None, name=None, recipients=None, report_link_num=None, schedule=None, schedule_timezone=None, type=None, user_permission=None, columns=None, data_point=None, data_source_instance_name=None, device_display_name=None, exclude_global=None, group_full_path=None, sorted_by=None):  # noqa: E501
        """AlertThresholdReport - a model defined in Swagger"""  # noqa: E501

        self._custom_report_type_id = None
        self._custom_report_type_name = None
        self._delivery = None
        self._description = None
        self._enable_view_as_other_user = None
        self._format = None
        self._group_id = None
        self._id = None
        self._last_generate_on = None
        self._last_generate_pages = None
        self._last_generate_size = None
        self._lastmodify_user_id = None
        self._lastmodify_user_name = None
        self._name = None
        self._recipients = None
        self._report_link_num = None
        self._schedule = None
        self._schedule_timezone = None
        self._type = None
        self._user_permission = None
        self._columns = None
        self._data_point = None
        self._data_source_instance_name = None
        self._device_display_name = None
        self._exclude_global = None
        self._group_full_path = None
        self._sorted_by = None
        self.discriminator = None

        if custom_report_type_id is not None:
            self.custom_report_type_id = custom_report_type_id
        if custom_report_type_name is not None:
            self.custom_report_type_name = custom_report_type_name
        if delivery is not None:
            self.delivery = delivery
        if description is not None:
            self.description = description
        if enable_view_as_other_user is not None:
            self.enable_view_as_other_user = enable_view_as_other_user
        if format is not None:
            self.format = format
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if last_generate_on is not None:
            self.last_generate_on = last_generate_on
        if last_generate_pages is not None:
            self.last_generate_pages = last_generate_pages
        if last_generate_size is not None:
            self.last_generate_size = last_generate_size
        if lastmodify_user_id is not None:
            self.lastmodify_user_id = lastmodify_user_id
        if lastmodify_user_name is not None:
            self.lastmodify_user_name = lastmodify_user_name
        self.name = name
        if recipients is not None:
            self.recipients = recipients
        if report_link_num is not None:
            self.report_link_num = report_link_num
        if schedule is not None:
            self.schedule = schedule
        if schedule_timezone is not None:
            self.schedule_timezone = schedule_timezone
        self.type = type
        if user_permission is not None:
            self.user_permission = user_permission
        if columns is not None:
            self.columns = columns
        if data_point is not None:
            self.data_point = data_point
        if data_source_instance_name is not None:
            self.data_source_instance_name = data_source_instance_name
        if device_display_name is not None:
            self.device_display_name = device_display_name
        if exclude_global is not None:
            self.exclude_global = exclude_global
        if group_full_path is not None:
            self.group_full_path = group_full_path
        if sorted_by is not None:
            self.sorted_by = sorted_by

    @property
    def custom_report_type_id(self):
        """Gets the custom_report_type_id of this AlertThresholdReport.  # noqa: E501

        The id of the custom report template, if the report is a custom report. An id of 0 indicates that the report is not a custom report  # noqa: E501

        :return: The custom_report_type_id of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._custom_report_type_id

    @custom_report_type_id.setter
    def custom_report_type_id(self, custom_report_type_id):
        """Sets the custom_report_type_id of this AlertThresholdReport.

        The id of the custom report template, if the report is a custom report. An id of 0 indicates that the report is not a custom report  # noqa: E501

        :param custom_report_type_id: The custom_report_type_id of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._custom_report_type_id = custom_report_type_id

    @property
    def custom_report_type_name(self):
        """Gets the custom_report_type_name of this AlertThresholdReport.  # noqa: E501

        The name of the custom report template  # noqa: E501

        :return: The custom_report_type_name of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._custom_report_type_name

    @custom_report_type_name.setter
    def custom_report_type_name(self, custom_report_type_name):
        """Sets the custom_report_type_name of this AlertThresholdReport.

        The name of the custom report template  # noqa: E501

        :param custom_report_type_name: The custom_report_type_name of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._custom_report_type_name = custom_report_type_name

    @property
    def delivery(self):
        """Gets the delivery of this AlertThresholdReport.  # noqa: E501

        Whether or not the report is configured to be delivered via email. Acceptable values are: none, email  # noqa: E501

        :return: The delivery of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this AlertThresholdReport.

        Whether or not the report is configured to be delivered via email. Acceptable values are: none, email  # noqa: E501

        :param delivery: The delivery of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._delivery = delivery

    @property
    def description(self):
        """Gets the description of this AlertThresholdReport.  # noqa: E501

        The description of the report  # noqa: E501

        :return: The description of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertThresholdReport.

        The description of the report  # noqa: E501

        :param description: The description of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_view_as_other_user(self):
        """Gets the enable_view_as_other_user of this AlertThresholdReport.  # noqa: E501

        Whether or not other users are allowed to view the report as the user who last modified the report  # noqa: E501

        :return: The enable_view_as_other_user of this AlertThresholdReport.  # noqa: E501
        :rtype: bool
        """
        return self._enable_view_as_other_user

    @enable_view_as_other_user.setter
    def enable_view_as_other_user(self, enable_view_as_other_user):
        """Sets the enable_view_as_other_user of this AlertThresholdReport.

        Whether or not other users are allowed to view the report as the user who last modified the report  # noqa: E501

        :param enable_view_as_other_user: The enable_view_as_other_user of this AlertThresholdReport.  # noqa: E501
        :type: bool
        """

        self._enable_view_as_other_user = enable_view_as_other_user

    @property
    def format(self):
        """Gets the format of this AlertThresholdReport.  # noqa: E501

        The format of the report. Allowable values are: HTML, PDF, CSV, WORD  # noqa: E501

        :return: The format of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AlertThresholdReport.

        The format of the report. Allowable values are: HTML, PDF, CSV, WORD  # noqa: E501

        :param format: The format of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def group_id(self):
        """Gets the group_id of this AlertThresholdReport.  # noqa: E501

        The Id of the group the report is in, where Id=0 is the root report group  # noqa: E501

        :return: The group_id of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AlertThresholdReport.

        The Id of the group the report is in, where Id=0 is the root report group  # noqa: E501

        :param group_id: The group_id of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this AlertThresholdReport.  # noqa: E501

        The id of the report  # noqa: E501

        :return: The id of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertThresholdReport.

        The id of the report  # noqa: E501

        :param id: The id of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_generate_on(self):
        """Gets the last_generate_on of this AlertThresholdReport.  # noqa: E501

        The time, in epoch format, that the report was last generated  # noqa: E501

        :return: The last_generate_on of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_on

    @last_generate_on.setter
    def last_generate_on(self, last_generate_on):
        """Sets the last_generate_on of this AlertThresholdReport.

        The time, in epoch format, that the report was last generated  # noqa: E501

        :param last_generate_on: The last_generate_on of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._last_generate_on = last_generate_on

    @property
    def last_generate_pages(self):
        """Gets the last_generate_pages of this AlertThresholdReport.  # noqa: E501

        The number of pages in the report, the last time it was generated  # noqa: E501

        :return: The last_generate_pages of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_pages

    @last_generate_pages.setter
    def last_generate_pages(self, last_generate_pages):
        """Sets the last_generate_pages of this AlertThresholdReport.

        The number of pages in the report, the last time it was generated  # noqa: E501

        :param last_generate_pages: The last_generate_pages of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._last_generate_pages = last_generate_pages

    @property
    def last_generate_size(self):
        """Gets the last_generate_size of this AlertThresholdReport.  # noqa: E501

        The size of the report, in Bytes, the last time it was generated  # noqa: E501

        :return: The last_generate_size of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._last_generate_size

    @last_generate_size.setter
    def last_generate_size(self, last_generate_size):
        """Sets the last_generate_size of this AlertThresholdReport.

        The size of the report, in Bytes, the last time it was generated  # noqa: E501

        :param last_generate_size: The last_generate_size of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._last_generate_size = last_generate_size

    @property
    def lastmodify_user_id(self):
        """Gets the lastmodify_user_id of this AlertThresholdReport.  # noqa: E501

        The Id of the user that last modified the report  # noqa: E501

        :return: The lastmodify_user_id of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._lastmodify_user_id

    @lastmodify_user_id.setter
    def lastmodify_user_id(self, lastmodify_user_id):
        """Sets the lastmodify_user_id of this AlertThresholdReport.

        The Id of the user that last modified the report  # noqa: E501

        :param lastmodify_user_id: The lastmodify_user_id of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._lastmodify_user_id = lastmodify_user_id

    @property
    def lastmodify_user_name(self):
        """Gets the lastmodify_user_name of this AlertThresholdReport.  # noqa: E501

        The username of the user that last modified the report  # noqa: E501

        :return: The lastmodify_user_name of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._lastmodify_user_name

    @lastmodify_user_name.setter
    def lastmodify_user_name(self, lastmodify_user_name):
        """Sets the lastmodify_user_name of this AlertThresholdReport.

        The username of the user that last modified the report  # noqa: E501

        :param lastmodify_user_name: The lastmodify_user_name of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._lastmodify_user_name = lastmodify_user_name

    @property
    def name(self):
        """Gets the name of this AlertThresholdReport.  # noqa: E501

        The name of the report  # noqa: E501

        :return: The name of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertThresholdReport.

        The name of the report  # noqa: E501

        :param name: The name of this AlertThresholdReport.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def recipients(self):
        """Gets the recipients of this AlertThresholdReport.  # noqa: E501

        If the report is configured to be delivered via email, this object provides the recipients that the report will be delivered to  # noqa: E501

        :return: The recipients of this AlertThresholdReport.  # noqa: E501
        :rtype: list[ReportRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this AlertThresholdReport.

        If the report is configured to be delivered via email, this object provides the recipients that the report will be delivered to  # noqa: E501

        :param recipients: The recipients of this AlertThresholdReport.  # noqa: E501
        :type: list[ReportRecipient]
        """

        self._recipients = recipients

    @property
    def report_link_num(self):
        """Gets the report_link_num of this AlertThresholdReport.  # noqa: E501

        The number of links associated with the report, where each link corresponds to a generated report  # noqa: E501

        :return: The report_link_num of this AlertThresholdReport.  # noqa: E501
        :rtype: int
        """
        return self._report_link_num

    @report_link_num.setter
    def report_link_num(self, report_link_num):
        """Sets the report_link_num of this AlertThresholdReport.

        The number of links associated with the report, where each link corresponds to a generated report  # noqa: E501

        :param report_link_num: The report_link_num of this AlertThresholdReport.  # noqa: E501
        :type: int
        """

        self._report_link_num = report_link_num

    @property
    def schedule(self):
        """Gets the schedule of this AlertThresholdReport.  # noqa: E501

        A cron schedule that indicates when the report will be delivered via email  # noqa: E501

        :return: The schedule of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AlertThresholdReport.

        A cron schedule that indicates when the report will be delivered via email  # noqa: E501

        :param schedule: The schedule of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def schedule_timezone(self):
        """Gets the schedule_timezone of this AlertThresholdReport.  # noqa: E501

        The sepecific timezone for the scheduled report  # noqa: E501

        :return: The schedule_timezone of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._schedule_timezone

    @schedule_timezone.setter
    def schedule_timezone(self, schedule_timezone):
        """Sets the schedule_timezone of this AlertThresholdReport.

        The sepecific timezone for the scheduled report  # noqa: E501

        :param schedule_timezone: The schedule_timezone of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._schedule_timezone = schedule_timezone

    @property
    def type(self):
        """Gets the type of this AlertThresholdReport.  # noqa: E501

        The report type. Acceptable values are: Alert,Alert SLA,Alert threshold,Alert trends,Host CPU,Host group inventory,Host inventory,Host metric trends,Interfaces Bandwidth,Netflow device metric,Service Level Agreement,Website Service Overview,Word template,Audit Log,Alert Forecasting,Dashboard,Website SLA,User,Role  # noqa: E501

        :return: The type of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlertThresholdReport.

        The report type. Acceptable values are: Alert,Alert SLA,Alert threshold,Alert trends,Host CPU,Host group inventory,Host inventory,Host metric trends,Interfaces Bandwidth,Netflow device metric,Service Level Agreement,Website Service Overview,Word template,Audit Log,Alert Forecasting,Dashboard,Website SLA,User,Role  # noqa: E501

        :param type: The type of this AlertThresholdReport.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_permission(self):
        """Gets the user_permission of this AlertThresholdReport.  # noqa: E501

        The permissions associated with the user who made the API call  # noqa: E501

        :return: The user_permission of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this AlertThresholdReport.

        The permissions associated with the user who made the API call  # noqa: E501

        :param user_permission: The user_permission of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def columns(self):
        """Gets the columns of this AlertThresholdReport.  # noqa: E501

        The columns that will be displayed in the report. You should specify the columns in the order in which you'd like them to be displayed  # noqa: E501

        :return: The columns of this AlertThresholdReport.  # noqa: E501
        :rtype: list[DynamicColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this AlertThresholdReport.

        The columns that will be displayed in the report. You should specify the columns in the order in which you'd like them to be displayed  # noqa: E501

        :param columns: The columns of this AlertThresholdReport.  # noqa: E501
        :type: list[DynamicColumn]
        """

        self._columns = columns

    @property
    def data_point(self):
        """Gets the data_point of this AlertThresholdReport.  # noqa: E501

        The datapoint to be included in the report. Glob expressions supported  # noqa: E501

        :return: The data_point of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._data_point

    @data_point.setter
    def data_point(self, data_point):
        """Sets the data_point of this AlertThresholdReport.

        The datapoint to be included in the report. Glob expressions supported  # noqa: E501

        :param data_point: The data_point of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._data_point = data_point

    @property
    def data_source_instance_name(self):
        """Gets the data_source_instance_name of this AlertThresholdReport.  # noqa: E501

        The name of the datasource instance to be included in the report, where the syntax should be dataSourceDisplayName-InstanceName. If you're referencing a single instance datasource, you can just specify dataSourceDisplayName. Glob expressions supported  # noqa: E501

        :return: The data_source_instance_name of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._data_source_instance_name

    @data_source_instance_name.setter
    def data_source_instance_name(self, data_source_instance_name):
        """Sets the data_source_instance_name of this AlertThresholdReport.

        The name of the datasource instance to be included in the report, where the syntax should be dataSourceDisplayName-InstanceName. If you're referencing a single instance datasource, you can just specify dataSourceDisplayName. Glob expressions supported  # noqa: E501

        :param data_source_instance_name: The data_source_instance_name of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._data_source_instance_name = data_source_instance_name

    @property
    def device_display_name(self):
        """Gets the device_display_name of this AlertThresholdReport.  # noqa: E501

        The display name of the device(s) to be included in the report. Glob expressions supported  # noqa: E501

        :return: The device_display_name of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this AlertThresholdReport.

        The display name of the device(s) to be included in the report. Glob expressions supported  # noqa: E501

        :param device_display_name: The device_display_name of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

    @property
    def exclude_global(self):
        """Gets the exclude_global of this AlertThresholdReport.  # noqa: E501

        true: only variations from the global thresholds will be displayed false: all thresholds will be displayed, including global thresholds an custom group and instance level thresholds the default value is true  # noqa: E501

        :return: The exclude_global of this AlertThresholdReport.  # noqa: E501
        :rtype: object
        """
        return self._exclude_global

    @exclude_global.setter
    def exclude_global(self, exclude_global):
        """Sets the exclude_global of this AlertThresholdReport.

        true: only variations from the global thresholds will be displayed false: all thresholds will be displayed, including global thresholds an custom group and instance level thresholds the default value is true  # noqa: E501

        :param exclude_global: The exclude_global of this AlertThresholdReport.  # noqa: E501
        :type: object
        """

        self._exclude_global = exclude_global

    @property
    def group_full_path(self):
        """Gets the group_full_path of this AlertThresholdReport.  # noqa: E501

        The full path of the group whose member devices you are going to include in the report. Glob expressions supported  # noqa: E501

        :return: The group_full_path of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._group_full_path

    @group_full_path.setter
    def group_full_path(self, group_full_path):
        """Sets the group_full_path of this AlertThresholdReport.

        The full path of the group whose member devices you are going to include in the report. Glob expressions supported  # noqa: E501

        :param group_full_path: The group_full_path of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._group_full_path = group_full_path

    @property
    def sorted_by(self):
        """Gets the sorted_by of this AlertThresholdReport.  # noqa: E501

        host | datasource | datapoint host: displayed thresholds will be sorted by device datasource: displayed thresholds will be sorted by datasource instance datapoint: displayed thresholds will be sorted by datapoint (metric)  # noqa: E501

        :return: The sorted_by of this AlertThresholdReport.  # noqa: E501
        :rtype: str
        """
        return self._sorted_by

    @sorted_by.setter
    def sorted_by(self, sorted_by):
        """Sets the sorted_by of this AlertThresholdReport.

        host | datasource | datapoint host: displayed thresholds will be sorted by device datasource: displayed thresholds will be sorted by datasource instance datapoint: displayed thresholds will be sorted by datapoint (metric)  # noqa: E501

        :param sorted_by: The sorted_by of this AlertThresholdReport.  # noqa: E501
        :type: str
        """

        self._sorted_by = sorted_by

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
        if issubclass(AlertThresholdReport, dict):
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
        if not isinstance(other, AlertThresholdReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
