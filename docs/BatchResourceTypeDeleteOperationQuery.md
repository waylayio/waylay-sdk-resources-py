# BatchResourceTypeDeleteOperationQuery


**Source:** `waylay.services.resources.models.batch_resource_type_delete_operation_query`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[ResourceTypeId]**](ResourceTypeId.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_resource_type_delete_operation_query import (
    BatchResourceTypeDeleteOperationQuery,
)

batch_resource_type_delete_operation_query = BatchResourceTypeDeleteOperationQuery(
    ids=...
)

# Create from JSON
batch_resource_type_delete_operation_query = (
    BatchResourceTypeDeleteOperationQuery.from_json('{ "ids": ... }')
)

# Export to dictionary
batch_resource_type_delete_operation_query_dict = (
    batch_resource_type_delete_operation_query.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


