# DeletedResourceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | [optional] 
**cascade_delete** | [**List[CascadeDeleteValuesInner]**](CascadeDeleteValuesInner.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.deleted_resource_event import DeletedResourceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedResourceEvent from a JSON string
deleted_resource_event_instance = DeletedResourceEvent.from_json(json)
# print the JSON string representation of the object
print DeletedResourceEvent.to_json()

# convert the object into a dict
deleted_resource_event_dict = deleted_resource_event_instance.to_dict()
# create an instance of DeletedResourceEvent from a dict
deleted_resource_event_form_dict = deleted_resource_event.from_dict(deleted_resource_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


