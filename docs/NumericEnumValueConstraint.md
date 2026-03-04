# NumericEnumValueConstraint

Specifies that a value must be one of the given numbers.

**Source:** `waylay.services.resources.models.numeric_enum_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NumericEnumValueConstraintType**](NumericEnumValueConstraintType.md) |  | 
**enum_type** | [**NumericValueConstraintType**](NumericValueConstraintType.md) |  | 
**items** | **List[float]** |  | 


## Example

```python
from waylay.services.resources.models.numeric_enum_value_constraint import (
    NumericEnumValueConstraint,
)

numeric_enum_value_constraint = NumericEnumValueConstraint(
    type=..., enum_type=..., items=...
)

# Create from JSON
numeric_enum_value_constraint = NumericEnumValueConstraint.from_json(
    '{ "type": ..., "enumType": ..., "items": ... }'
)

# Export to dictionary
numeric_enum_value_constraint_dict = numeric_enum_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


