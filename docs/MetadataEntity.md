# MetadataEntity

Common attributes for _Resource_ or _Resource Type_

**Source:** `waylay.services.resources.models.metadata_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**customer** | **str** | Customer name | [optional] 
**firmware** | **str** |  | [optional] 
**location** | [**MetadataEntityLocation**](MetadataEntityLocation.md) |  | [optional] 
**metrics** | [**List[ResourceMetric]**](ResourceMetric.md) | A documentation of possible measurements that are to be expected on _Waylay Events_ associated with this _Resource_. | [optional] 
**sensors** | [**List[ResourceSensor]**](ResourceSensor.md) | Set of sensors that are applicable for a given _Resource_. Please note that there is no explicit action taken by the Waylay platform on this meta key. The idea behind this abstraction is to assist integrations where an architect of the digital twin can specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_). | [optional] 


## Example

```python
from waylay.services.resources.models.metadata_entity import MetadataEntity

metadata_entity = MetadataEntity(
    provider=...,
    provider_id=...,
    customer=...,
    firmware=...,
    location=...,
    metrics=...,
    sensors=...,
)

# Create from JSON
metadata_entity = MetadataEntity.from_json(
    '{ "provider": ..., "providerId": ..., "customer": ..., "firmware": ..., "location": ..., "metrics": ..., "sensors": ... }'
)

# Export to dictionary
metadata_entity_dict = metadata_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


