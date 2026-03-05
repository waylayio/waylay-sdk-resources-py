# ValidationFailure


**Source:** `waylay.services.resources.models.validation_failure`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 
**code** | **str** | Optional error code | [optional] 
**details** | [**List[SchemaValidationError]**](SchemaValidationError.md) | List of SchemaValidationErrors | [optional] 


## Example

```python
from waylay.services.resources.models.validation_failure import ValidationFailure

validation_failure = ValidationFailure(
    status_code=..., error=..., code=..., details=...
)

# Create from JSON
validation_failure = ValidationFailure.from_json(
    '{ "statusCode": ..., "error": ..., "code": ..., "details": ... }'
)

# Export to dictionary
validation_failure_dict = validation_failure.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


