# CascadeDeleteOption


**Source:** `waylay.services.resources.models.cascade_delete_option`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ALARMS** | `'alarms'` |
**MEASUREMENTS** | `'measurements'` |
**TASKS** | `'tasks'` |

## Example

```python
from waylay.services.resources.models.cascade_delete_option import CascadeDeleteOption

# Use enum by value
my_cascade_delete_option = CascadeDeleteOption.ALARMS
print(my_cascade_delete_option)  # Output: 'alarms'

# Or by string value
my_cascade_delete_option = CascadeDeleteOption("alarms")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


