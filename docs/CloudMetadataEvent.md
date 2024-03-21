# CloudMetadataEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**source** | **str** |  | 
**subject** | **object** |  | 
**type** | **str** |  | 
**data** | [**MetadataEvent**](MetadataEvent.md) |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from waylay.services.resources.models.cloud_metadata_event import CloudMetadataEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CloudMetadataEvent from a JSON string
cloud_metadata_event_instance = CloudMetadataEvent.from_json(json)
# print the JSON string representation of the object
print CloudMetadataEvent.to_json()

# convert the object into a dict
cloud_metadata_event_dict = cloud_metadata_event_instance.to_dict()
# create an instance of CloudMetadataEvent from a dict
cloud_metadata_event_form_dict = cloud_metadata_event.from_dict(cloud_metadata_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


