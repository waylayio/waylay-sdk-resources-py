# HALResourceEntityAllOfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**HALResourceEntityAllOfLinksParent**](HALResourceEntityAllOfLinksParent.md) |  | [optional] 
**children** | [**HALResourceEntityAllOfLinksChildren**](HALResourceEntityAllOfLinksChildren.md) |  | [optional] 
**resource_type** | [**HALResourceEntityAllOfLinksResourceType**](HALResourceEntityAllOfLinksResourceType.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.hal_resource_entity_all_of_links import HALResourceEntityAllOfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of HALResourceEntityAllOfLinks from a JSON string
hal_resource_entity_all_of_links_instance = HALResourceEntityAllOfLinks.from_json(json)
# print the JSON string representation of the object
print HALResourceEntityAllOfLinks.to_json()

# convert the object into a dict
hal_resource_entity_all_of_links_dict = hal_resource_entity_all_of_links_instance.to_dict()
# create an instance of HALResourceEntityAllOfLinks from a dict
hal_resource_entity_all_of_links_form_dict = hal_resource_entity_all_of_links.from_dict(hal_resource_entity_all_of_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


