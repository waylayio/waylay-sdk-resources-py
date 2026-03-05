# StringEnumValueConstraint

Specifies that a value must be one of the given strings.

**Source:** `waylay.services.resources.models.string_enum_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NumericEnumValueConstraintType**](NumericEnumValueConstraintType.md) |  | 
**enum_type** | [**StringValueConstraintType**](StringValueConstraintType.md) |  | 
**items** | **List[str]** |  | 


## Example

```python
from waylay.services.resources.models.string_enum_value_constraint import (
    StringEnumValueConstraint,
)

string_enum_value_constraint = StringEnumValueConstraint(
    type=..., enum_type=..., items=...
)

# Create from JSON
string_enum_value_constraint = StringEnumValueConstraint.from_json(
    '{ "type": ..., "enumType": ..., "items": ... }'
)

# Export to dictionary
string_enum_value_constraint_dict = string_enum_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


