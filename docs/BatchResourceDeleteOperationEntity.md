# BatchResourceDeleteOperationEntity

Type of entities to remove

**Source:** `waylay.services.resources.models.batch_resource_delete_operation_entity`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**RESOURCE** | `'resource'` |

## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation_entity import (
    BatchResourceDeleteOperationEntity,
)

# Use enum by value
my_batch_resource_delete_operation_entity = BatchResourceDeleteOperationEntity.RESOURCE
print(my_batch_resource_delete_operation_entity)  # Output: 'resource'

# Or by string value
my_batch_resource_delete_operation_entity = BatchResourceDeleteOperationEntity(
    "resource"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


