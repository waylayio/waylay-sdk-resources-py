# CloudMetadataEventData


**Source:** `waylay.services.resources.models.cloud_metadata_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**source** | [**CloudMetadataEventDataSource**](CloudMetadataEventDataSource.md) |  | [optional] 
**subject** | **object** |  | [optional] 
**type** | [**CloudMetadataEventDataType**](CloudMetadataEventDataType.md) |  | [optional] 
**data** | [**MetadataEvent**](MetadataEvent.md) |  | [optional] 
**time** | **datetime** |  | [optional] 


## Example

```python
from waylay.services.resources.models.cloud_metadata_event_data import (
    CloudMetadataEventData,
)

cloud_metadata_event_data = CloudMetadataEventData(
    id=..., source=..., subject=..., type=..., data=..., time=...
)

# Create from JSON
cloud_metadata_event_data = CloudMetadataEventData.from_json(
    '{ "id": ..., "source": ..., "subject": ..., "type": ..., "data": ..., "time": ... }'
)

# Export to dictionary
cloud_metadata_event_data_dict = cloud_metadata_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


