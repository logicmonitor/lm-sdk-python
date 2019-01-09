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

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501
from logicmonitor_sdk.models.data_source_attribute import DataSourceAttribute  # noqa: F401,E501


class CIMCollectorAttribute(CollectorAttribute):
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
        'name': 'str',
        'ip': 'str',
        'namespace': 'str',
        'query_class': 'str',
        'query_index': 'str',
        'query_value': 'str',
        'fields': 'list[DataSourceAttribute]'
    }

    attribute_map = {
        'name': 'name',
        'ip': 'ip',
        'namespace': 'namespace',
        'query_class': 'queryClass',
        'query_index': 'queryIndex',
        'query_value': 'queryValue',
        'fields': 'fields'
    }

    def __init__(self, name=None, ip=None, namespace=None, query_class=None, query_index=None, query_value=None, fields=None):  # noqa: E501
        """CIMCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._ip = None
        self._namespace = None
        self._query_class = None
        self._query_index = None
        self._query_value = None
        self._fields = None
        self.discriminator = None

        self.name = name
        if ip is not None:
            self.ip = ip
        if namespace is not None:
            self.namespace = namespace
        if query_class is not None:
            self.query_class = query_class
        if query_index is not None:
            self.query_index = query_index
        if query_value is not None:
            self.query_value = query_value
        if fields is not None:
            self.fields = fields

    @property
    def name(self):
        """Gets the name of this CIMCollectorAttribute.  # noqa: E501


        :return: The name of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CIMCollectorAttribute.


        :param name: The name of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this CIMCollectorAttribute.  # noqa: E501


        :return: The ip of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this CIMCollectorAttribute.


        :param ip: The ip of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def namespace(self):
        """Gets the namespace of this CIMCollectorAttribute.  # noqa: E501


        :return: The namespace of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CIMCollectorAttribute.


        :param namespace: The namespace of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def query_class(self):
        """Gets the query_class of this CIMCollectorAttribute.  # noqa: E501


        :return: The query_class of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_class

    @query_class.setter
    def query_class(self, query_class):
        """Sets the query_class of this CIMCollectorAttribute.


        :param query_class: The query_class of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_class = query_class

    @property
    def query_index(self):
        """Gets the query_index of this CIMCollectorAttribute.  # noqa: E501


        :return: The query_index of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_index

    @query_index.setter
    def query_index(self, query_index):
        """Sets the query_index of this CIMCollectorAttribute.


        :param query_index: The query_index of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_index = query_index

    @property
    def query_value(self):
        """Gets the query_value of this CIMCollectorAttribute.  # noqa: E501


        :return: The query_value of this CIMCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        """Sets the query_value of this CIMCollectorAttribute.


        :param query_value: The query_value of this CIMCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_value = query_value

    @property
    def fields(self):
        """Gets the fields of this CIMCollectorAttribute.  # noqa: E501


        :return: The fields of this CIMCollectorAttribute.  # noqa: E501
        :rtype: list[DataSourceAttribute]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CIMCollectorAttribute.


        :param fields: The fields of this CIMCollectorAttribute.  # noqa: E501
        :type: list[DataSourceAttribute]
        """

        self._fields = fields

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
        if issubclass(CIMCollectorAttribute, dict):
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
        if not isinstance(other, CIMCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
