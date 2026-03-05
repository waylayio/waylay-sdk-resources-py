# DeletedEvent


**Source:** `waylay.services.resources.models.deleted_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.deleted_event import DeletedEvent

deleted_event = DeletedEvent(type=...)

# Create from JSON
deleted_event = DeletedEvent.from_json('{ "type": ... }')

# Export to dictionary
deleted_event_dict = deleted_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


