# ArrayValueConstraint

Specifies that a value must be an array and what type of elements it contains

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ArrayValueConstraintType**](ArrayValueConstraintType.md) |  | 
**element_type** | [**GenericModel**](GenericModel.md) |  | 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**unique_values** | **bool** | If true, all values in the array must be unique. | [optional] [default to False]
**contains** | [**List[ArrayMustContainInner]**](ArrayMustContainInner.md) | Only supported if the &#x60;elementType&#x60; is &#x60;boolean&#x60;, &#x60;numeric&#x60; or &#x60;string&#x60;. Specifies values the array attribute must contain. | [optional] 

## Example

```python
from waylay.services.resources.models.array_value_constraint import ArrayValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayValueConstraint from a JSON string
array_value_constraint_instance = ArrayValueConstraint.from_json(json)
# print the JSON string representation of the object
print ArrayValueConstraint.to_json()

# convert the object into a dict
array_value_constraint_dict = array_value_constraint_instance.to_dict()
# create an instance of ArrayValueConstraint from a dict
array_value_constraint_form_dict = array_value_constraint.from_dict(array_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


