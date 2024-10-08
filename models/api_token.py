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

class APIToken(object):
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
        'note': 'str',
        'last_used_on': 'int',
        'user_permission': 'str',
        'roles': 'list[str]',
        'created_on': 'int',
        'access_id': 'str',
        'admin_name': 'str',
        'last_auth_ip': 'str',
        'access_key': 'str',
        'created_by': 'str',
        'admin_id': 'int',
        'id': 'int',
        'status': 'int'
    }

    attribute_map = {
        'note': 'note',
        'last_used_on': 'lastUsedOn',
        'user_permission': 'userPermission',
        'roles': 'roles',
        'created_on': 'createdOn',
        'access_id': 'accessId',
        'admin_name': 'adminName',
        'last_auth_ip': 'lastAuthIp',
        'access_key': 'accessKey',
        'created_by': 'createdBy',
        'admin_id': 'adminId',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, note=None, last_used_on=None, user_permission=None, roles=None, created_on=None, access_id=None, admin_name=None, last_auth_ip=None, access_key=None, created_by=None, admin_id=None, id=None, status=None):  # noqa: E501
        """APIToken - a model defined in Swagger"""  # noqa: E501
        self._note = None
        self._last_used_on = None
        self._user_permission = None
        self._roles = None
        self._created_on = None
        self._access_id = None
        self._admin_name = None
        self._last_auth_ip = None
        self._access_key = None
        self._created_by = None
        self._admin_id = None
        self._id = None
        self._status = None
        self.discriminator = None
        if note is not None:
            self.note = note
        if last_used_on is not None:
            self.last_used_on = last_used_on
        if user_permission is not None:
            self.user_permission = user_permission
        if roles is not None:
            self.roles = roles
        if created_on is not None:
            self.created_on = created_on
        if access_id is not None:
            self.access_id = access_id
        if admin_name is not None:
            self.admin_name = admin_name
        if last_auth_ip is not None:
            self.last_auth_ip = last_auth_ip
        if access_key is not None:
            self.access_key = access_key
        if created_by is not None:
            self.created_by = created_by
        if admin_id is not None:
            self.admin_id = admin_id
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def note(self):
        """Gets the note of this APIToken.  # noqa: E501

        The note associated with the API Tokens  # noqa: E501

        :return: The note of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this APIToken.

        The note associated with the API Tokens  # noqa: E501

        :param note: The note of this APIToken.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def last_used_on(self):
        """Gets the last_used_on of this APIToken.  # noqa: E501

        The epoch at which the API Tokens were last used  # noqa: E501

        :return: The last_used_on of this APIToken.  # noqa: E501
        :rtype: int
        """
        return self._last_used_on

    @last_used_on.setter
    def last_used_on(self, last_used_on):
        """Sets the last_used_on of this APIToken.

        The epoch at which the API Tokens were last used  # noqa: E501

        :param last_used_on: The last_used_on of this APIToken.  # noqa: E501
        :type: int
        """

        self._last_used_on = last_used_on

    @property
    def user_permission(self):
        """Gets the user_permission of this APIToken.  # noqa: E501

        The permission of current apiToken with the admin. The values can be write|read|none  # noqa: E501

        :return: The user_permission of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this APIToken.

        The permission of current apiToken with the admin. The values can be write|read|none  # noqa: E501

        :param user_permission: The user_permission of this APIToken.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def roles(self):
        """Gets the roles of this APIToken.  # noqa: E501

        The roles assigned to the user that is associated with the API Tokens  # noqa: E501

        :return: The roles of this APIToken.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this APIToken.

        The roles assigned to the user that is associated with the API Tokens  # noqa: E501

        :param roles: The roles of this APIToken.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def created_on(self):
        """Gets the created_on of this APIToken.  # noqa: E501

        The epoch at which the API Tokens were created  # noqa: E501

        :return: The created_on of this APIToken.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this APIToken.

        The epoch at which the API Tokens were created  # noqa: E501

        :param created_on: The created_on of this APIToken.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def access_id(self):
        """Gets the access_id of this APIToken.  # noqa: E501

        The access Id associated with the API Tokens  # noqa: E501

        :return: The access_id of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this APIToken.

        The access Id associated with the API Tokens  # noqa: E501

        :param access_id: The access_id of this APIToken.  # noqa: E501
        :type: str
        """

        self._access_id = access_id

    @property
    def admin_name(self):
        """Gets the admin_name of this APIToken.  # noqa: E501

        The name of the user associated with the API Tokens  # noqa: E501

        :return: The admin_name of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """Sets the admin_name of this APIToken.

        The name of the user associated with the API Tokens  # noqa: E501

        :param admin_name: The admin_name of this APIToken.  # noqa: E501
        :type: str
        """

        self._admin_name = admin_name

    @property
    def last_auth_ip(self):
        """Gets the last_auth_ip of this APIToken.  # noqa: E501

        The IP from which the API Tokens were last used  # noqa: E501

        :return: The last_auth_ip of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._last_auth_ip

    @last_auth_ip.setter
    def last_auth_ip(self, last_auth_ip):
        """Sets the last_auth_ip of this APIToken.

        The IP from which the API Tokens were last used  # noqa: E501

        :param last_auth_ip: The last_auth_ip of this APIToken.  # noqa: E501
        :type: str
        """

        self._last_auth_ip = last_auth_ip

    @property
    def access_key(self):
        """Gets the access_key of this APIToken.  # noqa: E501

        The secret key associated with the API Tokens  # noqa: E501

        :return: The access_key of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this APIToken.

        The secret key associated with the API Tokens  # noqa: E501

        :param access_key: The access_key of this APIToken.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def created_by(self):
        """Gets the created_by of this APIToken.  # noqa: E501

        The user who is the API Tokens created by  # noqa: E501

        :return: The created_by of this APIToken.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this APIToken.

        The user who is the API Tokens created by  # noqa: E501

        :param created_by: The created_by of this APIToken.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def admin_id(self):
        """Gets the admin_id of this APIToken.  # noqa: E501

        The id of the user associated with the API Tokens  # noqa: E501

        :return: The admin_id of this APIToken.  # noqa: E501
        :rtype: int
        """
        return self._admin_id

    @admin_id.setter
    def admin_id(self, admin_id):
        """Sets the admin_id of this APIToken.

        The id of the user associated with the API Tokens  # noqa: E501

        :param admin_id: The admin_id of this APIToken.  # noqa: E501
        :type: int
        """

        self._admin_id = admin_id

    @property
    def id(self):
        """Gets the id of this APIToken.  # noqa: E501

        The id of the API Token  # noqa: E501

        :return: The id of this APIToken.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this APIToken.

        The id of the API Token  # noqa: E501

        :param id: The id of this APIToken.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this APIToken.  # noqa: E501

        The values can be 1 | 2. Specifies whether or not the API Tokens are enabled, where 2 = enabled  # noqa: E501

        :return: The status of this APIToken.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this APIToken.

        The values can be 1 | 2. Specifies whether or not the API Tokens are enabled, where 2 = enabled  # noqa: E501

        :param status: The status of this APIToken.  # noqa: E501
        :type: int
        """

        self._status = status

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
        if issubclass(APIToken, dict):
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
        if not isinstance(other, APIToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
