# ResourcetypeMetadataEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChangedEventType**](ChangedEventType.md) |  | 
**object_type** | [**ResourcetypeMetadataEventAllOfObjectType**](ResourcetypeMetadataEventAllOfObjectType.md) |  | 
**timestamp** | **datetime** |  | 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**resourcetype** | [**ResourceTypeEntity**](ResourceTypeEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.resourcetype_metadata_event import ResourcetypeMetadataEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcetypeMetadataEvent from a JSON string
resourcetype_metadata_event_instance = ResourcetypeMetadataEvent.from_json(json)
# print the JSON string representation of the object
print ResourcetypeMetadataEvent.to_json()

# convert the object into a dict
resourcetype_metadata_event_dict = resourcetype_metadata_event_instance.to_dict()
# create an instance of ResourcetypeMetadataEvent from a dict
resourcetype_metadata_event_form_dict = resourcetype_metadata_event.from_dict(resourcetype_metadata_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


