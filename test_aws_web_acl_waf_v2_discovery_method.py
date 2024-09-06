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
from logicmonitor_sdk.models.aws_web_acl_waf_v2_discovery_method import AwsWebACLWafV2DiscoveryMethod  # noqa: E501
from logicmonitor_sdk.rest import ApiException


class TestAwsWebACLWafV2DiscoveryMethod(unittest.TestCase):
    """AwsWebACLWafV2DiscoveryMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAwsWebACLWafV2DiscoveryMethod(self):
        """Test AwsWebACLWafV2DiscoveryMethod"""
        # FIXME: construct object with mandatory attributes with example values
        # model = logicmonitor_sdk.models.aws_web_acl_waf_v2_discovery_method.AwsWebACLWafV2DiscoveryMethod()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
