# BatchResourceDeleteOperationQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[ResourceId]**](ResourceId.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_resource_delete_operation_query import BatchResourceDeleteOperationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResourceDeleteOperationQuery from a JSON string
batch_resource_delete_operation_query_instance = BatchResourceDeleteOperationQuery.from_json(json)
# print the JSON string representation of the object
print BatchResourceDeleteOperationQuery.to_json()

# convert the object into a dict
batch_resource_delete_operation_query_dict = batch_resource_delete_operation_query_instance.to_dict()
# create an instance of BatchResourceDeleteOperationQuery from a dict
batch_resource_delete_operation_query_form_dict = batch_resource_delete_operation_query.from_dict(batch_resource_delete_operation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


