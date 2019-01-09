# AlertFilters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**severity** | **str** | Displayed alerts must have a severity that satisfies this criteria. Multiple severities are separated by commas | [optional] 
**sdted** | **str** | Displayed alerts must have an SDT status that meets this criteria | [optional] 
**chain** | **str** | Displayed alerts must be routed to an escalation chain that satisfies this filter. Glob is accepted, and * and an empty string both match all escalation chains | [optional] 
**instance** | **str** | Displayed alerts must be associated with instances that meet this filter criteria. Glob is accepted, and * and an empty string both match all instances | [optional] 
**data_point** | **str** | Displayed alerts must be associated with datapoints that meet this filter criteria. Glob is accepted, and * and an empty string both match all datapoints | [optional] 
**host** | **str** | Displayed alerts must be associated with devices that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all devices | [optional] 
**rule** | **str** | Displayed alerts must match a rule that satisfies this filter. Glob is accepted, and * and an empty string both match all rules | [optional] 
**keyword** | **str** | The key word for free search | [optional] 
**data_source** | **str** | Displayed alerts must be associated with datasources that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all datasources | [optional] 
**acked** | **str** | Displayed alerts must have an acknowledgement status that satisfies this criteria | [optional] 
**cleared** | **str** | Displayed alerts must be active if cleared&#x3D;no, and must have cleared in the past 7 days if cleared&#x3D;all | [optional] 
**group** | **str** | Displayed alerts must be associated with groups that meet this filter criteria. Glob is accepted, and * and an empty string both indicate all groups | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


