# BatchResourcePatchOperationActionParameters


**Source:** `waylay.services.resources.models.batch_resource_patch_operation_action_parameters`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_protected** | **bool** | Whether to allow updating protected entities | [optional] [default to False]


## Example

```python
from waylay.services.resources.models.batch_resource_patch_operation_action_parameters import (
    BatchResourcePatchOperationActionParameters,
)

batch_resource_patch_operation_action_parameters = (
    BatchResourcePatchOperationActionParameters(update_protected=...)
)

# Create from JSON
batch_resource_patch_operation_action_parameters = (
    BatchResourcePatchOperationActionParameters.from_json('{ "updateProtected": ... }')
)

# Export to dictionary
batch_resource_patch_operation_action_parameters_dict = (
    batch_resource_patch_operation_action_parameters.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


