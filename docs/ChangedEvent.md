# ChangedEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChangedEventType**](ChangedEventType.md) |  | [optional] 
**old_values** | **object** | old values of all attributes that have changed | [optional] 

## Example

```python
from waylay.services.resources.models.changed_event import ChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedEvent from a JSON string
changed_event_instance = ChangedEvent.from_json(json)
# print the JSON string representation of the object
print ChangedEvent.to_json()

# convert the object into a dict
changed_event_dict = changed_event_instance.to_dict()
# create an instance of ChangedEvent from a dict
changed_event_form_dict = changed_event.from_dict(changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


