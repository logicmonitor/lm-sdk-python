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


class AlertFilters(object):
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
        'severity': 'str',
        'sdted': 'str',
        'chain': 'str',
        'instance': 'str',
        'data_point': 'str',
        'host': 'str',
        'rule': 'str',
        'keyword': 'str',
        'data_source': 'str',
        'acked': 'str',
        'cleared': 'str',
        'group': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'sdted': 'sdted',
        'chain': 'chain',
        'instance': 'instance',
        'data_point': 'dataPoint',
        'host': 'host',
        'rule': 'rule',
        'keyword': 'keyword',
        'data_source': 'dataSource',
        'acked': 'acked',
        'cleared': 'cleared',
        'group': 'group'
    }

    def __init__(self, severity=None, sdted=None, chain=None, instance=None, data_point=None, host=None, rule=None, keyword=None, data_source=None, acked=None, cleared=None, group=None):  # noqa: E501
        """AlertFilters - a model defined in Swagger"""  # noqa: E501

        self._severity = None
        self._sdted = None
        self._chain = None
        self._instance = None
        self._data_point = None
        self._host = None
        self._rule = None
        self._keyword = None
        self._data_source = None
        self._acked = None
        self._cleared = None
        self._group = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if sdted is not None:
            self.sdted = sdted
        if chain is not None:
            self.chain = chain
        if instance is not None:
            self.instance = instance
        if data_point is not None:
            self.data_point = data_point
        if host is not None:
            self.host = host
        if rule is not None:
            self.rule = rule
        if keyword is not None:
            self.keyword = keyword
        if data_source is not None:
            self.data_source = data_source
        if acked is not None:
            self.acked = acked
        if cleared is not None:
            self.cleared = cleared
        if group is not None:
            self.group = group

    @property
    def severity(self):
        """Gets the severity of this AlertFilters.  # noqa: E501

        Displayed alerts must have a severity that satisfies this criteria. Multiple severities are separated by commas  # noqa: E501

        :return: The severity of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertFilters.

        Displayed alerts must have a severity that satisfies this criteria. Multiple severities are separated by commas  # noqa: E501

        :param severity: The severity of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def sdted(self):
        """Gets the sdted of this AlertFilters.  # noqa: E501

        Displayed alerts must have an SDT status that meets this criteria  # noqa: E501

        :return: The sdted of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._sdted

    @sdted.setter
    def sdted(self, sdted):
        """Sets the sdted of this AlertFilters.

        Displayed alerts must have an SDT status that meets this criteria  # noqa: E501

        :param sdted: The sdted of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._sdted = sdted

    @property
    def chain(self):
        """Gets the chain of this AlertFilters.  # noqa: E501

        Displayed alerts must be routed to an escalation chain that satisfies this filter. Glob is accepted, and * and an empty string both match all escalation chains  # noqa: E501

        :return: The chain of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this AlertFilters.

        Displayed alerts must be routed to an escalation chain that satisfies this filter. Glob is accepted, and * and an empty string both match all escalation chains  # noqa: E501

        :param chain: The chain of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._chain = chain

    @property
    def instance(self):
        """Gets the instance of this AlertFilters.  # noqa: E501

        Displayed alerts must be associated with instances that meet this filter criteria. Glob is accepted, and * and an empty string both match all instances  # noqa: E501

        :return: The instance of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this AlertFilters.

        Displayed alerts must be associated with instances that meet this filter criteria. Glob is accepted, and * and an empty string both match all instances  # noqa: E501

        :param instance: The instance of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def data_point(self):
        """Gets the data_point of this AlertFilters.  # noqa: E501

        Displayed alerts must be associated with datapoints that meet this filter criteria. Glob is accepted, and * and an empty string both match all datapoints  # noqa: E501

        :return: The data_point of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._data_point

    @data_point.setter
    def data_point(self, data_point):
        """Sets the data_point of this AlertFilters.

        Displayed alerts must be associated with datapoints that meet this filter criteria. Glob is accepted, and * and an empty string both match all datapoints  # noqa: E501

        :param data_point: The data_point of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._data_point = data_point

    @property
    def host(self):
        """Gets the host of this AlertFilters.  # noqa: E501

        Displayed alerts must be associated with devices that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all devices  # noqa: E501

        :return: The host of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AlertFilters.

        Displayed alerts must be associated with devices that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all devices  # noqa: E501

        :param host: The host of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def rule(self):
        """Gets the rule of this AlertFilters.  # noqa: E501

        Displayed alerts must match a rule that satisfies this filter. Glob is accepted, and * and an empty string both match all rules  # noqa: E501

        :return: The rule of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this AlertFilters.

        Displayed alerts must match a rule that satisfies this filter. Glob is accepted, and * and an empty string both match all rules  # noqa: E501

        :param rule: The rule of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._rule = rule

    @property
    def keyword(self):
        """Gets the keyword of this AlertFilters.  # noqa: E501

        The key word for free search  # noqa: E501

        :return: The keyword of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this AlertFilters.

        The key word for free search  # noqa: E501

        :param keyword: The keyword of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def data_source(self):
        """Gets the data_source of this AlertFilters.  # noqa: E501

        Displayed alerts must be associated with datasources that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all datasources  # noqa: E501

        :return: The data_source of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this AlertFilters.

        Displayed alerts must be associated with datasources that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all datasources  # noqa: E501

        :param data_source: The data_source of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def acked(self):
        """Gets the acked of this AlertFilters.  # noqa: E501

        Displayed alerts must have an acknowledgement status that satisfies this criteria  # noqa: E501

        :return: The acked of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._acked

    @acked.setter
    def acked(self, acked):
        """Sets the acked of this AlertFilters.

        Displayed alerts must have an acknowledgement status that satisfies this criteria  # noqa: E501

        :param acked: The acked of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._acked = acked

    @property
    def cleared(self):
        """Gets the cleared of this AlertFilters.  # noqa: E501

        Displayed alerts must be active if cleared=no,  display alerts must be closed if cleared=yes, and must have cleared in the past 7 days if cleared=all  # noqa: E501

        :return: The cleared of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this AlertFilters.

        Displayed alerts must be active if cleared=no,  display alerts must be closed if cleared=yes, and must have cleared in the past 7 days if cleared=all  # noqa: E501

        :param cleared: The cleared of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._cleared = cleared

    @property
    def group(self):
        """Gets the group of this AlertFilters.  # noqa: E501

        Displayed alerts must be associated with groups that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all groups  # noqa: E501

        :return: The group of this AlertFilters.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AlertFilters.

        Displayed alerts must be associated with groups that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all groups  # noqa: E501

        :param group: The group of this AlertFilters.  # noqa: E501
        :type: str
        """

        self._group = group

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
        if issubclass(AlertFilters, dict):
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
        if not isinstance(other, AlertFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
