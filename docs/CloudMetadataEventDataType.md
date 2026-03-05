# CloudMetadataEventDataType


**Source:** `waylay.services.resources.models.cloud_metadata_event_data_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCETYPE_DOT_CREATED** | `'io.waylay.resources.v1.resourcetype.created'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCETYPE_DOT_UPDATED** | `'io.waylay.resources.v1.resourcetype.updated'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCETYPE_DOT_DELETED** | `'io.waylay.resources.v1.resourcetype.deleted'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCE_DOT_CREATED** | `'io.waylay.resources.v1.resource.created'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCE_DOT_UPDATED** | `'io.waylay.resources.v1.resource.updated'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCE_DOT_DELETED** | `'io.waylay.resources.v1.resource.deleted'` |
**IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCE_DOT_DISCOVERED** | `'io.waylay.resources.v1.resource.discovered'` |

## Example

```python
from waylay.services.resources.models.cloud_metadata_event_data_type import (
    CloudMetadataEventDataType,
)

# Use enum by value
my_cloud_metadata_event_data_type = (
    CloudMetadataEventDataType.IO_DOT_WAYLAY_DOT_RESOURCES_DOT_V1_DOT_RESOURCETYPE_DOT_CREATED
)
print(
    my_cloud_metadata_event_data_type
)  # Output: 'io.waylay.resources.v1.resourcetype.created'

# Or by string value
my_cloud_metadata_event_data_type = CloudMetadataEventDataType(
    "io.waylay.resources.v1.resourcetype.created"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


