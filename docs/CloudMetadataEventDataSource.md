# CloudMetadataEventDataSource


**Source:** `waylay.services.resources.models.cloud_metadata_event_data_source`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SLASH_RESOURCES_SLASH_V1_SLASH_RESOURCES** | `'/resources/v1/resources'` |
**SLASH_RESOURCES_SLASH_V1_SLASH_RESOURCETYPES** | `'/resources/v1/resourcetypes'` |

## Example

```python
from waylay.services.resources.models.cloud_metadata_event_data_source import (
    CloudMetadataEventDataSource,
)

# Use enum by value
my_cloud_metadata_event_data_source = (
    CloudMetadataEventDataSource.SLASH_RESOURCES_SLASH_V1_SLASH_RESOURCES
)
print(my_cloud_metadata_event_data_source)  # Output: '/resources/v1/resources'

# Or by string value
my_cloud_metadata_event_data_source = CloudMetadataEventDataSource(
    "/resources/v1/resources"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


