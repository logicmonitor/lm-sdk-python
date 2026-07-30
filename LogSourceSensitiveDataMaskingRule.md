# LogSourceSensitiveDataMaskingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**masked_value** | **str** | Replacement value when the rule matches | [optional] 
**valid_masking_rule_for_type** | **bool** |  | [optional] 
**masking_rule** | **str** | Pattern or literal to match (for REGEX, a valid regular expression) | [optional] 
**description** | **str** | Optional description | [optional] 
**id** | **str** | Stable id for the rule | [optional] 
**type** | **str** | Match semantics: REGEX or JSON (stored as JSON type in DB) | [optional] 
**key** | **str** | Log field or attribute key this rule applies to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

