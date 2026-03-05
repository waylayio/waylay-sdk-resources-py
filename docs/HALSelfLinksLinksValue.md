# HALSelfLinksLinksValue


**Source:** `waylay.services.resources.models.hal_self_links_links_value`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 


## Example

```python
from waylay.services.resources.models.hal_self_links_links_value import (
    HALSelfLinksLinksValue,
)

hal_self_links_links_value = HALSelfLinksLinksValue(href=..., id=...)

# Create from JSON
hal_self_links_links_value = HALSelfLinksLinksValue.from_json(
    '{ "href": ..., "id": ... }'
)

# Export to dictionary
hal_self_links_links_value_dict = hal_self_links_links_value.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


