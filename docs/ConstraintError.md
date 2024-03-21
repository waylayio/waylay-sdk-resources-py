# ConstraintError

Validation Error report of a Resource Constraint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | User error message | 
**error_path** | **str** | Attribute path | 
**resources** | [**List[ResourceId]**](ResourceId.md) | Ids of the _Resources_ that fail the constraint | 

## Example

```python
from waylay.services.resources.models.constraint_error import ConstraintError

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintError from a JSON string
constraint_error_instance = ConstraintError.from_json(json)
# print the JSON string representation of the object
print ConstraintError.to_json()

# convert the object into a dict
constraint_error_dict = constraint_error_instance.to_dict()
# create an instance of ConstraintError from a dict
constraint_error_form_dict = constraint_error.from_dict(constraint_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


