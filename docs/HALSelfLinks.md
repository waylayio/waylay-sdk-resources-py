# HALSelfLinks


**Source:** `waylay.services.resources.models.hal_self_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**HALSelfLinksLinks**](HALSelfLinksLinks.md) |  | 


## Example

```python
from waylay.services.resources.models.hal_self_links import HALSelfLinks

hal_self_links = HALSelfLinks(links=...)

# Create from JSON
hal_self_links = HALSelfLinks.from_json('{ "_links": ... }')

# Export to dictionary
hal_self_links_dict = hal_self_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


