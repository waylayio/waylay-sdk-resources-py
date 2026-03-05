# ResourceListing

A full listing _Resource_ entities

**Source:** `waylay.services.resources.models.resource_listing`




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

resource_listing = ResourceListing(skip=..., limit=..., total=..., values=...)

# Create from JSON
resource_listing = ResourceListing.from_json(
    '{ "skip": ..., "limit": ..., "total": ..., "values": ... }'
)

# Export to dictionary
resource_listing_dict = resource_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


