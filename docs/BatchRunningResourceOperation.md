# BatchRunningResourceOperation


**Source:** `waylay.services.resources.models.batch_running_resource_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User subject id in the Waylay Accounts database | 
**queue_time** | **datetime** |  | 
**operation** | [**BatchRunningResourceOperationOperation**](BatchRunningResourceOperationOperation.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_running_resource_operation import (
    BatchRunningResourceOperation,
)

batch_running_resource_operation = BatchRunningResourceOperation(
    id=..., user=..., queue_time=..., operation=...
)

# Create from JSON
batch_running_resource_operation = BatchRunningResourceOperation.from_json(
    '{ "id": ..., "user": ..., "queueTime": ..., "operation": ... }'
)

# Export to dictionary
batch_running_resource_operation_dict = batch_running_resource_operation.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


