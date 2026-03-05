# HALSelfLinksLinks

Links to related objects

**Source:** `waylay.services.resources.models.hal_self_links_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HALSelfLinksLinksSelf**](HALSelfLinksLinksSelf.md) |  | 


## Example

```python
from waylay.services.resources.models.hal_self_links_links import HALSelfLinksLinks

hal_self_links_links = HALSelfLinksLinks(var_self=...)

# Create from JSON
hal_self_links_links = HALSelfLinksLinks.from_json('{ "self": ... }')

# Export to dictionary
hal_self_links_links_dict = hal_self_links_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


