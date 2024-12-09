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

class RestDNSMappingV3(object):
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
        'end_ip': 'str',
        'start_ip': 'str',
        'collector_description': 'str',
        'dns': 'str',
        'collector_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'end_ip': 'endIp',
        'start_ip': 'startIp',
        'collector_description': 'collectorDescription',
        'dns': 'dns',
        'collector_id': 'collectorId',
        'id': 'id'
    }

    def __init__(self, end_ip=None, start_ip=None, collector_description=None, dns=None, collector_id=None, id=None):  # noqa: E501
        """RestDNSMappingV3 - a model defined in Swagger"""  # noqa: E501
        self._end_ip = None
        self._start_ip = None
        self._collector_description = None
        self._dns = None
        self._collector_id = None
        self._id = None
        self.discriminator = None
        if end_ip is not None:
            self.end_ip = end_ip
        if start_ip is not None:
            self.start_ip = start_ip
        if collector_description is not None:
            self.collector_description = collector_description
        if dns is not None:
            self.dns = dns
        if collector_id is not None:
            self.collector_id = collector_id
        if id is not None:
            self.id = id

    @property
    def end_ip(self):
        """Gets the end_ip of this RestDNSMappingV3.  # noqa: E501


        :return: The end_ip of this RestDNSMappingV3.  # noqa: E501
        :rtype: str
        """
        return self._end_ip

    @end_ip.setter
    def end_ip(self, end_ip):
        """Sets the end_ip of this RestDNSMappingV3.


        :param end_ip: The end_ip of this RestDNSMappingV3.  # noqa: E501
        :type: str
        """

        self._end_ip = end_ip

    @property
    def start_ip(self):
        """Gets the start_ip of this RestDNSMappingV3.  # noqa: E501


        :return: The start_ip of this RestDNSMappingV3.  # noqa: E501
        :rtype: str
        """
        return self._start_ip

    @start_ip.setter
    def start_ip(self, start_ip):
        """Sets the start_ip of this RestDNSMappingV3.


        :param start_ip: The start_ip of this RestDNSMappingV3.  # noqa: E501
        :type: str
        """

        self._start_ip = start_ip

    @property
    def collector_description(self):
        """Gets the collector_description of this RestDNSMappingV3.  # noqa: E501


        :return: The collector_description of this RestDNSMappingV3.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this RestDNSMappingV3.


        :param collector_description: The collector_description of this RestDNSMappingV3.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def dns(self):
        """Gets the dns of this RestDNSMappingV3.  # noqa: E501


        :return: The dns of this RestDNSMappingV3.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this RestDNSMappingV3.


        :param dns: The dns of this RestDNSMappingV3.  # noqa: E501
        :type: str
        """

        self._dns = dns

    @property
    def collector_id(self):
        """Gets the collector_id of this RestDNSMappingV3.  # noqa: E501


        :return: The collector_id of this RestDNSMappingV3.  # noqa: E501
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this RestDNSMappingV3.


        :param collector_id: The collector_id of this RestDNSMappingV3.  # noqa: E501
        :type: int
        """

        self._collector_id = collector_id

    @property
    def id(self):
        """Gets the id of this RestDNSMappingV3.  # noqa: E501


        :return: The id of this RestDNSMappingV3.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RestDNSMappingV3.


        :param id: The id of this RestDNSMappingV3.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(RestDNSMappingV3, dict):
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
        if not isinstance(other, RestDNSMappingV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
