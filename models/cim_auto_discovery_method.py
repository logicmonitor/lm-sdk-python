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
from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501

class CIMAutoDiscoveryMethod(AutoDiscoveryMethod):
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
        'cim_class': 'str',
        '_property': 'str',
        'namespace': 'str'
    }
    if hasattr(AutoDiscoveryMethod, "swagger_types"):
        swagger_types.update(AutoDiscoveryMethod.swagger_types)

    attribute_map = {
        'cim_class': 'cimClass',
        '_property': 'property',
        'namespace': 'namespace'
    }
    if hasattr(AutoDiscoveryMethod, "attribute_map"):
        attribute_map.update(AutoDiscoveryMethod.attribute_map)

    def __init__(self, cim_class=None, _property=None, namespace=None, *args, **kwargs):  # noqa: E501
        """CIMAutoDiscoveryMethod - a model defined in Swagger"""  # noqa: E501
        self._cim_class = None
        self.__property = None
        self._namespace = None
        self.discriminator = None
        self.cim_class = cim_class
        self._property = _property
        self.namespace = namespace
        AutoDiscoveryMethod.__init__(self, *args, **kwargs)

    @property
    def cim_class(self):
        """Gets the cim_class of this CIMAutoDiscoveryMethod.  # noqa: E501


        :return: The cim_class of this CIMAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._cim_class

    @cim_class.setter
    def cim_class(self, cim_class):
        """Sets the cim_class of this CIMAutoDiscoveryMethod.


        :param cim_class: The cim_class of this CIMAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if cim_class is None:
            raise ValueError("Invalid value for `cim_class`, must not be `None`")  # noqa: E501

        self._cim_class = cim_class

    @property
    def _property(self):
        """Gets the _property of this CIMAutoDiscoveryMethod.  # noqa: E501


        :return: The _property of this CIMAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this CIMAutoDiscoveryMethod.


        :param _property: The _property of this CIMAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501

        self.__property = _property

    @property
    def namespace(self):
        """Gets the namespace of this CIMAutoDiscoveryMethod.  # noqa: E501


        :return: The namespace of this CIMAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CIMAutoDiscoveryMethod.


        :param namespace: The namespace of this CIMAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

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
        if issubclass(CIMAutoDiscoveryMethod, dict):
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
        if not isinstance(other, CIMAutoDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
