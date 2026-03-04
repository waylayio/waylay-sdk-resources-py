# ResourceChangeChange


**Source:** `waylay.services.resources.models.resource_change_change`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**CREATED** | `'created'` |
**UPDATED** | `'updated'` |
**DELETED** | `'deleted'` |

## Example

```python
from waylay.services.resources.models.resource_change_change import ResourceChangeChange

# Use enum by value
my_resource_change_change = ResourceChangeChange.CREATED
print(my_resource_change_change)  # Output: 'created'

# Or by string value
my_resource_change_change = ResourceChangeChange("created")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


