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


class AzureActiveDirectoryAppSecretDiscoveryMethod(AutoDiscoveryMethod):
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
        'name': 'str'
    }

    attribute_map = {
        'name': 'name'
    }

    def __init__(self, name=None):  # noqa: E501
        """AzureActiveDirectoryAppSecretDiscoveryMethod - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self.discriminator = None

        self.name = name

    @property
    def name(self):
        """Gets the name of this AzureActiveDirectoryAppSecretDiscoveryMethod.  # noqa: E501

        The auto discovery method name.  The values can be ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath|ad_awsrabbitmqqueue|ad_awssagemakerendpointvariant|ad_awsroute53resolveripaddress  # noqa: E501

        :return: The name of this AzureActiveDirectoryAppSecretDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureActiveDirectoryAppSecretDiscoveryMethod.

        The auto discovery method name.  The values can be ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath|ad_awsrabbitmqqueue|ad_awssagemakerendpointvariant|ad_awsroute53resolveripaddress  # noqa: E501

        :param name: The name of this AzureActiveDirectoryAppSecretDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(AzureActiveDirectoryAppSecretDiscoveryMethod, dict):
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
        if not isinstance(other, AzureActiveDirectoryAppSecretDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
