# BooleanValueConstraint

Specifies that the value must be a boolean

**Source:** `waylay.services.resources.models.boolean_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BooleanValueConstraintType**](BooleanValueConstraintType.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.boolean_value_constraint import (
    BooleanValueConstraint,
)

boolean_value_constraint = BooleanValueConstraint(type=...)

# Create from JSON
boolean_value_constraint = BooleanValueConstraint.from_json('{ "type": ... }')

# Export to dictionary
boolean_value_constraint_dict = boolean_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


