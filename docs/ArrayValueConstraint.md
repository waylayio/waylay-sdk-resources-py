# ArrayValueConstraint

Specifies that a value must be an array and what type of elements it contains

**Source:** `waylay.services.resources.models.array_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ArrayValueConstraintType**](ArrayValueConstraintType.md) |  | 
**element_type** | [**GenericModel**](GenericModel.md) |  | 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**unique_values** | **bool** | If true, all values in the array must be unique. | [optional] [default to False]
**contains** | [**List[ArrayContainValue]**](ArrayContainValue.md) | Only supported if the &#x60;elementType&#x60; is &#x60;boolean&#x60;, &#x60;numeric&#x60; or &#x60;string&#x60;. Specifies values the array attribute must contain. | [optional] 


## Example

```python
from waylay.services.resources.models.array_value_constraint import ArrayValueConstraint

array_value_constraint = ArrayValueConstraint(
    type=...,
    element_type=...,
    min_length=...,
    max_length=...,
    unique_values=...,
    contains=...,
)

# Create from JSON
array_value_constraint = ArrayValueConstraint.from_json(
    '{ "type": ..., "elementType": ..., "minLength": ..., "maxLength": ..., "uniqueValues": ..., "contains": ... }'
)

# Export to dictionary
array_value_constraint_dict = array_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


