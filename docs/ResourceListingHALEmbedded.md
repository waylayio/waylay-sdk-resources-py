# ResourceListingHALEmbedded


**Source:** `waylay.services.resources.models.resource_listing_hal_embedded`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[HALResourceEntity]**](HALResourceEntity.md) | _Resource_ entities in HAL format | 


## Example

```python
from waylay.services.resources.models.resource_listing_hal_embedded import (
    ResourceListingHALEmbedded,
)

resource_listing_hal_embedded = ResourceListingHALEmbedded(values=...)

# Create from JSON
resource_listing_hal_embedded = ResourceListingHALEmbedded.from_json(
    '{ "values": ... }'
)

# Export to dictionary
resource_listing_hal_embedded_dict = resource_listing_hal_embedded.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


