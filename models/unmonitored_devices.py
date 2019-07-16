# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UnmonitoredDevices(object):
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
        'collector_description': 'str',
        'collector_id': 'int',
        'device_status': 'str',
        'device_type': 'str',
        'display_as': 'str',
        'dns': 'str',
        'end_date': 'str',
        'end_timestamp': 'int',
        'forward_ip': 'str',
        'id': 'int',
        'ip': 'str',
        'manufacturer': 'str',
        'nse_id': 'int',
        'nse_scan_id': 'str',
        'nsp_id': 'int',
        'nsp_name': 'str',
        'ports': 'str',
        'status': 'str',
        'sys_name': 'str'
    }

    attribute_map = {
        'collector_description': 'collectorDescription',
        'collector_id': 'collectorId',
        'device_status': 'deviceStatus',
        'device_type': 'deviceType',
        'display_as': 'displayAs',
        'dns': 'dns',
        'end_date': 'endDate',
        'end_timestamp': 'endTimestamp',
        'forward_ip': 'forwardIp',
        'id': 'id',
        'ip': 'ip',
        'manufacturer': 'manufacturer',
        'nse_id': 'nseId',
        'nse_scan_id': 'nseScanId',
        'nsp_id': 'nspId',
        'nsp_name': 'nspName',
        'ports': 'ports',
        'status': 'status',
        'sys_name': 'sysName'
    }

    def __init__(self, collector_description=None, collector_id=None, device_status=None, device_type=None, display_as=None, dns=None, end_date=None, end_timestamp=None, forward_ip=None, id=None, ip=None, manufacturer=None, nse_id=None, nse_scan_id=None, nsp_id=None, nsp_name=None, ports=None, status=None, sys_name=None):  # noqa: E501
        """UnmonitoredDevices - a model defined in Swagger"""  # noqa: E501

        self._collector_description = None
        self._collector_id = None
        self._device_status = None
        self._device_type = None
        self._display_as = None
        self._dns = None
        self._end_date = None
        self._end_timestamp = None
        self._forward_ip = None
        self._id = None
        self._ip = None
        self._manufacturer = None
        self._nse_id = None
        self._nse_scan_id = None
        self._nsp_id = None
        self._nsp_name = None
        self._ports = None
        self._status = None
        self._sys_name = None
        self.discriminator = None

        if collector_description is not None:
            self.collector_description = collector_description
        if collector_id is not None:
            self.collector_id = collector_id
        if device_status is not None:
            self.device_status = device_status
        if device_type is not None:
            self.device_type = device_type
        if display_as is not None:
            self.display_as = display_as
        if dns is not None:
            self.dns = dns
        if end_date is not None:
            self.end_date = end_date
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if forward_ip is not None:
            self.forward_ip = forward_ip
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if nse_id is not None:
            self.nse_id = nse_id
        if nse_scan_id is not None:
            self.nse_scan_id = nse_scan_id
        if nsp_id is not None:
            self.nsp_id = nsp_id
        if nsp_name is not None:
            self.nsp_name = nsp_name
        if ports is not None:
            self.ports = ports
        if status is not None:
            self.status = status
        if sys_name is not None:
            self.sys_name = sys_name

    @property
    def collector_description(self):
        """Gets the collector_description of this UnmonitoredDevices.  # noqa: E501


        :return: The collector_description of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this UnmonitoredDevices.


        :param collector_description: The collector_description of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def collector_id(self):
        """Gets the collector_id of this UnmonitoredDevices.  # noqa: E501


        :return: The collector_id of this UnmonitoredDevices.  # noqa: E501
        :rtype: int
        """
        return self._collector_id

    @collector_id.setter
    def collector_id(self, collector_id):
        """Sets the collector_id of this UnmonitoredDevices.


        :param collector_id: The collector_id of this UnmonitoredDevices.  # noqa: E501
        :type: int
        """

        self._collector_id = collector_id

    @property
    def device_status(self):
        """Gets the device_status of this UnmonitoredDevices.  # noqa: E501


        :return: The device_status of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """Sets the device_status of this UnmonitoredDevices.


        :param device_status: The device_status of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._device_status = device_status

    @property
    def device_type(self):
        """Gets the device_type of this UnmonitoredDevices.  # noqa: E501


        :return: The device_type of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this UnmonitoredDevices.


        :param device_type: The device_type of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def display_as(self):
        """Gets the display_as of this UnmonitoredDevices.  # noqa: E501


        :return: The display_as of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._display_as

    @display_as.setter
    def display_as(self, display_as):
        """Sets the display_as of this UnmonitoredDevices.


        :param display_as: The display_as of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._display_as = display_as

    @property
    def dns(self):
        """Gets the dns of this UnmonitoredDevices.  # noqa: E501


        :return: The dns of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """Sets the dns of this UnmonitoredDevices.


        :param dns: The dns of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._dns = dns

    @property
    def end_date(self):
        """Gets the end_date of this UnmonitoredDevices.  # noqa: E501


        :return: The end_date of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this UnmonitoredDevices.


        :param end_date: The end_date of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this UnmonitoredDevices.  # noqa: E501


        :return: The end_timestamp of this UnmonitoredDevices.  # noqa: E501
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this UnmonitoredDevices.


        :param end_timestamp: The end_timestamp of this UnmonitoredDevices.  # noqa: E501
        :type: int
        """

        self._end_timestamp = end_timestamp

    @property
    def forward_ip(self):
        """Gets the forward_ip of this UnmonitoredDevices.  # noqa: E501


        :return: The forward_ip of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._forward_ip

    @forward_ip.setter
    def forward_ip(self, forward_ip):
        """Sets the forward_ip of this UnmonitoredDevices.


        :param forward_ip: The forward_ip of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._forward_ip = forward_ip

    @property
    def id(self):
        """Gets the id of this UnmonitoredDevices.  # noqa: E501


        :return: The id of this UnmonitoredDevices.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnmonitoredDevices.


        :param id: The id of this UnmonitoredDevices.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this UnmonitoredDevices.  # noqa: E501


        :return: The ip of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this UnmonitoredDevices.


        :param ip: The ip of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def manufacturer(self):
        """Gets the manufacturer of this UnmonitoredDevices.  # noqa: E501


        :return: The manufacturer of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this UnmonitoredDevices.


        :param manufacturer: The manufacturer of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def nse_id(self):
        """Gets the nse_id of this UnmonitoredDevices.  # noqa: E501


        :return: The nse_id of this UnmonitoredDevices.  # noqa: E501
        :rtype: int
        """
        return self._nse_id

    @nse_id.setter
    def nse_id(self, nse_id):
        """Sets the nse_id of this UnmonitoredDevices.


        :param nse_id: The nse_id of this UnmonitoredDevices.  # noqa: E501
        :type: int
        """

        self._nse_id = nse_id

    @property
    def nse_scan_id(self):
        """Gets the nse_scan_id of this UnmonitoredDevices.  # noqa: E501


        :return: The nse_scan_id of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._nse_scan_id

    @nse_scan_id.setter
    def nse_scan_id(self, nse_scan_id):
        """Sets the nse_scan_id of this UnmonitoredDevices.


        :param nse_scan_id: The nse_scan_id of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._nse_scan_id = nse_scan_id

    @property
    def nsp_id(self):
        """Gets the nsp_id of this UnmonitoredDevices.  # noqa: E501


        :return: The nsp_id of this UnmonitoredDevices.  # noqa: E501
        :rtype: int
        """
        return self._nsp_id

    @nsp_id.setter
    def nsp_id(self, nsp_id):
        """Sets the nsp_id of this UnmonitoredDevices.


        :param nsp_id: The nsp_id of this UnmonitoredDevices.  # noqa: E501
        :type: int
        """

        self._nsp_id = nsp_id

    @property
    def nsp_name(self):
        """Gets the nsp_name of this UnmonitoredDevices.  # noqa: E501


        :return: The nsp_name of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._nsp_name

    @nsp_name.setter
    def nsp_name(self, nsp_name):
        """Sets the nsp_name of this UnmonitoredDevices.


        :param nsp_name: The nsp_name of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._nsp_name = nsp_name

    @property
    def ports(self):
        """Gets the ports of this UnmonitoredDevices.  # noqa: E501


        :return: The ports of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this UnmonitoredDevices.


        :param ports: The ports of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._ports = ports

    @property
    def status(self):
        """Gets the status of this UnmonitoredDevices.  # noqa: E501


        :return: The status of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UnmonitoredDevices.


        :param status: The status of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sys_name(self):
        """Gets the sys_name of this UnmonitoredDevices.  # noqa: E501


        :return: The sys_name of this UnmonitoredDevices.  # noqa: E501
        :rtype: str
        """
        return self._sys_name

    @sys_name.setter
    def sys_name(self, sys_name):
        """Sets the sys_name of this UnmonitoredDevices.


        :param sys_name: The sys_name of this UnmonitoredDevices.  # noqa: E501
        :type: str
        """

        self._sys_name = sys_name

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
        if issubclass(UnmonitoredDevices, dict):
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
        if not isinstance(other, UnmonitoredDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
