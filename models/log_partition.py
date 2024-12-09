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

class LogPartition(object):
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
        'parent': 'int',
        'user_permission': 'str',
        'criteria': 'str',
        'changelogs': 'list[LogPartitionChangelog]',
        'description': 'str',
        'active': 'bool',
        'paused_at': 'int',
        'priority': 'int',
        'name': 'str',
        'id': 'str',
        'fullname': 'str',
        'tenant': 'str',
        'retention': 'int'
    }

    attribute_map = {
        'parent': 'parent',
        'user_permission': 'userPermission',
        'criteria': 'criteria',
        'changelogs': 'changelogs',
        'description': 'description',
        'active': 'active',
        'paused_at': 'pausedAt',
        'priority': 'priority',
        'name': 'name',
        'id': 'id',
        'fullname': 'fullname',
        'tenant': 'tenant',
        'retention': 'retention'
    }

    def __init__(self, parent=None, user_permission=None, criteria=None, changelogs=None, description=None, active=None, paused_at=None, priority=None, name=None, id=None, fullname=None, tenant=None, retention=None):  # noqa: E501
        """LogPartition - a model defined in Swagger"""  # noqa: E501
        self._parent = None
        self._user_permission = None
        self._criteria = None
        self._changelogs = None
        self._description = None
        self._active = None
        self._paused_at = None
        self._priority = None
        self._name = None
        self._id = None
        self._fullname = None
        self._tenant = None
        self._retention = None
        self.discriminator = None
        if parent is not None:
            self.parent = parent
        if user_permission is not None:
            self.user_permission = user_permission
        if criteria is not None:
            self.criteria = criteria
        if changelogs is not None:
            self.changelogs = changelogs
        if description is not None:
            self.description = description
        self.active = active
        if paused_at is not None:
            self.paused_at = paused_at
        if priority is not None:
            self.priority = priority
        self.name = name
        if id is not None:
            self.id = id
        if fullname is not None:
            self.fullname = fullname
        if tenant is not None:
            self.tenant = tenant
        self.retention = retention

    @property
    def parent(self):
        """Gets the parent of this LogPartition.  # noqa: E501

        Parent Partition Id  # noqa: E501

        :return: The parent of this LogPartition.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this LogPartition.

        Parent Partition Id  # noqa: E501

        :param parent: The parent of this LogPartition.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def user_permission(self):
        """Gets the user_permission of this LogPartition.  # noqa: E501

        Partition user permission  # noqa: E501

        :return: The user_permission of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this LogPartition.

        Partition user permission  # noqa: E501

        :param user_permission: The user_permission of this LogPartition.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def criteria(self):
        """Gets the criteria of this LogPartition.  # noqa: E501

        Partition Criteria  # noqa: E501

        :return: The criteria of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this LogPartition.

        Partition Criteria  # noqa: E501

        :param criteria: The criteria of this LogPartition.  # noqa: E501
        :type: str
        """

        self._criteria = criteria

    @property
    def changelogs(self):
        """Gets the changelogs of this LogPartition.  # noqa: E501


        :return: The changelogs of this LogPartition.  # noqa: E501
        :rtype: list[LogPartitionChangelog]
        """
        return self._changelogs

    @changelogs.setter
    def changelogs(self, changelogs):
        """Sets the changelogs of this LogPartition.


        :param changelogs: The changelogs of this LogPartition.  # noqa: E501
        :type: list[LogPartitionChangelog]
        """

        self._changelogs = changelogs

    @property
    def description(self):
        """Gets the description of this LogPartition.  # noqa: E501

        Partition description  # noqa: E501

        :return: The description of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LogPartition.

        Partition description  # noqa: E501

        :param description: The description of this LogPartition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this LogPartition.  # noqa: E501

        Partition active state  # noqa: E501

        :return: The active of this LogPartition.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this LogPartition.

        Partition active state  # noqa: E501

        :param active: The active of this LogPartition.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def paused_at(self):
        """Gets the paused_at of this LogPartition.  # noqa: E501

        Epoch time when partition was paused  # noqa: E501

        :return: The paused_at of this LogPartition.  # noqa: E501
        :rtype: int
        """
        return self._paused_at

    @paused_at.setter
    def paused_at(self, paused_at):
        """Sets the paused_at of this LogPartition.

        Epoch time when partition was paused  # noqa: E501

        :param paused_at: The paused_at of this LogPartition.  # noqa: E501
        :type: int
        """

        self._paused_at = paused_at

    @property
    def priority(self):
        """Gets the priority of this LogPartition.  # noqa: E501

        Partition Priority  # noqa: E501

        :return: The priority of this LogPartition.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this LogPartition.

        Partition Priority  # noqa: E501

        :param priority: The priority of this LogPartition.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def name(self):
        """Gets the name of this LogPartition.  # noqa: E501

        Partition Name  # noqa: E501

        :return: The name of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogPartition.

        Partition Name  # noqa: E501

        :param name: The name of this LogPartition.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this LogPartition.  # noqa: E501

        Partition Id  # noqa: E501

        :return: The id of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogPartition.

        Partition Id  # noqa: E501

        :param id: The id of this LogPartition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def fullname(self):
        """Gets the fullname of this LogPartition.  # noqa: E501

        Partition Fullname  # noqa: E501

        :return: The fullname of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this LogPartition.

        Partition Fullname  # noqa: E501

        :param fullname: The fullname of this LogPartition.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def tenant(self):
        """Gets the tenant of this LogPartition.  # noqa: E501

        Tenant Name  # noqa: E501

        :return: The tenant of this LogPartition.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this LogPartition.

        Tenant Name  # noqa: E501

        :param tenant: The tenant of this LogPartition.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def retention(self):
        """Gets the retention of this LogPartition.  # noqa: E501

        Partition Retention in days  # noqa: E501

        :return: The retention of this LogPartition.  # noqa: E501
        :rtype: int
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """Sets the retention of this LogPartition.

        Partition Retention in days  # noqa: E501

        :param retention: The retention of this LogPartition.  # noqa: E501
        :type: int
        """
        if retention is None:
            raise ValueError("Invalid value for `retention`, must not be `None`")  # noqa: E501

        self._retention = retention

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
        if issubclass(LogPartition, dict):
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
        if not isinstance(other, LogPartition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
