# MetadataEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChangedEventType**](ChangedEventType.md) |  | 
**object_type** | [**ResourcetypeMetadataEventAllOfObjectType**](ResourcetypeMetadataEventAllOfObjectType.md) |  | 
**timestamp** | **datetime** |  | 
**resource** | [**ResourceEntity**](ResourceEntity.md) |  | 
**cascade_delete** | [**List[CascadeDeleteValuesInner]**](CascadeDeleteValuesInner.md) |  | [optional] 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 
**resourcetype** | [**ResourceTypeEntity**](ResourceTypeEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.metadata_event import MetadataEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataEvent from a JSON string
metadata_event_instance = MetadataEvent.from_json(json)
# print the JSON string representation of the object
print MetadataEvent.to_json()

# convert the object into a dict
metadata_event_dict = metadata_event_instance.to_dict()
# create an instance of MetadataEvent from a dict
metadata_event_form_dict = metadata_event.from_dict(metadata_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


