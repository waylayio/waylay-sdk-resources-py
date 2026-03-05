# HALSelfLinksLinksSelf


**Source:** `waylay.services.resources.models.hal_self_links_links_self`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.hal_self_links_links_self import (
    HALSelfLinksLinksSelf,
)

hal_self_links_links_self = HALSelfLinksLinksSelf(href=...)

# Create from JSON
hal_self_links_links_self = HALSelfLinksLinksSelf.from_json('{ "href": ... }')

# Export to dictionary
hal_self_links_links_self_dict = hal_self_links_links_self.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


