# ResourceConstraintCreationResponse


**Source:** `waylay.services.resources.models.resource_constraint_creation_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**uri** | **str** |  | 
**entity** | [**ResourceConstraintWithIdEntity**](ResourceConstraintWithIdEntity.md) |  | 


## Example

```python
from waylay.services.resources.models.resource_constraint_creation_response import (
    ResourceConstraintCreationResponse,
)

resource_constraint_creation_response = ResourceConstraintCreationResponse(
    status_code=..., uri=..., entity=...
)

# Create from JSON
resource_constraint_creation_response = ResourceConstraintCreationResponse.from_json(
    '{ "statusCode": ..., "uri": ..., "entity": ... }'
)

# Export to dictionary
resource_constraint_creation_response_dict = (
    resource_constraint_creation_response.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


