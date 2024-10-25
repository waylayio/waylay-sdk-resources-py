# BatchResourceDeleteOperationActionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascade** | [**List[CascadeDeleteValuesInner]**](CascadeDeleteValuesInner.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation_action_parameters import BatchResourceDeleteOperationActionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResourceDeleteOperationActionParameters from a JSON string
batch_resource_delete_operation_action_parameters_instance = BatchResourceDeleteOperationActionParameters.from_json(json)
# print the JSON string representation of the object
print BatchResourceDeleteOperationActionParameters.to_json()

# convert the object into a dict
batch_resource_delete_operation_action_parameters_dict = batch_resource_delete_operation_action_parameters_instance.to_dict()
# create an instance of BatchResourceDeleteOperationActionParameters from a dict
batch_resource_delete_operation_action_parameters_form_dict = batch_resource_delete_operation_action_parameters.from_dict(batch_resource_delete_operation_action_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


