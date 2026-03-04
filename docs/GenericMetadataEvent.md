# GenericMetadataEvent


**Source:** `waylay.services.resources.models.generic_metadata_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**object_type** | **str** |  | 
**timestamp** | **datetime** |  | 


## Example

```python
from waylay.services.resources.models.generic_metadata_event import GenericMetadataEvent

generic_metadata_event = GenericMetadataEvent(type=..., object_type=..., timestamp=...)

# Create from JSON
generic_metadata_event = GenericMetadataEvent.from_json(
    '{ "type": ..., "objectType": ..., "timestamp": ... }'
)

# Export to dictionary
generic_metadata_event_dict = generic_metadata_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


