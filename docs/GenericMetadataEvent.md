# GenericMetadataEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**object_type** | **str** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from waylay.services.resources.models.generic_metadata_event import GenericMetadataEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GenericMetadataEvent from a JSON string
generic_metadata_event_instance = GenericMetadataEvent.from_json(json)
# print the JSON string representation of the object
print GenericMetadataEvent.to_json()

# convert the object into a dict
generic_metadata_event_dict = generic_metadata_event_instance.to_dict()
# create an instance of GenericMetadataEvent from a dict
generic_metadata_event_form_dict = generic_metadata_event.from_dict(generic_metadata_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


