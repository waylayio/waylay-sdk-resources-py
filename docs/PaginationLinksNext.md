# PaginationLinksNext


**Source:** `waylay.services.resources.models.pagination_links_next`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.pagination_links_next import PaginationLinksNext

pagination_links_next = PaginationLinksNext(href=...)

# Create from JSON
pagination_links_next = PaginationLinksNext.from_json('{ "href": ... }')

# Export to dictionary
pagination_links_next_dict = pagination_links_next.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


