# ParentResourceLink


**Source:** `waylay.services.resources.models.parent_resource_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 


## Example

```python
from waylay.services.resources.models.parent_resource_link import ParentResourceLink

parent_resource_link = ParentResourceLink(href=..., id=...)

# Create from JSON
parent_resource_link = ParentResourceLink.from_json('{ "href": ..., "id": ... }')

# Export to dictionary
parent_resource_link_dict = parent_resource_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


