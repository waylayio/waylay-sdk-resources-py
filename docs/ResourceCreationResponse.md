# ResourceCreationResponse


**Source:** `waylay.services.resources.models.resource_creation_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceWithIdEntity**](ResourceWithIdEntity.md) |  | 


## Example

```python
from waylay.services.resources.models.resource_creation_response import (
    ResourceCreationResponse,
)

resource_creation_response = ResourceCreationResponse(
    status_code=..., uri=..., entity=...
)

# Create from JSON
resource_creation_response = ResourceCreationResponse.from_json(
    '{ "statusCode": ..., "uri": ..., "entity": ... }'
)

# Export to dictionary
resource_creation_response_dict = resource_creation_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


