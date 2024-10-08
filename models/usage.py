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

class Usage(object):
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
        'num_of_stopped_azure_devices': 'int',
        'num_of_services': 'int',
        'num_of_terminated_azure_devices': 'int',
        'number_of_standard_devices': 'int',
        'num_of_stopped_gcp_devices': 'int',
        'num_of_combined_gcp_devices': 'int',
        'num_of_aws_devices': 'int',
        'number_of_kubernetes_devices': 'int',
        'num_of_gcp_devices': 'int',
        'num_of_azure_devices': 'int',
        'num_of_combined_azure_devices': 'int',
        'num_of_terminated_aws_devices': 'int',
        'num_of_terminated_gcp_cloud_devices': 'int',
        'num_of_stopped_aws_devices': 'int',
        'number_of_devices': 'int',
        'num_of_config_source_devices': 'int',
        'num_of_websites': 'int',
        'num_of_combined_aws_devices': 'int'
    }

    attribute_map = {
        'num_of_stopped_azure_devices': 'numOfStoppedAzureDevices',
        'num_of_services': 'numOfServices',
        'num_of_terminated_azure_devices': 'numOfTerminatedAzureDevices',
        'number_of_standard_devices': 'numberOfStandardDevices',
        'num_of_stopped_gcp_devices': 'numOfStoppedGcpDevices',
        'num_of_combined_gcp_devices': 'numOfCombinedGcpDevices',
        'num_of_aws_devices': 'numOfAWSDevices',
        'number_of_kubernetes_devices': 'numberOfKubernetesDevices',
        'num_of_gcp_devices': 'numOfGcpDevices',
        'num_of_azure_devices': 'numOfAzureDevices',
        'num_of_combined_azure_devices': 'numOfCombinedAzureDevices',
        'num_of_terminated_aws_devices': 'numOfTerminatedAWSDevices',
        'num_of_terminated_gcp_cloud_devices': 'numOfTerminatedGcpCloudDevices',
        'num_of_stopped_aws_devices': 'numOfStoppedAWSDevices',
        'number_of_devices': 'numberOfDevices',
        'num_of_config_source_devices': 'numOfConfigSourceDevices',
        'num_of_websites': 'numOfWebsites',
        'num_of_combined_aws_devices': 'numOfCombinedAWSDevices'
    }

    def __init__(self, num_of_stopped_azure_devices=None, num_of_services=None, num_of_terminated_azure_devices=None, number_of_standard_devices=None, num_of_stopped_gcp_devices=None, num_of_combined_gcp_devices=None, num_of_aws_devices=None, number_of_kubernetes_devices=None, num_of_gcp_devices=None, num_of_azure_devices=None, num_of_combined_azure_devices=None, num_of_terminated_aws_devices=None, num_of_terminated_gcp_cloud_devices=None, num_of_stopped_aws_devices=None, number_of_devices=None, num_of_config_source_devices=None, num_of_websites=None, num_of_combined_aws_devices=None):  # noqa: E501
        """Usage - a model defined in Swagger"""  # noqa: E501
        self._num_of_stopped_azure_devices = None
        self._num_of_services = None
        self._num_of_terminated_azure_devices = None
        self._number_of_standard_devices = None
        self._num_of_stopped_gcp_devices = None
        self._num_of_combined_gcp_devices = None
        self._num_of_aws_devices = None
        self._number_of_kubernetes_devices = None
        self._num_of_gcp_devices = None
        self._num_of_azure_devices = None
        self._num_of_combined_azure_devices = None
        self._num_of_terminated_aws_devices = None
        self._num_of_terminated_gcp_cloud_devices = None
        self._num_of_stopped_aws_devices = None
        self._number_of_devices = None
        self._num_of_config_source_devices = None
        self._num_of_websites = None
        self._num_of_combined_aws_devices = None
        self.discriminator = None
        if num_of_stopped_azure_devices is not None:
            self.num_of_stopped_azure_devices = num_of_stopped_azure_devices
        if num_of_services is not None:
            self.num_of_services = num_of_services
        if num_of_terminated_azure_devices is not None:
            self.num_of_terminated_azure_devices = num_of_terminated_azure_devices
        if number_of_standard_devices is not None:
            self.number_of_standard_devices = number_of_standard_devices
        if num_of_stopped_gcp_devices is not None:
            self.num_of_stopped_gcp_devices = num_of_stopped_gcp_devices
        if num_of_combined_gcp_devices is not None:
            self.num_of_combined_gcp_devices = num_of_combined_gcp_devices
        if num_of_aws_devices is not None:
            self.num_of_aws_devices = num_of_aws_devices
        if number_of_kubernetes_devices is not None:
            self.number_of_kubernetes_devices = number_of_kubernetes_devices
        if num_of_gcp_devices is not None:
            self.num_of_gcp_devices = num_of_gcp_devices
        if num_of_azure_devices is not None:
            self.num_of_azure_devices = num_of_azure_devices
        if num_of_combined_azure_devices is not None:
            self.num_of_combined_azure_devices = num_of_combined_azure_devices
        if num_of_terminated_aws_devices is not None:
            self.num_of_terminated_aws_devices = num_of_terminated_aws_devices
        if num_of_terminated_gcp_cloud_devices is not None:
            self.num_of_terminated_gcp_cloud_devices = num_of_terminated_gcp_cloud_devices
        if num_of_stopped_aws_devices is not None:
            self.num_of_stopped_aws_devices = num_of_stopped_aws_devices
        if number_of_devices is not None:
            self.number_of_devices = number_of_devices
        if num_of_config_source_devices is not None:
            self.num_of_config_source_devices = num_of_config_source_devices
        if num_of_websites is not None:
            self.num_of_websites = num_of_websites
        if num_of_combined_aws_devices is not None:
            self.num_of_combined_aws_devices = num_of_combined_aws_devices

    @property
    def num_of_stopped_azure_devices(self):
        """Gets the num_of_stopped_azure_devices of this Usage.  # noqa: E501

        Number of stopped Azure resources  # noqa: E501

        :return: The num_of_stopped_azure_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_stopped_azure_devices

    @num_of_stopped_azure_devices.setter
    def num_of_stopped_azure_devices(self, num_of_stopped_azure_devices):
        """Sets the num_of_stopped_azure_devices of this Usage.

        Number of stopped Azure resources  # noqa: E501

        :param num_of_stopped_azure_devices: The num_of_stopped_azure_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_stopped_azure_devices = num_of_stopped_azure_devices

    @property
    def num_of_services(self):
        """Gets the num_of_services of this Usage.  # noqa: E501

        Number of services (created via LM Service Insight)  # noqa: E501

        :return: The num_of_services of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_services

    @num_of_services.setter
    def num_of_services(self, num_of_services):
        """Sets the num_of_services of this Usage.

        Number of services (created via LM Service Insight)  # noqa: E501

        :param num_of_services: The num_of_services of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_services = num_of_services

    @property
    def num_of_terminated_azure_devices(self):
        """Gets the num_of_terminated_azure_devices of this Usage.  # noqa: E501

        Number of terminated Azure resources  # noqa: E501

        :return: The num_of_terminated_azure_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_terminated_azure_devices

    @num_of_terminated_azure_devices.setter
    def num_of_terminated_azure_devices(self, num_of_terminated_azure_devices):
        """Sets the num_of_terminated_azure_devices of this Usage.

        Number of terminated Azure resources  # noqa: E501

        :param num_of_terminated_azure_devices: The num_of_terminated_azure_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_terminated_azure_devices = num_of_terminated_azure_devices

    @property
    def number_of_standard_devices(self):
        """Gets the number_of_standard_devices of this Usage.  # noqa: E501

        Number of standard devices  # noqa: E501

        :return: The number_of_standard_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._number_of_standard_devices

    @number_of_standard_devices.setter
    def number_of_standard_devices(self, number_of_standard_devices):
        """Sets the number_of_standard_devices of this Usage.

        Number of standard devices  # noqa: E501

        :param number_of_standard_devices: The number_of_standard_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._number_of_standard_devices = number_of_standard_devices

    @property
    def num_of_stopped_gcp_devices(self):
        """Gets the num_of_stopped_gcp_devices of this Usage.  # noqa: E501

        Number of stopped GCP resources not monitored with a local Collector  # noqa: E501

        :return: The num_of_stopped_gcp_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_stopped_gcp_devices

    @num_of_stopped_gcp_devices.setter
    def num_of_stopped_gcp_devices(self, num_of_stopped_gcp_devices):
        """Sets the num_of_stopped_gcp_devices of this Usage.

        Number of stopped GCP resources not monitored with a local Collector  # noqa: E501

        :param num_of_stopped_gcp_devices: The num_of_stopped_gcp_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_stopped_gcp_devices = num_of_stopped_gcp_devices

    @property
    def num_of_combined_gcp_devices(self):
        """Gets the num_of_combined_gcp_devices of this Usage.  # noqa: E501

        Number of GCP resources monitored with a local Collector  # noqa: E501

        :return: The num_of_combined_gcp_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_combined_gcp_devices

    @num_of_combined_gcp_devices.setter
    def num_of_combined_gcp_devices(self, num_of_combined_gcp_devices):
        """Sets the num_of_combined_gcp_devices of this Usage.

        Number of GCP resources monitored with a local Collector  # noqa: E501

        :param num_of_combined_gcp_devices: The num_of_combined_gcp_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_combined_gcp_devices = num_of_combined_gcp_devices

    @property
    def num_of_aws_devices(self):
        """Gets the num_of_aws_devices of this Usage.  # noqa: E501

        Number of AWS resources not monitored with a local Collector  # noqa: E501

        :return: The num_of_aws_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_aws_devices

    @num_of_aws_devices.setter
    def num_of_aws_devices(self, num_of_aws_devices):
        """Sets the num_of_aws_devices of this Usage.

        Number of AWS resources not monitored with a local Collector  # noqa: E501

        :param num_of_aws_devices: The num_of_aws_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_aws_devices = num_of_aws_devices

    @property
    def number_of_kubernetes_devices(self):
        """Gets the number_of_kubernetes_devices of this Usage.  # noqa: E501

        Number of monitored Kubernetes Nodes, Pods, and Services  # noqa: E501

        :return: The number_of_kubernetes_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._number_of_kubernetes_devices

    @number_of_kubernetes_devices.setter
    def number_of_kubernetes_devices(self, number_of_kubernetes_devices):
        """Sets the number_of_kubernetes_devices of this Usage.

        Number of monitored Kubernetes Nodes, Pods, and Services  # noqa: E501

        :param number_of_kubernetes_devices: The number_of_kubernetes_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._number_of_kubernetes_devices = number_of_kubernetes_devices

    @property
    def num_of_gcp_devices(self):
        """Gets the num_of_gcp_devices of this Usage.  # noqa: E501

        Number of GCP resources  # noqa: E501

        :return: The num_of_gcp_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_gcp_devices

    @num_of_gcp_devices.setter
    def num_of_gcp_devices(self, num_of_gcp_devices):
        """Sets the num_of_gcp_devices of this Usage.

        Number of GCP resources  # noqa: E501

        :param num_of_gcp_devices: The num_of_gcp_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_gcp_devices = num_of_gcp_devices

    @property
    def num_of_azure_devices(self):
        """Gets the num_of_azure_devices of this Usage.  # noqa: E501

        Number of Azure resources not monitored with a local Collector  # noqa: E501

        :return: The num_of_azure_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_azure_devices

    @num_of_azure_devices.setter
    def num_of_azure_devices(self, num_of_azure_devices):
        """Sets the num_of_azure_devices of this Usage.

        Number of Azure resources not monitored with a local Collector  # noqa: E501

        :param num_of_azure_devices: The num_of_azure_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_azure_devices = num_of_azure_devices

    @property
    def num_of_combined_azure_devices(self):
        """Gets the num_of_combined_azure_devices of this Usage.  # noqa: E501

        Number of Azure resources monitored with a local Collector  # noqa: E501

        :return: The num_of_combined_azure_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_combined_azure_devices

    @num_of_combined_azure_devices.setter
    def num_of_combined_azure_devices(self, num_of_combined_azure_devices):
        """Sets the num_of_combined_azure_devices of this Usage.

        Number of Azure resources monitored with a local Collector  # noqa: E501

        :param num_of_combined_azure_devices: The num_of_combined_azure_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_combined_azure_devices = num_of_combined_azure_devices

    @property
    def num_of_terminated_aws_devices(self):
        """Gets the num_of_terminated_aws_devices of this Usage.  # noqa: E501

        Number of terminated AWS resources  # noqa: E501

        :return: The num_of_terminated_aws_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_terminated_aws_devices

    @num_of_terminated_aws_devices.setter
    def num_of_terminated_aws_devices(self, num_of_terminated_aws_devices):
        """Sets the num_of_terminated_aws_devices of this Usage.

        Number of terminated AWS resources  # noqa: E501

        :param num_of_terminated_aws_devices: The num_of_terminated_aws_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_terminated_aws_devices = num_of_terminated_aws_devices

    @property
    def num_of_terminated_gcp_cloud_devices(self):
        """Gets the num_of_terminated_gcp_cloud_devices of this Usage.  # noqa: E501

        Number of terminated GCP resources  # noqa: E501

        :return: The num_of_terminated_gcp_cloud_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_terminated_gcp_cloud_devices

    @num_of_terminated_gcp_cloud_devices.setter
    def num_of_terminated_gcp_cloud_devices(self, num_of_terminated_gcp_cloud_devices):
        """Sets the num_of_terminated_gcp_cloud_devices of this Usage.

        Number of terminated GCP resources  # noqa: E501

        :param num_of_terminated_gcp_cloud_devices: The num_of_terminated_gcp_cloud_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_terminated_gcp_cloud_devices = num_of_terminated_gcp_cloud_devices

    @property
    def num_of_stopped_aws_devices(self):
        """Gets the num_of_stopped_aws_devices of this Usage.  # noqa: E501

        Number of stopped AWS resources  # noqa: E501

        :return: The num_of_stopped_aws_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_stopped_aws_devices

    @num_of_stopped_aws_devices.setter
    def num_of_stopped_aws_devices(self, num_of_stopped_aws_devices):
        """Sets the num_of_stopped_aws_devices of this Usage.

        Number of stopped AWS resources  # noqa: E501

        :param num_of_stopped_aws_devices: The num_of_stopped_aws_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_stopped_aws_devices = num_of_stopped_aws_devices

    @property
    def number_of_devices(self):
        """Gets the number_of_devices of this Usage.  # noqa: E501

        Sum of numOfStandardDevices, numOfCombinedAWSDevices, numOfCombinedAzureDevices, and numOfCombinedGCPDevices  # noqa: E501

        :return: The number_of_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._number_of_devices

    @number_of_devices.setter
    def number_of_devices(self, number_of_devices):
        """Sets the number_of_devices of this Usage.

        Sum of numOfStandardDevices, numOfCombinedAWSDevices, numOfCombinedAzureDevices, and numOfCombinedGCPDevices  # noqa: E501

        :param number_of_devices: The number_of_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._number_of_devices = number_of_devices

    @property
    def num_of_config_source_devices(self):
        """Gets the num_of_config_source_devices of this Usage.  # noqa: E501

        Number of devices with active ConfigSources  # noqa: E501

        :return: The num_of_config_source_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_config_source_devices

    @num_of_config_source_devices.setter
    def num_of_config_source_devices(self, num_of_config_source_devices):
        """Sets the num_of_config_source_devices of this Usage.

        Number of devices with active ConfigSources  # noqa: E501

        :param num_of_config_source_devices: The num_of_config_source_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_config_source_devices = num_of_config_source_devices

    @property
    def num_of_websites(self):
        """Gets the num_of_websites of this Usage.  # noqa: E501

        Number of websites  # noqa: E501

        :return: The num_of_websites of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_websites

    @num_of_websites.setter
    def num_of_websites(self, num_of_websites):
        """Sets the num_of_websites of this Usage.

        Number of websites  # noqa: E501

        :param num_of_websites: The num_of_websites of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_websites = num_of_websites

    @property
    def num_of_combined_aws_devices(self):
        """Gets the num_of_combined_aws_devices of this Usage.  # noqa: E501

        Number of AWS resources monitored with a local Collector  # noqa: E501

        :return: The num_of_combined_aws_devices of this Usage.  # noqa: E501
        :rtype: int
        """
        return self._num_of_combined_aws_devices

    @num_of_combined_aws_devices.setter
    def num_of_combined_aws_devices(self, num_of_combined_aws_devices):
        """Sets the num_of_combined_aws_devices of this Usage.

        Number of AWS resources monitored with a local Collector  # noqa: E501

        :param num_of_combined_aws_devices: The num_of_combined_aws_devices of this Usage.  # noqa: E501
        :type: int
        """

        self._num_of_combined_aws_devices = num_of_combined_aws_devices

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
        if issubclass(Usage, dict):
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
        if not isinstance(other, Usage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
