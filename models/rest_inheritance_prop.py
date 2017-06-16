# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestInheritanceProp(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'fullpath': 'str',
        'id': 'int',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'fullpath': 'fullpath',
        'id': 'id',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, fullpath=None, id=None, type=None, value=None):
        """
        RestInheritanceProp - a model defined in Swagger
        """

        self._fullpath = None
        self._id = None
        self._type = None
        self._value = None

        if fullpath is not None:
          self.fullpath = fullpath
        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value

    @property
    def fullpath(self):
        """
        Gets the fullpath of this RestInheritanceProp.

        :return: The fullpath of this RestInheritanceProp.
        :rtype: str
        """
        return self._fullpath

    @fullpath.setter
    def fullpath(self, fullpath):
        """
        Sets the fullpath of this RestInheritanceProp.

        :param fullpath: The fullpath of this RestInheritanceProp.
        :type: str
        """

        self._fullpath = fullpath

    @property
    def id(self):
        """
        Gets the id of this RestInheritanceProp.

        :return: The id of this RestInheritanceProp.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RestInheritanceProp.

        :param id: The id of this RestInheritanceProp.
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this RestInheritanceProp.

        :return: The type of this RestInheritanceProp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RestInheritanceProp.

        :param type: The type of this RestInheritanceProp.
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this RestInheritanceProp.

        :return: The value of this RestInheritanceProp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this RestInheritanceProp.

        :param value: The value of this RestInheritanceProp.
        :type: str
        """

        self._value = value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RestInheritanceProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other