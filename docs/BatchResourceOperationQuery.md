# BatchResourceOperationQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[BatchResourceOperationQueryIdsInner]**](BatchResourceOperationQueryIdsInner.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_resource_operation_query import BatchResourceOperationQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResourceOperationQuery from a JSON string
batch_resource_operation_query_instance = BatchResourceOperationQuery.from_json(json)
# print the JSON string representation of the object
print BatchResourceOperationQuery.to_json()

# convert the object into a dict
batch_resource_operation_query_dict = batch_resource_operation_query_instance.to_dict()
# create an instance of BatchResourceOperationQuery from a dict
batch_resource_operation_query_form_dict = batch_resource_operation_query.from_dict(batch_resource_operation_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


