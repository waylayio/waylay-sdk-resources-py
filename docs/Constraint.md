# Constraint

Constraint on the attributes of a Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the _Resource Constraint_ | 
**description** | **str** | A description for the _Resource Constraint_ | [optional] 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | List of attribute descriptions | 

## Example

```python
from waylay.services.resources.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print Constraint.to_json()

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_form_dict = constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


