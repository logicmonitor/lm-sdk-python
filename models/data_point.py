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


class DataPoint(object):
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
        'alert_for_no_data': 'int',
        'post_processor_method': 'str',
        'post_processor_param': 'str',
        'max_digits': 'int',
        'raw_data_field_name': 'str',
        'description': 'str',
        'alert_clear_transition_interval': 'int',
        'user_param3': 'str',
        'user_param2': 'str',
        'type': 'int',
        'data_source_id': 'int',
        'min_value': 'str',
        'alert_body': 'str',
        'origin_id': 'str',
        'user_param1': 'str',
        'alert_subject': 'str',
        'id': 'int',
        'alert_transition_interval': 'int',
        'enable_anomaly_alert_suppression': 'str',
        'max_value': 'str',
        'data_type': 'int',
        'critical_ad_adv_setting': 'str',
        'alert_expr_note': 'str',
        'ad_adv_setting_enabled': 'bool',
        'error_ad_adv_setting': 'str',
        'warn_ad_adv_setting': 'str',
        'name': 'str',
        'alert_expr': 'str'
    }

    attribute_map = {
        'alert_for_no_data': 'alertForNoData',
        'post_processor_method': 'postProcessorMethod',
        'post_processor_param': 'postProcessorParam',
        'max_digits': 'maxDigits',
        'raw_data_field_name': 'rawDataFieldName',
        'description': 'description',
        'alert_clear_transition_interval': 'alertClearTransitionInterval',
        'user_param3': 'userParam3',
        'user_param2': 'userParam2',
        'type': 'type',
        'data_source_id': 'dataSourceId',
        'min_value': 'minValue',
        'alert_body': 'alertBody',
        'origin_id': 'originId',
        'user_param1': 'userParam1',
        'alert_subject': 'alertSubject',
        'id': 'id',
        'alert_transition_interval': 'alertTransitionInterval',
        'enable_anomaly_alert_suppression': 'enableAnomalyAlertSuppression',
        'max_value': 'maxValue',
        'data_type': 'dataType',
        'critical_ad_adv_setting': 'criticalAdAdvSetting',
        'alert_expr_note': 'alertExprNote',
        'ad_adv_setting_enabled': 'adAdvSettingEnabled',
        'error_ad_adv_setting': 'errorAdAdvSetting',
        'warn_ad_adv_setting': 'warnAdAdvSetting',
        'name': 'name',
        'alert_expr': 'alertExpr'
    }

    def __init__(self, alert_for_no_data=None, post_processor_method=None, post_processor_param=None, max_digits=None, raw_data_field_name=None, description=None, alert_clear_transition_interval=None, user_param3=None, user_param2=None, type=None, data_source_id=None, min_value=None, alert_body=None, origin_id=None, user_param1=None, alert_subject=None, id=None, alert_transition_interval=None, enable_anomaly_alert_suppression=None, max_value=None, data_type=None, critical_ad_adv_setting=None, alert_expr_note=None, ad_adv_setting_enabled=None, error_ad_adv_setting=None, warn_ad_adv_setting=None, name=None, alert_expr=None):  # noqa: E501
        """DataPoint - a model defined in Swagger"""  # noqa: E501

        self._alert_for_no_data = None
        self._post_processor_method = None
        self._post_processor_param = None
        self._max_digits = None
        self._raw_data_field_name = None
        self._description = None
        self._alert_clear_transition_interval = None
        self._user_param3 = None
        self._user_param2 = None
        self._type = None
        self._data_source_id = None
        self._min_value = None
        self._alert_body = None
        self._origin_id = None
        self._user_param1 = None
        self._alert_subject = None
        self._id = None
        self._alert_transition_interval = None
        self._enable_anomaly_alert_suppression = None
        self._max_value = None
        self._data_type = None
        self._critical_ad_adv_setting = None
        self._alert_expr_note = None
        self._ad_adv_setting_enabled = None
        self._error_ad_adv_setting = None
        self._warn_ad_adv_setting = None
        self._name = None
        self._alert_expr = None
        self.discriminator = None

        if alert_for_no_data is not None:
            self.alert_for_no_data = alert_for_no_data
        if post_processor_method is not None:
            self.post_processor_method = post_processor_method
        if post_processor_param is not None:
            self.post_processor_param = post_processor_param
        if max_digits is not None:
            self.max_digits = max_digits
        if raw_data_field_name is not None:
            self.raw_data_field_name = raw_data_field_name
        if description is not None:
            self.description = description
        if alert_clear_transition_interval is not None:
            self.alert_clear_transition_interval = alert_clear_transition_interval
        if user_param3 is not None:
            self.user_param3 = user_param3
        if user_param2 is not None:
            self.user_param2 = user_param2
        if type is not None:
            self.type = type
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if min_value is not None:
            self.min_value = min_value
        if alert_body is not None:
            self.alert_body = alert_body
        if origin_id is not None:
            self.origin_id = origin_id
        if user_param1 is not None:
            self.user_param1 = user_param1
        if alert_subject is not None:
            self.alert_subject = alert_subject
        if id is not None:
            self.id = id
        if alert_transition_interval is not None:
            self.alert_transition_interval = alert_transition_interval
        if enable_anomaly_alert_suppression is not None:
            self.enable_anomaly_alert_suppression = enable_anomaly_alert_suppression
        if max_value is not None:
            self.max_value = max_value
        if data_type is not None:
            self.data_type = data_type
        if critical_ad_adv_setting is not None:
            self.critical_ad_adv_setting = critical_ad_adv_setting
        if alert_expr_note is not None:
            self.alert_expr_note = alert_expr_note
        if ad_adv_setting_enabled is not None:
            self.ad_adv_setting_enabled = ad_adv_setting_enabled
        if error_ad_adv_setting is not None:
            self.error_ad_adv_setting = error_ad_adv_setting
        if warn_ad_adv_setting is not None:
            self.warn_ad_adv_setting = warn_ad_adv_setting
        self.name = name
        if alert_expr is not None:
            self.alert_expr = alert_expr

    @property
    def alert_for_no_data(self):
        """Gets the alert_for_no_data of this DataPoint.  # noqa: E501

        The triggered alert level if we cannot collect data for this datapoint, value can be 1-4 (0:unused alert, 1:alert ok, 2:warn alert, 2:error alert, 4:critical alert)  # noqa: E501

        :return: The alert_for_no_data of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._alert_for_no_data

    @alert_for_no_data.setter
    def alert_for_no_data(self, alert_for_no_data):
        """Sets the alert_for_no_data of this DataPoint.

        The triggered alert level if we cannot collect data for this datapoint, value can be 1-4 (0:unused alert, 1:alert ok, 2:warn alert, 2:error alert, 4:critical alert)  # noqa: E501

        :param alert_for_no_data: The alert_for_no_data of this DataPoint.  # noqa: E501
        :type: int
        """

        self._alert_for_no_data = alert_for_no_data

    @property
    def post_processor_method(self):
        """Gets the post_processor_method of this DataPoint.  # noqa: E501

        The post processor method for the data value. Currently support complex expression and groovy.  # noqa: E501

        :return: The post_processor_method of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._post_processor_method

    @post_processor_method.setter
    def post_processor_method(self, post_processor_method):
        """Sets the post_processor_method of this DataPoint.

        The post processor method for the data value. Currently support complex expression and groovy.  # noqa: E501

        :param post_processor_method: The post_processor_method of this DataPoint.  # noqa: E501
        :type: str
        """

        self._post_processor_method = post_processor_method

    @property
    def post_processor_param(self):
        """Gets the post_processor_param of this DataPoint.  # noqa: E501

        The post processor parameter, e.g. dataPoint1*2  # noqa: E501

        :return: The post_processor_param of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._post_processor_param

    @post_processor_param.setter
    def post_processor_param(self, post_processor_param):
        """Sets the post_processor_param of this DataPoint.

        The post processor parameter, e.g. dataPoint1*2  # noqa: E501

        :param post_processor_param: The post_processor_param of this DataPoint.  # noqa: E501
        :type: str
        """

        self._post_processor_param = post_processor_param

    @property
    def max_digits(self):
        """Gets the max_digits of this DataPoint.  # noqa: E501

        The max digits of the data value  # noqa: E501

        :return: The max_digits of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._max_digits

    @max_digits.setter
    def max_digits(self, max_digits):
        """Sets the max_digits of this DataPoint.

        The max digits of the data value  # noqa: E501

        :param max_digits: The max_digits of this DataPoint.  # noqa: E501
        :type: int
        """

        self._max_digits = max_digits

    @property
    def raw_data_field_name(self):
        """Gets the raw_data_field_name of this DataPoint.  # noqa: E501

        The name of the raw data field name used to fetch value, e.g. avgrtt, output  # noqa: E501

        :return: The raw_data_field_name of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._raw_data_field_name

    @raw_data_field_name.setter
    def raw_data_field_name(self, raw_data_field_name):
        """Sets the raw_data_field_name of this DataPoint.

        The name of the raw data field name used to fetch value, e.g. avgrtt, output  # noqa: E501

        :param raw_data_field_name: The raw_data_field_name of this DataPoint.  # noqa: E501
        :type: str
        """

        self._raw_data_field_name = raw_data_field_name

    @property
    def description(self):
        """Gets the description of this DataPoint.  # noqa: E501

        The datapoint description  # noqa: E501

        :return: The description of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataPoint.

        The datapoint description  # noqa: E501

        :param description: The description of this DataPoint.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def alert_clear_transition_interval(self):
        """Gets the alert_clear_transition_interval of this DataPoint.  # noqa: E501

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :return: The alert_clear_transition_interval of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._alert_clear_transition_interval

    @alert_clear_transition_interval.setter
    def alert_clear_transition_interval(self, alert_clear_transition_interval):
        """Sets the alert_clear_transition_interval of this DataPoint.

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :param alert_clear_transition_interval: The alert_clear_transition_interval of this DataPoint.  # noqa: E501
        :type: int
        """

        self._alert_clear_transition_interval = alert_clear_transition_interval

    @property
    def user_param3(self):
        """Gets the user_param3 of this DataPoint.  # noqa: E501

        The third user parameter will be used to fetch the datapoint value.   # noqa: E501

        :return: The user_param3 of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._user_param3

    @user_param3.setter
    def user_param3(self, user_param3):
        """Sets the user_param3 of this DataPoint.

        The third user parameter will be used to fetch the datapoint value.   # noqa: E501

        :param user_param3: The user_param3 of this DataPoint.  # noqa: E501
        :type: str
        """

        self._user_param3 = user_param3

    @property
    def user_param2(self):
        """Gets the user_param2 of this DataPoint.  # noqa: E501

        The second user parameter will be used to fetch the datapoint value. e.g. jmx attribute name  # noqa: E501

        :return: The user_param2 of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._user_param2

    @user_param2.setter
    def user_param2(self, user_param2):
        """Sets the user_param2 of this DataPoint.

        The second user parameter will be used to fetch the datapoint value. e.g. jmx attribute name  # noqa: E501

        :param user_param2: The user_param2 of this DataPoint.  # noqa: E501
        :type: str
        """

        self._user_param2 = user_param2

    @property
    def type(self):
        """Gets the type of this DataPoint.  # noqa: E501

        The data metric type, values can be 0-7 (0:unknown, 1:counter, 2:gauge, 3:derive, 5:status, 6:compute, 7:counter32, 8:counter64)  # noqa: E501

        :return: The type of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DataPoint.

        The data metric type, values can be 0-7 (0:unknown, 1:counter, 2:gauge, 3:derive, 5:status, 6:compute, 7:counter32, 8:counter64)  # noqa: E501

        :param type: The type of this DataPoint.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DataPoint.  # noqa: E501

        The datasource id  # noqa: E501

        :return: The data_source_id of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DataPoint.

        The datasource id  # noqa: E501

        :param data_source_id: The data_source_id of this DataPoint.  # noqa: E501
        :type: int
        """

        self._data_source_id = data_source_id

    @property
    def min_value(self):
        """Gets the min_value of this DataPoint.  # noqa: E501

        The minimum value of the datapoint value range  # noqa: E501

        :return: The min_value of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this DataPoint.

        The minimum value of the datapoint value range  # noqa: E501

        :param min_value: The min_value of this DataPoint.  # noqa: E501
        :type: str
        """

        self._min_value = min_value

    @property
    def alert_body(self):
        """Gets the alert_body of this DataPoint.  # noqa: E501

        The customized alert message body define,  empty string mean we will use the define in default template  # noqa: E501

        :return: The alert_body of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._alert_body

    @alert_body.setter
    def alert_body(self, alert_body):
        """Sets the alert_body of this DataPoint.

        The customized alert message body define,  empty string mean we will use the define in default template  # noqa: E501

        :param alert_body: The alert_body of this DataPoint.  # noqa: E501
        :type: str
        """

        self._alert_body = alert_body

    @property
    def origin_id(self):
        """Gets the origin_id of this DataPoint.  # noqa: E501

        portable id for origin tracking  # noqa: E501

        :return: The origin_id of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this DataPoint.

        portable id for origin tracking  # noqa: E501

        :param origin_id: The origin_id of this DataPoint.  # noqa: E501
        :type: str
        """

        self._origin_id = origin_id

    @property
    def user_param1(self):
        """Gets the user_param1 of this DataPoint.  # noqa: E501

        The first user parameter will be used to fetch the datapoint value. e.g. snmp oid  # noqa: E501

        :return: The user_param1 of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._user_param1

    @user_param1.setter
    def user_param1(self, user_param1):
        """Sets the user_param1 of this DataPoint.

        The first user parameter will be used to fetch the datapoint value. e.g. snmp oid  # noqa: E501

        :param user_param1: The user_param1 of this DataPoint.  # noqa: E501
        :type: str
        """

        self._user_param1 = user_param1

    @property
    def alert_subject(self):
        """Gets the alert_subject of this DataPoint.  # noqa: E501

        The customized alert message subject define, empty string mean we will use the define in default template  # noqa: E501

        :return: The alert_subject of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._alert_subject

    @alert_subject.setter
    def alert_subject(self, alert_subject):
        """Sets the alert_subject of this DataPoint.

        The customized alert message subject define, empty string mean we will use the define in default template  # noqa: E501

        :param alert_subject: The alert_subject of this DataPoint.  # noqa: E501
        :type: str
        """

        self._alert_subject = alert_subject

    @property
    def id(self):
        """Gets the id of this DataPoint.  # noqa: E501

        The datapoint id  # noqa: E501

        :return: The id of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataPoint.

        The datapoint id  # noqa: E501

        :param id: The id of this DataPoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def alert_transition_interval(self):
        """Gets the alert_transition_interval of this DataPoint.  # noqa: E501

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :return: The alert_transition_interval of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._alert_transition_interval

    @alert_transition_interval.setter
    def alert_transition_interval(self, alert_transition_interval):
        """Sets the alert_transition_interval of this DataPoint.

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :param alert_transition_interval: The alert_transition_interval of this DataPoint.  # noqa: E501
        :type: int
        """

        self._alert_transition_interval = alert_transition_interval

    @property
    def enable_anomaly_alert_suppression(self):
        """Gets the enable_anomaly_alert_suppression of this DataPoint.  # noqa: E501

        Expression of anomaly detection setting, split by comma 0 means off,  1 means on, -1 means invalid 1,0,1 =   warn : ON     error: OFF   critical: ON Empty value on this parameter means : 0,0,0  # noqa: E501

        :return: The enable_anomaly_alert_suppression of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_suppression

    @enable_anomaly_alert_suppression.setter
    def enable_anomaly_alert_suppression(self, enable_anomaly_alert_suppression):
        """Sets the enable_anomaly_alert_suppression of this DataPoint.

        Expression of anomaly detection setting, split by comma 0 means off,  1 means on, -1 means invalid 1,0,1 =   warn : ON     error: OFF   critical: ON Empty value on this parameter means : 0,0,0  # noqa: E501

        :param enable_anomaly_alert_suppression: The enable_anomaly_alert_suppression of this DataPoint.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_suppression = enable_anomaly_alert_suppression

    @property
    def max_value(self):
        """Gets the max_value of this DataPoint.  # noqa: E501

        The max value of the datapoint value range  # noqa: E501

        :return: The max_value of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this DataPoint.

        The max value of the datapoint value range  # noqa: E501

        :param max_value: The max_value of this DataPoint.  # noqa: E501
        :type: str
        """

        self._max_value = max_value

    @property
    def data_type(self):
        """Gets the data_type of this DataPoint.  # noqa: E501

        The data value type, values can be 1-8 (1:boolean, 2:byte, 3:short, 4:int, 5:long, 6:float, 7:double, 8:ulong)  # noqa: E501

        :return: The data_type of this DataPoint.  # noqa: E501
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataPoint.

        The data value type, values can be 1-8 (1:boolean, 2:byte, 3:short, 4:int, 5:long, 6:float, 7:double, 8:ulong)  # noqa: E501

        :param data_type: The data_type of this DataPoint.  # noqa: E501
        :type: int
        """

        self._data_type = data_type

    @property
    def critical_ad_adv_setting(self):
        """Gets the critical_ad_adv_setting of this DataPoint.  # noqa: E501

        enable anomaly detection advance setting for CRITICAL severity  # noqa: E501

        :return: The critical_ad_adv_setting of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._critical_ad_adv_setting

    @critical_ad_adv_setting.setter
    def critical_ad_adv_setting(self, critical_ad_adv_setting):
        """Sets the critical_ad_adv_setting of this DataPoint.

        enable anomaly detection advance setting for CRITICAL severity  # noqa: E501

        :param critical_ad_adv_setting: The critical_ad_adv_setting of this DataPoint.  # noqa: E501
        :type: str
        """

        self._critical_ad_adv_setting = critical_ad_adv_setting

    @property
    def alert_expr_note(self):
        """Gets the alert_expr_note of this DataPoint.  # noqa: E501

        alert expression note  # noqa: E501

        :return: The alert_expr_note of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr_note

    @alert_expr_note.setter
    def alert_expr_note(self, alert_expr_note):
        """Sets the alert_expr_note of this DataPoint.

        alert expression note  # noqa: E501

        :param alert_expr_note: The alert_expr_note of this DataPoint.  # noqa: E501
        :type: str
        """

        self._alert_expr_note = alert_expr_note

    @property
    def ad_adv_setting_enabled(self):
        """Gets the ad_adv_setting_enabled of this DataPoint.  # noqa: E501

        the AD advance setting enable flag  # noqa: E501

        :return: The ad_adv_setting_enabled of this DataPoint.  # noqa: E501
        :rtype: bool
        """
        return self._ad_adv_setting_enabled

    @ad_adv_setting_enabled.setter
    def ad_adv_setting_enabled(self, ad_adv_setting_enabled):
        """Sets the ad_adv_setting_enabled of this DataPoint.

        the AD advance setting enable flag  # noqa: E501

        :param ad_adv_setting_enabled: The ad_adv_setting_enabled of this DataPoint.  # noqa: E501
        :type: bool
        """

        self._ad_adv_setting_enabled = ad_adv_setting_enabled

    @property
    def error_ad_adv_setting(self):
        """Gets the error_ad_adv_setting of this DataPoint.  # noqa: E501

        enable anomaly detection advance setting for ERROR severity  # noqa: E501

        :return: The error_ad_adv_setting of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._error_ad_adv_setting

    @error_ad_adv_setting.setter
    def error_ad_adv_setting(self, error_ad_adv_setting):
        """Sets the error_ad_adv_setting of this DataPoint.

        enable anomaly detection advance setting for ERROR severity  # noqa: E501

        :param error_ad_adv_setting: The error_ad_adv_setting of this DataPoint.  # noqa: E501
        :type: str
        """

        self._error_ad_adv_setting = error_ad_adv_setting

    @property
    def warn_ad_adv_setting(self):
        """Gets the warn_ad_adv_setting of this DataPoint.  # noqa: E501

        enable anomaly detection advance setting for WARN severity  # noqa: E501

        :return: The warn_ad_adv_setting of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._warn_ad_adv_setting

    @warn_ad_adv_setting.setter
    def warn_ad_adv_setting(self, warn_ad_adv_setting):
        """Sets the warn_ad_adv_setting of this DataPoint.

        enable anomaly detection advance setting for WARN severity  # noqa: E501

        :param warn_ad_adv_setting: The warn_ad_adv_setting of this DataPoint.  # noqa: E501
        :type: str
        """

        self._warn_ad_adv_setting = warn_ad_adv_setting

    @property
    def name(self):
        """Gets the name of this DataPoint.  # noqa: E501

        The datapoint name  # noqa: E501

        :return: The name of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataPoint.

        The datapoint name  # noqa: E501

        :param name: The name of this DataPoint.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def alert_expr(self):
        """Gets the alert_expr of this DataPoint.  # noqa: E501

        The alert threshold define for the datapoint. e.g. '> 60 80 90' mean it will:  trigger warn alert if value > 60 trigger error alert if value > 80 trigger critical alert if value > 90  # noqa: E501

        :return: The alert_expr of this DataPoint.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """Sets the alert_expr of this DataPoint.

        The alert threshold define for the datapoint. e.g. '> 60 80 90' mean it will:  trigger warn alert if value > 60 trigger error alert if value > 80 trigger critical alert if value > 90  # noqa: E501

        :param alert_expr: The alert_expr of this DataPoint.  # noqa: E501
        :type: str
        """

        self._alert_expr = alert_expr

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
        if issubclass(DataPoint, dict):
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
        if not isinstance(other, DataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
