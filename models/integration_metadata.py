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

class IntegrationMetadata(object):
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
        'target_last_published_id': 'str',
        'target_last_published_checksum': 'str',
        'target_last_published_version': 'str',
        'origin_checksum': 'str',
        'origin_author_namespace': 'str',
        'origin_locator': 'str',
        'is_changed_from_origin': 'bool',
        'audited_registry_id': 'str',
        'target_lineage_id': 'str',
        'logic_module_type': 'str',
        'is_changed_from_target_last_published': 'bool',
        'origin_lineage_id': 'str',
        'origin_author_company_uuid': 'str',
        'local_module_id': 'int',
        'origin_registry_id': 'str',
        'origin_version': 'str',
        'audited_version': 'str',
        'origin_name': 'str'
    }

    attribute_map = {
        'target_last_published_id': 'targetLastPublishedId',
        'target_last_published_checksum': 'targetLastPublishedChecksum',
        'target_last_published_version': 'targetLastPublishedVersion',
        'origin_checksum': 'originChecksum',
        'origin_author_namespace': 'originAuthorNamespace',
        'origin_locator': 'originLocator',
        'is_changed_from_origin': 'isChangedFromOrigin',
        'audited_registry_id': 'auditedRegistryId',
        'target_lineage_id': 'targetLineageId',
        'logic_module_type': 'logicModuleType',
        'is_changed_from_target_last_published': 'isChangedFromTargetLastPublished',
        'origin_lineage_id': 'originLineageId',
        'origin_author_company_uuid': 'originAuthorCompanyUUID',
        'local_module_id': 'localModuleId',
        'origin_registry_id': 'originRegistryId',
        'origin_version': 'originVersion',
        'audited_version': 'auditedVersion',
        'origin_name': 'originName'
    }

    def __init__(self, target_last_published_id=None, target_last_published_checksum=None, target_last_published_version=None, origin_checksum=None, origin_author_namespace=None, origin_locator=None, is_changed_from_origin=None, audited_registry_id=None, target_lineage_id=None, logic_module_type=None, is_changed_from_target_last_published=None, origin_lineage_id=None, origin_author_company_uuid=None, local_module_id=None, origin_registry_id=None, origin_version=None, audited_version=None, origin_name=None):  # noqa: E501
        """IntegrationMetadata - a model defined in Swagger"""  # noqa: E501
        self._target_last_published_id = None
        self._target_last_published_checksum = None
        self._target_last_published_version = None
        self._origin_checksum = None
        self._origin_author_namespace = None
        self._origin_locator = None
        self._is_changed_from_origin = None
        self._audited_registry_id = None
        self._target_lineage_id = None
        self._logic_module_type = None
        self._is_changed_from_target_last_published = None
        self._origin_lineage_id = None
        self._origin_author_company_uuid = None
        self._local_module_id = None
        self._origin_registry_id = None
        self._origin_version = None
        self._audited_version = None
        self._origin_name = None
        self.discriminator = None
        if target_last_published_id is not None:
            self.target_last_published_id = target_last_published_id
        if target_last_published_checksum is not None:
            self.target_last_published_checksum = target_last_published_checksum
        if target_last_published_version is not None:
            self.target_last_published_version = target_last_published_version
        if origin_checksum is not None:
            self.origin_checksum = origin_checksum
        if origin_author_namespace is not None:
            self.origin_author_namespace = origin_author_namespace
        if origin_locator is not None:
            self.origin_locator = origin_locator
        if is_changed_from_origin is not None:
            self.is_changed_from_origin = is_changed_from_origin
        if audited_registry_id is not None:
            self.audited_registry_id = audited_registry_id
        if target_lineage_id is not None:
            self.target_lineage_id = target_lineage_id
        if logic_module_type is not None:
            self.logic_module_type = logic_module_type
        if is_changed_from_target_last_published is not None:
            self.is_changed_from_target_last_published = is_changed_from_target_last_published
        if origin_lineage_id is not None:
            self.origin_lineage_id = origin_lineage_id
        if origin_author_company_uuid is not None:
            self.origin_author_company_uuid = origin_author_company_uuid
        if local_module_id is not None:
            self.local_module_id = local_module_id
        if origin_registry_id is not None:
            self.origin_registry_id = origin_registry_id
        if origin_version is not None:
            self.origin_version = origin_version
        if audited_version is not None:
            self.audited_version = audited_version
        if origin_name is not None:
            self.origin_name = origin_name

    @property
    def target_last_published_id(self):
        """Gets the target_last_published_id of this IntegrationMetadata.  # noqa: E501

        Specifies the target last published Id  # noqa: E501

        :return: The target_last_published_id of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._target_last_published_id

    @target_last_published_id.setter
    def target_last_published_id(self, target_last_published_id):
        """Sets the target_last_published_id of this IntegrationMetadata.

        Specifies the target last published Id  # noqa: E501

        :param target_last_published_id: The target_last_published_id of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._target_last_published_id = target_last_published_id

    @property
    def target_last_published_checksum(self):
        """Gets the target_last_published_checksum of this IntegrationMetadata.  # noqa: E501

        The metadata checksum for the target last published LMModule content  # noqa: E501

        :return: The target_last_published_checksum of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._target_last_published_checksum

    @target_last_published_checksum.setter
    def target_last_published_checksum(self, target_last_published_checksum):
        """Sets the target_last_published_checksum of this IntegrationMetadata.

        The metadata checksum for the target last published LMModule content  # noqa: E501

        :param target_last_published_checksum: The target_last_published_checksum of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._target_last_published_checksum = target_last_published_checksum

    @property
    def target_last_published_version(self):
        """Gets the target_last_published_version of this IntegrationMetadata.  # noqa: E501

        Specifies the target last published version  # noqa: E501

        :return: The target_last_published_version of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._target_last_published_version

    @target_last_published_version.setter
    def target_last_published_version(self, target_last_published_version):
        """Sets the target_last_published_version of this IntegrationMetadata.

        Specifies the target last published version  # noqa: E501

        :param target_last_published_version: The target_last_published_version of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._target_last_published_version = target_last_published_version

    @property
    def origin_checksum(self):
        """Gets the origin_checksum of this IntegrationMetadata.  # noqa: E501

        The metadata checksum for the LMModule content  # noqa: E501

        :return: The origin_checksum of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_checksum

    @origin_checksum.setter
    def origin_checksum(self, origin_checksum):
        """Sets the origin_checksum of this IntegrationMetadata.

        The metadata checksum for the LMModule content  # noqa: E501

        :param origin_checksum: The origin_checksum of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_checksum = origin_checksum

    @property
    def origin_author_namespace(self):
        """Gets the origin_author_namespace of this IntegrationMetadata.  # noqa: E501

        Specifies the origin Author companies namespace  # noqa: E501

        :return: The origin_author_namespace of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_author_namespace

    @origin_author_namespace.setter
    def origin_author_namespace(self, origin_author_namespace):
        """Sets the origin_author_namespace of this IntegrationMetadata.

        Specifies the origin Author companies namespace  # noqa: E501

        :param origin_author_namespace: The origin_author_namespace of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_author_namespace = origin_author_namespace

    @property
    def origin_locator(self):
        """Gets the origin_locator of this IntegrationMetadata.  # noqa: E501

        Specifies the origin version locator  # noqa: E501

        :return: The origin_locator of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_locator

    @origin_locator.setter
    def origin_locator(self, origin_locator):
        """Sets the origin_locator of this IntegrationMetadata.

        Specifies the origin version locator  # noqa: E501

        :param origin_locator: The origin_locator of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_locator = origin_locator

    @property
    def is_changed_from_origin(self):
        """Gets the is_changed_from_origin of this IntegrationMetadata.  # noqa: E501

        Specifies if the Applies To function is changed from origin or not  # noqa: E501

        :return: The is_changed_from_origin of this IntegrationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_changed_from_origin

    @is_changed_from_origin.setter
    def is_changed_from_origin(self, is_changed_from_origin):
        """Sets the is_changed_from_origin of this IntegrationMetadata.

        Specifies if the Applies To function is changed from origin or not  # noqa: E501

        :param is_changed_from_origin: The is_changed_from_origin of this IntegrationMetadata.  # noqa: E501
        :type: bool
        """

        self._is_changed_from_origin = is_changed_from_origin

    @property
    def audited_registry_id(self):
        """Gets the audited_registry_id of this IntegrationMetadata.  # noqa: E501

        Specifies the audited registry Id  # noqa: E501

        :return: The audited_registry_id of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._audited_registry_id

    @audited_registry_id.setter
    def audited_registry_id(self, audited_registry_id):
        """Sets the audited_registry_id of this IntegrationMetadata.

        Specifies the audited registry Id  # noqa: E501

        :param audited_registry_id: The audited_registry_id of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._audited_registry_id = audited_registry_id

    @property
    def target_lineage_id(self):
        """Gets the target_lineage_id of this IntegrationMetadata.  # noqa: E501

        Specifies the target lineage Id  # noqa: E501

        :return: The target_lineage_id of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._target_lineage_id

    @target_lineage_id.setter
    def target_lineage_id(self, target_lineage_id):
        """Sets the target_lineage_id of this IntegrationMetadata.

        Specifies the target lineage Id  # noqa: E501

        :param target_lineage_id: The target_lineage_id of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._target_lineage_id = target_lineage_id

    @property
    def logic_module_type(self):
        """Gets the logic_module_type of this IntegrationMetadata.  # noqa: E501

        The values can be DataSources | EventSources | PropertySources | ConfigSources | LogSources | TopologySources | Jobmonitors | AppliesTo Functions | SNMP SysOID Maps The type of LogicModule  # noqa: E501

        :return: The logic_module_type of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._logic_module_type

    @logic_module_type.setter
    def logic_module_type(self, logic_module_type):
        """Sets the logic_module_type of this IntegrationMetadata.

        The values can be DataSources | EventSources | PropertySources | ConfigSources | LogSources | TopologySources | Jobmonitors | AppliesTo Functions | SNMP SysOID Maps The type of LogicModule  # noqa: E501

        :param logic_module_type: The logic_module_type of this IntegrationMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["DATASOURCE", "EVENTSOURCE", "JOBMONITOR", "APPLIESTO_FUNCTION", "SNMP_SYSOID_MAP", "PROPERTYSOURCE", "CONFIGSOURCE", "TOPOLOGYSOURCE", "LOGSOURCE"]  # noqa: E501
        if logic_module_type not in allowed_values:
            raise ValueError(
                "Invalid value for `logic_module_type` ({0}), must be one of {1}"  # noqa: E501
                .format(logic_module_type, allowed_values)
            )

        self._logic_module_type = logic_module_type

    @property
    def is_changed_from_target_last_published(self):
        """Gets the is_changed_from_target_last_published of this IntegrationMetadata.  # noqa: E501

        Specifies if the Applies To function is changed from target last published or not  # noqa: E501

        :return: The is_changed_from_target_last_published of this IntegrationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_changed_from_target_last_published

    @is_changed_from_target_last_published.setter
    def is_changed_from_target_last_published(self, is_changed_from_target_last_published):
        """Sets the is_changed_from_target_last_published of this IntegrationMetadata.

        Specifies if the Applies To function is changed from target last published or not  # noqa: E501

        :param is_changed_from_target_last_published: The is_changed_from_target_last_published of this IntegrationMetadata.  # noqa: E501
        :type: bool
        """

        self._is_changed_from_target_last_published = is_changed_from_target_last_published

    @property
    def origin_lineage_id(self):
        """Gets the origin_lineage_id of this IntegrationMetadata.  # noqa: E501

        The origin lineage Id of the LMmodule  # noqa: E501

        :return: The origin_lineage_id of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_lineage_id

    @origin_lineage_id.setter
    def origin_lineage_id(self, origin_lineage_id):
        """Sets the origin_lineage_id of this IntegrationMetadata.

        The origin lineage Id of the LMmodule  # noqa: E501

        :param origin_lineage_id: The origin_lineage_id of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_lineage_id = origin_lineage_id

    @property
    def origin_author_company_uuid(self):
        """Gets the origin_author_company_uuid of this IntegrationMetadata.  # noqa: E501

        Specifies the origin Author companies unique Id  # noqa: E501

        :return: The origin_author_company_uuid of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_author_company_uuid

    @origin_author_company_uuid.setter
    def origin_author_company_uuid(self, origin_author_company_uuid):
        """Sets the origin_author_company_uuid of this IntegrationMetadata.

        Specifies the origin Author companies unique Id  # noqa: E501

        :param origin_author_company_uuid: The origin_author_company_uuid of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_author_company_uuid = origin_author_company_uuid

    @property
    def local_module_id(self):
        """Gets the local_module_id of this IntegrationMetadata.  # noqa: E501

        The LocalModule Id  # noqa: E501

        :return: The local_module_id of this IntegrationMetadata.  # noqa: E501
        :rtype: int
        """
        return self._local_module_id

    @local_module_id.setter
    def local_module_id(self, local_module_id):
        """Sets the local_module_id of this IntegrationMetadata.

        The LocalModule Id  # noqa: E501

        :param local_module_id: The local_module_id of this IntegrationMetadata.  # noqa: E501
        :type: int
        """

        self._local_module_id = local_module_id

    @property
    def origin_registry_id(self):
        """Gets the origin_registry_id of this IntegrationMetadata.  # noqa: E501

        The Registry ID of the Exchange Integration this module is based from  # noqa: E501

        :return: The origin_registry_id of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_registry_id

    @origin_registry_id.setter
    def origin_registry_id(self, origin_registry_id):
        """Sets the origin_registry_id of this IntegrationMetadata.

        The Registry ID of the Exchange Integration this module is based from  # noqa: E501

        :param origin_registry_id: The origin_registry_id of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_registry_id = origin_registry_id

    @property
    def origin_version(self):
        """Gets the origin_version of this IntegrationMetadata.  # noqa: E501

        Specifies the origin version  # noqa: E501

        :return: The origin_version of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_version

    @origin_version.setter
    def origin_version(self, origin_version):
        """Sets the origin_version of this IntegrationMetadata.

        Specifies the origin version  # noqa: E501

        :param origin_version: The origin_version of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_version = origin_version

    @property
    def audited_version(self):
        """Gets the audited_version of this IntegrationMetadata.  # noqa: E501

        Specifies the audited registry version  # noqa: E501

        :return: The audited_version of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._audited_version

    @audited_version.setter
    def audited_version(self, audited_version):
        """Sets the audited_version of this IntegrationMetadata.

        Specifies the audited registry version  # noqa: E501

        :param audited_version: The audited_version of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._audited_version = audited_version

    @property
    def origin_name(self):
        """Gets the origin_name of this IntegrationMetadata.  # noqa: E501

        Specifies the origin module name  # noqa: E501

        :return: The origin_name of this IntegrationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._origin_name

    @origin_name.setter
    def origin_name(self, origin_name):
        """Sets the origin_name of this IntegrationMetadata.

        Specifies the origin module name  # noqa: E501

        :param origin_name: The origin_name of this IntegrationMetadata.  # noqa: E501
        :type: str
        """

        self._origin_name = origin_name

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
        if issubclass(IntegrationMetadata, dict):
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
        if not isinstance(other, IntegrationMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
