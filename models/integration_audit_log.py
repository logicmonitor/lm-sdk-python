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


class IntegrationAuditLog(object):
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
        'headers': 'str',
        'alert_type': 'int',
        'integration_name': 'str',
        'num_retries': 'int',
        'integration_alert_status': 'str',
        'error_message': 'str',
        'external_ticket_id': 'str',
        'payload_format': 'str',
        'url': 'str',
        'happened_on_ms': 'int',
        'integration_type': 'str',
        'alert_instance_id': 'str',
        'payload': 'str',
        'http_response_code': 'int',
        'id': 'str',
        'alert_id': 'str',
        'http_response': 'str'
    }

    attribute_map = {
        'headers': 'headers',
        'alert_type': 'alertType',
        'integration_name': 'integrationName',
        'num_retries': 'numRetries',
        'integration_alert_status': 'integrationAlertStatus',
        'error_message': 'errorMessage',
        'external_ticket_id': 'externalTicketId',
        'payload_format': 'payloadFormat',
        'url': 'url',
        'happened_on_ms': 'happenedOnMs',
        'integration_type': 'integrationType',
        'alert_instance_id': 'alertInstanceId',
        'payload': 'payload',
        'http_response_code': 'httpResponseCode',
        'id': 'id',
        'alert_id': 'alertId',
        'http_response': 'httpResponse'
    }

    def __init__(self, headers=None, alert_type=None, integration_name=None, num_retries=None, integration_alert_status=None, error_message=None, external_ticket_id=None, payload_format=None, url=None, happened_on_ms=None, integration_type=None, alert_instance_id=None, payload=None, http_response_code=None, id=None, alert_id=None, http_response=None):  # noqa: E501
        """IntegrationAuditLog - a model defined in Swagger"""  # noqa: E501

        self._headers = None
        self._alert_type = None
        self._integration_name = None
        self._num_retries = None
        self._integration_alert_status = None
        self._error_message = None
        self._external_ticket_id = None
        self._payload_format = None
        self._url = None
        self._happened_on_ms = None
        self._integration_type = None
        self._alert_instance_id = None
        self._payload = None
        self._http_response_code = None
        self._id = None
        self._alert_id = None
        self._http_response = None
        self.discriminator = None

        if headers is not None:
            self.headers = headers
        if alert_type is not None:
            self.alert_type = alert_type
        if integration_name is not None:
            self.integration_name = integration_name
        if num_retries is not None:
            self.num_retries = num_retries
        if integration_alert_status is not None:
            self.integration_alert_status = integration_alert_status
        if error_message is not None:
            self.error_message = error_message
        if external_ticket_id is not None:
            self.external_ticket_id = external_ticket_id
        if payload_format is not None:
            self.payload_format = payload_format
        if url is not None:
            self.url = url
        if happened_on_ms is not None:
            self.happened_on_ms = happened_on_ms
        if integration_type is not None:
            self.integration_type = integration_type
        if alert_instance_id is not None:
            self.alert_instance_id = alert_instance_id
        if payload is not None:
            self.payload = payload
        if http_response_code is not None:
            self.http_response_code = http_response_code
        if id is not None:
            self.id = id
        if alert_id is not None:
            self.alert_id = alert_id
        if http_response is not None:
            self.http_response = http_response

    @property
    def headers(self):
        """Gets the headers of this IntegrationAuditLog.  # noqa: E501

        HTTP request headers used in alert delivery  # noqa: E501

        :return: The headers of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this IntegrationAuditLog.

        HTTP request headers used in alert delivery  # noqa: E501

        :param headers: The headers of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._headers = headers

    @property
    def alert_type(self):
        """Gets the alert_type of this IntegrationAuditLog.  # noqa: E501

        The type of the alert  # noqa: E501

        :return: The alert_type of this IntegrationAuditLog.  # noqa: E501
        :rtype: int
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this IntegrationAuditLog.

        The type of the alert  # noqa: E501

        :param alert_type: The alert_type of this IntegrationAuditLog.  # noqa: E501
        :type: int
        """

        self._alert_type = alert_type

    @property
    def integration_name(self):
        """Gets the integration_name of this IntegrationAuditLog.  # noqa: E501

        The name of integration  # noqa: E501

        :return: The integration_name of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._integration_name

    @integration_name.setter
    def integration_name(self, integration_name):
        """Sets the integration_name of this IntegrationAuditLog.

        The name of integration  # noqa: E501

        :param integration_name: The integration_name of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._integration_name = integration_name

    @property
    def num_retries(self):
        """Gets the num_retries of this IntegrationAuditLog.  # noqa: E501

        The number of times delivery was retried  # noqa: E501

        :return: The num_retries of this IntegrationAuditLog.  # noqa: E501
        :rtype: int
        """
        return self._num_retries

    @num_retries.setter
    def num_retries(self, num_retries):
        """Sets the num_retries of this IntegrationAuditLog.

        The number of times delivery was retried  # noqa: E501

        :param num_retries: The num_retries of this IntegrationAuditLog.  # noqa: E501
        :type: int
        """

        self._num_retries = num_retries

    @property
    def integration_alert_status(self):
        """Gets the integration_alert_status of this IntegrationAuditLog.  # noqa: E501

        The Integration Alert Status used for delivery  # noqa: E501

        :return: The integration_alert_status of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._integration_alert_status

    @integration_alert_status.setter
    def integration_alert_status(self, integration_alert_status):
        """Sets the integration_alert_status of this IntegrationAuditLog.

        The Integration Alert Status used for delivery  # noqa: E501

        :param integration_alert_status: The integration_alert_status of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._integration_alert_status = integration_alert_status

    @property
    def error_message(self):
        """Gets the error_message of this IntegrationAuditLog.  # noqa: E501

        Error message (if any) from ADC  # noqa: E501

        :return: The error_message of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this IntegrationAuditLog.

        Error message (if any) from ADC  # noqa: E501

        :param error_message: The error_message of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def external_ticket_id(self):
        """Gets the external_ticket_id of this IntegrationAuditLog.  # noqa: E501

        The parsed External Ticket ID from alert delivery  # noqa: E501

        :return: The external_ticket_id of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._external_ticket_id

    @external_ticket_id.setter
    def external_ticket_id(self, external_ticket_id):
        """Sets the external_ticket_id of this IntegrationAuditLog.

        The parsed External Ticket ID from alert delivery  # noqa: E501

        :param external_ticket_id: The external_ticket_id of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._external_ticket_id = external_ticket_id

    @property
    def payload_format(self):
        """Gets the payload_format of this IntegrationAuditLog.  # noqa: E501

        The outbound payload format  # noqa: E501

        :return: The payload_format of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._payload_format

    @payload_format.setter
    def payload_format(self, payload_format):
        """Sets the payload_format of this IntegrationAuditLog.

        The outbound payload format  # noqa: E501

        :param payload_format: The payload_format of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._payload_format = payload_format

    @property
    def url(self):
        """Gets the url of this IntegrationAuditLog.  # noqa: E501

        The URL where the alert was delivered to  # noqa: E501

        :return: The url of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IntegrationAuditLog.

        The URL where the alert was delivered to  # noqa: E501

        :param url: The url of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def happened_on_ms(self):
        """Gets the happened_on_ms of this IntegrationAuditLog.  # noqa: E501

        When the delivery result was saved in LMES  # noqa: E501

        :return: The happened_on_ms of this IntegrationAuditLog.  # noqa: E501
        :rtype: int
        """
        return self._happened_on_ms

    @happened_on_ms.setter
    def happened_on_ms(self, happened_on_ms):
        """Sets the happened_on_ms of this IntegrationAuditLog.

        When the delivery result was saved in LMES  # noqa: E501

        :param happened_on_ms: The happened_on_ms of this IntegrationAuditLog.  # noqa: E501
        :type: int
        """

        self._happened_on_ms = happened_on_ms

    @property
    def integration_type(self):
        """Gets the integration_type of this IntegrationAuditLog.  # noqa: E501

        The type of integration  # noqa: E501

        :return: The integration_type of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this IntegrationAuditLog.

        The type of integration  # noqa: E501

        :param integration_type: The integration_type of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

    @property
    def alert_instance_id(self):
        """Gets the alert_instance_id of this IntegrationAuditLog.  # noqa: E501

        The id of the alert instance  # noqa: E501

        :return: The alert_instance_id of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._alert_instance_id

    @alert_instance_id.setter
    def alert_instance_id(self, alert_instance_id):
        """Sets the alert_instance_id of this IntegrationAuditLog.

        The id of the alert instance  # noqa: E501

        :param alert_instance_id: The alert_instance_id of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._alert_instance_id = alert_instance_id

    @property
    def payload(self):
        """Gets the payload of this IntegrationAuditLog.  # noqa: E501

        The HTTP Request payload  # noqa: E501

        :return: The payload of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this IntegrationAuditLog.

        The HTTP Request payload  # noqa: E501

        :param payload: The payload of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def http_response_code(self):
        """Gets the http_response_code of this IntegrationAuditLog.  # noqa: E501

        The HTTP Response Code received from 3rd party API  # noqa: E501

        :return: The http_response_code of this IntegrationAuditLog.  # noqa: E501
        :rtype: int
        """
        return self._http_response_code

    @http_response_code.setter
    def http_response_code(self, http_response_code):
        """Sets the http_response_code of this IntegrationAuditLog.

        The HTTP Response Code received from 3rd party API  # noqa: E501

        :param http_response_code: The http_response_code of this IntegrationAuditLog.  # noqa: E501
        :type: int
        """

        self._http_response_code = http_response_code

    @property
    def id(self):
        """Gets the id of this IntegrationAuditLog.  # noqa: E501

        The id of audit log record  # noqa: E501

        :return: The id of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntegrationAuditLog.

        The id of audit log record  # noqa: E501

        :param id: The id of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def alert_id(self):
        """Gets the alert_id of this IntegrationAuditLog.  # noqa: E501

        The id of the alert  # noqa: E501

        :return: The alert_id of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        """Sets the alert_id of this IntegrationAuditLog.

        The id of the alert  # noqa: E501

        :param alert_id: The alert_id of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._alert_id = alert_id

    @property
    def http_response(self):
        """Gets the http_response of this IntegrationAuditLog.  # noqa: E501

        The HTTP Response Body received after alert delivery  # noqa: E501

        :return: The http_response of this IntegrationAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._http_response

    @http_response.setter
    def http_response(self, http_response):
        """Sets the http_response of this IntegrationAuditLog.

        The HTTP Response Body received after alert delivery  # noqa: E501

        :param http_response: The http_response of this IntegrationAuditLog.  # noqa: E501
        :type: str
        """

        self._http_response = http_response

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
        if issubclass(IntegrationAuditLog, dict):
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
        if not isinstance(other, IntegrationAuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
