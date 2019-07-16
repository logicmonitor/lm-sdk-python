# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebsiteItemConfig(object):
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
        'exclude_sdt': 'bool',
        'website': 'str',
        'website_group': 'str'
    }

    attribute_map = {
        'exclude_sdt': 'excludeSDT',
        'website': 'website',
        'website_group': 'websiteGroup'
    }

    def __init__(self, exclude_sdt=None, website=None, website_group=None):  # noqa: E501
        """WebsiteItemConfig - a model defined in Swagger"""  # noqa: E501

        self._exclude_sdt = None
        self._website = None
        self._website_group = None
        self.discriminator = None

        if exclude_sdt is not None:
            self.exclude_sdt = exclude_sdt
        self.website = website
        self.website_group = website_group

    @property
    def exclude_sdt(self):
        """Gets the exclude_sdt of this WebsiteItemConfig.  # noqa: E501


        :return: The exclude_sdt of this WebsiteItemConfig.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_sdt

    @exclude_sdt.setter
    def exclude_sdt(self, exclude_sdt):
        """Sets the exclude_sdt of this WebsiteItemConfig.


        :param exclude_sdt: The exclude_sdt of this WebsiteItemConfig.  # noqa: E501
        :type: bool
        """

        self._exclude_sdt = exclude_sdt

    @property
    def website(self):
        """Gets the website of this WebsiteItemConfig.  # noqa: E501


        :return: The website of this WebsiteItemConfig.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this WebsiteItemConfig.


        :param website: The website of this WebsiteItemConfig.  # noqa: E501
        :type: str
        """
        if website is None:
            raise ValueError("Invalid value for `website`, must not be `None`")  # noqa: E501

        self._website = website

    @property
    def website_group(self):
        """Gets the website_group of this WebsiteItemConfig.  # noqa: E501


        :return: The website_group of this WebsiteItemConfig.  # noqa: E501
        :rtype: str
        """
        return self._website_group

    @website_group.setter
    def website_group(self, website_group):
        """Sets the website_group of this WebsiteItemConfig.


        :param website_group: The website_group of this WebsiteItemConfig.  # noqa: E501
        :type: str
        """
        if website_group is None:
            raise ValueError("Invalid value for `website_group`, must not be `None`")  # noqa: E501

        self._website_group = website_group

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
        if issubclass(WebsiteItemConfig, dict):
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
        if not isinstance(other, WebsiteItemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
