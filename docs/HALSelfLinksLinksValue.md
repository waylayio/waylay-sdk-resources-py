# HALSelfLinksLinksValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 

## Example

```python
from waylay.services.resources.models.hal_self_links_links_value import HALSelfLinksLinksValue

# TODO update the JSON string below
json = "{}"
# create an instance of HALSelfLinksLinksValue from a JSON string
hal_self_links_links_value_instance = HALSelfLinksLinksValue.from_json(json)
# print the JSON string representation of the object
print HALSelfLinksLinksValue.to_json()

# convert the object into a dict
hal_self_links_links_value_dict = hal_self_links_links_value_instance.to_dict()
# create an instance of HALSelfLinksLinksValue from a dict
hal_self_links_links_value_form_dict = hal_self_links_links_value.from_dict(hal_self_links_links_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


