# PaginationLinksNext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 

## Example

```python
from waylay.services.resources.models.pagination_links_next import PaginationLinksNext

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinksNext from a JSON string
pagination_links_next_instance = PaginationLinksNext.from_json(json)
# print the JSON string representation of the object
print PaginationLinksNext.to_json()

# convert the object into a dict
pagination_links_next_dict = pagination_links_next_instance.to_dict()
# create an instance of PaginationLinksNext from a dict
pagination_links_next_form_dict = pagination_links_next.from_dict(pagination_links_next_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


