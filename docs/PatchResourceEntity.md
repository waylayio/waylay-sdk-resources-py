# PatchResourceEntity


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

# TODO update the JSON string below
json = "{}"
# create an instance of PatchResourceEntity from a JSON string
patch_resource_entity_instance = PatchResourceEntity.from_json(json)
# print the JSON string representation of the object
print PatchResourceEntity.to_json()

# convert the object into a dict
patch_resource_entity_dict = patch_resource_entity_instance.to_dict()
# create an instance of PatchResourceEntity from a dict
patch_resource_entity_form_dict = patch_resource_entity.from_dict(patch_resource_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


