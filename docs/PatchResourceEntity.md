# PatchResourceEntity


**Source:** `waylay.services.resources.models.patch_resource_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**resource_type_id** | **object** |  | [optional] 
**parent_id** | **object** |  | [optional] 
**name** | **object** |  | [optional] 
**alias** | **object** |  | [optional] 
**last_message_timestamp** | **object** |  | [optional] 
**owner** | **object** |  | [optional] 
**icon** | **object** |  | [optional] 
**templates** | [**List[TaskConfiguration]**](TaskConfiguration.md) | Templates for the resource. Used to override diagnostic templates inherited from Resource Type. | [optional] 
**tags** | **object** |  | [optional] 
**provider** | **object** |  | [optional] 
**provider_id** | **object** |  | [optional] 
**customer** | **object** |  | [optional] 
**firmware** | **object** |  | [optional] 
**location** | **object** |  | [optional] 
**metrics** | **object** |  | [optional] 
**sensors** | **object** |  | [optional] 


## Example

```python
from waylay.services.resources.models.patch_resource_entity import PatchResourceEntity

patch_resource_entity = PatchResourceEntity(
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
    provider=...,
    provider_id=...,
    customer=...,
    firmware=...,
    location=...,
    metrics=...,
    sensors=...,
)

# Create from JSON
patch_resource_entity = PatchResourceEntity.from_json(
    '{ "id": ..., "resourceTypeId": ..., "parentId": ..., "name": ..., "alias": ..., "lastMessageTimestamp": ..., "owner": ..., "icon": ..., "templates": ..., "tags": ..., "provider": ..., "providerId": ..., "customer": ..., "firmware": ..., "location": ..., "metrics": ..., "sensors": ... }'
)

# Export to dictionary
patch_resource_entity_dict = patch_resource_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


