# PatchResourceTypeEntity


**Source:** `waylay.services.resources.models.patch_resource_type_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceTypeId**](ResourceTypeId.md) |  | [optional] 
**name** | **object** |  | [optional] 
**icon** | **object** |  | [optional] 
**templates** | **object** |  | [optional] 
**provider** | **object** |  | [optional] 
**provider_id** | **object** |  | [optional] 
**customer** | **object** |  | [optional] 
**firmware** | **object** |  | [optional] 
**location** | **object** |  | [optional] 
**metrics** | **object** |  | [optional] 
**sensors** | **object** |  | [optional] 
**constraints** | **List[str]** | Validation constraint to be applied to each _Resource_ that has its &#x60;resourceTypeId&#x60; attribute set to the &#x60;id&#x60; of this _Resource Type_. | [optional] 


## Example

```python
from waylay.services.resources.models.patch_resource_type_entity import (
    PatchResourceTypeEntity,
)

patch_resource_type_entity = PatchResourceTypeEntity(
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
    constraints=...,
)

# Create from JSON
patch_resource_type_entity = PatchResourceTypeEntity.from_json(
    '{ "id": ..., "name": ..., "icon": ..., "templates": ..., "provider": ..., "providerId": ..., "customer": ..., "firmware": ..., "location": ..., "metrics": ..., "sensors": ..., "$constraints": ... }'
)

# Export to dictionary
patch_resource_type_entity_dict = patch_resource_type_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


