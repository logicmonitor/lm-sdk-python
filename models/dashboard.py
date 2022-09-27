# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.widget_token import WidgetToken  # noqa: F401,E501


class Dashboard(object):
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
        'owner': 'str',
        'template': 'object',
        'user_permission': 'str',
        'group_id': 'int',
        'full_name': 'str',
        'description': 'str',
        'sharable': 'bool',
        'widgets_config': 'object',
        'group_name': 'str',
        'widget_tokens': 'list[WidgetToken]',
        'name': 'str',
        'overwrite_group_fields': 'bool',
        'id': 'int',
        'group_full_path': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'template': 'template',
        'user_permission': 'userPermission',
        'group_id': 'groupId',
        'full_name': 'fullName',
        'description': 'description',
        'sharable': 'sharable',
        'widgets_config': 'widgetsConfig',
        'group_name': 'groupName',
        'widget_tokens': 'widgetTokens',
        'name': 'name',
        'overwrite_group_fields': 'overwriteGroupFields',
        'id': 'id',
        'group_full_path': 'groupFullPath'
    }

    def __init__(self, owner=None, template=None, user_permission=None, group_id=None, full_name=None, description=None, sharable=None, widgets_config=None, group_name=None, widget_tokens=None, name=None, overwrite_group_fields=None, id=None, group_full_path=None):  # noqa: E501
        """Dashboard - a model defined in Swagger"""  # noqa: E501

        self._owner = None
        self._template = None
        self._user_permission = None
        self._group_id = None
        self._full_name = None
        self._description = None
        self._sharable = None
        self._widgets_config = None
        self._group_name = None
        self._widget_tokens = None
        self._name = None
        self._overwrite_group_fields = None
        self._id = None
        self._group_full_path = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if template is not None:
            self.template = template
        if user_permission is not None:
            self.user_permission = user_permission
        if group_id is not None:
            self.group_id = group_id
        if full_name is not None:
            self.full_name = full_name
        if description is not None:
            self.description = description
        if sharable is not None:
            self.sharable = sharable
        if widgets_config is not None:
            self.widgets_config = widgets_config
        if group_name is not None:
            self.group_name = group_name
        if widget_tokens is not None:
            self.widget_tokens = widget_tokens
        self.name = name
        if overwrite_group_fields is not None:
            self.overwrite_group_fields = overwrite_group_fields
        if id is not None:
            self.id = id
        if group_full_path is not None:
            self.group_full_path = group_full_path

    @property
    def owner(self):
        """Gets the owner of this Dashboard.  # noqa: E501

        This field will be empty unless the dashboard is a private dashboard, in which case the owner will be listed  # noqa: E501

        :return: The owner of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Dashboard.

        This field will be empty unless the dashboard is a private dashboard, in which case the owner will be listed  # noqa: E501

        :param owner: The owner of this Dashboard.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def template(self):
        """Gets the template of this Dashboard.  # noqa: E501

        The template which is used for importing dashboard  # noqa: E501

        :return: The template of this Dashboard.  # noqa: E501
        :rtype: object
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this Dashboard.

        The template which is used for importing dashboard  # noqa: E501

        :param template: The template of this Dashboard.  # noqa: E501
        :type: object
        """

        self._template = template

    @property
    def user_permission(self):
        """Gets the user_permission of this Dashboard.  # noqa: E501

        The permission of the user that made the API call  # noqa: E501

        :return: The user_permission of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this Dashboard.

        The permission of the user that made the API call  # noqa: E501

        :param user_permission: The user_permission of this Dashboard.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def group_id(self):
        """Gets the group_id of this Dashboard.  # noqa: E501

        The id of the group the dashboard belongs to  # noqa: E501

        :return: The group_id of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Dashboard.

        The id of the group the dashboard belongs to  # noqa: E501

        :param group_id: The group_id of this Dashboard.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def full_name(self):
        """Gets the full_name of this Dashboard.  # noqa: E501

        Full name of the dashboard, including group path  # noqa: E501

        :return: The full_name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Dashboard.

        Full name of the dashboard, including group path  # noqa: E501

        :param full_name: The full_name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def description(self):
        """Gets the description of this Dashboard.  # noqa: E501

        The description of the dashboard  # noqa: E501

        :return: The description of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Dashboard.

        The description of the dashboard  # noqa: E501

        :param description: The description of this Dashboard.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sharable(self):
        """Gets the sharable of this Dashboard.  # noqa: E501

        Whether or not the dashboard is sharable. This value will always be true unless the dashboard is a private dashboard  # noqa: E501

        :return: The sharable of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable):
        """Sets the sharable of this Dashboard.

        Whether or not the dashboard is sharable. This value will always be true unless the dashboard is a private dashboard  # noqa: E501

        :param sharable: The sharable of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._sharable = sharable

    @property
    def widgets_config(self):
        """Gets the widgets_config of this Dashboard.  # noqa: E501

        Information about widget configuration used by the UI  # noqa: E501

        :return: The widgets_config of this Dashboard.  # noqa: E501
        :rtype: object
        """
        return self._widgets_config

    @widgets_config.setter
    def widgets_config(self, widgets_config):
        """Sets the widgets_config of this Dashboard.

        Information about widget configuration used by the UI  # noqa: E501

        :param widgets_config: The widgets_config of this Dashboard.  # noqa: E501
        :type: object
        """

        self._widgets_config = widgets_config

    @property
    def group_name(self):
        """Gets the group_name of this Dashboard.  # noqa: E501

        The name of group where created dashboard will reside  # noqa: E501

        :return: The group_name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Dashboard.

        The name of group where created dashboard will reside  # noqa: E501

        :param group_name: The group_name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def widget_tokens(self):
        """Gets the widget_tokens of this Dashboard.  # noqa: E501

        If useDynamicWidget=true, this field must at least contain tokens defaultDeviceGroup and defaultServiceGroup  # noqa: E501

        :return: The widget_tokens of this Dashboard.  # noqa: E501
        :rtype: list[WidgetToken]
        """
        return self._widget_tokens

    @widget_tokens.setter
    def widget_tokens(self, widget_tokens):
        """Sets the widget_tokens of this Dashboard.

        If useDynamicWidget=true, this field must at least contain tokens defaultDeviceGroup and defaultServiceGroup  # noqa: E501

        :param widget_tokens: The widget_tokens of this Dashboard.  # noqa: E501
        :type: list[WidgetToken]
        """

        self._widget_tokens = widget_tokens

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501

        The name of the dashboard  # noqa: E501

        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.

        The name of the dashboard  # noqa: E501

        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def overwrite_group_fields(self):
        """Gets the overwrite_group_fields of this Dashboard.  # noqa: E501

        Overwrite existing Resource/Website Group fields with ##defaultResourceGroup## and/or ##defaultWebsiteGroup## tokens. This value of this attribute is only considered while updating the Dashboard configuration. While creating the new Dashboard, this value will always be considered as false irrespective of the passed value.  # noqa: E501

        :return: The overwrite_group_fields of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._overwrite_group_fields

    @overwrite_group_fields.setter
    def overwrite_group_fields(self, overwrite_group_fields):
        """Sets the overwrite_group_fields of this Dashboard.

        Overwrite existing Resource/Website Group fields with ##defaultResourceGroup## and/or ##defaultWebsiteGroup## tokens. This value of this attribute is only considered while updating the Dashboard configuration. While creating the new Dashboard, this value will always be considered as false irrespective of the passed value.  # noqa: E501

        :param overwrite_group_fields: The overwrite_group_fields of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._overwrite_group_fields = overwrite_group_fields

    @property
    def id(self):
        """Gets the id of this Dashboard.  # noqa: E501

        The Id of the dashboard  # noqa: E501

        :return: The id of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dashboard.

        The Id of the dashboard  # noqa: E501

        :param id: The id of this Dashboard.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_full_path(self):
        """Gets the group_full_path of this Dashboard.  # noqa: E501

        The full path (excluding root group) of the group the dashboard belongs to  # noqa: E501

        :return: The group_full_path of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._group_full_path

    @group_full_path.setter
    def group_full_path(self, group_full_path):
        """Sets the group_full_path of this Dashboard.

        The full path (excluding root group) of the group the dashboard belongs to  # noqa: E501

        :param group_full_path: The group_full_path of this Dashboard.  # noqa: E501
        :type: str
        """

        self._group_full_path = group_full_path

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
        if issubclass(Dashboard, dict):
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
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
