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
from logicmonitor_sdk.models.netscan import Netscan  # noqa: F401,E501

class Ec2Netscan(Netscan):
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
        'ddr': 'Ec2DDR',
        'credentials': 'EC2NetscanPolicyCredential',
        'accessibility': 'str',
        'dead_operation': 'str',
        'ports': 'RestNetscanPorts'
    }
    if hasattr(Netscan, "swagger_types"):
        swagger_types.update(Netscan.swagger_types)

    attribute_map = {
        'ddr': 'ddr',
        'credentials': 'credentials',
        'accessibility': 'accessibility',
        'dead_operation': 'deadOperation',
        'ports': 'ports'
    }
    if hasattr(Netscan, "attribute_map"):
        attribute_map.update(Netscan.attribute_map)

    def __init__(self, ddr=None, credentials=None, accessibility=None, dead_operation=None, ports=None, *args, **kwargs):  # noqa: E501
        """Ec2Netscan - a model defined in Swagger"""  # noqa: E501
        self._ddr = None
        self._credentials = None
        self._accessibility = None
        self._dead_operation = None
        self._ports = None
        self.discriminator = None
        if ddr is not None:
            self.ddr = ddr
        self.credentials = credentials
        self.accessibility = accessibility
        if dead_operation is not None:
            self.dead_operation = dead_operation
        if ports is not None:
            self.ports = ports
        Netscan.__init__(self, *args, **kwargs)

    @property
    def ddr(self):
        """Gets the ddr of this Ec2Netscan.  # noqa: E501


        :return: The ddr of this Ec2Netscan.  # noqa: E501
        :rtype: Ec2DDR
        """
        return self._ddr

    @ddr.setter
    def ddr(self, ddr):
        """Sets the ddr of this Ec2Netscan.


        :param ddr: The ddr of this Ec2Netscan.  # noqa: E501
        :type: Ec2DDR
        """

        self._ddr = ddr

    @property
    def credentials(self):
        """Gets the credentials of this Ec2Netscan.  # noqa: E501


        :return: The credentials of this Ec2Netscan.  # noqa: E501
        :rtype: EC2NetscanPolicyCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Ec2Netscan.


        :param credentials: The credentials of this Ec2Netscan.  # noqa: E501
        :type: EC2NetscanPolicyCredential
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def accessibility(self):
        """Gets the accessibility of this Ec2Netscan.  # noqa: E501

        Which IP the EC2 instance should be monitored with for nec2 scans: private or public  # noqa: E501

        :return: The accessibility of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this Ec2Netscan.

        Which IP the EC2 instance should be monitored with for nec2 scans: private or public  # noqa: E501

        :param accessibility: The accessibility of this Ec2Netscan.  # noqa: E501
        :type: str
        """
        if accessibility is None:
            raise ValueError("Invalid value for `accessibility`, must not be `None`")  # noqa: E501

        self._accessibility = accessibility

    @property
    def dead_operation(self):
        """Gets the dead_operation of this Ec2Netscan.  # noqa: E501

        How dead EC2 instances should be handled for nec2 scans. Must be Manually  # noqa: E501

        :return: The dead_operation of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._dead_operation

    @dead_operation.setter
    def dead_operation(self, dead_operation):
        """Sets the dead_operation of this Ec2Netscan.

        How dead EC2 instances should be handled for nec2 scans. Must be Manually  # noqa: E501

        :param dead_operation: The dead_operation of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._dead_operation = dead_operation

    @property
    def ports(self):
        """Gets the ports of this Ec2Netscan.  # noqa: E501


        :return: The ports of this Ec2Netscan.  # noqa: E501
        :rtype: RestNetscanPorts
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Ec2Netscan.


        :param ports: The ports of this Ec2Netscan.  # noqa: E501
        :type: RestNetscanPorts
        """

        self._ports = ports

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
        if issubclass(Ec2Netscan, dict):
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
        if not isinstance(other, Ec2Netscan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
