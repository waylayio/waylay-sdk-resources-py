# BatchOperationResult


**Source:** `waylay.services.resources.models.batch_operation_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User subject id in the Waylay Accounts database | 
**queue_time** | **datetime** |  | 
**operation** | [**BatchRunningResourceOperationOperation**](BatchRunningResourceOperationOperation.md) |  | 
**finished_time** | **datetime** |  | 
**results** | [**BatchOperationResults**](BatchOperationResults.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_operation_result import BatchOperationResult

batch_operation_result = BatchOperationResult(
    id=..., user=..., queue_time=..., operation=..., finished_time=..., results=...
)

# Create from JSON
batch_operation_result = BatchOperationResult.from_json(
    '{ "id": ..., "user": ..., "queueTime": ..., "operation": ..., "finishedTime": ..., "results": ... }'
)

# Export to dictionary
batch_operation_result_dict = batch_operation_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


