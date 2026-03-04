# HALResourceListing

Listing of _Resource_ entities in HAL format

**Source:** `waylay.services.resources.models.hal_resource_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**count** | **int** | The number of items in this result page. | 
**links** | [**PaginationLinks**](PaginationLinks.md) |  | 
**embedded** | [**ResourceListingHALEmbedded**](ResourceListingHALEmbedded.md) |  | 


## Example

```python
from waylay.services.resources.models.hal_resource_listing import HALResourceListing

hal_resource_listing = HALResourceListing(
    skip=..., limit=..., total=..., count=..., links=..., embedded=...
)

# Create from JSON
hal_resource_listing = HALResourceListing.from_json(
    '{ "skip": ..., "limit": ..., "total": ..., "count": ..., "_links": ..., "_embedded": ... }'
)

# Export to dictionary
hal_resource_listing_dict = hal_resource_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


