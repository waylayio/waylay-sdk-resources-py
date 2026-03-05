# BatchResourceDeleteOperationActionParameters


**Source:** `waylay.services.resources.models.batch_resource_delete_operation_action_parameters`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascade** | [**List[CascadeDeleteOption]**](CascadeDeleteOption.md) |  | 


## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation_action_parameters import (
    BatchResourceDeleteOperationActionParameters,
)

batch_resource_delete_operation_action_parameters = (
    BatchResourceDeleteOperationActionParameters(cascade=...)
)

# Create from JSON
batch_resource_delete_operation_action_parameters = (
    BatchResourceDeleteOperationActionParameters.from_json('{ "cascade": ... }')
)

# Export to dictionary
batch_resource_delete_operation_action_parameters_dict = (
    batch_resource_delete_operation_action_parameters.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


