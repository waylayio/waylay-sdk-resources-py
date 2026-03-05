# BatchResourcePatchOperationQuery


**Source:** `waylay.services.resources.models.batch_resource_patch_operation_query`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[PatchResourceEntity]**](PatchResourceEntity.md) | Array of resource objects to patch or insert | 


## Example

```python
from waylay.services.resources.models.batch_resource_patch_operation_query import (
    BatchResourcePatchOperationQuery,
)

batch_resource_patch_operation_query = BatchResourcePatchOperationQuery(resources=...)

# Create from JSON
batch_resource_patch_operation_query = BatchResourcePatchOperationQuery.from_json(
    '{ "resources": ... }'
)

# Export to dictionary
batch_resource_patch_operation_query_dict = (
    batch_resource_patch_operation_query.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


