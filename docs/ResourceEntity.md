# ResourceEntity

Representation of a Waylay Resource

**Source:** `waylay.services.resources.models.resource_entity`




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
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) | Id of the linked _Resource Type_ | [optional] 
**parent_id** | [**ResourceId**](ResourceId.md) | Id of the parent _Resource_ | [optional] 
**name** | **str** | Name for the _Resource_ | [optional] 
**alias** | **str** | Alias for the name of the _Resource_ | [optional] 
**last_message_timestamp** | **int** | Epoch time of the last contact | [optional] 
**owner** | **str** | Owner of the _Resource_ | [optional] 
**icon** | **str** | URL to the resource icon. | [optional] 
**templates** | [**List[TaskConfiguration]**](TaskConfiguration.md) | Templates for the resource. Used to override diagnostic templates inherited from Resource Type. | [optional] 
**tags** | **List[str]** | Custom classifiers for this _Resource_. | [optional] 


## Example

```python
from waylay.services.resources.models.resource_entity import ResourceEntity

resource_entity = ResourceEntity(
    provider=...,
    provider_id=...,
    customer=...,
    firmware=...,
    location=...,
    metrics=...,
    sensors=...,
    id=...,
    resource_type_id=...,
    parent_id=...,
    name=...,
    alias=...,
    last_message_timestamp=...,
    owner=...,
    icon=...,
    templates=...,
    tags=...,
)

# Create from JSON
resource_entity = ResourceEntity.from_json(
    '{ "provider": ..., "providerId": ..., "customer": ..., "firmware": ..., "location": ..., "metrics": ..., "sensors": ..., "id": ..., "resourceTypeId": ..., "parentId": ..., "name": ..., "alias": ..., "lastMessageTimestamp": ..., "owner": ..., "icon": ..., "templates": ..., "tags": ... }'
)

# Export to dictionary
resource_entity_dict = resource_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


