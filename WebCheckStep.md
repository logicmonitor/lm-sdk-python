# WebCheckStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema** | **str** | HTTP schema | [optional] 
**resp_type** | **str** | Plain Text/String | Glob expression | JSON | XML | Multi line key value pair Step Response Type | [optional] 
**http_headers** | **str** | HTTP header | [optional] 
**auth** | [**Authentication**](Authentication.md) | Authorization Information | [optional] 
**match_type** | **str** | Body match type | [optional] 
**description** | **str** | The description of the Step | [optional] 
**type** | **str** | script | config The type of service step | [optional] 
**timeout** | **int** | Request timeout measured in seconds | [optional] 
**use_default_root** | **object** | true | falseCheck if using the default root | [optional] 
**path** | **str** | Path for JSON, XPATH | [optional] 
**http_method** | **str** | GET | HEAD | POST Specifies the type of HTTP method | [optional] 
**enable** | **object** | true | false Specifies whether to enable step or not | [optional] 
**http_version** | **str** | 1.1 | 1 Specifies HTTP version | [optional] 
**keyword** | **str** | Keyword that matches the body | [optional] 
**resp_script** | **str** | The Step Response Script | [optional] 
**label** | **str** | The Label of the Step | [optional] 
**url** | **str** | The URL of service step | [optional] 
**invert_match** | **bool** | true | false Checks if invert matches or not | [optional] 
**req_script** | **str** | The Request Script | [optional] 
**http_body** | **str** | HTTP Body | [optional] 
**follow_redirection** | **object** | true | false Specifies whether to follow redirection or not | [optional] 
**post_data_edit_type** | **str** | Raw | Formatted Data Specifies POST data type | [optional] 
**name** | **str** | The name of the Step | [optional] 
**require_auth** | **bool** | true | false Checks if authorization required or not | [optional] 
**req_type** | **str** | script | config Step Request Type | [optional] 
**fullpage_load** | **bool** | true | false Checks if full page should be loaded or not | [optional] 
**status_code** | **str** | The expected status code | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


