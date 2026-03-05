# PaginationLinksSelf


**Source:** `waylay.services.resources.models.pagination_links_self`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.pagination_links_self import PaginationLinksSelf

pagination_links_self = PaginationLinksSelf(href=...)

# Create from JSON
pagination_links_self = PaginationLinksSelf.from_json('{ "href": ... }')

# Export to dictionary
pagination_links_self_dict = pagination_links_self.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


