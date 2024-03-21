# ValidationFailure


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

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationFailure from a JSON string
validation_failure_instance = ValidationFailure.from_json(json)
# print the JSON string representation of the object
print ValidationFailure.to_json()

# convert the object into a dict
validation_failure_dict = validation_failure_instance.to_dict()
# create an instance of ValidationFailure from a dict
validation_failure_form_dict = validation_failure.from_dict(validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


