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


class MongoCollectorAttribute(CollectorAttribute):
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
        'database': 'str',
        'port': 'str',
        'query': 'str',
        'collection': 'str'
    }

    attribute_map = {
        'name': 'name',
        'database': 'database',
        'port': 'port',
        'query': 'query',
        'collection': 'collection'
    }

    def __init__(self, name=None, database=None, port=None, query=None, collection=None):  # noqa: E501
        """MongoCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._database = None
        self._port = None
        self._query = None
        self._collection = None
        self.discriminator = None

        self.name = name
        if database is not None:
            self.database = database
        if port is not None:
            self.port = port
        if query is not None:
            self.query = query
        if collection is not None:
            self.collection = collection

    @property
    def name(self):
        """Gets the name of this MongoCollectorAttribute.  # noqa: E501


        :return: The name of this MongoCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MongoCollectorAttribute.


        :param name: The name of this MongoCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def database(self):
        """Gets the database of this MongoCollectorAttribute.  # noqa: E501


        :return: The database of this MongoCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this MongoCollectorAttribute.


        :param database: The database of this MongoCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def port(self):
        """Gets the port of this MongoCollectorAttribute.  # noqa: E501


        :return: The port of this MongoCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MongoCollectorAttribute.


        :param port: The port of this MongoCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def query(self):
        """Gets the query of this MongoCollectorAttribute.  # noqa: E501


        :return: The query of this MongoCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this MongoCollectorAttribute.


        :param query: The query of this MongoCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def collection(self):
        """Gets the collection of this MongoCollectorAttribute.  # noqa: E501


        :return: The collection of this MongoCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this MongoCollectorAttribute.


        :param collection: The collection of this MongoCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._collection = collection

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
        if issubclass(MongoCollectorAttribute, dict):
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
        if not isinstance(other, MongoCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
