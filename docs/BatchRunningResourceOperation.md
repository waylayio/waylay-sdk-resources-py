# BatchRunningResourceOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User subject id in the Waylay Accounts database | 
**queue_time** | **datetime** |  | 
**operation** | [**BatchRunningResourceOperationOperation**](BatchRunningResourceOperationOperation.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_running_resource_operation import BatchRunningResourceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRunningResourceOperation from a JSON string
batch_running_resource_operation_instance = BatchRunningResourceOperation.from_json(json)
# print the JSON string representation of the object
print BatchRunningResourceOperation.to_json()

# convert the object into a dict
batch_running_resource_operation_dict = batch_running_resource_operation_instance.to_dict()
# create an instance of BatchRunningResourceOperation from a dict
batch_running_resource_operation_form_dict = batch_running_resource_operation.from_dict(batch_running_resource_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


