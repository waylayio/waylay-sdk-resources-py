# BatchRunningResourceOperationOperation

Queued operation summary

**Source:** `waylay.services.resources.models.batch_running_resource_operation_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchRunningResourceOperationOperationEntity**](BatchRunningResourceOperationOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**description** | **str** |  | 


## Example

```python
from waylay.services.resources.models.batch_running_resource_operation_operation import (
    BatchRunningResourceOperationOperation,
)

batch_running_resource_operation_operation = BatchRunningResourceOperationOperation(
    entity=..., action=..., description=...
)

# Create from JSON
batch_running_resource_operation_operation = (
    BatchRunningResourceOperationOperation.from_json(
        '{ "entity": ..., "action": ..., "description": ... }'
    )
)

# Export to dictionary
batch_running_resource_operation_operation_dict = (
    batch_running_resource_operation_operation.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


