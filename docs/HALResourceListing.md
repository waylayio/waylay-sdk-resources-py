# HALResourceListing

Listing of _Resource_ entities in HAL format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**count** | **int** | The number of items in this result page. | 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | 
**embedded** | [**HALResourceListingAllOfEmbedded**](HALResourceListingAllOfEmbedded.md) |  | 

## Example

```python
from waylay.services.resources.models.hal_resource_listing import HALResourceListing

# TODO update the JSON string below
json = "{}"
# create an instance of HALResourceListing from a JSON string
hal_resource_listing_instance = HALResourceListing.from_json(json)
# print the JSON string representation of the object
print HALResourceListing.to_json()

# convert the object into a dict
hal_resource_listing_dict = hal_resource_listing_instance.to_dict()
# create an instance of HALResourceListing from a dict
hal_resource_listing_form_dict = hal_resource_listing.from_dict(hal_resource_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


