# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GroupData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'num_of_services': 'int',
        'alert_status': 'str',
        'full_path': 'str',
        'stop_monitoring': 'bool',
        'has_services_disabled': 'bool',
        'user_permission': 'str',
        'description': 'str',
        'disable_alerting': 'bool',
        'sdt_status': 'str',
        'name': 'str',
        'num_of_direct_sub_groups': 'int',
        'id': 'int',
        'alert_disable_status': 'str',
        'num_of_direct_services': 'int'
    }

    attribute_map = {
        'num_of_services': 'numOfServices',
        'alert_status': 'alertStatus',
        'full_path': 'fullPath',
        'stop_monitoring': 'stopMonitoring',
        'has_services_disabled': 'hasServicesDisabled',
        'user_permission': 'userPermission',
        'description': 'description',
        'disable_alerting': 'disableAlerting',
        'sdt_status': 'sdtStatus',
        'name': 'name',
        'num_of_direct_sub_groups': 'numOfDirectSubGroups',
        'id': 'id',
        'alert_disable_status': 'alertDisableStatus',
        'num_of_direct_services': 'numOfDirectServices'
    }

    def __init__(self, num_of_services=None, alert_status=None, full_path=None, stop_monitoring=None, has_services_disabled=None, user_permission=None, description=None, disable_alerting=None, sdt_status=None, name=None, num_of_direct_sub_groups=None, id=None, alert_disable_status=None, num_of_direct_services=None):
        """
        GroupData - a model defined in Swagger
        """

        self._num_of_services = None
        self._alert_status = None
        self._full_path = None
        self._stop_monitoring = None
        self._has_services_disabled = None
        self._user_permission = None
        self._description = None
        self._disable_alerting = None
        self._sdt_status = None
        self._name = None
        self._num_of_direct_sub_groups = None
        self._id = None
        self._alert_disable_status = None
        self._num_of_direct_services = None

        if num_of_services is not None:
          self.num_of_services = num_of_services
        if alert_status is not None:
          self.alert_status = alert_status
        if full_path is not None:
          self.full_path = full_path
        if stop_monitoring is not None:
          self.stop_monitoring = stop_monitoring
        if has_services_disabled is not None:
          self.has_services_disabled = has_services_disabled
        if user_permission is not None:
          self.user_permission = user_permission
        if description is not None:
          self.description = description
        if disable_alerting is not None:
          self.disable_alerting = disable_alerting
        if sdt_status is not None:
          self.sdt_status = sdt_status
        if name is not None:
          self.name = name
        if num_of_direct_sub_groups is not None:
          self.num_of_direct_sub_groups = num_of_direct_sub_groups
        if id is not None:
          self.id = id
        if alert_disable_status is not None:
          self.alert_disable_status = alert_disable_status
        if num_of_direct_services is not None:
          self.num_of_direct_services = num_of_direct_services

    @property
    def num_of_services(self):
        """
        Gets the num_of_services of this GroupData.

        :return: The num_of_services of this GroupData.
        :rtype: int
        """
        return self._num_of_services

    @num_of_services.setter
    def num_of_services(self, num_of_services):
        """
        Sets the num_of_services of this GroupData.

        :param num_of_services: The num_of_services of this GroupData.
        :type: int
        """

        self._num_of_services = num_of_services

    @property
    def alert_status(self):
        """
        Gets the alert_status of this GroupData.

        :return: The alert_status of this GroupData.
        :rtype: str
        """
        return self._alert_status

    @alert_status.setter
    def alert_status(self, alert_status):
        """
        Sets the alert_status of this GroupData.

        :param alert_status: The alert_status of this GroupData.
        :type: str
        """

        self._alert_status = alert_status

    @property
    def full_path(self):
        """
        Gets the full_path of this GroupData.

        :return: The full_path of this GroupData.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """
        Sets the full_path of this GroupData.

        :param full_path: The full_path of this GroupData.
        :type: str
        """

        self._full_path = full_path

    @property
    def stop_monitoring(self):
        """
        Gets the stop_monitoring of this GroupData.

        :return: The stop_monitoring of this GroupData.
        :rtype: bool
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """
        Sets the stop_monitoring of this GroupData.

        :param stop_monitoring: The stop_monitoring of this GroupData.
        :type: bool
        """

        self._stop_monitoring = stop_monitoring

    @property
    def has_services_disabled(self):
        """
        Gets the has_services_disabled of this GroupData.

        :return: The has_services_disabled of this GroupData.
        :rtype: bool
        """
        return self._has_services_disabled

    @has_services_disabled.setter
    def has_services_disabled(self, has_services_disabled):
        """
        Sets the has_services_disabled of this GroupData.

        :param has_services_disabled: The has_services_disabled of this GroupData.
        :type: bool
        """

        self._has_services_disabled = has_services_disabled

    @property
    def user_permission(self):
        """
        Gets the user_permission of this GroupData.

        :return: The user_permission of this GroupData.
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """
        Sets the user_permission of this GroupData.

        :param user_permission: The user_permission of this GroupData.
        :type: str
        """

        self._user_permission = user_permission

    @property
    def description(self):
        """
        Gets the description of this GroupData.

        :return: The description of this GroupData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupData.

        :param description: The description of this GroupData.
        :type: str
        """

        self._description = description

    @property
    def disable_alerting(self):
        """
        Gets the disable_alerting of this GroupData.

        :return: The disable_alerting of this GroupData.
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """
        Sets the disable_alerting of this GroupData.

        :param disable_alerting: The disable_alerting of this GroupData.
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def sdt_status(self):
        """
        Gets the sdt_status of this GroupData.

        :return: The sdt_status of this GroupData.
        :rtype: str
        """
        return self._sdt_status

    @sdt_status.setter
    def sdt_status(self, sdt_status):
        """
        Sets the sdt_status of this GroupData.

        :param sdt_status: The sdt_status of this GroupData.
        :type: str
        """

        self._sdt_status = sdt_status

    @property
    def name(self):
        """
        Gets the name of this GroupData.

        :return: The name of this GroupData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupData.

        :param name: The name of this GroupData.
        :type: str
        """

        self._name = name

    @property
    def num_of_direct_sub_groups(self):
        """
        Gets the num_of_direct_sub_groups of this GroupData.

        :return: The num_of_direct_sub_groups of this GroupData.
        :rtype: int
        """
        return self._num_of_direct_sub_groups

    @num_of_direct_sub_groups.setter
    def num_of_direct_sub_groups(self, num_of_direct_sub_groups):
        """
        Sets the num_of_direct_sub_groups of this GroupData.

        :param num_of_direct_sub_groups: The num_of_direct_sub_groups of this GroupData.
        :type: int
        """

        self._num_of_direct_sub_groups = num_of_direct_sub_groups

    @property
    def id(self):
        """
        Gets the id of this GroupData.

        :return: The id of this GroupData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupData.

        :param id: The id of this GroupData.
        :type: int
        """

        self._id = id

    @property
    def alert_disable_status(self):
        """
        Gets the alert_disable_status of this GroupData.

        :return: The alert_disable_status of this GroupData.
        :rtype: str
        """
        return self._alert_disable_status

    @alert_disable_status.setter
    def alert_disable_status(self, alert_disable_status):
        """
        Sets the alert_disable_status of this GroupData.

        :param alert_disable_status: The alert_disable_status of this GroupData.
        :type: str
        """

        self._alert_disable_status = alert_disable_status

    @property
    def num_of_direct_services(self):
        """
        Gets the num_of_direct_services of this GroupData.

        :return: The num_of_direct_services of this GroupData.
        :rtype: int
        """
        return self._num_of_direct_services

    @num_of_direct_services.setter
    def num_of_direct_services(self, num_of_direct_services):
        """
        Sets the num_of_direct_services of this GroupData.

        :param num_of_direct_services: The num_of_direct_services of this GroupData.
        :type: int
        """

        self._num_of_direct_services = num_of_direct_services

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GroupData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other