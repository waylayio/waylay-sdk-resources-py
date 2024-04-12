# BooleanValueConstraint

Specifies that the value must be a boolean

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BooleanValueConstraintType**](BooleanValueConstraintType.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.boolean_value_constraint import BooleanValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanValueConstraint from a JSON string
boolean_value_constraint_instance = BooleanValueConstraint.from_json(json)
# print the JSON string representation of the object
print BooleanValueConstraint.to_json()

# convert the object into a dict
boolean_value_constraint_dict = boolean_value_constraint_instance.to_dict()
# create an instance of BooleanValueConstraint from a dict
boolean_value_constraint_form_dict = boolean_value_constraint.from_dict(boolean_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


