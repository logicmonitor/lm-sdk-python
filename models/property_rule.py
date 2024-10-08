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

class PropertyRule(object):
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
        'schedule_option': 'str',
        'groovy_script': 'str',
        'access_groups': 'list[AccessGroup]',
        'windows_script': 'str',
        'data_type': 'int',
        'description': 'str',
        'applies_to': 'str',
        'technology': 'str',
        'linux_cmdline': 'str',
        'version': 'int',
        'windows_cmdline': 'str',
        'lineage_id': 'str',
        'tags': 'str',
        'audit_version': 'int',
        'installation_metadata': 'IntegrationMetadata',
        'script_type': 'str',
        'name': 'str',
        'checksum': 'str',
        'interval': 'int',
        'id': 'int',
        'access_group_ids': 'list[int]',
        'linux_script': 'str',
        'group': 'str'
    }

    attribute_map = {
        'schedule_option': 'scheduleOption',
        'groovy_script': 'groovyScript',
        'access_groups': 'accessGroups',
        'windows_script': 'windowsScript',
        'data_type': 'dataType',
        'description': 'description',
        'applies_to': 'appliesTo',
        'technology': 'technology',
        'linux_cmdline': 'linuxCmdline',
        'version': 'version',
        'windows_cmdline': 'windowsCmdline',
        'lineage_id': 'lineageId',
        'tags': 'tags',
        'audit_version': 'auditVersion',
        'installation_metadata': 'installationMetadata',
        'script_type': 'scriptType',
        'name': 'name',
        'checksum': 'checksum',
        'interval': 'interval',
        'id': 'id',
        'access_group_ids': 'accessGroupIds',
        'linux_script': 'linuxScript',
        'group': 'group'
    }

    def __init__(self, schedule_option=None, groovy_script=None, access_groups=None, windows_script=None, data_type=None, description=None, applies_to=None, technology=None, linux_cmdline=None, version=None, windows_cmdline=None, lineage_id=None, tags=None, audit_version=None, installation_metadata=None, script_type=None, name=None, checksum=None, interval=None, id=None, access_group_ids=None, linux_script=None, group=None):  # noqa: E501
        """PropertyRule - a model defined in Swagger"""  # noqa: E501
        self._schedule_option = None
        self._groovy_script = None
        self._access_groups = None
        self._windows_script = None
        self._data_type = None
        self._description = None
        self._applies_to = None
        self._technology = None
        self._linux_cmdline = None
        self._version = None
        self._windows_cmdline = None
        self._lineage_id = None
        self._tags = None
        self._audit_version = None
        self._installation_metadata = None
        self._script_type = None
        self._name = None
        self._checksum = None
        self._interval = None
        self._id = None
        self._access_group_ids = None
        self._linux_script = None
        self._group = None
        self.discriminator = None
        if schedule_option is not None:
            self.schedule_option = schedule_option
        if groovy_script is not None:
            self.groovy_script = groovy_script
        if access_groups is not None:
            self.access_groups = access_groups
        if windows_script is not None:
            self.windows_script = windows_script
        if data_type is not None:
            self.data_type = data_type
        if description is not None:
            self.description = description
        if applies_to is not None:
            self.applies_to = applies_to
        if technology is not None:
            self.technology = technology
        if linux_cmdline is not None:
            self.linux_cmdline = linux_cmdline
        if version is not None:
            self.version = version
        if windows_cmdline is not None:
            self.windows_cmdline = windows_cmdline
        if lineage_id is not None:
            self.lineage_id = lineage_id
        if tags is not None:
            self.tags = tags
        if audit_version is not None:
            self.audit_version = audit_version
        if installation_metadata is not None:
            self.installation_metadata = installation_metadata
        if script_type is not None:
            self.script_type = script_type
        if name is not None:
            self.name = name
        if checksum is not None:
            self.checksum = checksum
        if interval is not None:
            self.interval = interval
        if id is not None:
            self.id = id
        if access_group_ids is not None:
            self.access_group_ids = access_group_ids
        if linux_script is not None:
            self.linux_script = linux_script
        if group is not None:
            self.group = group

    @property
    def schedule_option(self):
        """Gets the schedule_option of this PropertyRule.  # noqa: E501

        The property rule schedule option. The values can be onAP|onAPpropertyChanges  # noqa: E501

        :return: The schedule_option of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._schedule_option

    @schedule_option.setter
    def schedule_option(self, schedule_option):
        """Sets the schedule_option of this PropertyRule.

        The property rule schedule option. The values can be onAP|onAPpropertyChanges  # noqa: E501

        :param schedule_option: The schedule_option of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._schedule_option = schedule_option

    @property
    def groovy_script(self):
        """Gets the groovy_script of this PropertyRule.  # noqa: E501

        groovy script  # noqa: E501

        :return: The groovy_script of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._groovy_script

    @groovy_script.setter
    def groovy_script(self, groovy_script):
        """Sets the groovy_script of this PropertyRule.

        groovy script  # noqa: E501

        :param groovy_script: The groovy_script of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._groovy_script = groovy_script

    @property
    def access_groups(self):
        """Gets the access_groups of this PropertyRule.  # noqa: E501

        Access group Details in response  # noqa: E501

        :return: The access_groups of this PropertyRule.  # noqa: E501
        :rtype: list[AccessGroup]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this PropertyRule.

        Access group Details in response  # noqa: E501

        :param access_groups: The access_groups of this PropertyRule.  # noqa: E501
        :type: list[AccessGroup]
        """

        self._access_groups = access_groups

    @property
    def windows_script(self):
        """Gets the windows_script of this PropertyRule.  # noqa: E501

        external windows script name  # noqa: E501

        :return: The windows_script of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._windows_script

    @windows_script.setter
    def windows_script(self, windows_script):
        """Sets the windows_script of this PropertyRule.

        external windows script name  # noqa: E501

        :param windows_script: The windows_script of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._windows_script = windows_script

    @property
    def data_type(self):
        """Gets the data_type of this PropertyRule.  # noqa: E501

        The data type of property source, default is 0. The values can be  0: property source  1: raw ERI     # noqa: E501

        :return: The data_type of this PropertyRule.  # noqa: E501
        :rtype: int
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this PropertyRule.

        The data type of property source, default is 0. The values can be  0: property source  1: raw ERI     # noqa: E501

        :param data_type: The data_type of this PropertyRule.  # noqa: E501
        :type: int
        """

        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this PropertyRule.  # noqa: E501

        The property rule description  # noqa: E501

        :return: The description of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PropertyRule.

        The property rule description  # noqa: E501

        :param description: The description of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applies_to(self):
        """Gets the applies_to of this PropertyRule.  # noqa: E501

        The property rule applies to  # noqa: E501

        :return: The applies_to of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this PropertyRule.

        The property rule applies to  # noqa: E501

        :param applies_to: The applies_to of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def technology(self):
        """Gets the technology of this PropertyRule.  # noqa: E501

        The technology notes  # noqa: E501

        :return: The technology of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this PropertyRule.

        The technology notes  # noqa: E501

        :param technology: The technology of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._technology = technology

    @property
    def linux_cmdline(self):
        """Gets the linux_cmdline of this PropertyRule.  # noqa: E501

        external linux script args  # noqa: E501

        :return: The linux_cmdline of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._linux_cmdline

    @linux_cmdline.setter
    def linux_cmdline(self, linux_cmdline):
        """Sets the linux_cmdline of this PropertyRule.

        external linux script args  # noqa: E501

        :param linux_cmdline: The linux_cmdline of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._linux_cmdline = linux_cmdline

    @property
    def version(self):
        """Gets the version of this PropertyRule.  # noqa: E501

        The property rule version  # noqa: E501

        :return: The version of this PropertyRule.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PropertyRule.

        The property rule version  # noqa: E501

        :param version: The version of this PropertyRule.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def windows_cmdline(self):
        """Gets the windows_cmdline of this PropertyRule.  # noqa: E501

        external windows script args  # noqa: E501

        :return: The windows_cmdline of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._windows_cmdline

    @windows_cmdline.setter
    def windows_cmdline(self, windows_cmdline):
        """Sets the windows_cmdline of this PropertyRule.

        external windows script args  # noqa: E501

        :param windows_cmdline: The windows_cmdline of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._windows_cmdline = windows_cmdline

    @property
    def lineage_id(self):
        """Gets the lineage_id of this PropertyRule.  # noqa: E501

        LM module lineageId  # noqa: E501

        :return: The lineage_id of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._lineage_id

    @lineage_id.setter
    def lineage_id(self, lineage_id):
        """Sets the lineage_id of this PropertyRule.

        LM module lineageId  # noqa: E501

        :param lineage_id: The lineage_id of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._lineage_id = lineage_id

    @property
    def tags(self):
        """Gets the tags of this PropertyRule.  # noqa: E501

        The property rule tags  # noqa: E501

        :return: The tags of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PropertyRule.

        The property rule tags  # noqa: E501

        :param tags: The tags of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def audit_version(self):
        """Gets the audit_version of this PropertyRule.  # noqa: E501

        The property rule auditVersion  # noqa: E501

        :return: The audit_version of this PropertyRule.  # noqa: E501
        :rtype: int
        """
        return self._audit_version

    @audit_version.setter
    def audit_version(self, audit_version):
        """Sets the audit_version of this PropertyRule.

        The property rule auditVersion  # noqa: E501

        :param audit_version: The audit_version of this PropertyRule.  # noqa: E501
        :type: int
        """

        self._audit_version = audit_version

    @property
    def installation_metadata(self):
        """Gets the installation_metadata of this PropertyRule.  # noqa: E501


        :return: The installation_metadata of this PropertyRule.  # noqa: E501
        :rtype: IntegrationMetadata
        """
        return self._installation_metadata

    @installation_metadata.setter
    def installation_metadata(self, installation_metadata):
        """Sets the installation_metadata of this PropertyRule.


        :param installation_metadata: The installation_metadata of this PropertyRule.  # noqa: E501
        :type: IntegrationMetadata
        """

        self._installation_metadata = installation_metadata

    @property
    def script_type(self):
        """Gets the script_type of this PropertyRule.  # noqa: E501

        script type: embed | powershell | external  # noqa: E501

        :return: The script_type of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._script_type

    @script_type.setter
    def script_type(self, script_type):
        """Sets the script_type of this PropertyRule.

        script type: embed | powershell | external  # noqa: E501

        :param script_type: The script_type of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._script_type = script_type

    @property
    def name(self):
        """Gets the name of this PropertyRule.  # noqa: E501

        The property rule name  # noqa: E501

        :return: The name of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyRule.

        The property rule name  # noqa: E501

        :param name: The name of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def checksum(self):
        """Gets the checksum of this PropertyRule.  # noqa: E501

        LM module checksum  # noqa: E501

        :return: The checksum of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this PropertyRule.

        LM module checksum  # noqa: E501

        :param checksum: The checksum of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def interval(self):
        """Gets the interval of this PropertyRule.  # noqa: E501

        The collect interval of raw ERI  # noqa: E501

        :return: The interval of this PropertyRule.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PropertyRule.

        The collect interval of raw ERI  # noqa: E501

        :param interval: The interval of this PropertyRule.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def id(self):
        """Gets the id of this PropertyRule.  # noqa: E501


        :return: The id of this PropertyRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PropertyRule.


        :param id: The id of this PropertyRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def access_group_ids(self):
        """Gets the access_group_ids of this PropertyRule.  # noqa: E501

        The Access Groups Id's  # noqa: E501

        :return: The access_group_ids of this PropertyRule.  # noqa: E501
        :rtype: list[int]
        """
        return self._access_group_ids

    @access_group_ids.setter
    def access_group_ids(self, access_group_ids):
        """Sets the access_group_ids of this PropertyRule.

        The Access Groups Id's  # noqa: E501

        :param access_group_ids: The access_group_ids of this PropertyRule.  # noqa: E501
        :type: list[int]
        """

        self._access_group_ids = access_group_ids

    @property
    def linux_script(self):
        """Gets the linux_script of this PropertyRule.  # noqa: E501

        external linux script name  # noqa: E501

        :return: The linux_script of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._linux_script

    @linux_script.setter
    def linux_script(self, linux_script):
        """Sets the linux_script of this PropertyRule.

        external linux script name  # noqa: E501

        :param linux_script: The linux_script of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._linux_script = linux_script

    @property
    def group(self):
        """Gets the group of this PropertyRule.  # noqa: E501

        The property rule group name  # noqa: E501

        :return: The group of this PropertyRule.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this PropertyRule.

        The property rule group name  # noqa: E501

        :param group: The group of this PropertyRule.  # noqa: E501
        :type: str
        """

        self._group = group

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
        if issubclass(PropertyRule, dict):
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
        if not isinstance(other, PropertyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
