# TaskConfigurationType


**Source:** `waylay.services.resources.models.task_configuration_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PERIODIC** | `'periodic'` |
**ONETIME** | `'onetime'` |
**SCHEDULED** | `'scheduled'` |
**REACTIVE** | `'reactive'` |

## Example

```python
from waylay.services.resources.models.task_configuration_type import (
    TaskConfigurationType,
)

# Use enum by value
my_task_configuration_type = TaskConfigurationType.PERIODIC
print(my_task_configuration_type)  # Output: 'periodic'

# Or by string value
my_task_configuration_type = TaskConfigurationType("periodic")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


