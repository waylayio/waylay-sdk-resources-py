# BatchResourceDeleteOperation


**Source:** `waylay.services.resources.models.batch_resource_delete_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchResourceDeleteOperationEntity**](BatchResourceDeleteOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**query** | [**BatchResourceDeleteOperationQuery**](BatchResourceDeleteOperationQuery.md) |  | 
**action_parameters** | [**BatchResourceDeleteOperationActionParameters**](BatchResourceDeleteOperationActionParameters.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation import (
    BatchResourceDeleteOperation,
)

batch_resource_delete_operation = BatchResourceDeleteOperation(
    entity=..., action=..., query=..., action_parameters=...
)

# Create from JSON
batch_resource_delete_operation = BatchResourceDeleteOperation.from_json(
    '{ "entity": ..., "action": ..., "query": ..., "actionParameters": ... }'
)

# Export to dictionary
batch_resource_delete_operation_dict = batch_resource_delete_operation.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


