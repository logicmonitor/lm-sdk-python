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

class SNMPAutoDiscoveryMethod(AutoDiscoveryMethod):
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
        'lookup_oid': 'str',
        'external_resource_id': 'str',
        'description_oid': 'str',
        'external_resource_type': 'str',
        'oid': 'str',
        'ilp': 'list[SNMPILP]',
        'discovery_type': 'str',
        'enable_snmpilp': 'bool'
    }
    if hasattr(AutoDiscoveryMethod, "swagger_types"):
        swagger_types.update(AutoDiscoveryMethod.swagger_types)

    attribute_map = {
        'lookup_oid': 'lookupOID',
        'external_resource_id': 'externalResourceID',
        'description_oid': 'descriptionOID',
        'external_resource_type': 'externalResourceType',
        'oid': 'OID',
        'ilp': 'ILP',
        'discovery_type': 'discoveryType',
        'enable_snmpilp': 'enableSNMPILP'
    }
    if hasattr(AutoDiscoveryMethod, "attribute_map"):
        attribute_map.update(AutoDiscoveryMethod.attribute_map)

    def __init__(self, lookup_oid=None, external_resource_id=None, description_oid=None, external_resource_type=None, oid=None, ilp=None, discovery_type=None, enable_snmpilp=None, *args, **kwargs):  # noqa: E501
        """SNMPAutoDiscoveryMethod - a model defined in Swagger"""  # noqa: E501
        self._lookup_oid = None
        self._external_resource_id = None
        self._description_oid = None
        self._external_resource_type = None
        self._oid = None
        self._ilp = None
        self._discovery_type = None
        self._enable_snmpilp = None
        self.discriminator = None
        self.lookup_oid = lookup_oid
        if external_resource_id is not None:
            self.external_resource_id = external_resource_id
        if description_oid is not None:
            self.description_oid = description_oid
        if external_resource_type is not None:
            self.external_resource_type = external_resource_type
        self.oid = oid
        if ilp is not None:
            self.ilp = ilp
        self.discovery_type = discovery_type
        if enable_snmpilp is not None:
            self.enable_snmpilp = enable_snmpilp
        AutoDiscoveryMethod.__init__(self, *args, **kwargs)

    @property
    def lookup_oid(self):
        """Gets the lookup_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The lookup_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._lookup_oid

    @lookup_oid.setter
    def lookup_oid(self, lookup_oid):
        """Sets the lookup_oid of this SNMPAutoDiscoveryMethod.


        :param lookup_oid: The lookup_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if lookup_oid is None:
            raise ValueError("Invalid value for `lookup_oid`, must not be `None`")  # noqa: E501

        self._lookup_oid = lookup_oid

    @property
    def external_resource_id(self):
        """Gets the external_resource_id of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The external_resource_id of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._external_resource_id

    @external_resource_id.setter
    def external_resource_id(self, external_resource_id):
        """Sets the external_resource_id of this SNMPAutoDiscoveryMethod.


        :param external_resource_id: The external_resource_id of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._external_resource_id = external_resource_id

    @property
    def description_oid(self):
        """Gets the description_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The description_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._description_oid

    @description_oid.setter
    def description_oid(self, description_oid):
        """Sets the description_oid of this SNMPAutoDiscoveryMethod.


        :param description_oid: The description_oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._description_oid = description_oid

    @property
    def external_resource_type(self):
        """Gets the external_resource_type of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The external_resource_type of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._external_resource_type

    @external_resource_type.setter
    def external_resource_type(self, external_resource_type):
        """Sets the external_resource_type of this SNMPAutoDiscoveryMethod.


        :param external_resource_type: The external_resource_type of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._external_resource_type = external_resource_type

    @property
    def oid(self):
        """Gets the oid of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this SNMPAutoDiscoveryMethod.


        :param oid: The oid of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if oid is None:
            raise ValueError("Invalid value for `oid`, must not be `None`")  # noqa: E501

        self._oid = oid

    @property
    def ilp(self):
        """Gets the ilp of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The ilp of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: list[SNMPILP]
        """
        return self._ilp

    @ilp.setter
    def ilp(self, ilp):
        """Sets the ilp of this SNMPAutoDiscoveryMethod.


        :param ilp: The ilp of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: list[SNMPILP]
        """

        self._ilp = ilp

    @property
    def discovery_type(self):
        """Gets the discovery_type of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The discovery_type of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._discovery_type

    @discovery_type.setter
    def discovery_type(self, discovery_type):
        """Sets the discovery_type of this SNMPAutoDiscoveryMethod.


        :param discovery_type: The discovery_type of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if discovery_type is None:
            raise ValueError("Invalid value for `discovery_type`, must not be `None`")  # noqa: E501

        self._discovery_type = discovery_type

    @property
    def enable_snmpilp(self):
        """Gets the enable_snmpilp of this SNMPAutoDiscoveryMethod.  # noqa: E501


        :return: The enable_snmpilp of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :rtype: bool
        """
        return self._enable_snmpilp

    @enable_snmpilp.setter
    def enable_snmpilp(self, enable_snmpilp):
        """Sets the enable_snmpilp of this SNMPAutoDiscoveryMethod.


        :param enable_snmpilp: The enable_snmpilp of this SNMPAutoDiscoveryMethod.  # noqa: E501
        :type: bool
        """

        self._enable_snmpilp = enable_snmpilp

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
        if issubclass(SNMPAutoDiscoveryMethod, dict):
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
        if not isinstance(other, SNMPAutoDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
