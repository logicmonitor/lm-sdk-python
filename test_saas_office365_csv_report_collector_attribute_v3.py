# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. <br> <br> Note: <ul> <li> For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. </li> <li> Both underscore and camelCase are supported if parameters are encapsulated within the body. </li> <li> Only camelCase is supported if parameters are encapsulated within the body and also if the user is passing raw JSON as REQUEST parameter. However, the RESPONSE parameters always contain an underscore. For example, you can use testLocation or test_location in the REQUEST parameter. But the RESPONSE parameter will always be test_location. </li> <li> The fields parameter only supports camelCase. </li> </ul>  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import logicmonitor_sdk
from logicmonitor_sdk.models.saas_office365_csv_report_collector_attribute_v3 import SaasOffice365CsvReportCollectorAttributeV3  # noqa: E501
from logicmonitor_sdk.rest import ApiException


class TestSaasOffice365CsvReportCollectorAttributeV3(unittest.TestCase):
    """SaasOffice365CsvReportCollectorAttributeV3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSaasOffice365CsvReportCollectorAttributeV3(self):
        """Test SaasOffice365CsvReportCollectorAttributeV3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = logicmonitor_sdk.models.saas_office365_csv_report_collector_attribute_v3.SaasOffice365CsvReportCollectorAttributeV3()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
