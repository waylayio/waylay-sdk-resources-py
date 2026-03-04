# ResourcetypeMetadataEvent


**Source:** `waylay.services.resources.models.resourcetype_metadata_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChangedEventType**](ChangedEventType.md) |  | 
**object_type** | [**ResourcetypeMetadataEventResourcetype**](ResourcetypeMetadataEventResourcetype.md) |  | 
**timestamp** | **datetime** |  | 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**resourcetype** | [**ResourceTypeEntity**](ResourceTypeEntity.md) |  | 


## Example

```python
from waylay.services.resources.models.resourcetype_metadata_event import (
    ResourcetypeMetadataEvent,
)

resourcetype_metadata_event = ResourcetypeMetadataEvent(
    type=..., object_type=..., timestamp=..., old_values=..., resourcetype=...
)

# Create from JSON
resourcetype_metadata_event = ResourcetypeMetadataEvent.from_json(
    '{ "type": ..., "objectType": ..., "timestamp": ..., "oldValues": ..., "resourcetype": ... }'
)

# Export to dictionary
resourcetype_metadata_event_dict = resourcetype_metadata_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


