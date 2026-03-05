# HALResourceTypeEntity


**Source:** `waylay.services.resources.models.hal_resource_type_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**HALSelfLinksLinks**](HALSelfLinksLinks.md) |  | 
**id** | [**ResourceTypeId**](ResourceTypeId.md) |  | [optional] 
**name** | **str** | Name for the _Resource Type_ | [optional] 
**icon** | **str** | URL to Resource Type icon. | [optional] 
**templates** | [**List[TaskConfiguration]**](TaskConfiguration.md) | Templates for task that is automatically created whenever a new  _Resource_ of this _Resource Type_ is created. | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**customer** | **str** | Customer name | [optional] 
**firmware** | **str** |  | [optional] 
**location** | [**MetadataEntityLocation**](MetadataEntityLocation.md) |  | [optional] 
**metrics** | [**List[ResourceMetric]**](ResourceMetric.md) | A documentation of possible measurements that are to be expected on _Waylay Events_ associated with this _Resource_. | [optional] 
**sensors** | [**List[ResourceSensor]**](ResourceSensor.md) | Set of sensors that are applicable for a given _Resource_. Please note that there is no explicit action taken by the Waylay platform on this meta key. The idea behind this abstraction is to assist integrations where an architect of the digital twin can specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_). | [optional] 


## Example

```python
from waylay.services.resources.models.hal_resource_type_entity import (
    HALResourceTypeEntity,
)

hal_resource_type_entity = HALResourceTypeEntity(
    links=...,
    id=...,
    name=...,
    icon=...,
    templates=...,
    provider=...,
    provider_id=...,
    customer=...,
    firmware=...,
    location=...,
    metrics=...,
    sensors=...,
)

# Create from JSON
hal_resource_type_entity = HALResourceTypeEntity.from_json(
    '{ "_links": ..., "id": ..., "name": ..., "icon": ..., "templates": ..., "provider": ..., "providerId": ..., "customer": ..., "firmware": ..., "location": ..., "metrics": ..., "sensors": ... }'
)

# Export to dictionary
hal_resource_type_entity_dict = hal_resource_type_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


