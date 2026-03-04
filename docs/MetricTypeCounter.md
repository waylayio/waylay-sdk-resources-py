# MetricTypeCounter

Keeps increasing over time (but might wrap/reset at some point) i.e. a gauge with the added notion of “i usually want to derive this to see the rate”

**Source:** `waylay.services.resources.models.metric_type_counter`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNTER** | `'counter'` |

## Example

```python
from waylay.services.resources.models.metric_type_counter import MetricTypeCounter

# Use enum by value
my_metric_type_counter = MetricTypeCounter.COUNTER
print(my_metric_type_counter)  # Output: 'counter'

# Or by string value
my_metric_type_counter = MetricTypeCounter("counter")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


