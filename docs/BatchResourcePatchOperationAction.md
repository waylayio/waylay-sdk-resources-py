# BatchResourcePatchOperationAction


**Source:** `waylay.services.resources.models.batch_resource_patch_operation_action`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PATCHORINSERT** | `'patchOrInsert'` |

## Example

```python
from waylay.services.resources.models.batch_resource_patch_operation_action import (
    BatchResourcePatchOperationAction,
)

# Use enum by value
my_batch_resource_patch_operation_action = (
    BatchResourcePatchOperationAction.PATCHORINSERT
)
print(my_batch_resource_patch_operation_action)  # Output: 'patchOrInsert'

# Or by string value
my_batch_resource_patch_operation_action = BatchResourcePatchOperationAction(
    "patchOrInsert"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


