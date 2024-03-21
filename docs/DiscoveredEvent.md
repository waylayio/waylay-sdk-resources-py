# DiscoveredEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**message** | **object** | The broker message that triggered the discovery | [optional] 

## Example

```python
from waylay.services.resources.models.discovered_event import DiscoveredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredEvent from a JSON string
discovered_event_instance = DiscoveredEvent.from_json(json)
# print the JSON string representation of the object
print DiscoveredEvent.to_json()

# convert the object into a dict
discovered_event_dict = discovered_event_instance.to_dict()
# create an instance of DiscoveredEvent from a dict
discovered_event_form_dict = discovered_event.from_dict(discovered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


