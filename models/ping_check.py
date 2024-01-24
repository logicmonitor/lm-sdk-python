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

from logicmonitor_sdk.models.name_and_value import NameAndValue  # noqa: F401,E501
from logicmonitor_sdk.models.web_check_step import WebCheckStep  # noqa: F401,E501
from logicmonitor_sdk.models.website import Website  # noqa: F401,E501
from logicmonitor_sdk.models.website_check_point import WebsiteCheckPoint  # noqa: F401,E501
from logicmonitor_sdk.models.website_collector_info import WebsiteCollectorInfo  # noqa: F401,E501
from logicmonitor_sdk.models.website_location import WebsiteLocation  # noqa: F401,E501


class PingCheck(Website):
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
        'template': 'object',
        'test_location': 'WebsiteLocation',
        'group_id': 'int',
        'overall_alert_level': 'str',
        'polling_interval': 'int',
        'description': 'str',
        'disable_alerting': 'bool',
        'type': 'str',
        'role_privileges': 'list[str]',
        'last_updated': 'int',
        'stop_monitoring_by_folder': 'bool',
        'id': 'int',
        'stop_monitoring': 'bool',
        'user_permission': 'str',
        'individual_sm_alert_enable': 'bool',
        'checkpoints': 'list[WebsiteCheckPoint]',
        'steps': 'list[WebCheckStep]',
        'transition': 'int',
        'global_sm_alert_cond': 'int',
        'is_internal': 'bool',
        'collectors': 'list[WebsiteCollectorInfo]',
        'domain': 'str',
        'name': 'str',
        'use_default_location_setting': 'bool',
        'use_default_alert_setting': 'bool',
        'individual_alert_level': 'str',
        'properties': 'list[NameAndValue]',
        'status': 'str',
        'percent_pkts_not_receive_in_time': 'int',
        'count': 'int',
        'host': 'str',
        'timeout_in_ms_pkts_not_receive': 'int'
    }

    attribute_map = {
        'template': 'template',
        'test_location': 'testLocation',
        'group_id': 'groupId',
        'overall_alert_level': 'overallAlertLevel',
        'polling_interval': 'pollingInterval',
        'description': 'description',
        'disable_alerting': 'disableAlerting',
        'type': 'type',
        'role_privileges': 'rolePrivileges',
        'last_updated': 'lastUpdated',
        'stop_monitoring_by_folder': 'stopMonitoringByFolder',
        'id': 'id',
        'stop_monitoring': 'stopMonitoring',
        'user_permission': 'userPermission',
        'individual_sm_alert_enable': 'individualSmAlertEnable',
        'checkpoints': 'checkpoints',
        'steps': 'steps',
        'transition': 'transition',
        'global_sm_alert_cond': 'globalSmAlertCond',
        'is_internal': 'isInternal',
        'collectors': 'collectors',
        'domain': 'domain',
        'name': 'name',
        'use_default_location_setting': 'useDefaultLocationSetting',
        'use_default_alert_setting': 'useDefaultAlertSetting',
        'individual_alert_level': 'individualAlertLevel',
        'properties': 'properties',
        'status': 'status',
        'percent_pkts_not_receive_in_time': 'percentPktsNotReceiveInTime',
        'count': 'count',
        'host': 'host',
        'timeout_in_ms_pkts_not_receive': 'timeoutInMSPktsNotReceive'
    }

    def __init__(self, template=None, test_location=None, group_id=None, overall_alert_level=None, polling_interval=None, description=None, disable_alerting=None, type=None, role_privileges=None, last_updated=None, stop_monitoring_by_folder=None, id=None, stop_monitoring=None, user_permission=None, individual_sm_alert_enable=None, checkpoints=None, steps=None, transition=None, global_sm_alert_cond=None, is_internal=None, collectors=None, domain=None, name=None, use_default_location_setting=None, use_default_alert_setting=None, individual_alert_level=None, properties=None, status=None, percent_pkts_not_receive_in_time=None, count=None, host=None, timeout_in_ms_pkts_not_receive=None):  # noqa: E501
        """PingCheck - a model defined in Swagger"""  # noqa: E501

        self._template = None
        self._test_location = None
        self._group_id = None
        self._overall_alert_level = None
        self._polling_interval = None
        self._description = None
        self._disable_alerting = None
        self._type = None
        self._role_privileges = None
        self._last_updated = None
        self._stop_monitoring_by_folder = None
        self._id = None
        self._stop_monitoring = None
        self._user_permission = None
        self._individual_sm_alert_enable = None
        self._checkpoints = None
        self._steps = None
        self._transition = None
        self._global_sm_alert_cond = None
        self._is_internal = None
        self._collectors = None
        self._domain = None
        self._name = None
        self._use_default_location_setting = None
        self._use_default_alert_setting = None
        self._individual_alert_level = None
        self._properties = None
        self._status = None
        self._percent_pkts_not_receive_in_time = None
        self._count = None
        self._host = None
        self._timeout_in_ms_pkts_not_receive = None
        self.discriminator = None

        if template is not None:
            self.template = template
        self.test_location = test_location
        if group_id is not None:
            self.group_id = group_id
        if overall_alert_level is not None:
            self.overall_alert_level = overall_alert_level
        if polling_interval is not None:
            self.polling_interval = polling_interval
        if description is not None:
            self.description = description
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        self.type = type
        if role_privileges is not None:
            self.role_privileges = role_privileges
        if last_updated is not None:
            self.last_updated = last_updated
        if stop_monitoring_by_folder is not None:
            self.stop_monitoring_by_folder = stop_monitoring_by_folder
        if id is not None:
            self.id = id
        if stop_monitoring is not None:
            self.stop_monitoring = stop_monitoring
        if user_permission is not None:
            self.user_permission = user_permission
        if individual_sm_alert_enable is not None:
            self.individual_sm_alert_enable = individual_sm_alert_enable
        if checkpoints is not None:
            self.checkpoints = checkpoints
        if steps is not None:
            self.steps = steps
        if transition is not None:
            self.transition = transition
        if global_sm_alert_cond is not None:
            self.global_sm_alert_cond = global_sm_alert_cond
        if is_internal is not None:
            self.is_internal = is_internal
        if collectors is not None:
            self.collectors = collectors
        if domain is not None:
            self.domain = domain
        self.name = name
        if use_default_location_setting is not None:
            self.use_default_location_setting = use_default_location_setting
        if use_default_alert_setting is not None:
            self.use_default_alert_setting = use_default_alert_setting
        if individual_alert_level is not None:
            self.individual_alert_level = individual_alert_level
        if properties is not None:
            self.properties = properties
        if status is not None:
            self.status = status
        if percent_pkts_not_receive_in_time is not None:
            self.percent_pkts_not_receive_in_time = percent_pkts_not_receive_in_time
        if count is not None:
            self.count = count
        self.host = host
        if timeout_in_ms_pkts_not_receive is not None:
            self.timeout_in_ms_pkts_not_receive = timeout_in_ms_pkts_not_receive

    @property
    def template(self):
        """Gets the template of this PingCheck.  # noqa: E501

        The website template  # noqa: E501

        :return: The template of this PingCheck.  # noqa: E501
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this PingCheck.

        The website template  # noqa: E501

        :param template: The template of this PingCheck.  # noqa: E501
        :type: object
        """

        self._template = template

    @property
    def test_location(self):
        """Gets the test_location of this PingCheck.  # noqa: E501

        The locations from which the website is monitored. If the website is internal, this field should include Collectors. If Non-Internal, possible test locations are: 1 : US - LA 2 : US - DC 3 : US - SF 4 : Europe - Dublin 5 : Asia - Singapore 6 : Australia - Sydney testLocation:\"{all:true}\" indicates that the service will be monitored from all checkpoint locations testLocation:\"{smgIds:[1,2,3]}\" indicates that the service will be monitored from checkpoint locations 1, 2 and 3 testLocation:\"{collectorIds:[85,90]}\" indicates that the service will be monitored by Collectors 85 and 90  # noqa: E501

        :return: The test_location of this PingCheck.  # noqa: E501
        :rtype: WebsiteLocation
        """
        return self._test_location

    @test_location.setter
    def test_location(self, test_location):
        """Sets the test_location of this PingCheck.

        The locations from which the website is monitored. If the website is internal, this field should include Collectors. If Non-Internal, possible test locations are: 1 : US - LA 2 : US - DC 3 : US - SF 4 : Europe - Dublin 5 : Asia - Singapore 6 : Australia - Sydney testLocation:\"{all:true}\" indicates that the service will be monitored from all checkpoint locations testLocation:\"{smgIds:[1,2,3]}\" indicates that the service will be monitored from checkpoint locations 1, 2 and 3 testLocation:\"{collectorIds:[85,90]}\" indicates that the service will be monitored by Collectors 85 and 90  # noqa: E501

        :param test_location: The test_location of this PingCheck.  # noqa: E501
        :type: WebsiteLocation
        """
        if test_location is None:
            raise ValueError("Invalid value for `test_location`, must not be `None`")  # noqa: E501

        self._test_location = test_location

    @property
    def group_id(self):
        """Gets the group_id of this PingCheck.  # noqa: E501

        The id of the group the website is in  # noqa: E501

        :return: The group_id of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this PingCheck.

        The id of the group the website is in  # noqa: E501

        :param group_id: The group_id of this PingCheck.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def overall_alert_level(self):
        """Gets the overall_alert_level of this PingCheck.  # noqa: E501

        The values can be warn|error|critical The level of alert to trigger if the website fails the number of checks specified by transition from the test locations specified by globalSmAlertCond  # noqa: E501

        :return: The overall_alert_level of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._overall_alert_level

    @overall_alert_level.setter
    def overall_alert_level(self, overall_alert_level):
        """Sets the overall_alert_level of this PingCheck.

        The values can be warn|error|critical The level of alert to trigger if the website fails the number of checks specified by transition from the test locations specified by globalSmAlertCond  # noqa: E501

        :param overall_alert_level: The overall_alert_level of this PingCheck.  # noqa: E501
        :type: str
        """

        self._overall_alert_level = overall_alert_level

    @property
    def polling_interval(self):
        """Gets the polling_interval of this PingCheck.  # noqa: E501

        The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 The polling interval for the website, in units of minutes. This value indicates how often the website is checked. The minimum is 1 minute, and the maximum is 10 minutes  # noqa: E501

        :return: The polling_interval of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this PingCheck.

        The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 The polling interval for the website, in units of minutes. This value indicates how often the website is checked. The minimum is 1 minute, and the maximum is 10 minutes  # noqa: E501

        :param polling_interval: The polling_interval of this PingCheck.  # noqa: E501
        :type: int
        """

        self._polling_interval = polling_interval

    @property
    def description(self):
        """Gets the description of this PingCheck.  # noqa: E501

        The description of the website  # noqa: E501

        :return: The description of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PingCheck.

        The description of the website  # noqa: E501

        :param description: The description of this PingCheck.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this PingCheck.  # noqa: E501

        The values can be true|false where true: alerting is disabled for the website false: alerting is enabled for the website If stopMonitoring=true, then alerting will also be disabled by default for the website  # noqa: E501

        :return: The disable_alerting of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this PingCheck.

        The values can be true|false where true: alerting is disabled for the website false: alerting is enabled for the website If stopMonitoring=true, then alerting will also be disabled by default for the website  # noqa: E501

        :param disable_alerting: The disable_alerting of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def type(self):
        """Gets the type of this PingCheck.  # noqa: E501

        The values can be pingcheck|webcheck Specifies the type of service  # noqa: E501

        :return: The type of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PingCheck.

        The values can be pingcheck|webcheck Specifies the type of service  # noqa: E501

        :param type: The type of this PingCheck.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def role_privileges(self):
        """Gets the role_privileges of this PingCheck.  # noqa: E501

        The role privilege operation(s) for this website that are granted to the user who made the API request  # noqa: E501

        :return: The role_privileges of this PingCheck.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_privileges

    @role_privileges.setter
    def role_privileges(self, role_privileges):
        """Sets the role_privileges of this PingCheck.

        The role privilege operation(s) for this website that are granted to the user who made the API request  # noqa: E501

        :param role_privileges: The role_privileges of this PingCheck.  # noqa: E501
        :type: list[str]
        """

        self._role_privileges = role_privileges

    @property
    def last_updated(self):
        """Gets the last_updated of this PingCheck.  # noqa: E501

        The time (in epoch format) that the website was updated  # noqa: E501

        :return: The last_updated of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this PingCheck.

        The time (in epoch format) that the website was updated  # noqa: E501

        :param last_updated: The last_updated of this PingCheck.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def stop_monitoring_by_folder(self):
        """Gets the stop_monitoring_by_folder of this PingCheck.  # noqa: E501

        The values can be true|false where true: monitoring is disabled for all services in the website's folder false: monitoring is not disabled for all services in website's folder  # noqa: E501

        :return: The stop_monitoring_by_folder of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._stop_monitoring_by_folder

    @stop_monitoring_by_folder.setter
    def stop_monitoring_by_folder(self, stop_monitoring_by_folder):
        """Sets the stop_monitoring_by_folder of this PingCheck.

        The values can be true|false where true: monitoring is disabled for all services in the website's folder false: monitoring is not disabled for all services in website's folder  # noqa: E501

        :param stop_monitoring_by_folder: The stop_monitoring_by_folder of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._stop_monitoring_by_folder = stop_monitoring_by_folder

    @property
    def id(self):
        """Gets the id of this PingCheck.  # noqa: E501

        The id of the website  # noqa: E501

        :return: The id of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PingCheck.

        The id of the website  # noqa: E501

        :param id: The id of this PingCheck.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def stop_monitoring(self):
        """Gets the stop_monitoring of this PingCheck.  # noqa: E501

        The values can be true|false where true: monitoring is disabled for the website false: monitoring is enabled for the website If stopMonitoring=true, then alerting will also be disabled by default for the website  # noqa: E501

        :return: The stop_monitoring of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """Sets the stop_monitoring of this PingCheck.

        The values can be true|false where true: monitoring is disabled for the website false: monitoring is enabled for the website If stopMonitoring=true, then alerting will also be disabled by default for the website  # noqa: E501

        :param stop_monitoring: The stop_monitoring of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._stop_monitoring = stop_monitoring

    @property
    def user_permission(self):
        """Gets the user_permission of this PingCheck.  # noqa: E501

        The values can be write|read|ack. The permission level of the user that made the API request  # noqa: E501

        :return: The user_permission of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this PingCheck.

        The values can be write|read|ack. The permission level of the user that made the API request  # noqa: E501

        :param user_permission: The user_permission of this PingCheck.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def individual_sm_alert_enable(self):
        """Gets the individual_sm_alert_enable of this PingCheck.  # noqa: E501

        The values can be true|false where true: an alert will be triggered if a check fails from an individual test location false: an alert will not be triggered if a check fails from an individual test location  # noqa: E501

        :return: The individual_sm_alert_enable of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._individual_sm_alert_enable

    @individual_sm_alert_enable.setter
    def individual_sm_alert_enable(self, individual_sm_alert_enable):
        """Sets the individual_sm_alert_enable of this PingCheck.

        The values can be true|false where true: an alert will be triggered if a check fails from an individual test location false: an alert will not be triggered if a check fails from an individual test location  # noqa: E501

        :param individual_sm_alert_enable: The individual_sm_alert_enable of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._individual_sm_alert_enable = individual_sm_alert_enable

    @property
    def checkpoints(self):
        """Gets the checkpoints of this PingCheck.  # noqa: E501

        The checkpoints from the which the website is monitored. This object should reference each location specified in testLocation in addition to an 'Overall' checkpoint  # noqa: E501

        :return: The checkpoints of this PingCheck.  # noqa: E501
        :rtype: list[WebsiteCheckPoint]
        """
        return self._checkpoints

    @checkpoints.setter
    def checkpoints(self, checkpoints):
        """Sets the checkpoints of this PingCheck.

        The checkpoints from the which the website is monitored. This object should reference each location specified in testLocation in addition to an 'Overall' checkpoint  # noqa: E501

        :param checkpoints: The checkpoints of this PingCheck.  # noqa: E501
        :type: list[WebsiteCheckPoint]
        """

        self._checkpoints = checkpoints

    @property
    def steps(self):
        """Gets the steps of this PingCheck.  # noqa: E501

        Required for type=webcheck , An object comprising one or more steps, see the table below for the properties included in each step  # noqa: E501

        :return: The steps of this PingCheck.  # noqa: E501
        :rtype: list[WebCheckStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this PingCheck.

        Required for type=webcheck , An object comprising one or more steps, see the table below for the properties included in each step  # noqa: E501

        :param steps: The steps of this PingCheck.  # noqa: E501
        :type: list[WebCheckStep]
        """

        self._steps = steps

    @property
    def transition(self):
        """Gets the transition of this PingCheck.  # noqa: E501

        The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 30 | 60 The number of checks that must fail before an alert is triggered  # noqa: E501

        :return: The transition of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._transition

    @transition.setter
    def transition(self, transition):
        """Sets the transition of this PingCheck.

        The values can be 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 30 | 60 The number of checks that must fail before an alert is triggered  # noqa: E501

        :param transition: The transition of this PingCheck.  # noqa: E501
        :type: int
        """

        self._transition = transition

    @property
    def global_sm_alert_cond(self):
        """Gets the global_sm_alert_cond of this PingCheck.  # noqa: E501

        The number of test locations that checks must fail at to trigger an alert, where the alert triggered will be consistent with the value of overallAlertLevel. Possible values and corresponding number of Site Monitor locations are 0 : all 1 : half 2 : more than one 3 : any  # noqa: E501

        :return: The global_sm_alert_cond of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._global_sm_alert_cond

    @global_sm_alert_cond.setter
    def global_sm_alert_cond(self, global_sm_alert_cond):
        """Sets the global_sm_alert_cond of this PingCheck.

        The number of test locations that checks must fail at to trigger an alert, where the alert triggered will be consistent with the value of overallAlertLevel. Possible values and corresponding number of Site Monitor locations are 0 : all 1 : half 2 : more than one 3 : any  # noqa: E501

        :param global_sm_alert_cond: The global_sm_alert_cond of this PingCheck.  # noqa: E501
        :type: int
        """

        self._global_sm_alert_cond = global_sm_alert_cond

    @property
    def is_internal(self):
        """Gets the is_internal of this PingCheck.  # noqa: E501

        Whether or not the website is internal  # noqa: E501

        :return: The is_internal of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this PingCheck.

        Whether or not the website is internal  # noqa: E501

        :param is_internal: The is_internal of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._is_internal = is_internal

    @property
    def collectors(self):
        """Gets the collectors of this PingCheck.  # noqa: E501

        The collectors that are monitoring the website, if the website is internal  # noqa: E501

        :return: The collectors of this PingCheck.  # noqa: E501
        :rtype: list[WebsiteCollectorInfo]
        """
        return self._collectors

    @collectors.setter
    def collectors(self, collectors):
        """Sets the collectors of this PingCheck.

        The collectors that are monitoring the website, if the website is internal  # noqa: E501

        :param collectors: The collectors of this PingCheck.  # noqa: E501
        :type: list[WebsiteCollectorInfo]
        """

        self._collectors = collectors

    @property
    def domain(self):
        """Gets the domain of this PingCheck.  # noqa: E501

        Required for type=webcheck , The domain of the service. This is the base URL of the service  # noqa: E501

        :return: The domain of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PingCheck.

        Required for type=webcheck , The domain of the service. This is the base URL of the service  # noqa: E501

        :param domain: The domain of this PingCheck.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def name(self):
        """Gets the name of this PingCheck.  # noqa: E501

        The name of the website  # noqa: E501

        :return: The name of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PingCheck.

        The name of the website  # noqa: E501

        :param name: The name of this PingCheck.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def use_default_location_setting(self):
        """Gets the use_default_location_setting of this PingCheck.  # noqa: E501

        The values can be true|false where true: The checkpoint locations configured in the website Default Settings will be used false: The checkpoint locations specified in the testLocation will be used  # noqa: E501

        :return: The use_default_location_setting of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_location_setting

    @use_default_location_setting.setter
    def use_default_location_setting(self, use_default_location_setting):
        """Sets the use_default_location_setting of this PingCheck.

        The values can be true|false where true: The checkpoint locations configured in the website Default Settings will be used false: The checkpoint locations specified in the testLocation will be used  # noqa: E501

        :param use_default_location_setting: The use_default_location_setting of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._use_default_location_setting = use_default_location_setting

    @property
    def use_default_alert_setting(self):
        """Gets the use_default_alert_setting of this PingCheck.  # noqa: E501

        The values can be true|false where true: The alert settings configured in the website Default Settings will be used false: Service Default Settings will not be used, and you will need to specify individualSMAlertEnable, individualAlertLevel, globalSmAlertConf, overallAlertLevel and pollingInterval  # noqa: E501

        :return: The use_default_alert_setting of this PingCheck.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_alert_setting

    @use_default_alert_setting.setter
    def use_default_alert_setting(self, use_default_alert_setting):
        """Sets the use_default_alert_setting of this PingCheck.

        The values can be true|false where true: The alert settings configured in the website Default Settings will be used false: Service Default Settings will not be used, and you will need to specify individualSMAlertEnable, individualAlertLevel, globalSmAlertConf, overallAlertLevel and pollingInterval  # noqa: E501

        :param use_default_alert_setting: The use_default_alert_setting of this PingCheck.  # noqa: E501
        :type: bool
        """

        self._use_default_alert_setting = use_default_alert_setting

    @property
    def individual_alert_level(self):
        """Gets the individual_alert_level of this PingCheck.  # noqa: E501

        The values can be warn|error|critical The level of alert to trigger if the website fails a check from an individual test location  # noqa: E501

        :return: The individual_alert_level of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._individual_alert_level

    @individual_alert_level.setter
    def individual_alert_level(self, individual_alert_level):
        """Sets the individual_alert_level of this PingCheck.

        The values can be warn|error|critical The level of alert to trigger if the website fails a check from an individual test location  # noqa: E501

        :param individual_alert_level: The individual_alert_level of this PingCheck.  # noqa: E501
        :type: str
        """

        self._individual_alert_level = individual_alert_level

    @property
    def properties(self):
        """Gets the properties of this PingCheck.  # noqa: E501

        The properties associated with the website  # noqa: E501

        :return: The properties of this PingCheck.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PingCheck.

        The properties associated with the website  # noqa: E501

        :param properties: The properties of this PingCheck.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._properties = properties

    @property
    def status(self):
        """Gets the status of this PingCheck.  # noqa: E501

        Whether the website is dead (the collector is down) or not  # noqa: E501

        :return: The status of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PingCheck.

        Whether the website is dead (the collector is down) or not  # noqa: E501

        :param status: The status of this PingCheck.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def percent_pkts_not_receive_in_time(self):
        """Gets the percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501

        The percentage of packets that should be returned in the time period specified by timeoutInMSPktsNotReceive for each ping check  # noqa: E501

        :return: The percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._percent_pkts_not_receive_in_time

    @percent_pkts_not_receive_in_time.setter
    def percent_pkts_not_receive_in_time(self, percent_pkts_not_receive_in_time):
        """Sets the percent_pkts_not_receive_in_time of this PingCheck.

        The percentage of packets that should be returned in the time period specified by timeoutInMSPktsNotReceive for each ping check  # noqa: E501

        :param percent_pkts_not_receive_in_time: The percent_pkts_not_receive_in_time of this PingCheck.  # noqa: E501
        :type: int
        """

        self._percent_pkts_not_receive_in_time = percent_pkts_not_receive_in_time

    @property
    def count(self):
        """Gets the count of this PingCheck.  # noqa: E501

        The number of packets to send  # noqa: E501

        :return: The count of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PingCheck.

        The number of packets to send  # noqa: E501

        :param count: The count of this PingCheck.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def host(self):
        """Gets the host of this PingCheck.  # noqa: E501

        The URL to check, without the scheme or protocol (e.g http or https) E.g. if the URL is \"http://www.google.com, then the host=\"www.google.com\"  # noqa: E501

        :return: The host of this PingCheck.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this PingCheck.

        The URL to check, without the scheme or protocol (e.g http or https) E.g. if the URL is \"http://www.google.com, then the host=\"www.google.com\"  # noqa: E501

        :param host: The host of this PingCheck.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def timeout_in_ms_pkts_not_receive(self):
        """Gets the timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501

        The time period that the percentage of packets specified by percentPktsNotReceiveInTime must be returned in for each ping check  # noqa: E501

        :return: The timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501
        :rtype: int
        """
        return self._timeout_in_ms_pkts_not_receive

    @timeout_in_ms_pkts_not_receive.setter
    def timeout_in_ms_pkts_not_receive(self, timeout_in_ms_pkts_not_receive):
        """Sets the timeout_in_ms_pkts_not_receive of this PingCheck.

        The time period that the percentage of packets specified by percentPktsNotReceiveInTime must be returned in for each ping check  # noqa: E501

        :param timeout_in_ms_pkts_not_receive: The timeout_in_ms_pkts_not_receive of this PingCheck.  # noqa: E501
        :type: int
        """

        self._timeout_in_ms_pkts_not_receive = timeout_in_ms_pkts_not_receive

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
        if issubclass(PingCheck, dict):
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
        if not isinstance(other, PingCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
