# ResourceTypeCreationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceTypeWithIdEntity**](ResourceTypeWithIdEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.resource_type_creation_response import ResourceTypeCreationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypeCreationResponse from a JSON string
resource_type_creation_response_instance = ResourceTypeCreationResponse.from_json(json)
# print the JSON string representation of the object
print ResourceTypeCreationResponse.to_json()

# convert the object into a dict
resource_type_creation_response_dict = resource_type_creation_response_instance.to_dict()
# create an instance of ResourceTypeCreationResponse from a dict
resource_type_creation_response_form_dict = resource_type_creation_response.from_dict(resource_type_creation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


