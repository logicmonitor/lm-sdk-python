# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestGraph(object):
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
        'display_prio': 'int',
        'name': 'str',
        'id': 'int',
        'title': 'str'
    }

    attribute_map = {
        'display_prio': 'displayPrio',
        'name': 'name',
        'id': 'id',
        'title': 'title'
    }

    def __init__(self, display_prio=None, name=None, id=None, title=None):
        """
        RestGraph - a model defined in Swagger
        """

        self._display_prio = None
        self._name = None
        self._id = None
        self._title = None

        if display_prio is not None:
          self.display_prio = display_prio
        if name is not None:
          self.name = name
        if id is not None:
          self.id = id
        if title is not None:
          self.title = title

    @property
    def display_prio(self):
        """
        Gets the display_prio of this RestGraph.

        :return: The display_prio of this RestGraph.
        :rtype: int
        """
        return self._display_prio

    @display_prio.setter
    def display_prio(self, display_prio):
        """
        Sets the display_prio of this RestGraph.

        :param display_prio: The display_prio of this RestGraph.
        :type: int
        """

        self._display_prio = display_prio

    @property
    def name(self):
        """
        Gets the name of this RestGraph.

        :return: The name of this RestGraph.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RestGraph.

        :param name: The name of this RestGraph.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this RestGraph.

        :return: The id of this RestGraph.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RestGraph.

        :param id: The id of this RestGraph.
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this RestGraph.

        :return: The title of this RestGraph.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this RestGraph.

        :param title: The title of this RestGraph.
        :type: str
        """

        self._title = title

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
        if not isinstance(other, RestGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
