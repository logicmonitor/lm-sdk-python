# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DataPointConfig(object):
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
        'global_alert_expr': 'str',
        'data_point_name': 'str',
        'data_point_id': 'int',
        'disable_alerting': 'bool',
        'alert_expr_note': 'str',
        'alert_expr': 'str',
        'data_point_description': 'str'
    }

    attribute_map = {
        'global_alert_expr': 'globalAlertExpr',
        'data_point_name': 'dataPointName',
        'data_point_id': 'dataPointId',
        'disable_alerting': 'disableAlerting',
        'alert_expr_note': 'alertExprNote',
        'alert_expr': 'alertExpr',
        'data_point_description': 'dataPointDescription'
    }

    def __init__(self, global_alert_expr=None, data_point_name=None, data_point_id=None, disable_alerting=None, alert_expr_note=None, alert_expr=None, data_point_description=None):
        """
        DataPointConfig - a model defined in Swagger
        """

        self._global_alert_expr = None
        self._data_point_name = None
        self._data_point_id = None
        self._disable_alerting = None
        self._alert_expr_note = None
        self._alert_expr = None
        self._data_point_description = None

        if global_alert_expr is not None:
          self.global_alert_expr = global_alert_expr
        if data_point_name is not None:
          self.data_point_name = data_point_name
        if data_point_id is not None:
          self.data_point_id = data_point_id
        self.disable_alerting = disable_alerting
        if alert_expr_note is not None:
          self.alert_expr_note = alert_expr_note
        self.alert_expr = alert_expr
        if data_point_description is not None:
          self.data_point_description = data_point_description

    @property
    def global_alert_expr(self):
        """
        Gets the global_alert_expr of this DataPointConfig.

        :return: The global_alert_expr of this DataPointConfig.
        :rtype: str
        """
        return self._global_alert_expr

    @global_alert_expr.setter
    def global_alert_expr(self, global_alert_expr):
        """
        Sets the global_alert_expr of this DataPointConfig.

        :param global_alert_expr: The global_alert_expr of this DataPointConfig.
        :type: str
        """

        self._global_alert_expr = global_alert_expr

    @property
    def data_point_name(self):
        """
        Gets the data_point_name of this DataPointConfig.

        :return: The data_point_name of this DataPointConfig.
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """
        Sets the data_point_name of this DataPointConfig.

        :param data_point_name: The data_point_name of this DataPointConfig.
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def data_point_id(self):
        """
        Gets the data_point_id of this DataPointConfig.

        :return: The data_point_id of this DataPointConfig.
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """
        Sets the data_point_id of this DataPointConfig.

        :param data_point_id: The data_point_id of this DataPointConfig.
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def disable_alerting(self):
        """
        Gets the disable_alerting of this DataPointConfig.

        :return: The disable_alerting of this DataPointConfig.
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """
        Sets the disable_alerting of this DataPointConfig.

        :param disable_alerting: The disable_alerting of this DataPointConfig.
        :type: bool
        """
        if disable_alerting is None:
            raise ValueError("Invalid value for `disable_alerting`, must not be `None`")

        self._disable_alerting = disable_alerting

    @property
    def alert_expr_note(self):
        """
        Gets the alert_expr_note of this DataPointConfig.

        :return: The alert_expr_note of this DataPointConfig.
        :rtype: str
        """
        return self._alert_expr_note

    @alert_expr_note.setter
    def alert_expr_note(self, alert_expr_note):
        """
        Sets the alert_expr_note of this DataPointConfig.

        :param alert_expr_note: The alert_expr_note of this DataPointConfig.
        :type: str
        """

        self._alert_expr_note = alert_expr_note

    @property
    def alert_expr(self):
        """
        Gets the alert_expr of this DataPointConfig.

        :return: The alert_expr of this DataPointConfig.
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """
        Sets the alert_expr of this DataPointConfig.

        :param alert_expr: The alert_expr of this DataPointConfig.
        :type: str
        """
        if alert_expr is None:
            raise ValueError("Invalid value for `alert_expr`, must not be `None`")

        self._alert_expr = alert_expr

    @property
    def data_point_description(self):
        """
        Gets the data_point_description of this DataPointConfig.

        :return: The data_point_description of this DataPointConfig.
        :rtype: str
        """
        return self._data_point_description

    @data_point_description.setter
    def data_point_description(self, data_point_description):
        """
        Sets the data_point_description of this DataPointConfig.

        :param data_point_description: The data_point_description of this DataPointConfig.
        :type: str
        """

        self._data_point_description = data_point_description

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
        if not isinstance(other, DataPointConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
