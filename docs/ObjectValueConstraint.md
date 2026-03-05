# ObjectValueConstraint

Specifies that a value must be an object and which attributes it needs to have

**Source:** `waylay.services.resources.models.object_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ObjectValueConstraintType**](ObjectValueConstraintType.md) |  | 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes descriptions | 


## Example

```python
from waylay.services.resources.models.object_value_constraint import (
    ObjectValueConstraint,
)

object_value_constraint = ObjectValueConstraint(type=..., attributes=...)

# Create from JSON
object_value_constraint = ObjectValueConstraint.from_json(
    '{ "type": ..., "attributes": ... }'
)

# Export to dictionary
object_value_constraint_dict = object_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


