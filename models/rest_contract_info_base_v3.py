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

class RestContractInfoBaseV3(object):
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
        'child_products': 'list[RestUsageContractInfoV4]',
        'product': 'str',
        'unit': 'list[str]',
        'quantity': 'list[float]',
        'feature': 'str',
        'rounding_required': 'bool',
        'unpaid': 'bool'
    }

    attribute_map = {
        'child_products': 'childProducts',
        'product': 'product',
        'unit': 'unit',
        'quantity': 'quantity',
        'feature': 'feature',
        'rounding_required': 'roundingRequired',
        'unpaid': 'unpaid'
    }

    def __init__(self, child_products=None, product=None, unit=None, quantity=None, feature=None, rounding_required=None, unpaid=None):  # noqa: E501
        """RestContractInfoBaseV3 - a model defined in Swagger"""  # noqa: E501
        self._child_products = None
        self._product = None
        self._unit = None
        self._quantity = None
        self._feature = None
        self._rounding_required = None
        self._unpaid = None
        self.discriminator = None
        if child_products is not None:
            self.child_products = child_products
        if product is not None:
            self.product = product
        if unit is not None:
            self.unit = unit
        if quantity is not None:
            self.quantity = quantity
        if feature is not None:
            self.feature = feature
        if rounding_required is not None:
            self.rounding_required = rounding_required
        if unpaid is not None:
            self.unpaid = unpaid

    @property
    def child_products(self):
        """Gets the child_products of this RestContractInfoBaseV3.  # noqa: E501


        :return: The child_products of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: list[RestUsageContractInfoV4]
        """
        return self._child_products

    @child_products.setter
    def child_products(self, child_products):
        """Sets the child_products of this RestContractInfoBaseV3.


        :param child_products: The child_products of this RestContractInfoBaseV3.  # noqa: E501
        :type: list[RestUsageContractInfoV4]
        """

        self._child_products = child_products

    @property
    def product(self):
        """Gets the product of this RestContractInfoBaseV3.  # noqa: E501


        :return: The product of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this RestContractInfoBaseV3.


        :param product: The product of this RestContractInfoBaseV3.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def unit(self):
        """Gets the unit of this RestContractInfoBaseV3.  # noqa: E501


        :return: The unit of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: list[str]
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this RestContractInfoBaseV3.


        :param unit: The unit of this RestContractInfoBaseV3.  # noqa: E501
        :type: list[str]
        """

        self._unit = unit

    @property
    def quantity(self):
        """Gets the quantity of this RestContractInfoBaseV3.  # noqa: E501


        :return: The quantity of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: list[float]
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this RestContractInfoBaseV3.


        :param quantity: The quantity of this RestContractInfoBaseV3.  # noqa: E501
        :type: list[float]
        """

        self._quantity = quantity

    @property
    def feature(self):
        """Gets the feature of this RestContractInfoBaseV3.  # noqa: E501


        :return: The feature of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this RestContractInfoBaseV3.


        :param feature: The feature of this RestContractInfoBaseV3.  # noqa: E501
        :type: str
        """

        self._feature = feature

    @property
    def rounding_required(self):
        """Gets the rounding_required of this RestContractInfoBaseV3.  # noqa: E501


        :return: The rounding_required of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: bool
        """
        return self._rounding_required

    @rounding_required.setter
    def rounding_required(self, rounding_required):
        """Sets the rounding_required of this RestContractInfoBaseV3.


        :param rounding_required: The rounding_required of this RestContractInfoBaseV3.  # noqa: E501
        :type: bool
        """

        self._rounding_required = rounding_required

    @property
    def unpaid(self):
        """Gets the unpaid of this RestContractInfoBaseV3.  # noqa: E501


        :return: The unpaid of this RestContractInfoBaseV3.  # noqa: E501
        :rtype: bool
        """
        return self._unpaid

    @unpaid.setter
    def unpaid(self, unpaid):
        """Sets the unpaid of this RestContractInfoBaseV3.


        :param unpaid: The unpaid of this RestContractInfoBaseV3.  # noqa: E501
        :type: bool
        """

        self._unpaid = unpaid

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
        if issubclass(RestContractInfoBaseV3, dict):
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
        if not isinstance(other, RestContractInfoBaseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other