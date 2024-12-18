# ResourceConstraintWithIdEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique _Resource Constraint_ id generated by the Waylay System | 
**name** | **str** | Name for the _Resource Constraint_ | 
**description** | **str** | A description for the _Resource Constraint_ | [optional] 
**tags** | **List[str]** |  | [optional] 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | List of attribute descriptions | 

## Example

```python
from waylay.services.resources.models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConstraintWithIdEntity from a JSON string
resource_constraint_with_id_entity_instance = ResourceConstraintWithIdEntity.from_json(json)
# print the JSON string representation of the object
print ResourceConstraintWithIdEntity.to_json()

# convert the object into a dict
resource_constraint_with_id_entity_dict = resource_constraint_with_id_entity_instance.to_dict()
# create an instance of ResourceConstraintWithIdEntity from a dict
resource_constraint_with_id_entity_form_dict = resource_constraint_with_id_entity.from_dict(resource_constraint_with_id_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


