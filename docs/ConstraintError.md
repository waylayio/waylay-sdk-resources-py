# ConstraintError

Validation Error report of a Resource Constraint

**Source:** `waylay.services.resources.models.constraint_error`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | User error message | 
**error_path** | **str** | Attribute path | 
**resources** | [**List[ResourceId]**](ResourceId.md) | Ids of the _Resources_ that fail the constraint | 


## Example

```python
from waylay.services.resources.models.constraint_error import ConstraintError

constraint_error = ConstraintError(error=..., error_path=..., resources=...)

# Create from JSON
constraint_error = ConstraintError.from_json(
    '{ "error": ..., "errorPath": ..., "resources": ... }'
)

# Export to dictionary
constraint_error_dict = constraint_error.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


