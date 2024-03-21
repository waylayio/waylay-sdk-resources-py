# MetadataEntityValue

Other key-value properties provisioned by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A URI for the _Resource_, formatted as &#x60;/resources/{resourceId}&#x60; | 

## Example

```python
from waylay.services.resources.models.metadata_entity_value import MetadataEntityValue

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataEntityValue from a JSON string
metadata_entity_value_instance = MetadataEntityValue.from_json(json)
# print the JSON string representation of the object
print MetadataEntityValue.to_json()

# convert the object into a dict
metadata_entity_value_dict = metadata_entity_value_instance.to_dict()
# create an instance of MetadataEntityValue from a dict
metadata_entity_value_form_dict = metadata_entity_value.from_dict(metadata_entity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


