# ResourceCreationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceWithIdEntity**](ResourceWithIdEntity.md) |  | 

## Example

```python
from waylay.services.resources.models.resource_creation_response import ResourceCreationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCreationResponse from a JSON string
resource_creation_response_instance = ResourceCreationResponse.from_json(json)
# print the JSON string representation of the object
print ResourceCreationResponse.to_json()

# convert the object into a dict
resource_creation_response_dict = resource_creation_response_instance.to_dict()
# create an instance of ResourceCreationResponse from a dict
resource_creation_response_form_dict = resource_creation_response.from_dict(resource_creation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


