# ResourceTypeChange


**Source:** `waylay.services.resources.models.resource_type_change`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**resource_type_id** | [**ResourceTypeId**](ResourceTypeId.md) |  | 
**user_id** | **str** | User subject id in the Waylay Accounts database | 
**change** | [**ResourceChangeChange**](ResourceChangeChange.md) |  | 
**resource_type** | [**ResourceTypeWithIdEntity**](ResourceTypeWithIdEntity.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.resource_type_change import ResourceTypeChange

resource_type_change = ResourceTypeChange(
    time=..., resource_type_id=..., user_id=..., change=..., resource_type=...
)

# Create from JSON
resource_type_change = ResourceTypeChange.from_json(
    '{ "time": ..., "resourceTypeId": ..., "userId": ..., "change": ..., "resourceType": ... }'
)

# Export to dictionary
resource_type_change_dict = resource_type_change.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


