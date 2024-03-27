# SSEventStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudMetadataEventDataType**](CloudMetadataEventDataType.md) |  | 
**object_type** | [**ResourcetypeMetadataEventAllOfObjectType**](ResourcetypeMetadataEventAllOfObjectType.md) |  | 
**timestamp** | **datetime** |  | 
**resource** | [**ResourceEntity**](ResourceEntity.md) |  | 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 
**resourcetype** | [**ResourceTypeEntity**](ResourceTypeEntity.md) |  | 
**id** | **object** |  | 
**source** | [**CloudMetadataEventDataSource**](CloudMetadataEventDataSource.md) |  | 
**subject** | **object** |  | 
**data** | [**MetadataEvent**](MetadataEvent.md) |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from waylay.services.resources.models.ss_event_stream import SSEventStream

# TODO update the JSON string below
json = "{}"
# create an instance of SSEventStream from a JSON string
ss_event_stream_instance = SSEventStream.from_json(json)
# print the JSON string representation of the object
print SSEventStream.to_json()

# convert the object into a dict
ss_event_stream_dict = ss_event_stream_instance.to_dict()
# create an instance of SSEventStream from a dict
ss_event_stream_form_dict = ss_event_stream.from_dict(ss_event_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


