# SchemaValidationError


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
from waylay.services.resources.models.schema_validation_error import SchemaValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaValidationError from a JSON string
schema_validation_error_instance = SchemaValidationError.from_json(json)
# print the JSON string representation of the object
print SchemaValidationError.to_json()

# convert the object into a dict
schema_validation_error_dict = schema_validation_error_instance.to_dict()
# create an instance of SchemaValidationError from a dict
schema_validation_error_form_dict = schema_validation_error.from_dict(schema_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


