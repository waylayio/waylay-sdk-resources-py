# BatchOperationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User subject id in the Waylay Accounts database | 
**queue_time** | **datetime** |  | 
**operation** | [**BatchRunningResourceOperationOperation**](BatchRunningResourceOperationOperation.md) |  | 
**finished_time** | **datetime** |  | 
**results** | [**OperationResultObjectResults**](OperationResultObjectResults.md) |  | 

## Example

```python
from waylay.services.resources.models.batch_operation_status_response import BatchOperationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationStatusResponse from a JSON string
batch_operation_status_response_instance = BatchOperationStatusResponse.from_json(json)
# print the JSON string representation of the object
print BatchOperationStatusResponse.to_json()

# convert the object into a dict
batch_operation_status_response_dict = batch_operation_status_response_instance.to_dict()
# create an instance of BatchOperationStatusResponse from a dict
batch_operation_status_response_form_dict = batch_operation_status_response.from_dict(batch_operation_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


