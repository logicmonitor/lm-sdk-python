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
from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501

class RestSavedMapWidgetV3(Widget):
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
        'scale': 'float',
        'saved_map_name': 'str',
        'saved_map_id': 'int',
        'saved_map_group_name': 'str'
    }
    if hasattr(Widget, "swagger_types"):
        swagger_types.update(Widget.swagger_types)

    attribute_map = {
        'scale': 'scale',
        'saved_map_name': 'savedMapName',
        'saved_map_id': 'savedMapId',
        'saved_map_group_name': 'savedMapGroupName'
    }
    if hasattr(Widget, "attribute_map"):
        attribute_map.update(Widget.attribute_map)

    def __init__(self, scale=None, saved_map_name=None, saved_map_id=None, saved_map_group_name=None, *args, **kwargs):  # noqa: E501
        """RestSavedMapWidgetV3 - a model defined in Swagger"""  # noqa: E501
        self._scale = None
        self._saved_map_name = None
        self._saved_map_id = None
        self._saved_map_group_name = None
        self.discriminator = None
        if scale is not None:
            self.scale = scale
        if saved_map_name is not None:
            self.saved_map_name = saved_map_name
        if saved_map_id is not None:
            self.saved_map_id = saved_map_id
        if saved_map_group_name is not None:
            self.saved_map_group_name = saved_map_group_name
        Widget.__init__(self, *args, **kwargs)

    @property
    def scale(self):
        """Gets the scale of this RestSavedMapWidgetV3.  # noqa: E501


        :return: The scale of this RestSavedMapWidgetV3.  # noqa: E501
        :rtype: float
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this RestSavedMapWidgetV3.


        :param scale: The scale of this RestSavedMapWidgetV3.  # noqa: E501
        :type: float
        """

        self._scale = scale

    @property
    def saved_map_name(self):
        """Gets the saved_map_name of this RestSavedMapWidgetV3.  # noqa: E501


        :return: The saved_map_name of this RestSavedMapWidgetV3.  # noqa: E501
        :rtype: str
        """
        return self._saved_map_name

    @saved_map_name.setter
    def saved_map_name(self, saved_map_name):
        """Sets the saved_map_name of this RestSavedMapWidgetV3.


        :param saved_map_name: The saved_map_name of this RestSavedMapWidgetV3.  # noqa: E501
        :type: str
        """

        self._saved_map_name = saved_map_name

    @property
    def saved_map_id(self):
        """Gets the saved_map_id of this RestSavedMapWidgetV3.  # noqa: E501


        :return: The saved_map_id of this RestSavedMapWidgetV3.  # noqa: E501
        :rtype: int
        """
        return self._saved_map_id

    @saved_map_id.setter
    def saved_map_id(self, saved_map_id):
        """Sets the saved_map_id of this RestSavedMapWidgetV3.


        :param saved_map_id: The saved_map_id of this RestSavedMapWidgetV3.  # noqa: E501
        :type: int
        """

        self._saved_map_id = saved_map_id

    @property
    def saved_map_group_name(self):
        """Gets the saved_map_group_name of this RestSavedMapWidgetV3.  # noqa: E501


        :return: The saved_map_group_name of this RestSavedMapWidgetV3.  # noqa: E501
        :rtype: str
        """
        return self._saved_map_group_name

    @saved_map_group_name.setter
    def saved_map_group_name(self, saved_map_group_name):
        """Sets the saved_map_group_name of this RestSavedMapWidgetV3.


        :param saved_map_group_name: The saved_map_group_name of this RestSavedMapWidgetV3.  # noqa: E501
        :type: str
        """

        self._saved_map_group_name = saved_map_group_name

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
        if issubclass(RestSavedMapWidgetV3, dict):
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
        if not isinstance(other, RestSavedMapWidgetV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
