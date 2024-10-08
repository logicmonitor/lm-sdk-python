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

class EventSource(object):
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
        'suppress_duplicates_es': 'bool',
        'access_groups': 'list[AccessGroup]',
        'alert_subject_template': 'str',
        'alert_level': 'str',
        'description': 'str',
        'applies_to': 'str',
        'technology': 'str',
        'filters': 'list[RestEventSourceFilter]',
        'version': 'int',
        'lineage_id': 'str',
        'collector': 'str',
        'tags': 'str',
        'audit_version': 'int',
        'installation_metadata': 'IntegrationMetadata',
        'alert_body_template': 'str',
        'checksum': 'str',
        'name': 'str',
        'clear_after_ack': 'bool',
        'id': 'int',
        'access_group_ids': 'list[int]',
        'alert_effective_ival': 'int',
        'group': 'str'
    }

    attribute_map = {
        'suppress_duplicates_es': 'suppressDuplicatesES',
        'access_groups': 'accessGroups',
        'alert_subject_template': 'alertSubjectTemplate',
        'alert_level': 'alertLevel',
        'description': 'description',
        'applies_to': 'appliesTo',
        'technology': 'technology',
        'filters': 'filters',
        'version': 'version',
        'lineage_id': 'lineageId',
        'collector': 'collector',
        'tags': 'tags',
        'audit_version': 'auditVersion',
        'installation_metadata': 'installationMetadata',
        'alert_body_template': 'alertBodyTemplate',
        'checksum': 'checksum',
        'name': 'name',
        'clear_after_ack': 'clearAfterAck',
        'id': 'id',
        'access_group_ids': 'accessGroupIds',
        'alert_effective_ival': 'alertEffectiveIval',
        'group': 'group'
    }

    discriminator_value_class_map = {
          'snmptrap': 'SnmpTrapEventSource',
'RestAwsRdsPerformanceInsightsEventSource': 'RestAwsRdsPerformanceInsightsEventSource',
'syslog': 'SysLogEventSource',
'scriptevent': 'ScriptEventSource',
'gcpatom': 'GcpAtomEventSource',
'RestAwsHealthEventSource': 'RestAwsHealthEventSource',
'wineventlog': 'WindowsEventLogEventSource',
'awsrss': 'AwsRssEventSource',
'echo': 'EchoEventSource',
'RestAzureAdvisorEventSource': 'RestAzureAdvisorEventSource',
'logfile': 'LogFileEventSource',
'IPMIEventSource': 'IPMIEventSource',
'RestAwsTrustedAdvisorEventSource': 'RestAwsTrustedAdvisorEventSource',
'RestAzureResourceLogAnalyticsWorkspacesSource': 'RestAzureResourceLogAnalyticsWorkspacesSource',
'RestAzureResourceHealthEventSource': 'RestAzureResourceHealthEventSource',
'AzureEmergingIssueEventSource': 'AzureEmergingIssueEventSource',
'azurerss': 'AzureRssEventSource',
'RestAwsOrganizationalHealthEventSource': 'RestAwsOrganizationalHealthEventSource'    }

    def __init__(self, suppress_duplicates_es=None, access_groups=None, alert_subject_template=None, alert_level=None, description=None, applies_to=None, technology=None, filters=None, version=None, lineage_id=None, collector=None, tags=None, audit_version=None, installation_metadata=None, alert_body_template=None, checksum=None, name=None, clear_after_ack=None, id=None, access_group_ids=None, alert_effective_ival=None, group=None):  # noqa: E501
        """EventSource - a model defined in Swagger"""  # noqa: E501
        self._suppress_duplicates_es = None
        self._access_groups = None
        self._alert_subject_template = None
        self._alert_level = None
        self._description = None
        self._applies_to = None
        self._technology = None
        self._filters = None
        self._version = None
        self._lineage_id = None
        self._collector = None
        self._tags = None
        self._audit_version = None
        self._installation_metadata = None
        self._alert_body_template = None
        self._checksum = None
        self._name = None
        self._clear_after_ack = None
        self._id = None
        self._access_group_ids = None
        self._alert_effective_ival = None
        self._group = None
        self.discriminator = 'collector'
        if suppress_duplicates_es is not None:
            self.suppress_duplicates_es = suppress_duplicates_es
        if access_groups is not None:
            self.access_groups = access_groups
        if alert_subject_template is not None:
            self.alert_subject_template = alert_subject_template
        if alert_level is not None:
            self.alert_level = alert_level
        if description is not None:
            self.description = description
        if applies_to is not None:
            self.applies_to = applies_to
        if technology is not None:
            self.technology = technology
        if filters is not None:
            self.filters = filters
        if version is not None:
            self.version = version
        if lineage_id is not None:
            self.lineage_id = lineage_id
        if collector is not None:
            self.collector = collector
        if tags is not None:
            self.tags = tags
        if audit_version is not None:
            self.audit_version = audit_version
        if installation_metadata is not None:
            self.installation_metadata = installation_metadata
        if alert_body_template is not None:
            self.alert_body_template = alert_body_template
        if checksum is not None:
            self.checksum = checksum
        self.name = name
        if clear_after_ack is not None:
            self.clear_after_ack = clear_after_ack
        if id is not None:
            self.id = id
        if access_group_ids is not None:
            self.access_group_ids = access_group_ids
        self.alert_effective_ival = alert_effective_ival
        if group is not None:
            self.group = group

    @property
    def suppress_duplicates_es(self):
        """Gets the suppress_duplicates_es of this EventSource.  # noqa: E501

        Whether or not duplicate alerts have to be suppressed  # noqa: E501

        :return: The suppress_duplicates_es of this EventSource.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_duplicates_es

    @suppress_duplicates_es.setter
    def suppress_duplicates_es(self, suppress_duplicates_es):
        """Sets the suppress_duplicates_es of this EventSource.

        Whether or not duplicate alerts have to be suppressed  # noqa: E501

        :param suppress_duplicates_es: The suppress_duplicates_es of this EventSource.  # noqa: E501
        :type: bool
        """

        self._suppress_duplicates_es = suppress_duplicates_es

    @property
    def access_groups(self):
        """Gets the access_groups of this EventSource.  # noqa: E501

        Module's access groups  # noqa: E501

        :return: The access_groups of this EventSource.  # noqa: E501
        :rtype: list[AccessGroup]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this EventSource.

        Module's access groups  # noqa: E501

        :param access_groups: The access_groups of this EventSource.  # noqa: E501
        :type: list[AccessGroup]
        """

        self._access_groups = access_groups

    @property
    def alert_subject_template(self):
        """Gets the alert_subject_template of this EventSource.  # noqa: E501

        The alert message subject for the EventSource  # noqa: E501

        :return: The alert_subject_template of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_subject_template

    @alert_subject_template.setter
    def alert_subject_template(self, alert_subject_template):
        """Sets the alert_subject_template of this EventSource.

        The alert message subject for the EventSource  # noqa: E501

        :param alert_subject_template: The alert_subject_template of this EventSource.  # noqa: E501
        :type: str
        """

        self._alert_subject_template = alert_subject_template

    @property
    def alert_level(self):
        """Gets the alert_level of this EventSource.  # noqa: E501

        The default alert level. The values can be warn | error | critical | doMapping  # noqa: E501

        :return: The alert_level of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this EventSource.

        The default alert level. The values can be warn | error | critical | doMapping  # noqa: E501

        :param alert_level: The alert_level of this EventSource.  # noqa: E501
        :type: str
        """

        self._alert_level = alert_level

    @property
    def description(self):
        """Gets the description of this EventSource.  # noqa: E501

        The description for the LMModule  # noqa: E501

        :return: The description of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventSource.

        The description for the LMModule  # noqa: E501

        :param description: The description of this EventSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applies_to(self):
        """Gets the applies_to of this EventSource.  # noqa: E501

        The Applies To for the LMModule  # noqa: E501

        :return: The applies_to of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this EventSource.

        The Applies To for the LMModule  # noqa: E501

        :param applies_to: The applies_to of this EventSource.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def technology(self):
        """Gets the technology of this EventSource.  # noqa: E501

        The Technical Notes for the LMModule  # noqa: E501

        :return: The technology of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this EventSource.

        The Technical Notes for the LMModule  # noqa: E501

        :param technology: The technology of this EventSource.  # noqa: E501
        :type: str
        """

        self._technology = technology

    @property
    def filters(self):
        """Gets the filters of this EventSource.  # noqa: E501

        The filters for the EventSource  # noqa: E501

        :return: The filters of this EventSource.  # noqa: E501
        :rtype: list[RestEventSourceFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this EventSource.

        The filters for the EventSource  # noqa: E501

        :param filters: The filters of this EventSource.  # noqa: E501
        :type: list[RestEventSourceFilter]
        """

        self._filters = filters

    @property
    def version(self):
        """Gets the version of this EventSource.  # noqa: E501

        The epoch time of the last update to the EventSource  # noqa: E501

        :return: The version of this EventSource.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EventSource.

        The epoch time of the last update to the EventSource  # noqa: E501

        :param version: The version of this EventSource.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def lineage_id(self):
        """Gets the lineage_id of this EventSource.  # noqa: E501

        The lineageId the LMModule belongs to  # noqa: E501

        :return: The lineage_id of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._lineage_id

    @lineage_id.setter
    def lineage_id(self, lineage_id):
        """Sets the lineage_id of this EventSource.

        The lineageId the LMModule belongs to  # noqa: E501

        :param lineage_id: The lineage_id of this EventSource.  # noqa: E501
        :type: str
        """

        self._lineage_id = lineage_id

    @property
    def collector(self):
        """Gets the collector of this EventSource.  # noqa: E501

        The EventSource collector type. The values can be wineventlog | syslog | snmptrap | echo | logfile | scriptevent | awsrss | azurerss | azureadvisor | gcpatom | awsrdspievent | azureresourcehealthevent | azureemergingissue | azureloganalyticsworkspacesevent | awstrustedadvisor | awshealth | awsorganizationalhealth | ipmievent  # noqa: E501

        :return: The collector of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this EventSource.

        The EventSource collector type. The values can be wineventlog | syslog | snmptrap | echo | logfile | scriptevent | awsrss | azurerss | azureadvisor | gcpatom | awsrdspievent | azureresourcehealthevent | azureemergingissue | azureloganalyticsworkspacesevent | awstrustedadvisor | awshealth | awsorganizationalhealth | ipmievent  # noqa: E501

        :param collector: The collector of this EventSource.  # noqa: E501
        :type: str
        """

        self._collector = collector

    @property
    def tags(self):
        """Gets the tags of this EventSource.  # noqa: E501

        The Tags for the LMModule  # noqa: E501

        :return: The tags of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EventSource.

        The Tags for the LMModule  # noqa: E501

        :param tags: The tags of this EventSource.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def audit_version(self):
        """Gets the audit_version of this EventSource.  # noqa: E501

        The auditVersion of the EventSource  # noqa: E501

        :return: The audit_version of this EventSource.  # noqa: E501
        :rtype: int
        """
        return self._audit_version

    @audit_version.setter
    def audit_version(self, audit_version):
        """Sets the audit_version of this EventSource.

        The auditVersion of the EventSource  # noqa: E501

        :param audit_version: The audit_version of this EventSource.  # noqa: E501
        :type: int
        """

        self._audit_version = audit_version

    @property
    def installation_metadata(self):
        """Gets the installation_metadata of this EventSource.  # noqa: E501


        :return: The installation_metadata of this EventSource.  # noqa: E501
        :rtype: IntegrationMetadata
        """
        return self._installation_metadata

    @installation_metadata.setter
    def installation_metadata(self, installation_metadata):
        """Sets the installation_metadata of this EventSource.


        :param installation_metadata: The installation_metadata of this EventSource.  # noqa: E501
        :type: IntegrationMetadata
        """

        self._installation_metadata = installation_metadata

    @property
    def alert_body_template(self):
        """Gets the alert_body_template of this EventSource.  # noqa: E501

        The alert message body for the EventSource  # noqa: E501

        :return: The alert_body_template of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._alert_body_template

    @alert_body_template.setter
    def alert_body_template(self, alert_body_template):
        """Sets the alert_body_template of this EventSource.

        The alert message body for the EventSource  # noqa: E501

        :param alert_body_template: The alert_body_template of this EventSource.  # noqa: E501
        :type: str
        """

        self._alert_body_template = alert_body_template

    @property
    def checksum(self):
        """Gets the checksum of this EventSource.  # noqa: E501

        The metadata checksum for the LMModule content  # noqa: E501

        :return: The checksum of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this EventSource.

        The metadata checksum for the LMModule content  # noqa: E501

        :param checksum: The checksum of this EventSource.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def name(self):
        """Gets the name of this EventSource.  # noqa: E501

        The name of the EventSource  # noqa: E501

        :return: The name of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventSource.

        The name of the EventSource  # noqa: E501

        :param name: The name of this EventSource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def clear_after_ack(self):
        """Gets the clear_after_ack of this EventSource.  # noqa: E501

        Whether or not the alert should clear after acknowledgement  # noqa: E501

        :return: The clear_after_ack of this EventSource.  # noqa: E501
        :rtype: bool
        """
        return self._clear_after_ack

    @clear_after_ack.setter
    def clear_after_ack(self, clear_after_ack):
        """Sets the clear_after_ack of this EventSource.

        Whether or not the alert should clear after acknowledgement  # noqa: E501

        :param clear_after_ack: The clear_after_ack of this EventSource.  # noqa: E501
        :type: bool
        """

        self._clear_after_ack = clear_after_ack

    @property
    def id(self):
        """Gets the id of this EventSource.  # noqa: E501

        The ID of the LMModule  # noqa: E501

        :return: The id of this EventSource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventSource.

        The ID of the LMModule  # noqa: E501

        :param id: The id of this EventSource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def access_group_ids(self):
        """Gets the access_group_ids of this EventSource.  # noqa: E501

        The Access Groups Id's  # noqa: E501

        :return: The access_group_ids of this EventSource.  # noqa: E501
        :rtype: list[int]
        """
        return self._access_group_ids

    @access_group_ids.setter
    def access_group_ids(self, access_group_ids):
        """Sets the access_group_ids of this EventSource.

        The Access Groups Id's  # noqa: E501

        :param access_group_ids: The access_group_ids of this EventSource.  # noqa: E501
        :type: list[int]
        """

        self._access_group_ids = access_group_ids

    @property
    def alert_effective_ival(self):
        """Gets the alert_effective_ival of this EventSource.  # noqa: E501

        The time in minutes after which the alert should clear  # noqa: E501

        :return: The alert_effective_ival of this EventSource.  # noqa: E501
        :rtype: int
        """
        return self._alert_effective_ival

    @alert_effective_ival.setter
    def alert_effective_ival(self, alert_effective_ival):
        """Sets the alert_effective_ival of this EventSource.

        The time in minutes after which the alert should clear  # noqa: E501

        :param alert_effective_ival: The alert_effective_ival of this EventSource.  # noqa: E501
        :type: int
        """
        if alert_effective_ival is None:
            raise ValueError("Invalid value for `alert_effective_ival`, must not be `None`")  # noqa: E501

        self._alert_effective_ival = alert_effective_ival

    @property
    def group(self):
        """Gets the group of this EventSource.  # noqa: E501

        The group the LMModule is in  # noqa: E501

        :return: The group of this EventSource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this EventSource.

        The group the LMModule is in  # noqa: E501

        :param group: The group of this EventSource.  # noqa: E501
        :type: str
        """

        self._group = group

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(EventSource, dict):
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
        if not isinstance(other, EventSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
