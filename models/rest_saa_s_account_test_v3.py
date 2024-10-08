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

class RestSaaSAccountTestV3(object):
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
        'private_key': 'str',
        'account_id': 'str',
        'client_id': 'str',
        'secret_key': 'str',
        'status_type': 'str',
        'account_type': 'str',
        'tenant_id': 'str',
        'service_name': 'str',
        'user_id': 'str',
        'status_urls': 'str'
    }

    attribute_map = {
        'private_key': 'privateKey',
        'account_id': 'accountId',
        'client_id': 'clientId',
        'secret_key': 'secretKey',
        'status_type': 'statusType',
        'account_type': 'accountType',
        'tenant_id': 'tenantId',
        'service_name': 'serviceName',
        'user_id': 'userId',
        'status_urls': 'statusUrls'
    }

    def __init__(self, private_key=None, account_id=None, client_id=None, secret_key=None, status_type=None, account_type=None, tenant_id=None, service_name=None, user_id=None, status_urls=None):  # noqa: E501
        """RestSaaSAccountTestV3 - a model defined in Swagger"""  # noqa: E501
        self._private_key = None
        self._account_id = None
        self._client_id = None
        self._secret_key = None
        self._status_type = None
        self._account_type = None
        self._tenant_id = None
        self._service_name = None
        self._user_id = None
        self._status_urls = None
        self.discriminator = None
        if private_key is not None:
            self.private_key = private_key
        if account_id is not None:
            self.account_id = account_id
        if client_id is not None:
            self.client_id = client_id
        if secret_key is not None:
            self.secret_key = secret_key
        if status_type is not None:
            self.status_type = status_type
        if account_type is not None:
            self.account_type = account_type
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if service_name is not None:
            self.service_name = service_name
        if user_id is not None:
            self.user_id = user_id
        if status_urls is not None:
            self.status_urls = status_urls

    @property
    def private_key(self):
        """Gets the private_key of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The private_key of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this RestSaaSAccountTestV3.


        :param private_key: The private_key of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def account_id(self):
        """Gets the account_id of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The account_id of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RestSaaSAccountTestV3.


        :param account_id: The account_id of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def client_id(self):
        """Gets the client_id of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The client_id of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RestSaaSAccountTestV3.


        :param client_id: The client_id of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def secret_key(self):
        """Gets the secret_key of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The secret_key of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this RestSaaSAccountTestV3.


        :param secret_key: The secret_key of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def status_type(self):
        """Gets the status_type of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The status_type of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._status_type

    @status_type.setter
    def status_type(self, status_type):
        """Sets the status_type of this RestSaaSAccountTestV3.


        :param status_type: The status_type of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._status_type = status_type

    @property
    def account_type(self):
        """Gets the account_type of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The account_type of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this RestSaaSAccountTestV3.


        :param account_type: The account_type of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The tenant_id of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RestSaaSAccountTestV3.


        :param tenant_id: The tenant_id of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def service_name(self):
        """Gets the service_name of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The service_name of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this RestSaaSAccountTestV3.


        :param service_name: The service_name of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def user_id(self):
        """Gets the user_id of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The user_id of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RestSaaSAccountTestV3.


        :param user_id: The user_id of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def status_urls(self):
        """Gets the status_urls of this RestSaaSAccountTestV3.  # noqa: E501


        :return: The status_urls of this RestSaaSAccountTestV3.  # noqa: E501
        :rtype: str
        """
        return self._status_urls

    @status_urls.setter
    def status_urls(self, status_urls):
        """Sets the status_urls of this RestSaaSAccountTestV3.


        :param status_urls: The status_urls of this RestSaaSAccountTestV3.  # noqa: E501
        :type: str
        """

        self._status_urls = status_urls

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
        if issubclass(RestSaaSAccountTestV3, dict):
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
        if not isinstance(other, RestSaaSAccountTestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
