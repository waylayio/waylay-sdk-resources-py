# ResourceTypeCreationResponse


**Source:** `waylay.services.resources.models.resource_type_creation_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceTypeWithIdEntity**](ResourceTypeWithIdEntity.md) |  | 


## Example

```python
from waylay.services.resources.models.resource_type_creation_response import (
    ResourceTypeCreationResponse,
)

resource_type_creation_response = ResourceTypeCreationResponse(
    status_code=..., uri=..., entity=...
)

# Create from JSON
resource_type_creation_response = ResourceTypeCreationResponse.from_json(
    '{ "statusCode": ..., "uri": ..., "entity": ... }'
)

# Export to dictionary
resource_type_creation_response_dict = resource_type_creation_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


