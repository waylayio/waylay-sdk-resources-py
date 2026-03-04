# ResourceTypeConstraintsListing


**Source:** `waylay.services.resources.models.resource_type_constraints_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceConstraintWithIdEntity]**](ResourceConstraintWithIdEntity.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.resource_type_constraints_listing import (
    ResourceTypeConstraintsListing,
)

resource_type_constraints_listing = ResourceTypeConstraintsListing(
    skip=..., limit=..., total=..., values=...
)

# Create from JSON
resource_type_constraints_listing = ResourceTypeConstraintsListing.from_json(
    '{ "skip": ..., "limit": ..., "total": ..., "values": ... }'
)

# Export to dictionary
resource_type_constraints_listing_dict = resource_type_constraints_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


