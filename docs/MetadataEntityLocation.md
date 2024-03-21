# MetadataEntityLocation

A global location, expressed as a longitude-latitude pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude degrees of a location. | 
**lon** | **float** | The longitudinal degrees of a location. | 

## Example

```python
from waylay.services.resources.models.metadata_entity_location import MetadataEntityLocation

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataEntityLocation from a JSON string
metadata_entity_location_instance = MetadataEntityLocation.from_json(json)
# print the JSON string representation of the object
print MetadataEntityLocation.to_json()

# convert the object into a dict
metadata_entity_location_dict = metadata_entity_location_instance.to_dict()
# create an instance of MetadataEntityLocation from a dict
metadata_entity_location_form_dict = metadata_entity_location.from_dict(metadata_entity_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


