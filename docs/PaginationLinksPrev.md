# PaginationLinksPrev


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 

## Example

```python
from waylay.services.resources.models.pagination_links_prev import PaginationLinksPrev

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinksPrev from a JSON string
pagination_links_prev_instance = PaginationLinksPrev.from_json(json)
# print the JSON string representation of the object
print PaginationLinksPrev.to_json()

# convert the object into a dict
pagination_links_prev_dict = pagination_links_prev_instance.to_dict()
# create an instance of PaginationLinksPrev from a dict
pagination_links_prev_form_dict = pagination_links_prev.from_dict(pagination_links_prev_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


