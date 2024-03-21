# StringEnumValueConstraint

Specifies that a value must be one of the given strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**enum_type** | **str** |  | 
**items** | **List[str]** |  | 

## Example

```python
from waylay.services.resources.models.string_enum_value_constraint import StringEnumValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of StringEnumValueConstraint from a JSON string
string_enum_value_constraint_instance = StringEnumValueConstraint.from_json(json)
# print the JSON string representation of the object
print StringEnumValueConstraint.to_json()

# convert the object into a dict
string_enum_value_constraint_dict = string_enum_value_constraint_instance.to_dict()
# create an instance of StringEnumValueConstraint from a dict
string_enum_value_constraint_form_dict = string_enum_value_constraint.from_dict(string_enum_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


