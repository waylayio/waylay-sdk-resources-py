# StringValueConstraint

Specifies that a value must be a string.

**Source:** `waylay.services.resources.models.string_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StringValueConstraintType**](StringValueConstraintType.md) |  | [optional] 
**min_length** | **int** | Minimum length a value must have | [optional] 
**max_length** | **int** | Maximum length a value can have | [optional] 


## Example

```python
from waylay.services.resources.models.string_value_constraint import (
    StringValueConstraint,
)

string_value_constraint = StringValueConstraint(
    type=..., min_length=..., max_length=...
)

# Create from JSON
string_value_constraint = StringValueConstraint.from_json(
    '{ "type": ..., "minLength": ..., "maxLength": ... }'
)

# Export to dictionary
string_value_constraint_dict = string_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


