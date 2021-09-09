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

from logicmonitor_sdk.models.name_and_value import NameAndValue  # noqa: F401,E501


class CollectorGroup(object):
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
        'auto_balance': 'str',
        'custom_properties': 'list[NameAndValue]',
        'user_permission': 'str',
        'num_of_collectors': 'int',
        'name': 'str',
        'auto_balance_instance_count_threshold': 'int',
        'auto_balance_strategy': 'str',
        'description': 'str',
        'create_on': 'int',
        'id': 'int'
    }

    attribute_map = {
        'auto_balance': 'autoBalance',
        'custom_properties': 'customProperties',
        'user_permission': 'userPermission',
        'num_of_collectors': 'numOfCollectors',
        'name': 'name',
        'auto_balance_instance_count_threshold': 'autoBalanceInstanceCountThreshold',
        'auto_balance_strategy': 'autoBalanceStrategy',
        'description': 'description',
        'create_on': 'createOn',
        'id': 'id'
    }

    def __init__(self, auto_balance=None, custom_properties=None, user_permission=None, num_of_collectors=None, name=None, auto_balance_instance_count_threshold=None, auto_balance_strategy=None, description=None, create_on=None, id=None):  # noqa: E501
        """CollectorGroup - a model defined in Swagger"""  # noqa: E501

        self._auto_balance = None
        self._custom_properties = None
        self._user_permission = None
        self._num_of_collectors = None
        self._name = None
        self._auto_balance_instance_count_threshold = None
        self._auto_balance_strategy = None
        self._description = None
        self._create_on = None
        self._id = None
        self.discriminator = None

        if auto_balance is not None:
            self.auto_balance = auto_balance
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if user_permission is not None:
            self.user_permission = user_permission
        if num_of_collectors is not None:
            self.num_of_collectors = num_of_collectors
        self.name = name
        if auto_balance_instance_count_threshold is not None:
            self.auto_balance_instance_count_threshold = auto_balance_instance_count_threshold
        if auto_balance_strategy is not None:
            self.auto_balance_strategy = auto_balance_strategy
        if description is not None:
            self.description = description
        if create_on is not None:
            self.create_on = create_on
        if id is not None:
            self.id = id

    @property
    def auto_balance(self):
        """Gets the auto_balance of this CollectorGroup.  # noqa: E501

        if the collector is autoBalance set as true or false  # noqa: E501

        :return: The auto_balance of this CollectorGroup.  # noqa: E501
        :rtype: str
        """
        return self._auto_balance

    @auto_balance.setter
    def auto_balance(self, auto_balance):
        """Sets the auto_balance of this CollectorGroup.

        if the collector is autoBalance set as true or false  # noqa: E501

        :param auto_balance: The auto_balance of this CollectorGroup.  # noqa: E501
        :type: str
        """

        self._auto_balance = auto_balance

    @property
    def custom_properties(self):
        """Gets the custom_properties of this CollectorGroup.  # noqa: E501

        The custom properties defined for the Collector group  # noqa: E501

        :return: The custom_properties of this CollectorGroup.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this CollectorGroup.

        The custom properties defined for the Collector group  # noqa: E501

        :param custom_properties: The custom_properties of this CollectorGroup.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._custom_properties = custom_properties

    @property
    def user_permission(self):
        """Gets the user_permission of this CollectorGroup.  # noqa: E501

        The permission level of the user that made the API request  # noqa: E501

        :return: The user_permission of this CollectorGroup.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this CollectorGroup.

        The permission level of the user that made the API request  # noqa: E501

        :param user_permission: The user_permission of this CollectorGroup.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def num_of_collectors(self):
        """Gets the num_of_collectors of this CollectorGroup.  # noqa: E501

        The number of Collectors that belong to the group  # noqa: E501

        :return: The num_of_collectors of this CollectorGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_collectors

    @num_of_collectors.setter
    def num_of_collectors(self, num_of_collectors):
        """Sets the num_of_collectors of this CollectorGroup.

        The number of Collectors that belong to the group  # noqa: E501

        :param num_of_collectors: The num_of_collectors of this CollectorGroup.  # noqa: E501
        :type: int
        """

        self._num_of_collectors = num_of_collectors

    @property
    def name(self):
        """Gets the name of this CollectorGroup.  # noqa: E501

        The name of the Collector Group  # noqa: E501

        :return: The name of this CollectorGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectorGroup.

        The name of the Collector Group  # noqa: E501

        :param name: The name of this CollectorGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def auto_balance_instance_count_threshold(self):
        """Gets the auto_balance_instance_count_threshold of this CollectorGroup.  # noqa: E501

        threshold for instance count strategy to check if a collector has high load  # noqa: E501

        :return: The auto_balance_instance_count_threshold of this CollectorGroup.  # noqa: E501
        :rtype: int
        """
        return self._auto_balance_instance_count_threshold

    @auto_balance_instance_count_threshold.setter
    def auto_balance_instance_count_threshold(self, auto_balance_instance_count_threshold):
        """Sets the auto_balance_instance_count_threshold of this CollectorGroup.

        threshold for instance count strategy to check if a collector has high load  # noqa: E501

        :param auto_balance_instance_count_threshold: The auto_balance_instance_count_threshold of this CollectorGroup.  # noqa: E501
        :type: int
        """

        self._auto_balance_instance_count_threshold = auto_balance_instance_count_threshold

    @property
    def auto_balance_strategy(self):
        """Gets the auto_balance_strategy of this CollectorGroup.  # noqa: E501

        the auto balance strategy   # noqa: E501

        :return: The auto_balance_strategy of this CollectorGroup.  # noqa: E501
        :rtype: str
        """
        return self._auto_balance_strategy

    @auto_balance_strategy.setter
    def auto_balance_strategy(self, auto_balance_strategy):
        """Sets the auto_balance_strategy of this CollectorGroup.

        the auto balance strategy   # noqa: E501

        :param auto_balance_strategy: The auto_balance_strategy of this CollectorGroup.  # noqa: E501
        :type: str
        """

        self._auto_balance_strategy = auto_balance_strategy

    @property
    def description(self):
        """Gets the description of this CollectorGroup.  # noqa: E501

        The description of the Collector Group  # noqa: E501

        :return: The description of this CollectorGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CollectorGroup.

        The description of the Collector Group  # noqa: E501

        :param description: The description of this CollectorGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def create_on(self):
        """Gets the create_on of this CollectorGroup.  # noqa: E501

        The time at which the group was created, in epoch format  # noqa: E501

        :return: The create_on of this CollectorGroup.  # noqa: E501
        :rtype: int
        """
        return self._create_on

    @create_on.setter
    def create_on(self, create_on):
        """Sets the create_on of this CollectorGroup.

        The time at which the group was created, in epoch format  # noqa: E501

        :param create_on: The create_on of this CollectorGroup.  # noqa: E501
        :type: int
        """

        self._create_on = create_on

    @property
    def id(self):
        """Gets the id of this CollectorGroup.  # noqa: E501

        The id of the Collector Group  # noqa: E501

        :return: The id of this CollectorGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectorGroup.

        The id of the Collector Group  # noqa: E501

        :param id: The id of this CollectorGroup.  # noqa: E501
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
        if issubclass(CollectorGroup, dict):
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
        if not isinstance(other, CollectorGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
