# ResourceMetadataEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DiscoveredEventType**](DiscoveredEventType.md) |  | 
**object_type** | [**ResourceMetadataEventAllOfObjectType**](ResourceMetadataEventAllOfObjectType.md) |  | 
**timestamp** | **datetime** |  | 
**resource** | [**ResourceEntity**](ResourceEntity.md) |  | 
**cascade_delete** | [**List[CascadeDeleteValuesInner]**](CascadeDeleteValuesInner.md) |  | [optional] 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 

## Example

```python
from waylay.services.resources.models.resource_metadata_event import ResourceMetadataEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMetadataEvent from a JSON string
resource_metadata_event_instance = ResourceMetadataEvent.from_json(json)
# print the JSON string representation of the object
print ResourceMetadataEvent.to_json()

# convert the object into a dict
resource_metadata_event_dict = resource_metadata_event_instance.to_dict()
# create an instance of ResourceMetadataEvent from a dict
resource_metadata_event_form_dict = resource_metadata_event.from_dict(resource_metadata_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


