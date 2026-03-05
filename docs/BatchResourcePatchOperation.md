# BatchResourcePatchOperation


**Source:** `waylay.services.resources.models.batch_resource_patch_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchResourcePatchOperationEntity**](BatchResourcePatchOperationEntity.md) |  | 
**action** | [**BatchResourcePatchOperationAction**](BatchResourcePatchOperationAction.md) |  | 
**query** | [**BatchResourcePatchOperationQuery**](BatchResourcePatchOperationQuery.md) |  | 
**action_parameters** | [**BatchResourcePatchOperationActionParameters**](BatchResourcePatchOperationActionParameters.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.batch_resource_patch_operation import (
    BatchResourcePatchOperation,
)

batch_resource_patch_operation = BatchResourcePatchOperation(
    entity=..., action=..., query=..., action_parameters=...
)

# Create from JSON
batch_resource_patch_operation = BatchResourcePatchOperation.from_json(
    '{ "entity": ..., "action": ..., "query": ..., "actionParameters": ... }'
)

# Export to dictionary
batch_resource_patch_operation_dict = batch_resource_patch_operation.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


