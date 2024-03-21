# PaginationLinksSelf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 

## Example

```python
from waylay.services.resources.models.pagination_links_self import PaginationLinksSelf

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinksSelf from a JSON string
pagination_links_self_instance = PaginationLinksSelf.from_json(json)
# print the JSON string representation of the object
print PaginationLinksSelf.to_json()

# convert the object into a dict
pagination_links_self_dict = pagination_links_self_instance.to_dict()
# create an instance of PaginationLinksSelf from a dict
pagination_links_self_form_dict = pagination_links_self.from_dict(pagination_links_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


