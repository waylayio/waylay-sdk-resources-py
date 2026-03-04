# ResourceRefValueConstraint

Specifies that a value is an object having a required '$ref' attribute that references another _Resource_.

**Source:** `waylay.services.resources.models.resource_ref_value_constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceRefValueConstraintType**](ResourceRefValueConstraintType.md) |  | [optional] 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Additional attributes in the reference object, describing the relation. | [optional] 
**resource_types** | [**List[ResourceTypeId]**](ResourceTypeId.md) | The possible _Resource Types_ for the referenced _Resource_. | [optional] 
**exists** | **bool** | Flag to indicate if the referenced _Resource_ must exist | [optional] [default to False]


## Example

```python
from waylay.services.resources.models.resource_ref_value_constraint import (
    ResourceRefValueConstraint,
)

resource_ref_value_constraint = ResourceRefValueConstraint(
    type=..., attributes=..., resource_types=..., exists=...
)

# Create from JSON
resource_ref_value_constraint = ResourceRefValueConstraint.from_json(
    '{ "type": ..., "attributes": ..., "resourceTypes": ..., "exists": ... }'
)

# Export to dictionary
resource_ref_value_constraint_dict = resource_ref_value_constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


