# ObjectValueConstraint

Specifies that a value must be an object and which attributes it needs to have

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes descriptions | 

## Example

```python
from waylay.services.resources.models.object_value_constraint import ObjectValueConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectValueConstraint from a JSON string
object_value_constraint_instance = ObjectValueConstraint.from_json(json)
# print the JSON string representation of the object
print ObjectValueConstraint.to_json()

# convert the object into a dict
object_value_constraint_dict = object_value_constraint_instance.to_dict()
# create an instance of ObjectValueConstraint from a dict
object_value_constraint_form_dict = object_value_constraint.from_dict(object_value_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


