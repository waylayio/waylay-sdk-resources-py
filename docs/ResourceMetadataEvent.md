# ResourceMetadataEvent


**Source:** `waylay.services.resources.models.resource_metadata_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DiscoveredEventType**](DiscoveredEventType.md) |  | 
**object_type** | [**ResourceMetadataEventResource**](ResourceMetadataEventResource.md) |  | 
**timestamp** | **datetime** |  | 
**resource** | [**ResourceEntity**](ResourceEntity.md) |  | 
**cascade_delete** | [**List[CascadeDeleteOption]**](CascadeDeleteOption.md) |  | [optional] 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 


## Example

```python
from waylay.services.resources.models.resource_metadata_event import (
    ResourceMetadataEvent,
)

resource_metadata_event = ResourceMetadataEvent(
    type=...,
    object_type=...,
    timestamp=...,
    resource=...,
    cascade_delete=...,
    old_values=...,
    message=...,
)

# Create from JSON
resource_metadata_event = ResourceMetadataEvent.from_json(
    '{ "type": ..., "objectType": ..., "timestamp": ..., "resource": ..., "cascadeDelete": ..., "oldValues": ..., "message": ... }'
)

# Export to dictionary
resource_metadata_event_dict = resource_metadata_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


