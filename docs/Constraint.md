# Constraint

Constraint on the attributes of a Resource

**Source:** `waylay.services.resources.models.constraint`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the _Resource Constraint_ | 
**description** | **str** | A description for the _Resource Constraint_ | [optional] 
**tags** | **List[str]** |  | [optional] 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | List of attribute descriptions | 


## Example

```python
from waylay.services.resources.models.constraint import Constraint

constraint = Constraint(name=..., description=..., tags=..., attributes=...)

# Create from JSON
constraint = Constraint.from_json(
    '{ "name": ..., "description": ..., "tags": ..., "attributes": ... }'
)

# Export to dictionary
constraint_dict = constraint.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


