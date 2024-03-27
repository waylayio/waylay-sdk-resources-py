# StringValueConstraint

Specifies that a value must be a string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StringValueConstraintType**](StringValueConstraintType.md) |  | [optional] 
**min_length** | **int** | Minimum length a value must have | [optional] 
**max_length** | **int** | Maximum length a value can have | [optional] 

## Example

```python
from waylay.services.resources.models.string_value_constraint import StringValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of StringValueConstraint from a JSON string
string_value_constraint_instance = StringValueConstraint.from_json(json)
# print the JSON string representation of the object
print StringValueConstraint.to_json()

# convert the object into a dict
string_value_constraint_dict = string_value_constraint_instance.to_dict()
# create an instance of StringValueConstraint from a dict
string_value_constraint_form_dict = string_value_constraint.from_dict(string_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


