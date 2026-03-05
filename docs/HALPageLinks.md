# HALPageLinks


**Source:** `waylay.services.resources.models.hal_page_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.hal_page_links import HALPageLinks

hal_page_links = HALPageLinks(links=...)

# Create from JSON
hal_page_links = HALPageLinks.from_json('{ "_links": ... }')

# Export to dictionary
hal_page_links_dict = hal_page_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


