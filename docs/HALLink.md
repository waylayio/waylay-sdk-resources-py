# HALLink


**Source:** `waylay.services.resources.models.hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 


## Example

```python
from waylay.services.resources.models.hal_link import HALLink

hal_link = HALLink(href=...)

# Create from JSON
hal_link = HALLink.from_json('{ "href": ... }')

# Export to dictionary
hal_link_dict = hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


