# MetadataEntityLocation

A global location, expressed as a longitude-latitude pair.

**Source:** `waylay.services.resources.models.metadata_entity_location`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude degrees of a location. | 
**lon** | **float** | The longitudinal degrees of a location. | 


## Example

```python
from waylay.services.resources.models.metadata_entity_location import (
    MetadataEntityLocation,
)

metadata_entity_location = MetadataEntityLocation(lat=..., lon=...)

# Create from JSON
metadata_entity_location = MetadataEntityLocation.from_json(
    '{ "lat": ..., "lon": ... }'
)

# Export to dictionary
metadata_entity_location_dict = metadata_entity_location.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


