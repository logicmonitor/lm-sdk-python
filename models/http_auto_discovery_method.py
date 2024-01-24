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


class HttpAutoDiscoveryMethod(AutoDiscoveryMethod):
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
        'regex': 'str',
        'case_sensitive': 'bool',
        'follow_redirect': 'bool',
        'ports': 'str',
        'uri': 'str',
        'use_ssl': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'regex': 'regex',
        'case_sensitive': 'caseSensitive',
        'follow_redirect': 'followRedirect',
        'ports': 'ports',
        'uri': 'uri',
        'use_ssl': 'useSSL'
    }

    def __init__(self, name=None, regex=None, case_sensitive=None, follow_redirect=None, ports=None, uri=None, use_ssl=None):  # noqa: E501
        """HttpAutoDiscoveryMethod - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._regex = None
        self._case_sensitive = None
        self._follow_redirect = None
        self._ports = None
        self._uri = None
        self._use_ssl = None
        self.discriminator = None

        self.name = name
        self.regex = regex
        self.case_sensitive = case_sensitive
        self.follow_redirect = follow_redirect
        self.ports = ports
        self.uri = uri
        self.use_ssl = use_ssl

    @property
    def name(self):
        """Gets the name of this HttpAutoDiscoveryMethod.  # noqa: E501

        The auto discovery method name.  The values can be ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath|ad_awsrabbitmqqueue|ad_awssagemakerendpointvariant|ad_awsroute53resolveripaddress  # noqa: E501

        :return: The name of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HttpAutoDiscoveryMethod.

        The auto discovery method name.  The values can be ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath|ad_awsrabbitmqqueue|ad_awssagemakerendpointvariant|ad_awsroute53resolveripaddress  # noqa: E501

        :param name: The name of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def regex(self):
        """Gets the regex of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The regex of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this HttpAutoDiscoveryMethod.


        :param regex: The regex of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if regex is None:
            raise ValueError("Invalid value for `regex`, must not be `None`")  # noqa: E501

        self._regex = regex

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The case_sensitive of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this HttpAutoDiscoveryMethod.


        :param case_sensitive: The case_sensitive of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: bool
        """
        if case_sensitive is None:
            raise ValueError("Invalid value for `case_sensitive`, must not be `None`")  # noqa: E501

        self._case_sensitive = case_sensitive

    @property
    def follow_redirect(self):
        """Gets the follow_redirect of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The follow_redirect of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirect

    @follow_redirect.setter
    def follow_redirect(self, follow_redirect):
        """Sets the follow_redirect of this HttpAutoDiscoveryMethod.


        :param follow_redirect: The follow_redirect of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: bool
        """
        if follow_redirect is None:
            raise ValueError("Invalid value for `follow_redirect`, must not be `None`")  # noqa: E501

        self._follow_redirect = follow_redirect

    @property
    def ports(self):
        """Gets the ports of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The ports of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this HttpAutoDiscoveryMethod.


        :param ports: The ports of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if ports is None:
            raise ValueError("Invalid value for `ports`, must not be `None`")  # noqa: E501

        self._ports = ports

    @property
    def uri(self):
        """Gets the uri of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The uri of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this HttpAutoDiscoveryMethod.


        :param uri: The uri of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def use_ssl(self):
        """Gets the use_ssl of this HttpAutoDiscoveryMethod.  # noqa: E501


        :return: The use_ssl of this HttpAutoDiscoveryMethod.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this HttpAutoDiscoveryMethod.


        :param use_ssl: The use_ssl of this HttpAutoDiscoveryMethod.  # noqa: E501
        :type: bool
        """
        if use_ssl is None:
            raise ValueError("Invalid value for `use_ssl`, must not be `None`")  # noqa: E501

        self._use_ssl = use_ssl

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
        if issubclass(HttpAutoDiscoveryMethod, dict):
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
        if not isinstance(other, HttpAutoDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
