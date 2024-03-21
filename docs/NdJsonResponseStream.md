# NdJsonResponseStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**object_type** | **str** |  | 
**timestamp** | **datetime** |  | 
**resource** | [**ResourceEntity**](ResourceEntity.md) |  | 
**old_values** | **object** | old values of all attributes that have changed | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 
**resourcetype** | [**ResourceTypeEntity**](ResourceTypeEntity.md) |  | 
**id** | **object** |  | 
**source** | **str** |  | 
**subject** | **object** |  | 
**data** | [**MetadataEvent**](MetadataEvent.md) |  | [optional] 
**time** | **datetime** |  | 

## Example

```python
from waylay.services.resources.models.nd_json_response_stream import NdJsonResponseStream

# TODO update the JSON string below
json = "{}"
# create an instance of NdJsonResponseStream from a JSON string
nd_json_response_stream_instance = NdJsonResponseStream.from_json(json)
# print the JSON string representation of the object
print NdJsonResponseStream.to_json()

# convert the object into a dict
nd_json_response_stream_dict = nd_json_response_stream_instance.to_dict()
# create an instance of NdJsonResponseStream from a dict
nd_json_response_stream_form_dict = nd_json_response_stream.from_dict(nd_json_response_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


