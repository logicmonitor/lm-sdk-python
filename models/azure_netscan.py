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

from logicmonitor_sdk.models.exclude_duplicate_ips import ExcludeDuplicateIps  # noqa: F401,E501
from logicmonitor_sdk.models.netscan import Netscan  # noqa: F401,E501
from logicmonitor_sdk.models.rest_schedule import RestSchedule  # noqa: F401,E501


class AzureNetscan(Netscan):
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
        'collector': 'int',
        'collector_description': 'str',
        'collector_group': 'int',
        'collector_group_name': 'str',
        'creator': 'str',
        'description': 'str',
        'duplicate': 'ExcludeDuplicateIps',
        'group': 'str',
        'id': 'int',
        'method': 'str',
        'name': 'str',
        'next_start': 'str',
        'next_start_epoch': 'int',
        'nsg_id': 'int',
        'schedule': 'RestSchedule',
        'version': 'int',
        'azure_az': 'str',
        'azure_service': 'str',
        'client_id': 'str',
        'group_id': 'int',
        'root_name': 'str',
        'secret_key': 'str',
        'subscription_ids': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'collector': 'collector',
        'collector_description': 'collectorDescription',
        'collector_group': 'collectorGroup',
        'collector_group_name': 'collectorGroupName',
        'creator': 'creator',
        'description': 'description',
        'duplicate': 'duplicate',
        'group': 'group',
        'id': 'id',
        'method': 'method',
        'name': 'name',
        'next_start': 'nextStart',
        'next_start_epoch': 'nextStartEpoch',
        'nsg_id': 'nsgId',
        'schedule': 'schedule',
        'version': 'version',
        'azure_az': 'azureAZ',
        'azure_service': 'azureService',
        'client_id': 'clientId',
        'group_id': 'groupId',
        'root_name': 'rootName',
        'secret_key': 'secretKey',
        'subscription_ids': 'subscriptionIds',
        'tenant_id': 'tenantId'
    }

    def __init__(self, collector=None, collector_description=None, collector_group=None, collector_group_name=None, creator=None, description=None, duplicate=None, group=None, id=None, method=None, name=None, next_start=None, next_start_epoch=None, nsg_id=None, schedule=None, version=None, azure_az=None, azure_service=None, client_id=None, group_id=None, root_name=None, secret_key=None, subscription_ids=None, tenant_id=None):  # noqa: E501
        """AzureNetscan - a model defined in Swagger"""  # noqa: E501

        self._collector = None
        self._collector_description = None
        self._collector_group = None
        self._collector_group_name = None
        self._creator = None
        self._description = None
        self._duplicate = None
        self._group = None
        self._id = None
        self._method = None
        self._name = None
        self._next_start = None
        self._next_start_epoch = None
        self._nsg_id = None
        self._schedule = None
        self._version = None
        self._azure_az = None
        self._azure_service = None
        self._client_id = None
        self._group_id = None
        self._root_name = None
        self._secret_key = None
        self._subscription_ids = None
        self._tenant_id = None
        self.discriminator = None

        self.collector = collector
        if collector_description is not None:
            self.collector_description = collector_description
        if collector_group is not None:
            self.collector_group = collector_group
        if collector_group_name is not None:
            self.collector_group_name = collector_group_name
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        self.duplicate = duplicate
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        self.method = method
        self.name = name
        if next_start is not None:
            self.next_start = next_start
        if next_start_epoch is not None:
            self.next_start_epoch = next_start_epoch
        if nsg_id is not None:
            self.nsg_id = nsg_id
        if schedule is not None:
            self.schedule = schedule
        if version is not None:
            self.version = version
        if azure_az is not None:
            self.azure_az = azure_az
        if azure_service is not None:
            self.azure_service = azure_service
        if client_id is not None:
            self.client_id = client_id
        if group_id is not None:
            self.group_id = group_id
        if root_name is not None:
            self.root_name = root_name
        if secret_key is not None:
            self.secret_key = secret_key
        if subscription_ids is not None:
            self.subscription_ids = subscription_ids
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def collector(self):
        """Gets the collector of this AzureNetscan.  # noqa: E501

        The ID of the Collector associated with this Netscan  # noqa: E501

        :return: The collector of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this AzureNetscan.

        The ID of the Collector associated with this Netscan  # noqa: E501

        :param collector: The collector of this AzureNetscan.  # noqa: E501
        :type: int
        """
        if collector is None:
            raise ValueError("Invalid value for `collector`, must not be `None`")  # noqa: E501

        self._collector = collector

    @property
    def collector_description(self):
        """Gets the collector_description of this AzureNetscan.  # noqa: E501

        The description of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_description of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this AzureNetscan.

        The description of the Collector associated with this Netscan  # noqa: E501

        :param collector_description: The collector_description of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def collector_group(self):
        """Gets the collector_group of this AzureNetscan.  # noqa: E501

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector_group

    @collector_group.setter
    def collector_group(self, collector_group):
        """Sets the collector_group of this AzureNetscan.

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group: The collector_group of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._collector_group = collector_group

    @property
    def collector_group_name(self):
        """Gets the collector_group_name of this AzureNetscan.  # noqa: E501

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group_name of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_group_name

    @collector_group_name.setter
    def collector_group_name(self, collector_group_name):
        """Sets the collector_group_name of this AzureNetscan.

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group_name: The collector_group_name of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._collector_group_name = collector_group_name

    @property
    def creator(self):
        """Gets the creator of this AzureNetscan.  # noqa: E501

        The user that created the policy  # noqa: E501

        :return: The creator of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AzureNetscan.

        The user that created the policy  # noqa: E501

        :param creator: The creator of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this AzureNetscan.  # noqa: E501

        The description of the Netscan Policy  # noqa: E501

        :return: The description of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AzureNetscan.

        The description of the Netscan Policy  # noqa: E501

        :param description: The description of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duplicate(self):
        """Gets the duplicate of this AzureNetscan.  # noqa: E501

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :return: The duplicate of this AzureNetscan.  # noqa: E501
        :rtype: ExcludeDuplicateIps
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this AzureNetscan.

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :param duplicate: The duplicate of this AzureNetscan.  # noqa: E501
        :type: ExcludeDuplicateIps
        """
        if duplicate is None:
            raise ValueError("Invalid value for `duplicate`, must not be `None`")  # noqa: E501

        self._duplicate = duplicate

    @property
    def group(self):
        """Gets the group of this AzureNetscan.  # noqa: E501

        The group the Netscan policy should belong to  # noqa: E501

        :return: The group of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this AzureNetscan.

        The group the Netscan policy should belong to  # noqa: E501

        :param group: The group of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def id(self):
        """Gets the id of this AzureNetscan.  # noqa: E501

        The ID of the Netscan Policy  # noqa: E501

        :return: The id of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureNetscan.

        The ID of the Netscan Policy  # noqa: E501

        :param id: The id of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this AzureNetscan.  # noqa: E501

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :return: The method of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this AzureNetscan.

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :param method: The method of this AzureNetscan.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def name(self):
        """Gets the name of this AzureNetscan.  # noqa: E501

        The name of the Netscan Policy  # noqa: E501

        :return: The name of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureNetscan.

        The name of the Netscan Policy  # noqa: E501

        :param name: The name of this AzureNetscan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def next_start(self):
        """Gets the next_start of this AzureNetscan.  # noqa: E501

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :return: The next_start of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._next_start

    @next_start.setter
    def next_start(self, next_start):
        """Sets the next_start of this AzureNetscan.

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :param next_start: The next_start of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._next_start = next_start

    @property
    def next_start_epoch(self):
        """Gets the next_start_epoch of this AzureNetscan.  # noqa: E501

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :return: The next_start_epoch of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._next_start_epoch

    @next_start_epoch.setter
    def next_start_epoch(self, next_start_epoch):
        """Sets the next_start_epoch of this AzureNetscan.

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :param next_start_epoch: The next_start_epoch of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._next_start_epoch = next_start_epoch

    @property
    def nsg_id(self):
        """Gets the nsg_id of this AzureNetscan.  # noqa: E501

        The ID of the group the policy belongs to  # noqa: E501

        :return: The nsg_id of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._nsg_id

    @nsg_id.setter
    def nsg_id(self, nsg_id):
        """Sets the nsg_id of this AzureNetscan.

        The ID of the group the policy belongs to  # noqa: E501

        :param nsg_id: The nsg_id of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._nsg_id = nsg_id

    @property
    def schedule(self):
        """Gets the schedule of this AzureNetscan.  # noqa: E501

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :return: The schedule of this AzureNetscan.  # noqa: E501
        :rtype: RestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AzureNetscan.

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :param schedule: The schedule of this AzureNetscan.  # noqa: E501
        :type: RestSchedule
        """

        self._schedule = schedule

    @property
    def version(self):
        """Gets the version of this AzureNetscan.  # noqa: E501

        The Id of the device  # noqa: E501

        :return: The version of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AzureNetscan.

        The Id of the device  # noqa: E501

        :param version: The version of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def azure_az(self):
        """Gets the azure_az of this AzureNetscan.  # noqa: E501


        :return: The azure_az of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._azure_az

    @azure_az.setter
    def azure_az(self, azure_az):
        """Sets the azure_az of this AzureNetscan.


        :param azure_az: The azure_az of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._azure_az = azure_az

    @property
    def azure_service(self):
        """Gets the azure_service of this AzureNetscan.  # noqa: E501


        :return: The azure_service of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._azure_service

    @azure_service.setter
    def azure_service(self, azure_service):
        """Sets the azure_service of this AzureNetscan.


        :param azure_service: The azure_service of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._azure_service = azure_service

    @property
    def client_id(self):
        """Gets the client_id of this AzureNetscan.  # noqa: E501


        :return: The client_id of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AzureNetscan.


        :param client_id: The client_id of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def group_id(self):
        """Gets the group_id of this AzureNetscan.  # noqa: E501


        :return: The group_id of this AzureNetscan.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AzureNetscan.


        :param group_id: The group_id of this AzureNetscan.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def root_name(self):
        """Gets the root_name of this AzureNetscan.  # noqa: E501


        :return: The root_name of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._root_name

    @root_name.setter
    def root_name(self, root_name):
        """Sets the root_name of this AzureNetscan.


        :param root_name: The root_name of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._root_name = root_name

    @property
    def secret_key(self):
        """Gets the secret_key of this AzureNetscan.  # noqa: E501


        :return: The secret_key of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AzureNetscan.


        :param secret_key: The secret_key of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def subscription_ids(self):
        """Gets the subscription_ids of this AzureNetscan.  # noqa: E501


        :return: The subscription_ids of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """Sets the subscription_ids of this AzureNetscan.


        :param subscription_ids: The subscription_ids of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._subscription_ids = subscription_ids

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureNetscan.  # noqa: E501


        :return: The tenant_id of this AzureNetscan.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureNetscan.


        :param tenant_id: The tenant_id of this AzureNetscan.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if issubclass(AzureNetscan, dict):
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
        if not isinstance(other, AzureNetscan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
