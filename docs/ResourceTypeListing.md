# ResourceTypeListing

A listing of _Resource Type_ entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceTypeWithIdEntity]**](ResourceTypeWithIdEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.resource_type_listing import ResourceTypeListing

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypeListing from a JSON string
resource_type_listing_instance = ResourceTypeListing.from_json(json)
# print the JSON string representation of the object
print ResourceTypeListing.to_json()

# convert the object into a dict
resource_type_listing_dict = resource_type_listing_instance.to_dict()
# create an instance of ResourceTypeListing from a dict
resource_type_listing_form_dict = resource_type_listing.from_dict(resource_type_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


