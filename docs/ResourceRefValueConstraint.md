# ResourceRefValueConstraint

Specifies that a value is an object having a required '$ref' attribute that references another _Resource_.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ResourceRefValueConstraintType**](ResourceRefValueConstraintType.md) |  | [optional] 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Additional attributes in the reference object, describing the relation. | [optional] 
**resource_types** | [**List[ResourceTypeId]**](ResourceTypeId.md) | The possible _Resource Types_ for the referenced _Resource_. | [optional] 
**exists** | **bool** | Flag to indicate if the referenced _Resource_ must exist | [optional] [default to False]

## Example

```python
from waylay.services.resources.models.resource_ref_value_constraint import ResourceRefValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRefValueConstraint from a JSON string
resource_ref_value_constraint_instance = ResourceRefValueConstraint.from_json(json)
# print the JSON string representation of the object
print ResourceRefValueConstraint.to_json()

# convert the object into a dict
resource_ref_value_constraint_dict = resource_ref_value_constraint_instance.to_dict()
# create an instance of ResourceRefValueConstraint from a dict
resource_ref_value_constraint_form_dict = resource_ref_value_constraint.from_dict(resource_ref_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


