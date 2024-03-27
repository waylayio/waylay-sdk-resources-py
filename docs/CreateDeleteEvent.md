# CreateDeleteEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CreateDeleteEventType**](CreateDeleteEventType.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.create_delete_event import CreateDeleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeleteEvent from a JSON string
create_delete_event_instance = CreateDeleteEvent.from_json(json)
# print the JSON string representation of the object
print CreateDeleteEvent.to_json()

# convert the object into a dict
create_delete_event_dict = create_delete_event_instance.to_dict()
# create an instance of CreateDeleteEvent from a dict
create_delete_event_form_dict = create_delete_event.from_dict(create_delete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


