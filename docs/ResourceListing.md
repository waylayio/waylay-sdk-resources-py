# ResourceListing

A full listing _Resource_ entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceWithIdEntity]**](ResourceWithIdEntity.md) | _Resource_ entities | 

## Example

```python
from waylay.services.resources.models.resource_listing import ResourceListing

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListing from a JSON string
resource_listing_instance = ResourceListing.from_json(json)
# print the JSON string representation of the object
print ResourceListing.to_json()

# convert the object into a dict
resource_listing_dict = resource_listing_instance.to_dict()
# create an instance of ResourceListing from a dict
resource_listing_form_dict = resource_listing.from_dict(resource_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


