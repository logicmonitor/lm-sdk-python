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

from logicmonitor_sdk.models.authentication import Authentication  # noqa: F401,E501


class NTLMAuthentication(Authentication):
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
        'password': 'str',
        'type': 'str',
        'user_name': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'password': 'password',
        'type': 'type',
        'user_name': 'userName',
        'domain': 'domain'
    }

    def __init__(self, password=None, type=None, user_name=None, domain=None):  # noqa: E501
        """NTLMAuthentication - a model defined in Swagger"""  # noqa: E501

        self._password = None
        self._type = None
        self._user_name = None
        self._domain = None
        self.discriminator = None

        self.password = password
        self.type = type
        self.user_name = user_name
        if domain is not None:
            self.domain = domain

    @property
    def password(self):
        """Gets the password of this NTLMAuthentication.  # noqa: E501

        NTLM authentication password  # noqa: E501

        :return: The password of this NTLMAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NTLMAuthentication.

        NTLM authentication password  # noqa: E501

        :param password: The password of this NTLMAuthentication.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def type(self):
        """Gets the type of this NTLMAuthentication.  # noqa: E501

        Authentication type  # noqa: E501

        :return: The type of this NTLMAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NTLMAuthentication.

        Authentication type  # noqa: E501

        :param type: The type of this NTLMAuthentication.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_name(self):
        """Gets the user_name of this NTLMAuthentication.  # noqa: E501

        NTLM  authentication userName  # noqa: E501

        :return: The user_name of this NTLMAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NTLMAuthentication.

        NTLM  authentication userName  # noqa: E501

        :param user_name: The user_name of this NTLMAuthentication.  # noqa: E501
        :type: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def domain(self):
        """Gets the domain of this NTLMAuthentication.  # noqa: E501


        :return: The domain of this NTLMAuthentication.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this NTLMAuthentication.


        :param domain: The domain of this NTLMAuthentication.  # noqa: E501
        :type: str
        """

        self._domain = domain

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
        if issubclass(NTLMAuthentication, dict):
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
        if not isinstance(other, NTLMAuthentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
