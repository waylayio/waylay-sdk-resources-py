# GetStreamEventFormatParameter


**Source:** `waylay.services.resources.models.get_stream_event_format_parameter`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON** | `'application/cloudevents+json'` |

## Example

```python
from waylay.services.resources.models.get_stream_event_format_parameter import (
    GetStreamEventFormatParameter,
)

# Use enum by value
my_get_stream_event_format_parameter = (
    GetStreamEventFormatParameter.APPLICATION_SLASH_CLOUDEVENTS_PLUS_JSON
)
print(my_get_stream_event_format_parameter)  # Output: 'application/cloudevents+json'

# Or by string value
my_get_stream_event_format_parameter = GetStreamEventFormatParameter(
    "application/cloudevents+json"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


