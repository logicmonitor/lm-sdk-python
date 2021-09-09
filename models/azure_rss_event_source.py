# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.event_source import EventSource  # noqa: F401,E501
from logicmonitor_sdk.models.rest_event_source_filter import RestEventSourceFilter  # noqa: F401,E501


class AzureRssEventSource(EventSource):
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
        'suppress_duplicates_es': 'bool',
        'alert_subject_template': 'str',
        'alert_level': 'str',
        'description': 'str',
        'applies_to': 'str',
        'technology': 'str',
        'filters': 'list[RestEventSourceFilter]',
        'version': 'int',
        'collector': 'str',
        'tags': 'str',
        'alert_body_template': 'str',
        'name': 'str',
        'clear_after_ack': 'bool',
        'id': 'int',
        'alert_effective_ival': 'int',
        'group': 'str',
        'schedule': 'int'
    }

    attribute_map = {
        'suppress_duplicates_es': 'suppressDuplicatesES',
        'alert_subject_template': 'alertSubjectTemplate',
        'alert_level': 'alertLevel',
        'description': 'description',
        'applies_to': 'appliesTo',
        'technology': 'technology',
        'filters': 'filters',
        'version': 'version',
        'collector': 'collector',
        'tags': 'tags',
        'alert_body_template': 'alertBodyTemplate',
        'name': 'name',
        'clear_after_ack': 'clearAfterAck',
        'id': 'id',
        'alert_effective_ival': 'alertEffectiveIval',
        'group': 'group',
        'schedule': 'schedule'
    }

    def __init__(self, suppress_duplicates_es=None, alert_subject_template=None, alert_level=None, description=None, applies_to=None, technology=None, filters=None, version=None, collector=None, tags=None, alert_body_template=None, name=None, clear_after_ack=None, id=None, alert_effective_ival=None, group=None, schedule=None):  # noqa: E501
        """AzureRssEventSource - a model defined in Swagger"""  # noqa: E501

        self._suppress_duplicates_es = None
        self._alert_subject_template = None
        self._alert_level = None
        self._description = None
        self._applies_to = None
        self._technology = None
        self._filters = None
        self._version = None
        self._collector = None
        self._tags = None
        self._alert_body_template = None
        self._name = None
        self._clear_after_ack = None
        self._id = None
        self._alert_effective_ival = None
        self._group = None
        self._schedule = None
        self.discriminator = None

        if suppress_duplicates_es is not None:
            self.suppress_duplicates_es = suppress_duplicates_es
        if alert_subject_template is not None:
            self.alert_subject_template = alert_subject_template
        if alert_level is not None:
            self.alert_level = alert_level
        if description is not None:
            self.description = description
        if applies_to is not None:
            self.applies_to = applies_to
        if technology is not None:
            self.technology = technology
        if filters is not None:
            self.filters = filters
        if version is not None:
            self.version = version
        if collector is not None:
            self.collector = collector
        if tags is not None:
            self.tags = tags
        if alert_body_template is not None:
            self.alert_body_template = alert_body_template
        self.name = name
        if clear_after_ack is not None:
            self.clear_after_ack = clear_after_ack
        self.id = id
        self.alert_effective_ival = alert_effective_ival
        if group is not None:
            self.group = group
        if schedule is not None:
            self.schedule = schedule

    @property
    def suppress_duplicates_es(self):
        """Gets the suppress_duplicates_es of this AzureRssEventSource.  # noqa: E501

        Whether or not duplicate alerts should be suppressed at eventsource level  # noqa: E501

        :return: The suppress_duplicates_es of this AzureRssEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_duplicates_es

    @suppress_duplicates_es.setter
    def suppress_duplicates_es(self, suppress_duplicates_es):
        """Sets the suppress_duplicates_es of this AzureRssEventSource.

        Whether or not duplicate alerts should be suppressed at eventsource level  # noqa: E501

        :param suppress_duplicates_es: The suppress_duplicates_es of this AzureRssEventSource.  # noqa: E501
        :type: bool
        """

        self._suppress_duplicates_es = suppress_duplicates_es

    @property
    def alert_subject_template(self):
        """Gets the alert_subject_template of this AzureRssEventSource.  # noqa: E501

        The alert message subject for the EventSource  # noqa: E501

        :return: The alert_subject_template of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_subject_template

    @alert_subject_template.setter
    def alert_subject_template(self, alert_subject_template):
        """Sets the alert_subject_template of this AzureRssEventSource.

        The alert message subject for the EventSource  # noqa: E501

        :param alert_subject_template: The alert_subject_template of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._alert_subject_template = alert_subject_template

    @property
    def alert_level(self):
        """Gets the alert_level of this AzureRssEventSource.  # noqa: E501

        The default alert level: warn | error |critical  # noqa: E501

        :return: The alert_level of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this AzureRssEventSource.

        The default alert level: warn | error |critical  # noqa: E501

        :param alert_level: The alert_level of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._alert_level = alert_level

    @property
    def description(self):
        """Gets the description of this AzureRssEventSource.  # noqa: E501

        The description for the LMModule  # noqa: E501

        :return: The description of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AzureRssEventSource.

        The description for the LMModule  # noqa: E501

        :param description: The description of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applies_to(self):
        """Gets the applies_to of this AzureRssEventSource.  # noqa: E501

        The Applies To for the LMModule  # noqa: E501

        :return: The applies_to of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this AzureRssEventSource.

        The Applies To for the LMModule  # noqa: E501

        :param applies_to: The applies_to of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def technology(self):
        """Gets the technology of this AzureRssEventSource.  # noqa: E501

        The Technical Notes for the LMModule  # noqa: E501

        :return: The technology of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this AzureRssEventSource.

        The Technical Notes for the LMModule  # noqa: E501

        :param technology: The technology of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._technology = technology

    @property
    def filters(self):
        """Gets the filters of this AzureRssEventSource.  # noqa: E501

        The filters for the EventSource  # noqa: E501

        :return: The filters of this AzureRssEventSource.  # noqa: E501
        :rtype: list[RestEventSourceFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this AzureRssEventSource.

        The filters for the EventSource  # noqa: E501

        :param filters: The filters of this AzureRssEventSource.  # noqa: E501
        :type: list[RestEventSourceFilter]
        """

        self._filters = filters

    @property
    def version(self):
        """Gets the version of this AzureRssEventSource.  # noqa: E501

        The epoch time of the last update to the EventSource  # noqa: E501

        :return: The version of this AzureRssEventSource.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AzureRssEventSource.

        The epoch time of the last update to the EventSource  # noqa: E501

        :param version: The version of this AzureRssEventSource.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def collector(self):
        """Gets the collector of this AzureRssEventSource.  # noqa: E501

        The EventSource type: logfile | snmptrap | syslog | wineventlog | scriptevent  # noqa: E501

        :return: The collector of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this AzureRssEventSource.

        The EventSource type: logfile | snmptrap | syslog | wineventlog | scriptevent  # noqa: E501

        :param collector: The collector of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._collector = collector

    @property
    def tags(self):
        """Gets the tags of this AzureRssEventSource.  # noqa: E501

        The Tags for the LMModule  # noqa: E501

        :return: The tags of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AzureRssEventSource.

        The Tags for the LMModule  # noqa: E501

        :param tags: The tags of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def alert_body_template(self):
        """Gets the alert_body_template of this AzureRssEventSource.  # noqa: E501

        The alert message body for the EventSource  # noqa: E501

        :return: The alert_body_template of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_body_template

    @alert_body_template.setter
    def alert_body_template(self, alert_body_template):
        """Sets the alert_body_template of this AzureRssEventSource.

        The alert message body for the EventSource  # noqa: E501

        :param alert_body_template: The alert_body_template of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._alert_body_template = alert_body_template

    @property
    def name(self):
        """Gets the name of this AzureRssEventSource.  # noqa: E501

        The name of the EventSource  # noqa: E501

        :return: The name of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureRssEventSource.

        The name of the EventSource  # noqa: E501

        :param name: The name of this AzureRssEventSource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def clear_after_ack(self):
        """Gets the clear_after_ack of this AzureRssEventSource.  # noqa: E501

        Whether or not the alert should clear after acknowledgement  # noqa: E501

        :return: The clear_after_ack of this AzureRssEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._clear_after_ack

    @clear_after_ack.setter
    def clear_after_ack(self, clear_after_ack):
        """Sets the clear_after_ack of this AzureRssEventSource.

        Whether or not the alert should clear after acknowledgement  # noqa: E501

        :param clear_after_ack: The clear_after_ack of this AzureRssEventSource.  # noqa: E501
        :type: bool
        """

        self._clear_after_ack = clear_after_ack

    @property
    def id(self):
        """Gets the id of this AzureRssEventSource.  # noqa: E501

        The ID of the LMModule  # noqa: E501

        :return: The id of this AzureRssEventSource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureRssEventSource.

        The ID of the LMModule  # noqa: E501

        :param id: The id of this AzureRssEventSource.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def alert_effective_ival(self):
        """Gets the alert_effective_ival of this AzureRssEventSource.  # noqa: E501

        The time in minutes after which the alert should clear  # noqa: E501

        :return: The alert_effective_ival of this AzureRssEventSource.  # noqa: E501
        :rtype: int
        """
        return self._alert_effective_ival

    @alert_effective_ival.setter
    def alert_effective_ival(self, alert_effective_ival):
        """Sets the alert_effective_ival of this AzureRssEventSource.

        The time in minutes after which the alert should clear  # noqa: E501

        :param alert_effective_ival: The alert_effective_ival of this AzureRssEventSource.  # noqa: E501
        :type: int
        """
        if alert_effective_ival is None:
            raise ValueError("Invalid value for `alert_effective_ival`, must not be `None`")  # noqa: E501

        self._alert_effective_ival = alert_effective_ival

    @property
    def group(self):
        """Gets the group of this AzureRssEventSource.  # noqa: E501

        The group the LMModule is in  # noqa: E501

        :return: The group of this AzureRssEventSource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AzureRssEventSource.

        The group the LMModule is in  # noqa: E501

        :param group: The group of this AzureRssEventSource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def schedule(self):
        """Gets the schedule of this AzureRssEventSource.  # noqa: E501

        The polling interval for the EventSource  # noqa: E501

        :return: The schedule of this AzureRssEventSource.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AzureRssEventSource.

        The polling interval for the EventSource  # noqa: E501

        :param schedule: The schedule of this AzureRssEventSource.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

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
        if issubclass(AzureRssEventSource, dict):
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
        if not isinstance(other, AzureRssEventSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
