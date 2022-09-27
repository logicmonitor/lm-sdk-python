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

from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501


class PaaSJsonPathDiscoveryMethod(AutoDiscoveryMethod):
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
        'value_attribute': 'str',
        'alias_attribute': 'str',
        'description_attribute': 'str',
        'resource_url': 'str',
        'property_attributes': 'str',
        'value2_attribute': 'str',
        'instance_path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value_attribute': 'valueAttribute',
        'alias_attribute': 'aliasAttribute',
        'description_attribute': 'descriptionAttribute',
        'resource_url': 'resourceUrl',
        'property_attributes': 'propertyAttributes',
        'value2_attribute': 'value2Attribute',
        'instance_path': 'instancePath'
    }

    def __init__(self, name=None, value_attribute=None, alias_attribute=None, description_attribute=None, resource_url=None, property_attributes=None, value2_attribute=None, instance_path=None):  # noqa: E501
        """PaaSJsonPathDiscoveryMethod - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value_attribute = None
        self._alias_attribute = None
        self._description_attribute = None
        self._resource_url = None
        self._property_attributes = None
        self._value2_attribute = None
        self._instance_path = None
        self.discriminator = None

        self.name = name
        self.value_attribute = value_attribute
        if alias_attribute is not None:
            self.alias_attribute = alias_attribute
        if description_attribute is not None:
            self.description_attribute = description_attribute
        self.resource_url = resource_url
        if property_attributes is not None:
            self.property_attributes = property_attributes
        if value2_attribute is not None:
            self.value2_attribute = value2_attribute
        self.instance_path = instance_path

    @property
    def name(self):
        """Gets the name of this PaaSJsonPathDiscoveryMethod.  # noqa: E501

        The auto discovery method name values can be : ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath  # noqa: E501

        :return: The name of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaaSJsonPathDiscoveryMethod.

        The auto discovery method name values can be : ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath  # noqa: E501

        :param name: The name of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value_attribute(self):
        """Gets the value_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The value_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._value_attribute

    @value_attribute.setter
    def value_attribute(self, value_attribute):
        """Sets the value_attribute of this PaaSJsonPathDiscoveryMethod.


        :param value_attribute: The value_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if value_attribute is None:
            raise ValueError("Invalid value for `value_attribute`, must not be `None`")  # noqa: E501

        self._value_attribute = value_attribute

    @property
    def alias_attribute(self):
        """Gets the alias_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The alias_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._alias_attribute

    @alias_attribute.setter
    def alias_attribute(self, alias_attribute):
        """Sets the alias_attribute of this PaaSJsonPathDiscoveryMethod.


        :param alias_attribute: The alias_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._alias_attribute = alias_attribute

    @property
    def description_attribute(self):
        """Gets the description_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The description_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._description_attribute

    @description_attribute.setter
    def description_attribute(self, description_attribute):
        """Sets the description_attribute of this PaaSJsonPathDiscoveryMethod.


        :param description_attribute: The description_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._description_attribute = description_attribute

    @property
    def resource_url(self):
        """Gets the resource_url of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The resource_url of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        """Sets the resource_url of this PaaSJsonPathDiscoveryMethod.


        :param resource_url: The resource_url of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if resource_url is None:
            raise ValueError("Invalid value for `resource_url`, must not be `None`")  # noqa: E501

        self._resource_url = resource_url

    @property
    def property_attributes(self):
        """Gets the property_attributes of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The property_attributes of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._property_attributes

    @property_attributes.setter
    def property_attributes(self, property_attributes):
        """Sets the property_attributes of this PaaSJsonPathDiscoveryMethod.


        :param property_attributes: The property_attributes of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._property_attributes = property_attributes

    @property
    def value2_attribute(self):
        """Gets the value2_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The value2_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._value2_attribute

    @value2_attribute.setter
    def value2_attribute(self, value2_attribute):
        """Sets the value2_attribute of this PaaSJsonPathDiscoveryMethod.


        :param value2_attribute: The value2_attribute of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._value2_attribute = value2_attribute

    @property
    def instance_path(self):
        """Gets the instance_path of this PaaSJsonPathDiscoveryMethod.  # noqa: E501


        :return: The instance_path of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._instance_path

    @instance_path.setter
    def instance_path(self, instance_path):
        """Sets the instance_path of this PaaSJsonPathDiscoveryMethod.


        :param instance_path: The instance_path of this PaaSJsonPathDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if instance_path is None:
            raise ValueError("Invalid value for `instance_path`, must not be `None`")  # noqa: E501

        self._instance_path = instance_path

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
        if issubclass(PaaSJsonPathDiscoveryMethod, dict):
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
        if not isinstance(other, PaaSJsonPathDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other