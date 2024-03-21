# NumericValueConstraint

Specifies that a value must be a number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**minimum** | **float** | Specifies the minimum value the attribute can have | [optional] 
**maximum** | **float** | Specifies the maximum value the attribute can have | [optional] 

## Example

```python
from waylay.services.resources.models.numeric_value_constraint import NumericValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of NumericValueConstraint from a JSON string
numeric_value_constraint_instance = NumericValueConstraint.from_json(json)
# print the JSON string representation of the object
print NumericValueConstraint.to_json()

# convert the object into a dict
numeric_value_constraint_dict = numeric_value_constraint_instance.to_dict()
# create an instance of NumericValueConstraint from a dict
numeric_value_constraint_form_dict = numeric_value_constraint.from_dict(numeric_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


