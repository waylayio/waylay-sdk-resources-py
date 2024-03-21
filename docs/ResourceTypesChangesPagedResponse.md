# ResourceTypesChangesPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceTypeChange]**](ResourceTypeChange.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.resource_types_changes_paged_response import ResourceTypesChangesPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypesChangesPagedResponse from a JSON string
resource_types_changes_paged_response_instance = ResourceTypesChangesPagedResponse.from_json(json)
# print the JSON string representation of the object
print ResourceTypesChangesPagedResponse.to_json()

# convert the object into a dict
resource_types_changes_paged_response_dict = resource_types_changes_paged_response_instance.to_dict()
# create an instance of ResourceTypesChangesPagedResponse from a dict
resource_types_changes_paged_response_form_dict = resource_types_changes_paged_response.from_dict(resource_types_changes_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


