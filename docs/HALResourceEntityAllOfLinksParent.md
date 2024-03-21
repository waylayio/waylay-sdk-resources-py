# HALResourceEntityAllOfLinksParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 

## Example

```python
from waylay.services.resources.models.hal_resource_entity_all_of_links_parent import HALResourceEntityAllOfLinksParent

# TODO update the JSON string below
json = "{}"
# create an instance of HALResourceEntityAllOfLinksParent from a JSON string
hal_resource_entity_all_of_links_parent_instance = HALResourceEntityAllOfLinksParent.from_json(json)
# print the JSON string representation of the object
print HALResourceEntityAllOfLinksParent.to_json()

# convert the object into a dict
hal_resource_entity_all_of_links_parent_dict = hal_resource_entity_all_of_links_parent_instance.to_dict()
# create an instance of HALResourceEntityAllOfLinksParent from a dict
hal_resource_entity_all_of_links_parent_form_dict = hal_resource_entity_all_of_links_parent.from_dict(hal_resource_entity_all_of_links_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


