# CloudMetadataEvent


**Source:** `waylay.services.resources.models.cloud_metadata_event`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | 
**source** | [**CloudMetadataEventDataSource**](CloudMetadataEventDataSource.md) |  | 
**subject** | **object** |  | 
**type** | [**CloudMetadataEventDataType**](CloudMetadataEventDataType.md) |  | 
**data** | [**MetadataEvent**](MetadataEvent.md) |  | [optional] 
**time** | **datetime** |  | 


## Example

```python
from waylay.services.resources.models.cloud_metadata_event import CloudMetadataEvent

cloud_metadata_event = CloudMetadataEvent(
    id=..., source=..., subject=..., type=..., data=..., time=...
)

# Create from JSON
cloud_metadata_event = CloudMetadataEvent.from_json(
    '{ "id": ..., "source": ..., "subject": ..., "type": ..., "data": ..., "time": ... }'
)

# Export to dictionary
cloud_metadata_event_dict = cloud_metadata_event.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


