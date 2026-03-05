# BatchResourceDeleteOperationQuery


**Source:** `waylay.services.resources.models.batch_resource_delete_operation_query`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[ResourceId]**](ResourceId.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation_query import (
    BatchResourceDeleteOperationQuery,
)

batch_resource_delete_operation_query = BatchResourceDeleteOperationQuery(ids=...)

# Create from JSON
batch_resource_delete_operation_query = BatchResourceDeleteOperationQuery.from_json(
    '{ "ids": ... }'
)

# Export to dictionary
batch_resource_delete_operation_query_dict = (
    batch_resource_delete_operation_query.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


