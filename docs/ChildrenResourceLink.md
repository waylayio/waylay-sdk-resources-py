# ChildrenResourceLink


**Source:** `waylay.services.resources.models.children_resource_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.children_resource_link import ChildrenResourceLink

children_resource_link = ChildrenResourceLink(href=...)

# Create from JSON
children_resource_link = ChildrenResourceLink.from_json('{ "href": ... }')

# Export to dictionary
children_resource_link_dict = children_resource_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


