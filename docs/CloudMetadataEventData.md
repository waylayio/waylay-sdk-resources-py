# CloudMetadataEventData


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
from waylay.services.resources.models.cloud_metadata_event_data import CloudMetadataEventData

# TODO update the JSON string below
json = "{}"
# create an instance of CloudMetadataEventData from a JSON string
cloud_metadata_event_data_instance = CloudMetadataEventData.from_json(json)
# print the JSON string representation of the object
print CloudMetadataEventData.to_json()

# convert the object into a dict
cloud_metadata_event_data_dict = cloud_metadata_event_data_instance.to_dict()
# create an instance of CloudMetadataEventData from a dict
cloud_metadata_event_data_form_dict = cloud_metadata_event_data.from_dict(cloud_metadata_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


