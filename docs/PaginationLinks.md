# PaginationLinks

HAL links for pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**PaginationLinksSelf**](PaginationLinksSelf.md) |  | 
**next** | [**PaginationLinksNext**](PaginationLinksNext.md) |  | [optional] 
**prev** | [**PaginationLinksPrev**](PaginationLinksPrev.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.pagination_links import PaginationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationLinks from a JSON string
pagination_links_instance = PaginationLinks.from_json(json)
# print the JSON string representation of the object
print PaginationLinks.to_json()

# convert the object into a dict
pagination_links_dict = pagination_links_instance.to_dict()
# create an instance of PaginationLinks from a dict
pagination_links_form_dict = pagination_links.from_dict(pagination_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


