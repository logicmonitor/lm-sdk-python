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

from logicmonitor_sdk.models.netflow_data_base import NetflowDataBase  # noqa: F401,E501


class GroupNetFlowRecord(NetflowDataBase):
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
        'data_type': 'str',
        'src_ip': 'str',
        'percent_usage': 'float',
        'last_epoch_in_sec': 'int',
        'if_out': 'int',
        'usage': 'float',
        'src_asn': 'int',
        'dst_dns': 'str',
        'src_port': 'int',
        'device_display_name': 'str',
        'if_in_display_name': 'str',
        'first_epoch_in_sec': 'int',
        'protocol': 'str',
        'dst_port': 'int',
        'if_in': 'int',
        'source_m_bytes': 'float',
        'src_asn_name': 'str',
        'src_dns': 'str',
        'destination_m_bytes': 'float',
        'dst_asn': 'int',
        'dst_ip': 'str',
        'if_out_display_name': 'str',
        'dest_asn_name': 'str'
    }

    attribute_map = {
        'data_type': 'dataType',
        'src_ip': 'srcIP',
        'percent_usage': 'percentUsage',
        'last_epoch_in_sec': 'lastEpochInSec',
        'if_out': 'ifOut',
        'usage': 'usage',
        'src_asn': 'srcASN',
        'dst_dns': 'dstDNS',
        'src_port': 'srcPort',
        'device_display_name': 'deviceDisplayName',
        'if_in_display_name': 'ifInDisplayName',
        'first_epoch_in_sec': 'firstEpochInSec',
        'protocol': 'protocol',
        'dst_port': 'dstPort',
        'if_in': 'ifIn',
        'source_m_bytes': 'sourceMBytes',
        'src_asn_name': 'srcAsnName',
        'src_dns': 'srcDNS',
        'destination_m_bytes': 'destinationMBytes',
        'dst_asn': 'dstASN',
        'dst_ip': 'dstIP',
        'if_out_display_name': 'ifOutDisplayName',
        'dest_asn_name': 'destAsnName'
    }

    def __init__(self, data_type=None, src_ip=None, percent_usage=None, last_epoch_in_sec=None, if_out=None, usage=None, src_asn=None, dst_dns=None, src_port=None, device_display_name=None, if_in_display_name=None, first_epoch_in_sec=None, protocol=None, dst_port=None, if_in=None, source_m_bytes=None, src_asn_name=None, src_dns=None, destination_m_bytes=None, dst_asn=None, dst_ip=None, if_out_display_name=None, dest_asn_name=None):  # noqa: E501
        """GroupNetFlowRecord - a model defined in Swagger"""  # noqa: E501

        self._data_type = None
        self._src_ip = None
        self._percent_usage = None
        self._last_epoch_in_sec = None
        self._if_out = None
        self._usage = None
        self._src_asn = None
        self._dst_dns = None
        self._src_port = None
        self._device_display_name = None
        self._if_in_display_name = None
        self._first_epoch_in_sec = None
        self._protocol = None
        self._dst_port = None
        self._if_in = None
        self._source_m_bytes = None
        self._src_asn_name = None
        self._src_dns = None
        self._destination_m_bytes = None
        self._dst_asn = None
        self._dst_ip = None
        self._if_out_display_name = None
        self._dest_asn_name = None
        self.discriminator = None

        if data_type is not None:
            self.data_type = data_type
        if src_ip is not None:
            self.src_ip = src_ip
        if percent_usage is not None:
            self.percent_usage = percent_usage
        if last_epoch_in_sec is not None:
            self.last_epoch_in_sec = last_epoch_in_sec
        if if_out is not None:
            self.if_out = if_out
        if usage is not None:
            self.usage = usage
        if src_asn is not None:
            self.src_asn = src_asn
        if dst_dns is not None:
            self.dst_dns = dst_dns
        if src_port is not None:
            self.src_port = src_port
        if device_display_name is not None:
            self.device_display_name = device_display_name
        if if_in_display_name is not None:
            self.if_in_display_name = if_in_display_name
        if first_epoch_in_sec is not None:
            self.first_epoch_in_sec = first_epoch_in_sec
        if protocol is not None:
            self.protocol = protocol
        if dst_port is not None:
            self.dst_port = dst_port
        if if_in is not None:
            self.if_in = if_in
        if source_m_bytes is not None:
            self.source_m_bytes = source_m_bytes
        if src_asn_name is not None:
            self.src_asn_name = src_asn_name
        if src_dns is not None:
            self.src_dns = src_dns
        if destination_m_bytes is not None:
            self.destination_m_bytes = destination_m_bytes
        if dst_asn is not None:
            self.dst_asn = dst_asn
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if if_out_display_name is not None:
            self.if_out_display_name = if_out_display_name
        if dest_asn_name is not None:
            self.dest_asn_name = dest_asn_name

    @property
    def data_type(self):
        """Gets the data_type of this GroupNetFlowRecord.  # noqa: E501


        :return: The data_type of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this GroupNetFlowRecord.


        :param data_type: The data_type of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def src_ip(self):
        """Gets the src_ip of this GroupNetFlowRecord.  # noqa: E501

        the source ip of flow record  # noqa: E501

        :return: The src_ip of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this GroupNetFlowRecord.

        the source ip of flow record  # noqa: E501

        :param src_ip: The src_ip of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._src_ip = src_ip

    @property
    def percent_usage(self):
        """Gets the percent_usage of this GroupNetFlowRecord.  # noqa: E501

        the percent traffic of the flow record  # noqa: E501

        :return: The percent_usage of this GroupNetFlowRecord.  # noqa: E501
        :rtype: float
        """
        return self._percent_usage

    @percent_usage.setter
    def percent_usage(self, percent_usage):
        """Sets the percent_usage of this GroupNetFlowRecord.

        the percent traffic of the flow record  # noqa: E501

        :param percent_usage: The percent_usage of this GroupNetFlowRecord.  # noqa: E501
        :type: float
        """

        self._percent_usage = percent_usage

    @property
    def last_epoch_in_sec(self):
        """Gets the last_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501

        the end time  of this flow record  # noqa: E501

        :return: The last_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._last_epoch_in_sec

    @last_epoch_in_sec.setter
    def last_epoch_in_sec(self, last_epoch_in_sec):
        """Sets the last_epoch_in_sec of this GroupNetFlowRecord.

        the end time  of this flow record  # noqa: E501

        :param last_epoch_in_sec: The last_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._last_epoch_in_sec = last_epoch_in_sec

    @property
    def if_out(self):
        """Gets the if_out of this GroupNetFlowRecord.  # noqa: E501

        the out interface of this flow record  # noqa: E501

        :return: The if_out of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._if_out

    @if_out.setter
    def if_out(self, if_out):
        """Sets the if_out of this GroupNetFlowRecord.

        the out interface of this flow record  # noqa: E501

        :param if_out: The if_out of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._if_out = if_out

    @property
    def usage(self):
        """Gets the usage of this GroupNetFlowRecord.  # noqa: E501

        the total bytes of this flow record (source bytes + destination bytes)  # noqa: E501

        :return: The usage of this GroupNetFlowRecord.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this GroupNetFlowRecord.

        the total bytes of this flow record (source bytes + destination bytes)  # noqa: E501

        :param usage: The usage of this GroupNetFlowRecord.  # noqa: E501
        :type: float
        """

        self._usage = usage

    @property
    def src_asn(self):
        """Gets the src_asn of this GroupNetFlowRecord.  # noqa: E501

        source autonomous system number  # noqa: E501

        :return: The src_asn of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._src_asn

    @src_asn.setter
    def src_asn(self, src_asn):
        """Sets the src_asn of this GroupNetFlowRecord.

        source autonomous system number  # noqa: E501

        :param src_asn: The src_asn of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._src_asn = src_asn

    @property
    def dst_dns(self):
        """Gets the dst_dns of this GroupNetFlowRecord.  # noqa: E501

        the dns name of destination ip  # noqa: E501

        :return: The dst_dns of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._dst_dns

    @dst_dns.setter
    def dst_dns(self, dst_dns):
        """Sets the dst_dns of this GroupNetFlowRecord.

        the dns name of destination ip  # noqa: E501

        :param dst_dns: The dst_dns of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._dst_dns = dst_dns

    @property
    def src_port(self):
        """Gets the src_port of this GroupNetFlowRecord.  # noqa: E501

        the source port of the flow record  # noqa: E501

        :return: The src_port of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this GroupNetFlowRecord.

        the source port of the flow record  # noqa: E501

        :param src_port: The src_port of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._src_port = src_port

    @property
    def device_display_name(self):
        """Gets the device_display_name of this GroupNetFlowRecord.  # noqa: E501


        :return: The device_display_name of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this GroupNetFlowRecord.


        :param device_display_name: The device_display_name of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

    @property
    def if_in_display_name(self):
        """Gets the if_in_display_name of this GroupNetFlowRecord.  # noqa: E501


        :return: The if_in_display_name of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._if_in_display_name

    @if_in_display_name.setter
    def if_in_display_name(self, if_in_display_name):
        """Sets the if_in_display_name of this GroupNetFlowRecord.


        :param if_in_display_name: The if_in_display_name of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._if_in_display_name = if_in_display_name

    @property
    def first_epoch_in_sec(self):
        """Gets the first_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501

        the start time of this flow record  # noqa: E501

        :return: The first_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._first_epoch_in_sec

    @first_epoch_in_sec.setter
    def first_epoch_in_sec(self, first_epoch_in_sec):
        """Sets the first_epoch_in_sec of this GroupNetFlowRecord.

        the start time of this flow record  # noqa: E501

        :param first_epoch_in_sec: The first_epoch_in_sec of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._first_epoch_in_sec = first_epoch_in_sec

    @property
    def protocol(self):
        """Gets the protocol of this GroupNetFlowRecord.  # noqa: E501

        the protocol name of this flow record  # noqa: E501

        :return: The protocol of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this GroupNetFlowRecord.

        the protocol name of this flow record  # noqa: E501

        :param protocol: The protocol of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def dst_port(self):
        """Gets the dst_port of this GroupNetFlowRecord.  # noqa: E501

        the destination port  # noqa: E501

        :return: The dst_port of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this GroupNetFlowRecord.

        the destination port  # noqa: E501

        :param dst_port: The dst_port of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._dst_port = dst_port

    @property
    def if_in(self):
        """Gets the if_in of this GroupNetFlowRecord.  # noqa: E501

        the in interface of this flow record  # noqa: E501

        :return: The if_in of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._if_in

    @if_in.setter
    def if_in(self, if_in):
        """Sets the if_in of this GroupNetFlowRecord.

        the in interface of this flow record  # noqa: E501

        :param if_in: The if_in of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._if_in = if_in

    @property
    def source_m_bytes(self):
        """Gets the source_m_bytes of this GroupNetFlowRecord.  # noqa: E501

        the source bytes of this flow record  # noqa: E501

        :return: The source_m_bytes of this GroupNetFlowRecord.  # noqa: E501
        :rtype: float
        """
        return self._source_m_bytes

    @source_m_bytes.setter
    def source_m_bytes(self, source_m_bytes):
        """Sets the source_m_bytes of this GroupNetFlowRecord.

        the source bytes of this flow record  # noqa: E501

        :param source_m_bytes: The source_m_bytes of this GroupNetFlowRecord.  # noqa: E501
        :type: float
        """

        self._source_m_bytes = source_m_bytes

    @property
    def src_asn_name(self):
        """Gets the src_asn_name of this GroupNetFlowRecord.  # noqa: E501

        the name of src ASN number  # noqa: E501

        :return: The src_asn_name of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._src_asn_name

    @src_asn_name.setter
    def src_asn_name(self, src_asn_name):
        """Sets the src_asn_name of this GroupNetFlowRecord.

        the name of src ASN number  # noqa: E501

        :param src_asn_name: The src_asn_name of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._src_asn_name = src_asn_name

    @property
    def src_dns(self):
        """Gets the src_dns of this GroupNetFlowRecord.  # noqa: E501

        the dns name of source ip  # noqa: E501

        :return: The src_dns of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._src_dns

    @src_dns.setter
    def src_dns(self, src_dns):
        """Sets the src_dns of this GroupNetFlowRecord.

        the dns name of source ip  # noqa: E501

        :param src_dns: The src_dns of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._src_dns = src_dns

    @property
    def destination_m_bytes(self):
        """Gets the destination_m_bytes of this GroupNetFlowRecord.  # noqa: E501

        the destination byte of this flow record  # noqa: E501

        :return: The destination_m_bytes of this GroupNetFlowRecord.  # noqa: E501
        :rtype: float
        """
        return self._destination_m_bytes

    @destination_m_bytes.setter
    def destination_m_bytes(self, destination_m_bytes):
        """Sets the destination_m_bytes of this GroupNetFlowRecord.

        the destination byte of this flow record  # noqa: E501

        :param destination_m_bytes: The destination_m_bytes of this GroupNetFlowRecord.  # noqa: E501
        :type: float
        """

        self._destination_m_bytes = destination_m_bytes

    @property
    def dst_asn(self):
        """Gets the dst_asn of this GroupNetFlowRecord.  # noqa: E501

        destination autonomous system number  # noqa: E501

        :return: The dst_asn of this GroupNetFlowRecord.  # noqa: E501
        :rtype: int
        """
        return self._dst_asn

    @dst_asn.setter
    def dst_asn(self, dst_asn):
        """Sets the dst_asn of this GroupNetFlowRecord.

        destination autonomous system number  # noqa: E501

        :param dst_asn: The dst_asn of this GroupNetFlowRecord.  # noqa: E501
        :type: int
        """

        self._dst_asn = dst_asn

    @property
    def dst_ip(self):
        """Gets the dst_ip of this GroupNetFlowRecord.  # noqa: E501

        the destination ip of the flow record  # noqa: E501

        :return: The dst_ip of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this GroupNetFlowRecord.

        the destination ip of the flow record  # noqa: E501

        :param dst_ip: The dst_ip of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._dst_ip = dst_ip

    @property
    def if_out_display_name(self):
        """Gets the if_out_display_name of this GroupNetFlowRecord.  # noqa: E501


        :return: The if_out_display_name of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._if_out_display_name

    @if_out_display_name.setter
    def if_out_display_name(self, if_out_display_name):
        """Sets the if_out_display_name of this GroupNetFlowRecord.


        :param if_out_display_name: The if_out_display_name of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._if_out_display_name = if_out_display_name

    @property
    def dest_asn_name(self):
        """Gets the dest_asn_name of this GroupNetFlowRecord.  # noqa: E501

        the name of dest ASN number  # noqa: E501

        :return: The dest_asn_name of this GroupNetFlowRecord.  # noqa: E501
        :rtype: str
        """
        return self._dest_asn_name

    @dest_asn_name.setter
    def dest_asn_name(self, dest_asn_name):
        """Sets the dest_asn_name of this GroupNetFlowRecord.

        the name of dest ASN number  # noqa: E501

        :param dest_asn_name: The dest_asn_name of this GroupNetFlowRecord.  # noqa: E501
        :type: str
        """

        self._dest_asn_name = dest_asn_name

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
        if issubclass(GroupNetFlowRecord, dict):
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
        if not isinstance(other, GroupNetFlowRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
