# ValueConstraint

Constraint on the value of _Resource_ attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the attribute | 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**minimum** | **float** | Specifies the minimum value the attribute can have | [optional] 
**maximum** | **float** | Specifies the maximum value the attribute can have | [optional] 
**enum_type** | [**NumericValueConstraintType**](NumericValueConstraintType.md) |  | 
**items** | **List[float]** |  | 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes descriptions | 
**resource_types** | [**List[ResourceTypeId]**](ResourceTypeId.md) | The possible _Resource Types_ for the referenced _Resource_. | [optional] 
**exists** | **bool** | Flag to indicate if the referenced _Resource_ must exist | [optional] [default to False]
**element_type** | [**ValueConstraint**](ValueConstraint.md) |  | 
**unique_values** | **bool** | If true, all values in the array must be unique. | [optional] [default to False]
**contains** | [**List[ArrayMustContainInner]**](ArrayMustContainInner.md) | Only supported if the &#x60;elementType&#x60; is &#x60;boolean&#x60;, &#x60;numeric&#x60; or &#x60;string&#x60;. Specifies values the array attribute must contain. | [optional] 

## Example

```python
from waylay.services.resources.models.value_constraint import ValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ValueConstraint from a JSON string
value_constraint_instance = ValueConstraint.from_json(json)
# print the JSON string representation of the object
print ValueConstraint.to_json()

# convert the object into a dict
value_constraint_dict = value_constraint_instance.to_dict()
# create an instance of ValueConstraint from a dict
value_constraint_form_dict = value_constraint.from_dict(value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


