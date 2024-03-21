# ResourceTypeChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) |  | 
**user_id** | **str** | User subject id in the Waylay Accounts database | 
**change** | **str** |  | 
**resource_type** | [**ResourceTypeWithIdEntity**](ResourceTypeWithIdEntity.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.resource_type_change import ResourceTypeChange

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTypeChange from a JSON string
resource_type_change_instance = ResourceTypeChange.from_json(json)
# print the JSON string representation of the object
print ResourceTypeChange.to_json()

# convert the object into a dict
resource_type_change_dict = resource_type_change_instance.to_dict()
# create an instance of ResourceTypeChange from a dict
resource_type_change_form_dict = resource_type_change.from_dict(resource_type_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


