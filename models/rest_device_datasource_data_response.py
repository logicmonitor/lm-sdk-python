# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestDeviceDatasourceDataResponse(object):
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
        'data': 'RestDeviceDataSourceData',
        'errmsg': 'str',
        'status': 'int'
    }

    attribute_map = {
        'data': 'data',
        'errmsg': 'errmsg',
        'status': 'status'
    }

    def __init__(self, data=None, errmsg=None, status=None):
        """
        RestDeviceDatasourceDataResponse - a model defined in Swagger
        """

        self._data = None
        self._errmsg = None
        self._status = None

        if data is not None:
          self.data = data
        if errmsg is not None:
          self.errmsg = errmsg
        if status is not None:
          self.status = status

    @property
    def data(self):
        """
        Gets the data of this RestDeviceDatasourceDataResponse.

        :return: The data of this RestDeviceDatasourceDataResponse.
        :rtype: RestDeviceDataSourceData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this RestDeviceDatasourceDataResponse.

        :param data: The data of this RestDeviceDatasourceDataResponse.
        :type: RestDeviceDataSourceData
        """

        self._data = data

    @property
    def errmsg(self):
        """
        Gets the errmsg of this RestDeviceDatasourceDataResponse.

        :return: The errmsg of this RestDeviceDatasourceDataResponse.
        :rtype: str
        """
        return self._errmsg

    @errmsg.setter
    def errmsg(self, errmsg):
        """
        Sets the errmsg of this RestDeviceDatasourceDataResponse.

        :param errmsg: The errmsg of this RestDeviceDatasourceDataResponse.
        :type: str
        """

        self._errmsg = errmsg

    @property
    def status(self):
        """
        Gets the status of this RestDeviceDatasourceDataResponse.

        :return: The status of this RestDeviceDatasourceDataResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RestDeviceDatasourceDataResponse.

        :param status: The status of this RestDeviceDatasourceDataResponse.
        :type: int
        """

        self._status = status

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
        if not isinstance(other, RestDeviceDatasourceDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
