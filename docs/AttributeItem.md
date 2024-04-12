# AttributeItem

Constraint on the presence and value of a single named _Resource_ attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the attribute | 
**required** | **bool** | Indicates if the attribute must be present or is optional | 
**type** | [**GenericModel**](GenericModel.md) |  | 

## Example

```python
from waylay.services.resources.models.attribute_item import AttributeItem

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeItem from a JSON string
attribute_item_instance = AttributeItem.from_json(json)
# print the JSON string representation of the object
print AttributeItem.to_json()

# convert the object into a dict
attribute_item_dict = attribute_item_instance.to_dict()
# create an instance of AttributeItem from a dict
attribute_item_form_dict = attribute_item.from_dict(attribute_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


