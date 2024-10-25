# BatchResourceDeleteOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchResourceDeleteOperationEntity**](BatchResourceDeleteOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**query** | [**BatchResourceDeleteOperationQuery**](BatchResourceDeleteOperationQuery.md) |  | 
**action_parameters** | [**BatchResourceDeleteOperationActionParameters**](BatchResourceDeleteOperationActionParameters.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation import BatchResourceDeleteOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResourceDeleteOperation from a JSON string
batch_resource_delete_operation_instance = BatchResourceDeleteOperation.from_json(json)
# print the JSON string representation of the object
print BatchResourceDeleteOperation.to_json()

# convert the object into a dict
batch_resource_delete_operation_dict = batch_resource_delete_operation_instance.to_dict()
# create an instance of BatchResourceDeleteOperation from a dict
batch_resource_delete_operation_form_dict = batch_resource_delete_operation.from_dict(batch_resource_delete_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


