# CreateEvent


**Source:** `waylay.services.resources.models.create_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CreateEventType**](CreateEventType.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.create_event import CreateEvent

create_event = CreateEvent(type=...)

# Create from JSON
create_event = CreateEvent.from_json('{ "type": ... }')

# Export to dictionary
create_event_dict = create_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


