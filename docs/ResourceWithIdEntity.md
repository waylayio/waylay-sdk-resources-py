# ResourceWithIdEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) | Id of the linked _Resource Type_ | [optional] 
**parent_id** | [**ResourceId**](ResourceId.md) | Id of the parent _Resource_ | [optional] 
**name** | **str** | Name for the _Resource_ | [optional] 
**alias** | **str** | Alias for the name of the _Resource_ | [optional] 
**last_message_timestamp** | **int** | Epoch time of the last contact | [optional] 
**owner** | **str** | Owner of the _Resource_ | [optional] 
**tags** | **List[str]** | Custom classifiers for this _Resource_. | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**customer** | **str** | Customer name | [optional] 
**firmware** | **str** |  | [optional] 
**location** | [**MetadataEntityLocation**](MetadataEntityLocation.md) |  | [optional] 
**metrics** | [**List[ResourceMetric]**](ResourceMetric.md) | A documentation of possible measurements that are to be expected on _Waylay Events_ associated with this _Resource_. | [optional] 
**sensors** | [**List[ResourceSensor]**](ResourceSensor.md) | Set of sensors that are applicable for a given _Resource_. Please note that there is no explicit action taken by the Waylay platform on this meta key. The idea behind this abstraction is to assist integrations where an architect of the digital twin can specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_). | [optional] 

## Example

```python
from waylay.services.resources.models.resource_with_id_entity import ResourceWithIdEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceWithIdEntity from a JSON string
resource_with_id_entity_instance = ResourceWithIdEntity.from_json(json)
# print the JSON string representation of the object
print ResourceWithIdEntity.to_json()

# convert the object into a dict
resource_with_id_entity_dict = resource_with_id_entity_instance.to_dict()
# create an instance of ResourceWithIdEntity from a dict
resource_with_id_entity_form_dict = resource_with_id_entity.from_dict(resource_with_id_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


