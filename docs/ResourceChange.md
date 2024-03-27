# ResourceChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**resource_id** | [**ResourceId**](ResourceId.md) |  | 
**user_id** | **str** | User subject id in the Waylay Accounts database | 
**change** | [**ResourceChangeChange**](ResourceChangeChange.md) |  | 
**resource** | [**ResourceWithIdEntity**](ResourceWithIdEntity.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.resource_change import ResourceChange

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceChange from a JSON string
resource_change_instance = ResourceChange.from_json(json)
# print the JSON string representation of the object
print ResourceChange.to_json()

# convert the object into a dict
resource_change_dict = resource_change_instance.to_dict()
# create an instance of ResourceChange from a dict
resource_change_form_dict = resource_change.from_dict(resource_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


