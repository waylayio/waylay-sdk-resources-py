# DiscoveredEvent


**Source:** `waylay.services.resources.models.discovered_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DiscoveredEventType**](DiscoveredEventType.md) |  | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 


## Example

```python
from waylay.services.resources.models.discovered_event import DiscoveredEvent

discovered_event = DiscoveredEvent(type=..., message=...)

# Create from JSON
discovered_event = DiscoveredEvent.from_json('{ "type": ..., "message": ... }')

# Export to dictionary
discovered_event_dict = discovered_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


