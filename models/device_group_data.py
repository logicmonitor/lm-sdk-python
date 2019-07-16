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


class DeviceGroupData(object):
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
        'full_path': 'str',
        'group_type': 'str',
        'user_permission': 'str',
        'gcp_regions_info': 'str',
        'description': 'str',
        'applies_to': 'str',
        'aws_regions_info': 'str',
        'num_of_hosts': 'int',
        'name': 'str',
        'num_of_direct_sub_groups': 'int',
        'num_of_direct_devices': 'int',
        'id': 'int',
        'azure_regions_info': 'str'
    }

    attribute_map = {
        'full_path': 'fullPath',
        'group_type': 'groupType',
        'user_permission': 'userPermission',
        'gcp_regions_info': 'gcpRegionsInfo',
        'description': 'description',
        'applies_to': 'appliesTo',
        'aws_regions_info': 'awsRegionsInfo',
        'num_of_hosts': 'numOfHosts',
        'name': 'name',
        'num_of_direct_sub_groups': 'numOfDirectSubGroups',
        'num_of_direct_devices': 'numOfDirectDevices',
        'id': 'id',
        'azure_regions_info': 'azureRegionsInfo'
    }

    def __init__(self, full_path=None, group_type=None, user_permission=None, gcp_regions_info=None, description=None, applies_to=None, aws_regions_info=None, num_of_hosts=None, name=None, num_of_direct_sub_groups=None, num_of_direct_devices=None, id=None, azure_regions_info=None):  # noqa: E501
        """DeviceGroupData - a model defined in Swagger"""  # noqa: E501

        self._full_path = None
        self._group_type = None
        self._user_permission = None
        self._gcp_regions_info = None
        self._description = None
        self._applies_to = None
        self._aws_regions_info = None
        self._num_of_hosts = None
        self._name = None
        self._num_of_direct_sub_groups = None
        self._num_of_direct_devices = None
        self._id = None
        self._azure_regions_info = None
        self.discriminator = None

        if full_path is not None:
            self.full_path = full_path
        if group_type is not None:
            self.group_type = group_type
        if user_permission is not None:
            self.user_permission = user_permission
        if gcp_regions_info is not None:
            self.gcp_regions_info = gcp_regions_info
        if description is not None:
            self.description = description
        if applies_to is not None:
            self.applies_to = applies_to
        if aws_regions_info is not None:
            self.aws_regions_info = aws_regions_info
        if num_of_hosts is not None:
            self.num_of_hosts = num_of_hosts
        if name is not None:
            self.name = name
        if num_of_direct_sub_groups is not None:
            self.num_of_direct_sub_groups = num_of_direct_sub_groups
        if num_of_direct_devices is not None:
            self.num_of_direct_devices = num_of_direct_devices
        if id is not None:
            self.id = id
        if azure_regions_info is not None:
            self.azure_regions_info = azure_regions_info

    @property
    def full_path(self):
        """Gets the full_path of this DeviceGroupData.  # noqa: E501

        The full path of the device group (i.e. if the group 'Dev' is under a parent group named 'Production', the fullPath would be 'Production/Dev'  # noqa: E501

        :return: The full_path of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this DeviceGroupData.

        The full path of the device group (i.e. if the group 'Dev' is under a parent group named 'Production', the fullPath would be 'Production/Dev'  # noqa: E501

        :param full_path: The full_path of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def group_type(self):
        """Gets the group_type of this DeviceGroupData.  # noqa: E501

        The type of device group: normal and dynamic device groups will have groupType=Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3)  # noqa: E501

        :return: The group_type of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this DeviceGroupData.

        The type of device group: normal and dynamic device groups will have groupType=Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3)  # noqa: E501

        :param group_type: The group_type of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def user_permission(self):
        """Gets the user_permission of this DeviceGroupData.  # noqa: E501

        The permissions for the device group that are granted to the user that made this API request  # noqa: E501

        :return: The user_permission of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this DeviceGroupData.

        The permissions for the device group that are granted to the user that made this API request  # noqa: E501

        :param user_permission: The user_permission of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def gcp_regions_info(self):
        """Gets the gcp_regions_info of this DeviceGroupData.  # noqa: E501


        :return: The gcp_regions_info of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._gcp_regions_info

    @gcp_regions_info.setter
    def gcp_regions_info(self, gcp_regions_info):
        """Sets the gcp_regions_info of this DeviceGroupData.


        :param gcp_regions_info: The gcp_regions_info of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._gcp_regions_info = gcp_regions_info

    @property
    def description(self):
        """Gets the description of this DeviceGroupData.  # noqa: E501

        The description of the device group  # noqa: E501

        :return: The description of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceGroupData.

        The description of the device group  # noqa: E501

        :param description: The description of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applies_to(self):
        """Gets the applies_to of this DeviceGroupData.  # noqa: E501

        The Applies to custom query for this group (only for dynamic groups)  # noqa: E501

        :return: The applies_to of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this DeviceGroupData.

        The Applies to custom query for this group (only for dynamic groups)  # noqa: E501

        :param applies_to: The applies_to of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def aws_regions_info(self):
        """Gets the aws_regions_info of this DeviceGroupData.  # noqa: E501

        The number of instances in each AWS region (only applies to AWS groups)  # noqa: E501

        :return: The aws_regions_info of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._aws_regions_info

    @aws_regions_info.setter
    def aws_regions_info(self, aws_regions_info):
        """Sets the aws_regions_info of this DeviceGroupData.

        The number of instances in each AWS region (only applies to AWS groups)  # noqa: E501

        :param aws_regions_info: The aws_regions_info of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._aws_regions_info = aws_regions_info

    @property
    def num_of_hosts(self):
        """Gets the num_of_hosts of this DeviceGroupData.  # noqa: E501

        The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups)  # noqa: E501

        :return: The num_of_hosts of this DeviceGroupData.  # noqa: E501
        :rtype: int
        """
        return self._num_of_hosts

    @num_of_hosts.setter
    def num_of_hosts(self, num_of_hosts):
        """Sets the num_of_hosts of this DeviceGroupData.

        The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups)  # noqa: E501

        :param num_of_hosts: The num_of_hosts of this DeviceGroupData.  # noqa: E501
        :type: int
        """

        self._num_of_hosts = num_of_hosts

    @property
    def name(self):
        """Gets the name of this DeviceGroupData.  # noqa: E501

        The name of the device group  # noqa: E501

        :return: The name of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceGroupData.

        The name of the device group  # noqa: E501

        :param name: The name of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_of_direct_sub_groups(self):
        """Gets the num_of_direct_sub_groups of this DeviceGroupData.  # noqa: E501

        The number of sub-groups that belong only to this device group (doesn't include groups under sub-groups)  # noqa: E501

        :return: The num_of_direct_sub_groups of this DeviceGroupData.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_sub_groups

    @num_of_direct_sub_groups.setter
    def num_of_direct_sub_groups(self, num_of_direct_sub_groups):
        """Sets the num_of_direct_sub_groups of this DeviceGroupData.

        The number of sub-groups that belong only to this device group (doesn't include groups under sub-groups)  # noqa: E501

        :param num_of_direct_sub_groups: The num_of_direct_sub_groups of this DeviceGroupData.  # noqa: E501
        :type: int
        """

        self._num_of_direct_sub_groups = num_of_direct_sub_groups

    @property
    def num_of_direct_devices(self):
        """Gets the num_of_direct_devices of this DeviceGroupData.  # noqa: E501

        The number of AWS and normal devices that belong only to this device group (doesn't include devices in sub-groups)  # noqa: E501

        :return: The num_of_direct_devices of this DeviceGroupData.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_devices

    @num_of_direct_devices.setter
    def num_of_direct_devices(self, num_of_direct_devices):
        """Sets the num_of_direct_devices of this DeviceGroupData.

        The number of AWS and normal devices that belong only to this device group (doesn't include devices in sub-groups)  # noqa: E501

        :param num_of_direct_devices: The num_of_direct_devices of this DeviceGroupData.  # noqa: E501
        :type: int
        """

        self._num_of_direct_devices = num_of_direct_devices

    @property
    def id(self):
        """Gets the id of this DeviceGroupData.  # noqa: E501

        The id of the device group  # noqa: E501

        :return: The id of this DeviceGroupData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceGroupData.

        The id of the device group  # noqa: E501

        :param id: The id of this DeviceGroupData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def azure_regions_info(self):
        """Gets the azure_regions_info of this DeviceGroupData.  # noqa: E501

        The number of instances in each Azure region (only applies to Azure groups)  # noqa: E501

        :return: The azure_regions_info of this DeviceGroupData.  # noqa: E501
        :rtype: str
        """
        return self._azure_regions_info

    @azure_regions_info.setter
    def azure_regions_info(self, azure_regions_info):
        """Sets the azure_regions_info of this DeviceGroupData.

        The number of instances in each Azure region (only applies to Azure groups)  # noqa: E501

        :param azure_regions_info: The azure_regions_info of this DeviceGroupData.  # noqa: E501
        :type: str
        """

        self._azure_regions_info = azure_regions_info

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
        if issubclass(DeviceGroupData, dict):
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
        if not isinstance(other, DeviceGroupData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
