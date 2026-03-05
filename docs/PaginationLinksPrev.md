# PaginationLinksPrev


**Source:** `waylay.services.resources.models.pagination_links_prev`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.pagination_links_prev import PaginationLinksPrev

pagination_links_prev = PaginationLinksPrev(href=...)

# Create from JSON
pagination_links_prev = PaginationLinksPrev.from_json('{ "href": ... }')

# Export to dictionary
pagination_links_prev_dict = pagination_links_prev.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


