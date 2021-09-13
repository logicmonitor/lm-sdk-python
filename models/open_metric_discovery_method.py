# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501


class OpenMetricDiscoveryMethod(AutoDiscoveryMethod):
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
        'headers': 'str',
        'metric_name': 'str',
        'read_timeout': 'int',
        'follow_redirect': 'bool',
        'connect_timeout': 'int',
        'group_label': 'str',
        'instance_label': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'headers': 'headers',
        'metric_name': 'metricName',
        'read_timeout': 'readTimeout',
        'follow_redirect': 'followRedirect',
        'connect_timeout': 'connectTimeout',
        'group_label': 'groupLabel',
        'instance_label': 'instanceLabel',
        'url': 'url'
    }

    def __init__(self, name=None, headers=None, metric_name=None, read_timeout=None, follow_redirect=None, connect_timeout=None, group_label=None, instance_label=None, url=None):  # noqa: E501
        """OpenMetricDiscoveryMethod - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._headers = None
        self._metric_name = None
        self._read_timeout = None
        self._follow_redirect = None
        self._connect_timeout = None
        self._group_label = None
        self._instance_label = None
        self._url = None
        self.discriminator = None

        self.name = name
        self.headers = headers
        self.metric_name = metric_name
        if read_timeout is not None:
            self.read_timeout = read_timeout
        self.follow_redirect = follow_redirect
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if group_label is not None:
            self.group_label = group_label
        self.instance_label = instance_label
        self.url = url

    @property
    def name(self):
        """Gets the name of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The name of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenMetricDiscoveryMethod.


        :param name: The name of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def headers(self):
        """Gets the headers of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The headers of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this OpenMetricDiscoveryMethod.


        :param headers: The headers of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if headers is None:
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def metric_name(self):
        """Gets the metric_name of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The metric_name of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this OpenMetricDiscoveryMethod.


        :param metric_name: The metric_name of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def read_timeout(self):
        """Gets the read_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The read_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this OpenMetricDiscoveryMethod.


        :param read_timeout: The read_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: int
        """

        self._read_timeout = read_timeout

    @property
    def follow_redirect(self):
        """Gets the follow_redirect of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The follow_redirect of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirect

    @follow_redirect.setter
    def follow_redirect(self, follow_redirect):
        """Sets the follow_redirect of this OpenMetricDiscoveryMethod.


        :param follow_redirect: The follow_redirect of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: bool
        """
        if follow_redirect is None:
            raise ValueError("Invalid value for `follow_redirect`, must not be `None`")  # noqa: E501

        self._follow_redirect = follow_redirect

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The connect_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this OpenMetricDiscoveryMethod.


        :param connect_timeout: The connect_timeout of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: int
        """

        self._connect_timeout = connect_timeout

    @property
    def group_label(self):
        """Gets the group_label of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The group_label of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._group_label

    @group_label.setter
    def group_label(self, group_label):
        """Sets the group_label of this OpenMetricDiscoveryMethod.


        :param group_label: The group_label of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._group_label = group_label

    @property
    def instance_label(self):
        """Gets the instance_label of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The instance_label of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._instance_label

    @instance_label.setter
    def instance_label(self, instance_label):
        """Sets the instance_label of this OpenMetricDiscoveryMethod.


        :param instance_label: The instance_label of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if instance_label is None:
            raise ValueError("Invalid value for `instance_label`, must not be `None`")  # noqa: E501

        self._instance_label = instance_label

    @property
    def url(self):
        """Gets the url of this OpenMetricDiscoveryMethod.  # noqa: E501


        :return: The url of this OpenMetricDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OpenMetricDiscoveryMethod.


        :param url: The url of this OpenMetricDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(OpenMetricDiscoveryMethod, dict):
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
        if not isinstance(other, OpenMetricDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other