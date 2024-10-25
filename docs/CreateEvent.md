# CreateEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CreateEventType**](CreateEventType.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.create_event import CreateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEvent from a JSON string
create_event_instance = CreateEvent.from_json(json)
# print the JSON string representation of the object
print CreateEvent.to_json()

# convert the object into a dict
create_event_dict = create_event_instance.to_dict()
# create an instance of CreateEvent from a dict
create_event_form_dict = create_event.from_dict(create_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


