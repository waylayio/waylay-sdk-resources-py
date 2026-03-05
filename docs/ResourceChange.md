# ResourceChange


**Source:** `waylay.services.resources.models.resource_change`




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

resource_change = ResourceChange(
    time=..., resource_id=..., user_id=..., change=..., resource=...
)

# Create from JSON
resource_change = ResourceChange.from_json(
    '{ "time": ..., "resourceId": ..., "userId": ..., "change": ..., "resource": ... }'
)

# Export to dictionary
resource_change_dict = resource_change.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


