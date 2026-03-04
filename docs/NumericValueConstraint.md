# NumericValueConstraint

Specifies that a value must be a number.

**Source:** `waylay.services.resources.models.numeric_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NumericValueConstraintType**](NumericValueConstraintType.md) |  | [optional] 
**minimum** | **float** | Specifies the minimum value the attribute can have | [optional] 
**maximum** | **float** | Specifies the maximum value the attribute can have | [optional] 


## Example

```python
from waylay.services.resources.models.numeric_value_constraint import (
    NumericValueConstraint,
)

numeric_value_constraint = NumericValueConstraint(type=..., minimum=..., maximum=...)

# Create from JSON
numeric_value_constraint = NumericValueConstraint.from_json(
    '{ "type": ..., "minimum": ..., "maximum": ... }'
)

# Export to dictionary
numeric_value_constraint_dict = numeric_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


