# ResourceTypeWithIdEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceTypeId**](ResourceTypeId.md) |  | 
**name** | **str** | Name for the _Resource Type_ | [optional] 
**templates** | [**List[TaskConfiguration]**](TaskConfiguration.md) | Templates for task that is automatically created whenever a new  _Resource_ of this _Resource Type_ is created. | [optional] 
**provider** | **str** |  | [optional] 
**provider_id** | **str** |  | [optional] 
**customer** | **str** | Customer name | [optional] 
**firmware** | **str** |  | [optional] 
**location** | [**MetadataEntityLocation**](MetadataEntityLocation.md) |  | [optional] 
**metrics** | [**List[ResourceMetric]**](ResourceMetric.md) | A documentation of possible measurements that are to be expected on _Waylay Events_ associated with this _Resource_. | [optional] 
**sensors** | [**List[ResourceSensor]**](ResourceSensor.md) | Set of sensors that are applicable for a given _Resource_. Please note that there is no explicit action taken by the Waylay platform on this meta key. The idea behind this abstraction is to assist integrations where an architect of the digital twin can specify which sensors from waylay library are applicable for a given _Resource_ (or _Resource Type_). | [optional] 
**bulk_operation** | **str** | Indicates an asynchronous operation is busy for the _Resource Type_. | [optional] 
**constraints** | [**List[ConstraintStatus]**](ConstraintStatus.md) | Validation constraint as applied to each _Resource_ that has its &#x60;resourceTypeId&#x60; attribute set to the &#x60;id&#x60; of this _Resource Type_. | [optional] 

## Example

```python
from waylay.services.resources.models.resource_type_with_id_entity import ResourceTypeWithIdEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypeWithIdEntity from a JSON string
resource_type_with_id_entity_instance = ResourceTypeWithIdEntity.from_json(json)
# print the JSON string representation of the object
print ResourceTypeWithIdEntity.to_json()

# convert the object into a dict
resource_type_with_id_entity_dict = resource_type_with_id_entity_instance.to_dict()
# create an instance of ResourceTypeWithIdEntity from a dict
resource_type_with_id_entity_form_dict = resource_type_with_id_entity.from_dict(resource_type_with_id_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


