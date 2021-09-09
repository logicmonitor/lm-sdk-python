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


class WebsiteCheckPoint(object):
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
        'geo_info': 'str',
        'id': 'int',
        'smg_id': 'int'
    }

    attribute_map = {
        'geo_info': 'geoInfo',
        'id': 'id',
        'smg_id': 'smgId'
    }

    def __init__(self, geo_info=None, id=None, smg_id=None):  # noqa: E501
        """WebsiteCheckPoint - a model defined in Swagger"""  # noqa: E501

        self._geo_info = None
        self._id = None
        self._smg_id = None
        self.discriminator = None

        if geo_info is not None:
            self.geo_info = geo_info
        if id is not None:
            self.id = id
        if smg_id is not None:
            self.smg_id = smg_id

    @property
    def geo_info(self):
        """Gets the geo_info of this WebsiteCheckPoint.  # noqa: E501


        :return: The geo_info of this WebsiteCheckPoint.  # noqa: E501
        :rtype: str
        """
        return self._geo_info

    @geo_info.setter
    def geo_info(self, geo_info):
        """Sets the geo_info of this WebsiteCheckPoint.


        :param geo_info: The geo_info of this WebsiteCheckPoint.  # noqa: E501
        :type: str
        """

        self._geo_info = geo_info

    @property
    def id(self):
        """Gets the id of this WebsiteCheckPoint.  # noqa: E501


        :return: The id of this WebsiteCheckPoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebsiteCheckPoint.


        :param id: The id of this WebsiteCheckPoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def smg_id(self):
        """Gets the smg_id of this WebsiteCheckPoint.  # noqa: E501


        :return: The smg_id of this WebsiteCheckPoint.  # noqa: E501
        :rtype: int
        """
        return self._smg_id

    @smg_id.setter
    def smg_id(self, smg_id):
        """Sets the smg_id of this WebsiteCheckPoint.


        :param smg_id: The smg_id of this WebsiteCheckPoint.  # noqa: E501
        :type: int
        """

        self._smg_id = smg_id

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
        if issubclass(WebsiteCheckPoint, dict):
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
        if not isinstance(other, WebsiteCheckPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
