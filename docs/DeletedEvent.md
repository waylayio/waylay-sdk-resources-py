# DeletedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.deleted_event import DeletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedEvent from a JSON string
deleted_event_instance = DeletedEvent.from_json(json)
# print the JSON string representation of the object
print DeletedEvent.to_json()

# convert the object into a dict
deleted_event_dict = deleted_event_instance.to_dict()
# create an instance of DeletedEvent from a dict
deleted_event_form_dict = deleted_event.from_dict(deleted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


