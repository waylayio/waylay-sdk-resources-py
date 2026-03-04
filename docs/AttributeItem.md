# AttributeItem

Constraint on the presence and value of a single named _Resource_ attribute.

**Source:** `waylay.services.resources.models.attribute_item`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the attribute | 
**required** | **bool** | Indicates if the attribute must be present or is optional | 
**type** | [**GenericModel**](GenericModel.md) |  | 


## Example

```python
from waylay.services.resources.models.attribute_item import AttributeItem

attribute_item = AttributeItem(name=..., required=..., type=...)

# Create from JSON
attribute_item = AttributeItem.from_json(
    '{ "name": ..., "required": ..., "type": ... }'
)

# Export to dictionary
attribute_item_dict = attribute_item.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


