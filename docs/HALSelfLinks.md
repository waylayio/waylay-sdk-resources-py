# HALSelfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**HALSelfLinksLinks**](HALSelfLinksLinks.md) |  | 

## Example

```python
from waylay.services.resources.models.hal_self_links import HALSelfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of HALSelfLinks from a JSON string
hal_self_links_instance = HALSelfLinks.from_json(json)
# print the JSON string representation of the object
print HALSelfLinks.to_json()

# convert the object into a dict
hal_self_links_dict = hal_self_links_instance.to_dict()
# create an instance of HALSelfLinks from a dict
hal_self_links_form_dict = hal_self_links.from_dict(hal_self_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


