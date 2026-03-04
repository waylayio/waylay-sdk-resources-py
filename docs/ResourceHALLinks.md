# ResourceHALLinks


**Source:** `waylay.services.resources.models.resource_hal_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**ParentResourceLink**](ParentResourceLink.md) |  | [optional] 
**children** | [**ChildrenResourceLink**](ChildrenResourceLink.md) |  | [optional] 
**resource_type** | [**ResourceTypeLink**](ResourceTypeLink.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.resource_hal_links import ResourceHALLinks

resource_hal_links = ResourceHALLinks(parent=..., children=..., resource_type=...)

# Create from JSON
resource_hal_links = ResourceHALLinks.from_json(
    '{ "parent": ..., "children": ..., "resourceType": ... }'
)

# Export to dictionary
resource_hal_links_dict = resource_hal_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


