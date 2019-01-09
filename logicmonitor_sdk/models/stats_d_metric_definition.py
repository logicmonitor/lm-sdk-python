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

from logicmonitor_sdk.models.stats_d_graph_display import StatsDGraphDisplay  # noqa: F401,E501


class StatsDMetricDefinition(object):
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
        'consolidate_function': 'int',
        'display': 'StatsDGraphDisplay',
        'name': 'str',
        'aggregate_function': 'str'
    }

    attribute_map = {
        'consolidate_function': 'consolidateFunction',
        'display': 'display',
        'name': 'name',
        'aggregate_function': 'aggregateFunction'
    }

    def __init__(self, consolidate_function=None, display=None, name=None, aggregate_function=None):  # noqa: E501
        """StatsDMetricDefinition - a model defined in Swagger"""  # noqa: E501

        self._consolidate_function = None
        self._display = None
        self._name = None
        self._aggregate_function = None
        self.discriminator = None

        if consolidate_function is not None:
            self.consolidate_function = consolidate_function
        if display is not None:
            self.display = display
        if name is not None:
            self.name = name
        if aggregate_function is not None:
            self.aggregate_function = aggregate_function

    @property
    def consolidate_function(self):
        """Gets the consolidate_function of this StatsDMetricDefinition.  # noqa: E501


        :return: The consolidate_function of this StatsDMetricDefinition.  # noqa: E501
        :rtype: int
        """
        return self._consolidate_function

    @consolidate_function.setter
    def consolidate_function(self, consolidate_function):
        """Sets the consolidate_function of this StatsDMetricDefinition.


        :param consolidate_function: The consolidate_function of this StatsDMetricDefinition.  # noqa: E501
        :type: int
        """

        self._consolidate_function = consolidate_function

    @property
    def display(self):
        """Gets the display of this StatsDMetricDefinition.  # noqa: E501


        :return: The display of this StatsDMetricDefinition.  # noqa: E501
        :rtype: StatsDGraphDisplay
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this StatsDMetricDefinition.


        :param display: The display of this StatsDMetricDefinition.  # noqa: E501
        :type: StatsDGraphDisplay
        """

        self._display = display

    @property
    def name(self):
        """Gets the name of this StatsDMetricDefinition.  # noqa: E501


        :return: The name of this StatsDMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatsDMetricDefinition.


        :param name: The name of this StatsDMetricDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def aggregate_function(self):
        """Gets the aggregate_function of this StatsDMetricDefinition.  # noqa: E501


        :return: The aggregate_function of this StatsDMetricDefinition.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_function

    @aggregate_function.setter
    def aggregate_function(self, aggregate_function):
        """Sets the aggregate_function of this StatsDMetricDefinition.


        :param aggregate_function: The aggregate_function of this StatsDMetricDefinition.  # noqa: E501
        :type: str
        """

        self._aggregate_function = aggregate_function

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
        if issubclass(StatsDMetricDefinition, dict):
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
        if not isinstance(other, StatsDMetricDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
