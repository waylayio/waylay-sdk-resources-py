# HALPageLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.hal_page_links import HALPageLinks

# TODO update the JSON string below
json = "{}"
# create an instance of HALPageLinks from a JSON string
hal_page_links_instance = HALPageLinks.from_json(json)
# print the JSON string representation of the object
print HALPageLinks.to_json()

# convert the object into a dict
hal_page_links_dict = hal_page_links_instance.to_dict()
# create an instance of HALPageLinks from a dict
hal_page_links_form_dict = hal_page_links.from_dict(hal_page_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


