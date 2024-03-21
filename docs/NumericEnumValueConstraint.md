# NumericEnumValueConstraint

Specifies that a value must be one of the given numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**enum_type** | **str** |  | 
**items** | **List[float]** |  | 

## Example

```python
from waylay.services.resources.models.numeric_enum_value_constraint import NumericEnumValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of NumericEnumValueConstraint from a JSON string
numeric_enum_value_constraint_instance = NumericEnumValueConstraint.from_json(json)
# print the JSON string representation of the object
print NumericEnumValueConstraint.to_json()

# convert the object into a dict
numeric_enum_value_constraint_dict = numeric_enum_value_constraint_instance.to_dict()
# create an instance of NumericEnumValueConstraint from a dict
numeric_enum_value_constraint_form_dict = numeric_enum_value_constraint.from_dict(numeric_enum_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


