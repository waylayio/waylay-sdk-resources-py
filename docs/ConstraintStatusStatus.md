# ConstraintStatusStatus


**Source:** `waylay.services.resources.models.constraint_status_status`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**APPLYING** | `'applying'` |
**INEFFECT** | `'ineffect'` |
**FAILED** | `'failed'` |

## Example

```python
from waylay.services.resources.models.constraint_status_status import (
    ConstraintStatusStatus,
)

# Use enum by value
my_constraint_status_status = ConstraintStatusStatus.APPLYING
print(my_constraint_status_status)  # Output: 'applying'

# Or by string value
my_constraint_status_status = ConstraintStatusStatus("applying")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


