# DeletedResourceEvent


**Source:** `waylay.services.resources.models.deleted_resource_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | [optional] 
**cascade_delete** | [**List[CascadeDeleteOption]**](CascadeDeleteOption.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.deleted_resource_event import DeletedResourceEvent

deleted_resource_event = DeletedResourceEvent(type=..., cascade_delete=...)

# Create from JSON
deleted_resource_event = DeletedResourceEvent.from_json(
    '{ "type": ..., "cascadeDelete": ... }'
)

# Export to dictionary
deleted_resource_event_dict = deleted_resource_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


