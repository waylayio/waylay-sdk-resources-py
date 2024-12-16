# BatchRunningResourceOperationOperation

Queued operation summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchRunningResourceOperationOperationEntity**](BatchRunningResourceOperationOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**description** | **str** |  | 

## Example

```python
from waylay.services.resources.models.batch_running_resource_operation_operation import BatchRunningResourceOperationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRunningResourceOperationOperation from a JSON string
batch_running_resource_operation_operation_instance = BatchRunningResourceOperationOperation.from_json(json)
# print the JSON string representation of the object
print BatchRunningResourceOperationOperation.to_json()

# convert the object into a dict
batch_running_resource_operation_operation_dict = batch_running_resource_operation_operation_instance.to_dict()
# create an instance of BatchRunningResourceOperationOperation from a dict
batch_running_resource_operation_operation_form_dict = batch_running_resource_operation_operation.from_dict(batch_running_resource_operation_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


