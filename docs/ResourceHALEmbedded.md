# ResourceHALEmbedded


**Source:** `waylay.services.resources.models.resource_hal_embedded`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**HALResourceTypeEntity**](HALResourceTypeEntity.md) |  | [optional] 


## Example

```python
from waylay.services.resources.models.resource_hal_embedded import ResourceHALEmbedded

resource_hal_embedded = ResourceHALEmbedded(resource_type=...)

# Create from JSON
resource_hal_embedded = ResourceHALEmbedded.from_json('{ "resourceType": ... }')

# Export to dictionary
resource_hal_embedded_dict = resource_hal_embedded.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


