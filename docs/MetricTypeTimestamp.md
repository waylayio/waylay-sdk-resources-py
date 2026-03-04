# MetricTypeTimestamp

Value represents a unix timestamp. so basically a gauge or counter but we know we can also render the “age” at each point.

**Source:** `waylay.services.resources.models.metric_type_timestamp`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**TIMESTAMP** | `'timestamp'` |

## Example

```python
from waylay.services.resources.models.metric_type_timestamp import MetricTypeTimestamp

# Use enum by value
my_metric_type_timestamp = MetricTypeTimestamp.TIMESTAMP
print(my_metric_type_timestamp)  # Output: 'timestamp'

# Or by string value
my_metric_type_timestamp = MetricTypeTimestamp("timestamp")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


