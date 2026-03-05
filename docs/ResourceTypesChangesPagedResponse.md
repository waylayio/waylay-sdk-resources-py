# ResourceTypesChangesPagedResponse


**Source:** `waylay.services.resources.models.resource_types_changes_paged_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceTypeChange]**](ResourceTypeChange.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.resource_types_changes_paged_response import (
    ResourceTypesChangesPagedResponse,
)

resource_types_changes_paged_response = ResourceTypesChangesPagedResponse(
    skip=..., limit=..., total=..., values=...
)

# Create from JSON
resource_types_changes_paged_response = ResourceTypesChangesPagedResponse.from_json(
    '{ "skip": ..., "limit": ..., "total": ..., "values": ... }'
)

# Export to dictionary
resource_types_changes_paged_response_dict = (
    resource_types_changes_paged_response.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


