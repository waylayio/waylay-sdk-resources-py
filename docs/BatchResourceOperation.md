# BatchResourceOperation


**Source:** `waylay.services.resources.models.batch_resource_operation`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**BatchResourceDeleteOperation**](BatchResourceDeleteOperation.md) | -
[**BatchResourceTypeDeleteOperation**](BatchResourceTypeDeleteOperation.md) | -
[**BatchResourcePatchOperation**](BatchResourcePatchOperation.md) | -

## Example

```python
from waylay.services.resources.models.batch_resource_operation import (
    BatchResourceOperation,
)

# Use any of the accepted types (see table above)
my_batch_resource_operation: BatchResourceOperation = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


