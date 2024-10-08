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
from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501

class WMICollectorAttribute(CollectorAttribute):
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
        'method_inputs': 'str',
        'ip': 'str',
        'namespace': 'str',
        'method_name': 'str',
        'target_path': 'str',
        'query_class': 'str',
        'query_index': 'str',
        'query_value': 'str',
        'type': 'str'
    }
    if hasattr(CollectorAttribute, "swagger_types"):
        swagger_types.update(CollectorAttribute.swagger_types)

    attribute_map = {
        'method_inputs': 'methodInputs',
        'ip': 'ip',
        'namespace': 'namespace',
        'method_name': 'methodName',
        'target_path': 'targetPath',
        'query_class': 'queryClass',
        'query_index': 'queryIndex',
        'query_value': 'queryValue',
        'type': 'type'
    }
    if hasattr(CollectorAttribute, "attribute_map"):
        attribute_map.update(CollectorAttribute.attribute_map)

    def __init__(self, method_inputs=None, ip=None, namespace=None, method_name=None, target_path=None, query_class=None, query_index=None, query_value=None, type=None, *args, **kwargs):  # noqa: E501
        """WMICollectorAttribute - a model defined in Swagger"""  # noqa: E501
        self._method_inputs = None
        self._ip = None
        self._namespace = None
        self._method_name = None
        self._target_path = None
        self._query_class = None
        self._query_index = None
        self._query_value = None
        self._type = None
        self.discriminator = None
        if method_inputs is not None:
            self.method_inputs = method_inputs
        if ip is not None:
            self.ip = ip
        if namespace is not None:
            self.namespace = namespace
        if method_name is not None:
            self.method_name = method_name
        if target_path is not None:
            self.target_path = target_path
        if query_class is not None:
            self.query_class = query_class
        if query_index is not None:
            self.query_index = query_index
        if query_value is not None:
            self.query_value = query_value
        if type is not None:
            self.type = type
        CollectorAttribute.__init__(self, *args, **kwargs)

    @property
    def method_inputs(self):
        """Gets the method_inputs of this WMICollectorAttribute.  # noqa: E501


        :return: The method_inputs of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._method_inputs

    @method_inputs.setter
    def method_inputs(self, method_inputs):
        """Sets the method_inputs of this WMICollectorAttribute.


        :param method_inputs: The method_inputs of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._method_inputs = method_inputs

    @property
    def ip(self):
        """Gets the ip of this WMICollectorAttribute.  # noqa: E501


        :return: The ip of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this WMICollectorAttribute.


        :param ip: The ip of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def namespace(self):
        """Gets the namespace of this WMICollectorAttribute.  # noqa: E501


        :return: The namespace of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this WMICollectorAttribute.


        :param namespace: The namespace of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def method_name(self):
        """Gets the method_name of this WMICollectorAttribute.  # noqa: E501


        :return: The method_name of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this WMICollectorAttribute.


        :param method_name: The method_name of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def target_path(self):
        """Gets the target_path of this WMICollectorAttribute.  # noqa: E501


        :return: The target_path of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """Sets the target_path of this WMICollectorAttribute.


        :param target_path: The target_path of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._target_path = target_path

    @property
    def query_class(self):
        """Gets the query_class of this WMICollectorAttribute.  # noqa: E501


        :return: The query_class of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_class

    @query_class.setter
    def query_class(self, query_class):
        """Sets the query_class of this WMICollectorAttribute.


        :param query_class: The query_class of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_class = query_class

    @property
    def query_index(self):
        """Gets the query_index of this WMICollectorAttribute.  # noqa: E501


        :return: The query_index of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_index

    @query_index.setter
    def query_index(self, query_index):
        """Sets the query_index of this WMICollectorAttribute.


        :param query_index: The query_index of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_index = query_index

    @property
    def query_value(self):
        """Gets the query_value of this WMICollectorAttribute.  # noqa: E501


        :return: The query_value of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        """Sets the query_value of this WMICollectorAttribute.


        :param query_value: The query_value of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._query_value = query_value

    @property
    def type(self):
        """Gets the type of this WMICollectorAttribute.  # noqa: E501


        :return: The type of this WMICollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WMICollectorAttribute.


        :param type: The type of this WMICollectorAttribute.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(WMICollectorAttribute, dict):
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
        if not isinstance(other, WMICollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
