# HALIdLink


**Source:** `waylay.services.resources.models.halid_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 


## Example

```python
from waylay.services.resources.models.halid_link import HALIdLink

halid_link = HALIdLink(href=..., id=...)

# Create from JSON
halid_link = HALIdLink.from_json('{ "href": ..., "id": ... }')

# Export to dictionary
halid_link_dict = halid_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


