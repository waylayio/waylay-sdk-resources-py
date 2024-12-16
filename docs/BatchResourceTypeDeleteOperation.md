# BatchResourceTypeDeleteOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchResourceTypeDeleteOperationEntity**](BatchResourceTypeDeleteOperationEntity.md) |  | 
**action** | [**BatchResourceDeleteOperationAction**](BatchResourceDeleteOperationAction.md) |  | 
**query** | [**BatchResourceTypeDeleteOperationQuery**](BatchResourceTypeDeleteOperationQuery.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_resource_type_delete_operation import BatchResourceTypeDeleteOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResourceTypeDeleteOperation from a JSON string
batch_resource_type_delete_operation_instance = BatchResourceTypeDeleteOperation.from_json(json)
# print the JSON string representation of the object
print BatchResourceTypeDeleteOperation.to_json()

# convert the object into a dict
batch_resource_type_delete_operation_dict = batch_resource_type_delete_operation_instance.to_dict()
# create an instance of BatchResourceTypeDeleteOperation from a dict
batch_resource_type_delete_operation_form_dict = batch_resource_type_delete_operation.from_dict(batch_resource_type_delete_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


