# SchemaValidationError


**Source:** `waylay.services.resources.models.schema_validation_error`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_path** | **str** |  | [optional] 
**errors** | **object** |  | [optional] 
**keyword** | **str** |  | [optional] 
**msgs** | **List[str]** |  | [optional] 
**value** | **object** |  | [optional] 
**instance_path** | **str** |  | [optional] 


## Example

```python
from waylay.services.resources.models.schema_validation_error import (
    SchemaValidationError,
)

schema_validation_error = SchemaValidationError(
    schema_path=..., errors=..., keyword=..., msgs=..., value=..., instance_path=...
)

# Create from JSON
schema_validation_error = SchemaValidationError.from_json(
    '{ "schemaPath": ..., "errors": ..., "keyword": ..., "msgs": ..., "value": ..., "instancePath": ... }'
)

# Export to dictionary
schema_validation_error_dict = schema_validation_error.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


