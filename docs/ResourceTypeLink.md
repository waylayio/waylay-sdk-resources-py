# ResourceTypeLink


**Source:** `waylay.services.resources.models.resource_type_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 


## Example

```python
from waylay.services.resources.models.resource_type_link import ResourceTypeLink

resource_type_link = ResourceTypeLink(href=..., id=...)

# Create from JSON
resource_type_link = ResourceTypeLink.from_json('{ "href": ..., "id": ... }')

# Export to dictionary
resource_type_link_dict = resource_type_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


