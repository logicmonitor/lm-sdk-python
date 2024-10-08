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

class WebPageCollectorAttribute(CollectorAttribute):
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
        'request': 'str',
        'port': 'str',
        'follow_redirect': 'bool',
        'ip': 'str',
        'read_timeout': 'int',
        'connect_timeout': 'int',
        'use_ssl': 'bool'
    }
    if hasattr(CollectorAttribute, "swagger_types"):
        swagger_types.update(CollectorAttribute.swagger_types)

    attribute_map = {
        'request': 'request',
        'port': 'port',
        'follow_redirect': 'followRedirect',
        'ip': 'ip',
        'read_timeout': 'readTimeout',
        'connect_timeout': 'connectTimeout',
        'use_ssl': 'useSSL'
    }
    if hasattr(CollectorAttribute, "attribute_map"):
        attribute_map.update(CollectorAttribute.attribute_map)

    def __init__(self, request=None, port=None, follow_redirect=None, ip=None, read_timeout=None, connect_timeout=None, use_ssl=None, *args, **kwargs):  # noqa: E501
        """WebPageCollectorAttribute - a model defined in Swagger"""  # noqa: E501
        self._request = None
        self._port = None
        self._follow_redirect = None
        self._ip = None
        self._read_timeout = None
        self._connect_timeout = None
        self._use_ssl = None
        self.discriminator = None
        if request is not None:
            self.request = request
        if port is not None:
            self.port = port
        if follow_redirect is not None:
            self.follow_redirect = follow_redirect
        if ip is not None:
            self.ip = ip
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if use_ssl is not None:
            self.use_ssl = use_ssl
        CollectorAttribute.__init__(self, *args, **kwargs)

    @property
    def request(self):
        """Gets the request of this WebPageCollectorAttribute.  # noqa: E501


        :return: The request of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this WebPageCollectorAttribute.


        :param request: The request of this WebPageCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._request = request

    @property
    def port(self):
        """Gets the port of this WebPageCollectorAttribute.  # noqa: E501


        :return: The port of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WebPageCollectorAttribute.


        :param port: The port of this WebPageCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def follow_redirect(self):
        """Gets the follow_redirect of this WebPageCollectorAttribute.  # noqa: E501


        :return: The follow_redirect of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._follow_redirect

    @follow_redirect.setter
    def follow_redirect(self, follow_redirect):
        """Sets the follow_redirect of this WebPageCollectorAttribute.


        :param follow_redirect: The follow_redirect of this WebPageCollectorAttribute.  # noqa: E501
        :type: bool
        """

        self._follow_redirect = follow_redirect

    @property
    def ip(self):
        """Gets the ip of this WebPageCollectorAttribute.  # noqa: E501


        :return: The ip of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this WebPageCollectorAttribute.


        :param ip: The ip of this WebPageCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def read_timeout(self):
        """Gets the read_timeout of this WebPageCollectorAttribute.  # noqa: E501


        :return: The read_timeout of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this WebPageCollectorAttribute.


        :param read_timeout: The read_timeout of this WebPageCollectorAttribute.  # noqa: E501
        :type: int
        """

        self._read_timeout = read_timeout

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this WebPageCollectorAttribute.  # noqa: E501


        :return: The connect_timeout of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this WebPageCollectorAttribute.


        :param connect_timeout: The connect_timeout of this WebPageCollectorAttribute.  # noqa: E501
        :type: int
        """

        self._connect_timeout = connect_timeout

    @property
    def use_ssl(self):
        """Gets the use_ssl of this WebPageCollectorAttribute.  # noqa: E501


        :return: The use_ssl of this WebPageCollectorAttribute.  # noqa: E501
        :rtype: bool
        """
        return self._use_ssl

    @use_ssl.setter
    def use_ssl(self, use_ssl):
        """Sets the use_ssl of this WebPageCollectorAttribute.


        :param use_ssl: The use_ssl of this WebPageCollectorAttribute.  # noqa: E501
        :type: bool
        """

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
        if issubclass(WebPageCollectorAttribute, dict):
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
        if not isinstance(other, WebPageCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
