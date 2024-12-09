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

class Admin(object):
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
        'last_name': 'str',
        'note': 'str',
        'view_permission': 'object',
        'timezone': 'str',
        'roles': 'list[Role]',
        'last_login_on': 'int',
        'last_action_on_local': 'str',
        'sms_email_format': 'str',
        'apionly': 'bool',
        'last_auth_ip': 'str',
        'api_tokens': 'list[APIToken]',
        'admin_group_ids': 'list[int]',
        'password': 'str',
        'last_action': 'str',
        'training_email': 'str',
        'last_action_on': 'int',
        'last_access_on': 'int',
        'id': 'int',
        'email': 'str',
        'contact_method': 'str',
        'accept_eulaon': 'int',
        'immediate_force_logout': 'bool',
        'user_permission': 'str',
        'sms_email': 'str',
        'two_fa_enabled': 'bool',
        'first_name': 'str',
        'phone': 'str',
        'created_by': 'str',
        'force_password_change': 'bool',
        'tenant_id': 'int',
        'accept_eula': 'bool',
        'user_type': 'str',
        'username': 'str',
        'status': 'str'
    }

    attribute_map = {
        'last_name': 'lastName',
        'note': 'note',
        'view_permission': 'viewPermission',
        'timezone': 'timezone',
        'roles': 'roles',
        'last_login_on': 'lastLoginOn',
        'last_action_on_local': 'lastActionOnLocal',
        'sms_email_format': 'smsEmailFormat',
        'apionly': 'apionly',
        'last_auth_ip': 'lastAuthIp',
        'api_tokens': 'apiTokens',
        'admin_group_ids': 'adminGroupIds',
        'password': 'password',
        'last_action': 'lastAction',
        'training_email': 'trainingEmail',
        'last_action_on': 'lastActionOn',
        'last_access_on': 'lastAccessOn',
        'id': 'id',
        'email': 'email',
        'contact_method': 'contactMethod',
        'accept_eulaon': 'acceptEULAOn',
        'immediate_force_logout': 'immediateForceLogout',
        'user_permission': 'userPermission',
        'sms_email': 'smsEmail',
        'two_fa_enabled': 'twoFAEnabled',
        'first_name': 'firstName',
        'phone': 'phone',
        'created_by': 'createdBy',
        'force_password_change': 'forcePasswordChange',
        'tenant_id': 'tenantId',
        'accept_eula': 'acceptEULA',
        'user_type': 'userType',
        'username': 'username',
        'status': 'status'
    }

    def __init__(self, last_name=None, note=None, view_permission=None, timezone=None, roles=None, last_login_on=None, last_action_on_local=None, sms_email_format=None, apionly=None, last_auth_ip=None, api_tokens=None, admin_group_ids=None, password=None, last_action=None, training_email=None, last_action_on=None, last_access_on=None, id=None, email=None, contact_method=None, accept_eulaon=None, immediate_force_logout=None, user_permission=None, sms_email=None, two_fa_enabled=None, first_name=None, phone=None, created_by=None, force_password_change=None, tenant_id=None, accept_eula=None, user_type=None, username=None, status=None):  # noqa: E501
        """Admin - a model defined in Swagger"""  # noqa: E501
        self._last_name = None
        self._note = None
        self._view_permission = None
        self._timezone = None
        self._roles = None
        self._last_login_on = None
        self._last_action_on_local = None
        self._sms_email_format = None
        self._apionly = None
        self._last_auth_ip = None
        self._api_tokens = None
        self._admin_group_ids = None
        self._password = None
        self._last_action = None
        self._training_email = None
        self._last_action_on = None
        self._last_access_on = None
        self._id = None
        self._email = None
        self._contact_method = None
        self._accept_eulaon = None
        self._immediate_force_logout = None
        self._user_permission = None
        self._sms_email = None
        self._two_fa_enabled = None
        self._first_name = None
        self._phone = None
        self._created_by = None
        self._force_password_change = None
        self._tenant_id = None
        self._accept_eula = None
        self._user_type = None
        self._username = None
        self._status = None
        self.discriminator = None
        if last_name is not None:
            self.last_name = last_name
        if note is not None:
            self.note = note
        if view_permission is not None:
            self.view_permission = view_permission
        if timezone is not None:
            self.timezone = timezone
        self.roles = roles
        if last_login_on is not None:
            self.last_login_on = last_login_on
        if last_action_on_local is not None:
            self.last_action_on_local = last_action_on_local
        if sms_email_format is not None:
            self.sms_email_format = sms_email_format
        if apionly is not None:
            self.apionly = apionly
        if last_auth_ip is not None:
            self.last_auth_ip = last_auth_ip
        if api_tokens is not None:
            self.api_tokens = api_tokens
        if admin_group_ids is not None:
            self.admin_group_ids = admin_group_ids
        self.password = password
        if last_action is not None:
            self.last_action = last_action
        if training_email is not None:
            self.training_email = training_email
        if last_action_on is not None:
            self.last_action_on = last_action_on
        if last_access_on is not None:
            self.last_access_on = last_access_on
        if id is not None:
            self.id = id
        self.email = email
        if contact_method is not None:
            self.contact_method = contact_method
        if accept_eulaon is not None:
            self.accept_eulaon = accept_eulaon
        if immediate_force_logout is not None:
            self.immediate_force_logout = immediate_force_logout
        if user_permission is not None:
            self.user_permission = user_permission
        if sms_email is not None:
            self.sms_email = sms_email
        if two_fa_enabled is not None:
            self.two_fa_enabled = two_fa_enabled
        if first_name is not None:
            self.first_name = first_name
        if phone is not None:
            self.phone = phone
        if created_by is not None:
            self.created_by = created_by
        if force_password_change is not None:
            self.force_password_change = force_password_change
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if accept_eula is not None:
            self.accept_eula = accept_eula
        if user_type is not None:
            self.user_type = user_type
        self.username = username
        if status is not None:
            self.status = status

    @property
    def last_name(self):
        """Gets the last_name of this Admin.  # noqa: E501

        The last name associated with the user  # noqa: E501

        :return: The last_name of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Admin.

        The last name associated with the user  # noqa: E501

        :param last_name: The last_name of this Admin.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def note(self):
        """Gets the note of this Admin.  # noqa: E501

        Any notes assocaited with the user  # noqa: E501

        :return: The note of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this Admin.

        Any notes assocaited with the user  # noqa: E501

        :param note: The note of this Admin.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def view_permission(self):
        """Gets the view_permission of this Admin.  # noqa: E501

        The account tabs that will be visible to the user  # noqa: E501

        :return: The view_permission of this Admin.  # noqa: E501
        :rtype: object
        """
        return self._view_permission

    @view_permission.setter
    def view_permission(self, view_permission):
        """Sets the view_permission of this Admin.

        The account tabs that will be visible to the user  # noqa: E501

        :param view_permission: The view_permission of this Admin.  # noqa: E501
        :type: object
        """

        self._view_permission = view_permission

    @property
    def timezone(self):
        """Gets the timezone of this Admin.  # noqa: E501

        The timezone of the user  # noqa: E501

        :return: The timezone of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Admin.

        The timezone of the user  # noqa: E501

        :param timezone: The timezone of this Admin.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def roles(self):
        """Gets the roles of this Admin.  # noqa: E501

        The roles assigned to the user  # noqa: E501

        :return: The roles of this Admin.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Admin.

        The roles assigned to the user  # noqa: E501

        :param roles: The roles of this Admin.  # noqa: E501
        :type: list[Role]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

    @property
    def last_login_on(self):
        """Gets the last_login_on of this Admin.  # noqa: E501

        The time that the user last logged in, in epoch format  # noqa: E501

        :return: The last_login_on of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._last_login_on

    @last_login_on.setter
    def last_login_on(self, last_login_on):
        """Sets the last_login_on of this Admin.

        The time that the user last logged in, in epoch format  # noqa: E501

        :param last_login_on: The last_login_on of this Admin.  # noqa: E501
        :type: int
        """

        self._last_login_on = last_login_on

    @property
    def last_action_on_local(self):
        """Gets the last_action_on_local of this Admin.  # noqa: E501

        The time, in local format, of the user's last action  # noqa: E501

        :return: The last_action_on_local of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._last_action_on_local

    @last_action_on_local.setter
    def last_action_on_local(self, last_action_on_local):
        """Sets the last_action_on_local of this Admin.

        The time, in local format, of the user's last action  # noqa: E501

        :param last_action_on_local: The last_action_on_local of this Admin.  # noqa: E501
        :type: str
        """

        self._last_action_on_local = last_action_on_local

    @property
    def sms_email_format(self):
        """Gets the sms_email_format of this Admin.  # noqa: E501

        The values can be sms | fullText, where sms = 160 characters and fullText = all characters  # noqa: E501

        :return: The sms_email_format of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._sms_email_format

    @sms_email_format.setter
    def sms_email_format(self, sms_email_format):
        """Sets the sms_email_format of this Admin.

        The values can be sms | fullText, where sms = 160 characters and fullText = all characters  # noqa: E501

        :param sms_email_format: The sms_email_format of this Admin.  # noqa: E501
        :type: str
        """

        self._sms_email_format = sms_email_format

    @property
    def apionly(self):
        """Gets the apionly of this Admin.  # noqa: E501

        Specifies whether the user is an API only user. The values can be true|false  # noqa: E501

        :return: The apionly of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._apionly

    @apionly.setter
    def apionly(self, apionly):
        """Sets the apionly of this Admin.

        Specifies whether the user is an API only user. The values can be true|false  # noqa: E501

        :param apionly: The apionly of this Admin.  # noqa: E501
        :type: bool
        """

        self._apionly = apionly

    @property
    def last_auth_ip(self):
        """Gets the last_auth_ip of this Admin.  # noqa: E501

        The Last User IP  # noqa: E501

        :return: The last_auth_ip of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._last_auth_ip

    @last_auth_ip.setter
    def last_auth_ip(self, last_auth_ip):
        """Sets the last_auth_ip of this Admin.

        The Last User IP  # noqa: E501

        :param last_auth_ip: The last_auth_ip of this Admin.  # noqa: E501
        :type: str
        """

        self._last_auth_ip = last_auth_ip

    @property
    def api_tokens(self):
        """Gets the api_tokens of this Admin.  # noqa: E501

        Any API Tokens associated with the user  # noqa: E501

        :return: The api_tokens of this Admin.  # noqa: E501
        :rtype: list[APIToken]
        """
        return self._api_tokens

    @api_tokens.setter
    def api_tokens(self, api_tokens):
        """Sets the api_tokens of this Admin.

        Any API Tokens associated with the user  # noqa: E501

        :param api_tokens: The api_tokens of this Admin.  # noqa: E501
        :type: list[APIToken]
        """

        self._api_tokens = api_tokens

    @property
    def admin_group_ids(self):
        """Gets the admin_group_ids of this Admin.  # noqa: E501

        The Id(s) of the groups the admin is in, where multiple group ids are comma separated  # noqa: E501

        :return: The admin_group_ids of this Admin.  # noqa: E501
        :rtype: list[int]
        """
        return self._admin_group_ids

    @admin_group_ids.setter
    def admin_group_ids(self, admin_group_ids):
        """Sets the admin_group_ids of this Admin.

        The Id(s) of the groups the admin is in, where multiple group ids are comma separated  # noqa: E501

        :param admin_group_ids: The admin_group_ids of this Admin.  # noqa: E501
        :type: list[int]
        """

        self._admin_group_ids = admin_group_ids

    @property
    def password(self):
        """Gets the password of this Admin.  # noqa: E501

        The password associated with the user  # noqa: E501

        :return: The password of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Admin.

        The password associated with the user  # noqa: E501

        :param password: The password of this Admin.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def last_action(self):
        """Gets the last_action of this Admin.  # noqa: E501

        The last action taken by the user  # noqa: E501

        :return: The last_action of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._last_action

    @last_action.setter
    def last_action(self, last_action):
        """Sets the last_action of this Admin.

        The last action taken by the user  # noqa: E501

        :param last_action: The last_action of this Admin.  # noqa: E501
        :type: str
        """

        self._last_action = last_action

    @property
    def training_email(self):
        """Gets the training_email of this Admin.  # noqa: E501

        The email address for user's Training account  # noqa: E501

        :return: The training_email of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._training_email

    @training_email.setter
    def training_email(self, training_email):
        """Sets the training_email of this Admin.

        The email address for user's Training account  # noqa: E501

        :param training_email: The training_email of this Admin.  # noqa: E501
        :type: str
        """

        self._training_email = training_email

    @property
    def last_action_on(self):
        """Gets the last_action_on of this Admin.  # noqa: E501

        The time, in epoch format, of the user's last action  # noqa: E501

        :return: The last_action_on of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._last_action_on

    @last_action_on.setter
    def last_action_on(self, last_action_on):
        """Sets the last_action_on of this Admin.

        The time, in epoch format, of the user's last action  # noqa: E501

        :param last_action_on: The last_action_on of this Admin.  # noqa: E501
        :type: int
        """

        self._last_action_on = last_action_on

    @property
    def last_access_on(self):
        """Gets the last_access_on of this Admin.  # noqa: E501

        The time that the user last accessed the portal  # noqa: E501

        :return: The last_access_on of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._last_access_on

    @last_access_on.setter
    def last_access_on(self, last_access_on):
        """Sets the last_access_on of this Admin.

        The time that the user last accessed the portal  # noqa: E501

        :param last_access_on: The last_access_on of this Admin.  # noqa: E501
        :type: int
        """

        self._last_access_on = last_access_on

    @property
    def id(self):
        """Gets the id of this Admin.  # noqa: E501

        The Id of the user  # noqa: E501

        :return: The id of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Admin.

        The Id of the user  # noqa: E501

        :param id: The id of this Admin.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this Admin.  # noqa: E501

        The email address associated with the user  # noqa: E501

        :return: The email of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Admin.

        The email address associated with the user  # noqa: E501

        :param email: The email of this Admin.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def contact_method(self):
        """Gets the contact_method of this Admin.  # noqa: E501

        The values can be email | smsemail. Specifies the contact method for this admin  # noqa: E501

        :return: The contact_method of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._contact_method

    @contact_method.setter
    def contact_method(self, contact_method):
        """Sets the contact_method of this Admin.

        The values can be email | smsemail. Specifies the contact method for this admin  # noqa: E501

        :param contact_method: The contact_method of this Admin.  # noqa: E501
        :type: str
        """

        self._contact_method = contact_method

    @property
    def accept_eulaon(self):
        """Gets the accept_eulaon of this Admin.  # noqa: E501

        The time, in epoch format, that the user accepted the EULA (if required to)  # noqa: E501

        :return: The accept_eulaon of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._accept_eulaon

    @accept_eulaon.setter
    def accept_eulaon(self, accept_eulaon):
        """Sets the accept_eulaon of this Admin.

        The time, in epoch format, that the user accepted the EULA (if required to)  # noqa: E501

        :param accept_eulaon: The accept_eulaon of this Admin.  # noqa: E501
        :type: int
        """

        self._accept_eulaon = accept_eulaon

    @property
    def immediate_force_logout(self):
        """Gets the immediate_force_logout of this Admin.  # noqa: E501

        Specifies whether the user need to be logged off, if Force Password Change is enabled. The values can be true|false  # noqa: E501

        :return: The immediate_force_logout of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_force_logout

    @immediate_force_logout.setter
    def immediate_force_logout(self, immediate_force_logout):
        """Sets the immediate_force_logout of this Admin.

        Specifies whether the user need to be logged off, if Force Password Change is enabled. The values can be true|false  # noqa: E501

        :param immediate_force_logout: The immediate_force_logout of this Admin.  # noqa: E501
        :type: bool
        """

        self._immediate_force_logout = immediate_force_logout

    @property
    def user_permission(self):
        """Gets the user_permission of this Admin.  # noqa: E501

        The permission of current user with the admin. values can be write|read|none  # noqa: E501

        :return: The user_permission of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this Admin.

        The permission of current user with the admin. values can be write|read|none  # noqa: E501

        :param user_permission: The user_permission of this Admin.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def sms_email(self):
        """Gets the sms_email of this Admin.  # noqa: E501

        The sms email address associated with the user  # noqa: E501

        :return: The sms_email of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._sms_email

    @sms_email.setter
    def sms_email(self, sms_email):
        """Sets the sms_email of this Admin.

        The sms email address associated with the user  # noqa: E501

        :param sms_email: The sms_email of this Admin.  # noqa: E501
        :type: str
        """

        self._sms_email = sms_email

    @property
    def two_fa_enabled(self):
        """Gets the two_fa_enabled of this Admin.  # noqa: E501

        Whether or not two factor authentication is enabled for the user  # noqa: E501

        :return: The two_fa_enabled of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._two_fa_enabled

    @two_fa_enabled.setter
    def two_fa_enabled(self, two_fa_enabled):
        """Sets the two_fa_enabled of this Admin.

        Whether or not two factor authentication is enabled for the user  # noqa: E501

        :param two_fa_enabled: The two_fa_enabled of this Admin.  # noqa: E501
        :type: bool
        """

        self._two_fa_enabled = two_fa_enabled

    @property
    def first_name(self):
        """Gets the first_name of this Admin.  # noqa: E501

        The first name associated with the user  # noqa: E501

        :return: The first_name of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Admin.

        The first name associated with the user  # noqa: E501

        :param first_name: The first_name of this Admin.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def phone(self):
        """Gets the phone of this Admin.  # noqa: E501

        The phone number associated with the user  # noqa: E501

        :return: The phone of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Admin.

        The phone number associated with the user  # noqa: E501

        :param phone: The phone of this Admin.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def created_by(self):
        """Gets the created_by of this Admin.  # noqa: E501

        Species who created the user. This may be another user, SAML or LogicMonitor  # noqa: E501

        :return: The created_by of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Admin.

        Species who created the user. This may be another user, SAML or LogicMonitor  # noqa: E501

        :param created_by: The created_by of this Admin.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def force_password_change(self):
        """Gets the force_password_change of this Admin.  # noqa: E501

        Whether or not the user should be forced to change their password on the next login  # noqa: E501

        :return: The force_password_change of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._force_password_change

    @force_password_change.setter
    def force_password_change(self, force_password_change):
        """Sets the force_password_change of this Admin.

        Whether or not the user should be forced to change their password on the next login  # noqa: E501

        :param force_password_change: The force_password_change of this Admin.  # noqa: E501
        :type: bool
        """

        self._force_password_change = force_password_change

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Admin.  # noqa: E501

        The tenant id of the user  # noqa: E501

        :return: The tenant_id of this Admin.  # noqa: E501
        :rtype: int
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Admin.

        The tenant id of the user  # noqa: E501

        :param tenant_id: The tenant_id of this Admin.  # noqa: E501
        :type: int
        """

        self._tenant_id = tenant_id

    @property
    def accept_eula(self):
        """Gets the accept_eula of this Admin.  # noqa: E501

        Whether or not the user is required to accept the EULA (end user license agreement)  # noqa: E501

        :return: The accept_eula of this Admin.  # noqa: E501
        :rtype: bool
        """
        return self._accept_eula

    @accept_eula.setter
    def accept_eula(self, accept_eula):
        """Sets the accept_eula of this Admin.

        Whether or not the user is required to accept the EULA (end user license agreement)  # noqa: E501

        :param accept_eula: The accept_eula of this Admin.  # noqa: E501
        :type: bool
        """

        self._accept_eula = accept_eula

    @property
    def user_type(self):
        """Gets the user_type of this Admin.  # noqa: E501

        The type of user  # noqa: E501

        :return: The user_type of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this Admin.

        The type of user  # noqa: E501

        :param user_type: The user_type of this Admin.  # noqa: E501
        :type: str
        """

        self._user_type = user_type

    @property
    def username(self):
        """Gets the username of this Admin.  # noqa: E501

        The username associated with the user  # noqa: E501

        :return: The username of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Admin.

        The username associated with the user  # noqa: E501

        :param username: The username of this Admin.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def status(self):
        """Gets the status of this Admin.  # noqa: E501

        The user's status. The values can be active|suspended  # noqa: E501

        :return: The status of this Admin.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Admin.

        The user's status. The values can be active|suspended  # noqa: E501

        :param status: The status of this Admin.  # noqa: E501
        :type: str
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
        if issubclass(Admin, dict):
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
        if not isinstance(other, Admin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
