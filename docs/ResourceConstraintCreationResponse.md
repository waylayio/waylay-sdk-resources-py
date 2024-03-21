# ResourceConstraintCreationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceConstraintWithIdEntity**](ResourceConstraintWithIdEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.resource_constraint_creation_response import ResourceConstraintCreationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConstraintCreationResponse from a JSON string
resource_constraint_creation_response_instance = ResourceConstraintCreationResponse.from_json(json)
# print the JSON string representation of the object
print ResourceConstraintCreationResponse.to_json()

# convert the object into a dict
resource_constraint_creation_response_dict = resource_constraint_creation_response_instance.to_dict()
# create an instance of ResourceConstraintCreationResponse from a dict
resource_constraint_creation_response_form_dict = resource_constraint_creation_response.from_dict(resource_constraint_creation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


