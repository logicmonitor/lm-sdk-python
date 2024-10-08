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

class BatchJobExecutionItem(object):
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
        'started_on_local': 'str',
        'finished_on_local': 'str',
        'user_data': 'str',
        'stdout': 'str',
        'bj_name': 'str',
        'alert_level': 'int',
        'device_batch_job_id': 'int',
        'stderr': 'str',
        'device_display_name': 'str',
        'cmdline': 'str',
        'exit_code': 'int',
        'id': 'int',
        'execution_no': 'int',
        'finished_on': 'int',
        'started_on': 'int'
    }

    attribute_map = {
        'started_on_local': 'startedOnLocal',
        'finished_on_local': 'finishedOnLocal',
        'user_data': 'userData',
        'stdout': 'stdout',
        'bj_name': 'bjName',
        'alert_level': 'alertLevel',
        'device_batch_job_id': 'deviceBatchJobId',
        'stderr': 'stderr',
        'device_display_name': 'deviceDisplayName',
        'cmdline': 'cmdline',
        'exit_code': 'exitCode',
        'id': 'id',
        'execution_no': 'executionNo',
        'finished_on': 'finishedOn',
        'started_on': 'startedOn'
    }

    def __init__(self, started_on_local=None, finished_on_local=None, user_data=None, stdout=None, bj_name=None, alert_level=None, device_batch_job_id=None, stderr=None, device_display_name=None, cmdline=None, exit_code=None, id=None, execution_no=None, finished_on=None, started_on=None):  # noqa: E501
        """BatchJobExecutionItem - a model defined in Swagger"""  # noqa: E501
        self._started_on_local = None
        self._finished_on_local = None
        self._user_data = None
        self._stdout = None
        self._bj_name = None
        self._alert_level = None
        self._device_batch_job_id = None
        self._stderr = None
        self._device_display_name = None
        self._cmdline = None
        self._exit_code = None
        self._id = None
        self._execution_no = None
        self._finished_on = None
        self._started_on = None
        self.discriminator = None
        if started_on_local is not None:
            self.started_on_local = started_on_local
        if finished_on_local is not None:
            self.finished_on_local = finished_on_local
        if user_data is not None:
            self.user_data = user_data
        if stdout is not None:
            self.stdout = stdout
        if bj_name is not None:
            self.bj_name = bj_name
        if alert_level is not None:
            self.alert_level = alert_level
        if device_batch_job_id is not None:
            self.device_batch_job_id = device_batch_job_id
        if stderr is not None:
            self.stderr = stderr
        if device_display_name is not None:
            self.device_display_name = device_display_name
        if cmdline is not None:
            self.cmdline = cmdline
        if exit_code is not None:
            self.exit_code = exit_code
        if id is not None:
            self.id = id
        if execution_no is not None:
            self.execution_no = execution_no
        if finished_on is not None:
            self.finished_on = finished_on
        if started_on is not None:
            self.started_on = started_on

    @property
    def started_on_local(self):
        """Gets the started_on_local of this BatchJobExecutionItem.  # noqa: E501


        :return: The started_on_local of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._started_on_local

    @started_on_local.setter
    def started_on_local(self, started_on_local):
        """Sets the started_on_local of this BatchJobExecutionItem.


        :param started_on_local: The started_on_local of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._started_on_local = started_on_local

    @property
    def finished_on_local(self):
        """Gets the finished_on_local of this BatchJobExecutionItem.  # noqa: E501


        :return: The finished_on_local of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._finished_on_local

    @finished_on_local.setter
    def finished_on_local(self, finished_on_local):
        """Sets the finished_on_local of this BatchJobExecutionItem.


        :param finished_on_local: The finished_on_local of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._finished_on_local = finished_on_local

    @property
    def user_data(self):
        """Gets the user_data of this BatchJobExecutionItem.  # noqa: E501


        :return: The user_data of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this BatchJobExecutionItem.


        :param user_data: The user_data of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def stdout(self):
        """Gets the stdout of this BatchJobExecutionItem.  # noqa: E501


        :return: The stdout of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._stdout

    @stdout.setter
    def stdout(self, stdout):
        """Sets the stdout of this BatchJobExecutionItem.


        :param stdout: The stdout of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._stdout = stdout

    @property
    def bj_name(self):
        """Gets the bj_name of this BatchJobExecutionItem.  # noqa: E501


        :return: The bj_name of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._bj_name

    @bj_name.setter
    def bj_name(self, bj_name):
        """Sets the bj_name of this BatchJobExecutionItem.


        :param bj_name: The bj_name of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._bj_name = bj_name

    @property
    def alert_level(self):
        """Gets the alert_level of this BatchJobExecutionItem.  # noqa: E501


        :return: The alert_level of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this BatchJobExecutionItem.


        :param alert_level: The alert_level of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._alert_level = alert_level

    @property
    def device_batch_job_id(self):
        """Gets the device_batch_job_id of this BatchJobExecutionItem.  # noqa: E501


        :return: The device_batch_job_id of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._device_batch_job_id

    @device_batch_job_id.setter
    def device_batch_job_id(self, device_batch_job_id):
        """Sets the device_batch_job_id of this BatchJobExecutionItem.


        :param device_batch_job_id: The device_batch_job_id of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._device_batch_job_id = device_batch_job_id

    @property
    def stderr(self):
        """Gets the stderr of this BatchJobExecutionItem.  # noqa: E501


        :return: The stderr of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._stderr

    @stderr.setter
    def stderr(self, stderr):
        """Sets the stderr of this BatchJobExecutionItem.


        :param stderr: The stderr of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._stderr = stderr

    @property
    def device_display_name(self):
        """Gets the device_display_name of this BatchJobExecutionItem.  # noqa: E501


        :return: The device_display_name of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this BatchJobExecutionItem.


        :param device_display_name: The device_display_name of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

    @property
    def cmdline(self):
        """Gets the cmdline of this BatchJobExecutionItem.  # noqa: E501


        :return: The cmdline of this BatchJobExecutionItem.  # noqa: E501
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        """Sets the cmdline of this BatchJobExecutionItem.


        :param cmdline: The cmdline of this BatchJobExecutionItem.  # noqa: E501
        :type: str
        """

        self._cmdline = cmdline

    @property
    def exit_code(self):
        """Gets the exit_code of this BatchJobExecutionItem.  # noqa: E501


        :return: The exit_code of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this BatchJobExecutionItem.


        :param exit_code: The exit_code of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def id(self):
        """Gets the id of this BatchJobExecutionItem.  # noqa: E501


        :return: The id of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchJobExecutionItem.


        :param id: The id of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def execution_no(self):
        """Gets the execution_no of this BatchJobExecutionItem.  # noqa: E501


        :return: The execution_no of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._execution_no

    @execution_no.setter
    def execution_no(self, execution_no):
        """Sets the execution_no of this BatchJobExecutionItem.


        :param execution_no: The execution_no of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._execution_no = execution_no

    @property
    def finished_on(self):
        """Gets the finished_on of this BatchJobExecutionItem.  # noqa: E501


        :return: The finished_on of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._finished_on

    @finished_on.setter
    def finished_on(self, finished_on):
        """Sets the finished_on of this BatchJobExecutionItem.


        :param finished_on: The finished_on of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._finished_on = finished_on

    @property
    def started_on(self):
        """Gets the started_on of this BatchJobExecutionItem.  # noqa: E501


        :return: The started_on of this BatchJobExecutionItem.  # noqa: E501
        :rtype: int
        """
        return self._started_on

    @started_on.setter
    def started_on(self, started_on):
        """Sets the started_on of this BatchJobExecutionItem.


        :param started_on: The started_on of this BatchJobExecutionItem.  # noqa: E501
        :type: int
        """

        self._started_on = started_on

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
        if issubclass(BatchJobExecutionItem, dict):
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
        if not isinstance(other, BatchJobExecutionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
