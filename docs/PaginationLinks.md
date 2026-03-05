# PaginationLinks

HAL links for pagination

**Source:** `waylay.services.resources.models.pagination_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PaginationLinksSelf**](PaginationLinksSelf.md) |  | 
**next** | [**PaginationLinksNext**](PaginationLinksNext.md) |  | [optional] 
**prev** | [**PaginationLinksPrev**](PaginationLinksPrev.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.pagination_links import PaginationLinks

pagination_links = PaginationLinks(var_self=..., next=..., prev=...)

# Create from JSON
pagination_links = PaginationLinks.from_json(
    '{ "self": ..., "next": ..., "prev": ... }'
)

# Export to dictionary
pagination_links_dict = pagination_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


