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

class TopologySource(object):
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
        'collector_attribute': 'ScriptCollectorAttribute',
        'collection_method': 'str',
        'access_groups': 'list[AccessGroup]',
        'description': 'str',
        'applies_to': 'str',
        'technology': 'str',
        'version': 'int',
        'lineage_id': 'str',
        'tags': 'str',
        'audit_version': 'int',
        'installation_metadata': 'IntegrationMetadata',
        'collect_interval': 'int',
        'checksum': 'str',
        'name': 'str',
        'id': 'int',
        'access_group_ids': 'list[int]',
        'group': 'str'
    }

    attribute_map = {
        'collector_attribute': 'collectorAttribute',
        'collection_method': 'collectionMethod',
        'access_groups': 'accessGroups',
        'description': 'description',
        'applies_to': 'appliesTo',
        'technology': 'technology',
        'version': 'version',
        'lineage_id': 'lineageId',
        'tags': 'tags',
        'audit_version': 'auditVersion',
        'installation_metadata': 'installationMetadata',
        'collect_interval': 'collectInterval',
        'checksum': 'checksum',
        'name': 'name',
        'id': 'id',
        'access_group_ids': 'accessGroupIds',
        'group': 'group'
    }

    def __init__(self, collector_attribute=None, collection_method=None, access_groups=None, description=None, applies_to=None, technology=None, version=None, lineage_id=None, tags=None, audit_version=None, installation_metadata=None, collect_interval=None, checksum=None, name=None, id=None, access_group_ids=None, group=None):  # noqa: E501
        """TopologySource - a model defined in Swagger"""  # noqa: E501
        self._collector_attribute = None
        self._collection_method = None
        self._access_groups = None
        self._description = None
        self._applies_to = None
        self._technology = None
        self._version = None
        self._lineage_id = None
        self._tags = None
        self._audit_version = None
        self._installation_metadata = None
        self._collect_interval = None
        self._checksum = None
        self._name = None
        self._id = None
        self._access_group_ids = None
        self._group = None
        self.discriminator = None
        self.collector_attribute = collector_attribute
        self.collection_method = collection_method
        if access_groups is not None:
            self.access_groups = access_groups
        if description is not None:
            self.description = description
        if applies_to is not None:
            self.applies_to = applies_to
        if technology is not None:
            self.technology = technology
        if version is not None:
            self.version = version
        if lineage_id is not None:
            self.lineage_id = lineage_id
        if tags is not None:
            self.tags = tags
        if audit_version is not None:
            self.audit_version = audit_version
        if installation_metadata is not None:
            self.installation_metadata = installation_metadata
        if collect_interval is not None:
            self.collect_interval = collect_interval
        if checksum is not None:
            self.checksum = checksum
        self.name = name
        if id is not None:
            self.id = id
        if access_group_ids is not None:
            self.access_group_ids = access_group_ids
        if group is not None:
            self.group = group

    @property
    def collector_attribute(self):
        """Gets the collector_attribute of this TopologySource.  # noqa: E501


        :return: The collector_attribute of this TopologySource.  # noqa: E501
        :rtype: ScriptCollectorAttribute
        """
        return self._collector_attribute

    @collector_attribute.setter
    def collector_attribute(self, collector_attribute):
        """Sets the collector_attribute of this TopologySource.


        :param collector_attribute: The collector_attribute of this TopologySource.  # noqa: E501
        :type: ScriptCollectorAttribute
        """
        if collector_attribute is None:
            raise ValueError("Invalid value for `collector_attribute`, must not be `None`")  # noqa: E501

        self._collector_attribute = collector_attribute

    @property
    def collection_method(self):
        """Gets the collection_method of this TopologySource.  # noqa: E501

        The topology will be build on properties or traditional way, default 'script'  # noqa: E501

        :return: The collection_method of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """Sets the collection_method of this TopologySource.

        The topology will be build on properties or traditional way, default 'script'  # noqa: E501

        :param collection_method: The collection_method of this TopologySource.  # noqa: E501
        :type: str
        """
        if collection_method is None:
            raise ValueError("Invalid value for `collection_method`, must not be `None`")  # noqa: E501

        self._collection_method = collection_method

    @property
    def access_groups(self):
        """Gets the access_groups of this TopologySource.  # noqa: E501

        Module's access groups  # noqa: E501

        :return: The access_groups of this TopologySource.  # noqa: E501
        :rtype: list[AccessGroup]
        """
        return self._access_groups

    @access_groups.setter
    def access_groups(self, access_groups):
        """Sets the access_groups of this TopologySource.

        Module's access groups  # noqa: E501

        :param access_groups: The access_groups of this TopologySource.  # noqa: E501
        :type: list[AccessGroup]
        """

        self._access_groups = access_groups

    @property
    def description(self):
        """Gets the description of this TopologySource.  # noqa: E501

        The description for the LMModule  # noqa: E501

        :return: The description of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TopologySource.

        The description for the LMModule  # noqa: E501

        :param description: The description of this TopologySource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applies_to(self):
        """Gets the applies_to of this TopologySource.  # noqa: E501

        The Applies To for the LMModule  # noqa: E501

        :return: The applies_to of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this TopologySource.

        The Applies To for the LMModule  # noqa: E501

        :param applies_to: The applies_to of this TopologySource.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def technology(self):
        """Gets the technology of this TopologySource.  # noqa: E501

        The Technical Notes for the LMModule  # noqa: E501

        :return: The technology of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this TopologySource.

        The Technical Notes for the LMModule  # noqa: E501

        :param technology: The technology of this TopologySource.  # noqa: E501
        :type: str
        """

        self._technology = technology

    @property
    def version(self):
        """Gets the version of this TopologySource.  # noqa: E501

        The TopologySource version  # noqa: E501

        :return: The version of this TopologySource.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TopologySource.

        The TopologySource version  # noqa: E501

        :param version: The version of this TopologySource.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def lineage_id(self):
        """Gets the lineage_id of this TopologySource.  # noqa: E501

        The lineageId the LMModule belongs to  # noqa: E501

        :return: The lineage_id of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._lineage_id

    @lineage_id.setter
    def lineage_id(self, lineage_id):
        """Sets the lineage_id of this TopologySource.

        The lineageId the LMModule belongs to  # noqa: E501

        :param lineage_id: The lineage_id of this TopologySource.  # noqa: E501
        :type: str
        """

        self._lineage_id = lineage_id

    @property
    def tags(self):
        """Gets the tags of this TopologySource.  # noqa: E501

        The Tags for the LMModule  # noqa: E501

        :return: The tags of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TopologySource.

        The Tags for the LMModule  # noqa: E501

        :param tags: The tags of this TopologySource.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def audit_version(self):
        """Gets the audit_version of this TopologySource.  # noqa: E501

        The TopologySource audit Version  # noqa: E501

        :return: The audit_version of this TopologySource.  # noqa: E501
        :rtype: int
        """
        return self._audit_version

    @audit_version.setter
    def audit_version(self, audit_version):
        """Sets the audit_version of this TopologySource.

        The TopologySource audit Version  # noqa: E501

        :param audit_version: The audit_version of this TopologySource.  # noqa: E501
        :type: int
        """

        self._audit_version = audit_version

    @property
    def installation_metadata(self):
        """Gets the installation_metadata of this TopologySource.  # noqa: E501


        :return: The installation_metadata of this TopologySource.  # noqa: E501
        :rtype: IntegrationMetadata
        """
        return self._installation_metadata

    @installation_metadata.setter
    def installation_metadata(self, installation_metadata):
        """Sets the installation_metadata of this TopologySource.


        :param installation_metadata: The installation_metadata of this TopologySource.  # noqa: E501
        :type: IntegrationMetadata
        """

        self._installation_metadata = installation_metadata

    @property
    def collect_interval(self):
        """Gets the collect_interval of this TopologySource.  # noqa: E501

        The TopologySource data collect interval in seconds, default 3600  # noqa: E501

        :return: The collect_interval of this TopologySource.  # noqa: E501
        :rtype: int
        """
        return self._collect_interval

    @collect_interval.setter
    def collect_interval(self, collect_interval):
        """Sets the collect_interval of this TopologySource.

        The TopologySource data collect interval in seconds, default 3600  # noqa: E501

        :param collect_interval: The collect_interval of this TopologySource.  # noqa: E501
        :type: int
        """
        allowed_values = [1800, 3600, 14400, 43200]  # noqa: E501
        if collect_interval not in allowed_values:
            raise ValueError(
                "Invalid value for `collect_interval` ({0}), must be one of {1}"  # noqa: E501
                .format(collect_interval, allowed_values)
            )

        self._collect_interval = collect_interval

    @property
    def checksum(self):
        """Gets the checksum of this TopologySource.  # noqa: E501

        The metadata checksum for the LMModule content  # noqa: E501

        :return: The checksum of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this TopologySource.

        The metadata checksum for the LMModule content  # noqa: E501

        :param checksum: The checksum of this TopologySource.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def name(self):
        """Gets the name of this TopologySource.  # noqa: E501

        The TopologySource name  # noqa: E501

        :return: The name of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TopologySource.

        The TopologySource name  # noqa: E501

        :param name: The name of this TopologySource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this TopologySource.  # noqa: E501

        The ID of the LMModule  # noqa: E501

        :return: The id of this TopologySource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopologySource.

        The ID of the LMModule  # noqa: E501

        :param id: The id of this TopologySource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def access_group_ids(self):
        """Gets the access_group_ids of this TopologySource.  # noqa: E501

        The Access Groups Id's  # noqa: E501

        :return: The access_group_ids of this TopologySource.  # noqa: E501
        :rtype: list[int]
        """
        return self._access_group_ids

    @access_group_ids.setter
    def access_group_ids(self, access_group_ids):
        """Sets the access_group_ids of this TopologySource.

        The Access Groups Id's  # noqa: E501

        :param access_group_ids: The access_group_ids of this TopologySource.  # noqa: E501
        :type: list[int]
        """

        self._access_group_ids = access_group_ids

    @property
    def group(self):
        """Gets the group of this TopologySource.  # noqa: E501

        The group the LMModule is in  # noqa: E501

        :return: The group of this TopologySource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TopologySource.

        The group the LMModule is in  # noqa: E501

        :param group: The group of this TopologySource.  # noqa: E501
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
        if issubclass(TopologySource, dict):
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
        if not isinstance(other, TopologySource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
