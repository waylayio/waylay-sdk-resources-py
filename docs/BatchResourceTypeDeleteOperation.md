# BatchResourceTypeDeleteOperation


**Source:** `waylay.services.resources.models.batch_resource_type_delete_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchResourceTypeDeleteOperationEntity**](BatchResourceTypeDeleteOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**query** | [**BatchResourceTypeDeleteOperationQuery**](BatchResourceTypeDeleteOperationQuery.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_resource_type_delete_operation import (
    BatchResourceTypeDeleteOperation,
)

batch_resource_type_delete_operation = BatchResourceTypeDeleteOperation(
    entity=..., action=..., query=...
)

# Create from JSON
batch_resource_type_delete_operation = BatchResourceTypeDeleteOperation.from_json(
    '{ "entity": ..., "action": ..., "query": ... }'
)

# Export to dictionary
batch_resource_type_delete_operation_dict = (
    batch_resource_type_delete_operation.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


