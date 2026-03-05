# ChangedEvent


**Source:** `waylay.services.resources.models.changed_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChangedEventType**](ChangedEventType.md) |  | [optional] 
**old_values** | **object** | old values of all attributes that have changed | [optional] 


## Example

```python
from waylay.services.resources.models.changed_event import ChangedEvent

changed_event = ChangedEvent(type=..., old_values=...)

# Create from JSON
changed_event = ChangedEvent.from_json('{ "type": ..., "oldValues": ... }')

# Export to dictionary
changed_event_dict = changed_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


