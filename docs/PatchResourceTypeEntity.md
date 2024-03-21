# PatchResourceTypeEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceTypeId**](ResourceTypeId.md) |  | [optional] 
**name** | **object** |  | [optional] 
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
from waylay.services.resources.models.patch_resource_type_entity import PatchResourceTypeEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PatchResourceTypeEntity from a JSON string
patch_resource_type_entity_instance = PatchResourceTypeEntity.from_json(json)
# print the JSON string representation of the object
print PatchResourceTypeEntity.to_json()

# convert the object into a dict
patch_resource_type_entity_dict = patch_resource_type_entity_instance.to_dict()
# create an instance of PatchResourceTypeEntity from a dict
patch_resource_type_entity_form_dict = patch_resource_type_entity.from_dict(patch_resource_type_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


