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

class AuditLog(object):
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
        'happened_on_local': 'str',
        'ip': 'str',
        'happened_on': 'int',
        'description': 'str',
        'id': 'str',
        'username': 'str'
    }

    attribute_map = {
        'happened_on_local': 'happenedOnLocal',
        'ip': 'ip',
        'happened_on': 'happenedOn',
        'description': 'description',
        'id': 'id',
        'username': 'username'
    }

    def __init__(self, happened_on_local=None, ip=None, happened_on=None, description=None, id=None, username=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501
        self._happened_on_local = None
        self._ip = None
        self._happened_on = None
        self._description = None
        self._id = None
        self._username = None
        self.discriminator = None
        if happened_on_local is not None:
            self.happened_on_local = happened_on_local
        if ip is not None:
            self.ip = ip
        if happened_on is not None:
            self.happened_on = happened_on
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username

    @property
    def happened_on_local(self):
        """Gets the happened_on_local of this AuditLog.  # noqa: E501

        The date and time that the action recorded in the access log entry occurred  # noqa: E501

        :return: The happened_on_local of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._happened_on_local

    @happened_on_local.setter
    def happened_on_local(self, happened_on_local):
        """Sets the happened_on_local of this AuditLog.

        The date and time that the action recorded in the access log entry occurred  # noqa: E501

        :param happened_on_local: The happened_on_local of this AuditLog.  # noqa: E501
        :type: str
        """

        self._happened_on_local = happened_on_local

    @property
    def ip(self):
        """Gets the ip of this AuditLog.  # noqa: E501

        The IP address that the action was performed from  # noqa: E501

        :return: The ip of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this AuditLog.

        The IP address that the action was performed from  # noqa: E501

        :param ip: The ip of this AuditLog.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def happened_on(self):
        """Gets the happened_on of this AuditLog.  # noqa: E501

        The time, in epoch seconds, that the action recorded in the access log entry occurred  # noqa: E501

        :return: The happened_on of this AuditLog.  # noqa: E501
        :rtype: int
        """
        return self._happened_on

    @happened_on.setter
    def happened_on(self, happened_on):
        """Sets the happened_on of this AuditLog.

        The time, in epoch seconds, that the action recorded in the access log entry occurred  # noqa: E501

        :param happened_on: The happened_on of this AuditLog.  # noqa: E501
        :type: int
        """

        self._happened_on = happened_on

    @property
    def description(self):
        """Gets the description of this AuditLog.  # noqa: E501

        The description of the action recorded in the access log entry  # noqa: E501

        :return: The description of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuditLog.

        The description of the action recorded in the access log entry  # noqa: E501

        :param description: The description of this AuditLog.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AuditLog.  # noqa: E501

        The Id of the access log entry  # noqa: E501

        :return: The id of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLog.

        The Id of the access log entry  # noqa: E501

        :param id: The id of this AuditLog.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this AuditLog.  # noqa: E501

        The username associated with the user that performed the action recorded in the access log entry   # noqa: E501

        :return: The username of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuditLog.

        The username associated with the user that performed the action recorded in the access log entry   # noqa: E501

        :param username: The username of this AuditLog.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
