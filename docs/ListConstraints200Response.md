# ListConstraints200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 100]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[ResourceConstraintWithIdEntity]**](ResourceConstraintWithIdEntity.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.list_constraints200_response import ListConstraints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListConstraints200Response from a JSON string
list_constraints200_response_instance = ListConstraints200Response.from_json(json)
# print the JSON string representation of the object
print ListConstraints200Response.to_json()

# convert the object into a dict
list_constraints200_response_dict = list_constraints200_response_instance.to_dict()
# create an instance of ListConstraints200Response from a dict
list_constraints200_response_form_dict = list_constraints200_response.from_dict(list_constraints200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


