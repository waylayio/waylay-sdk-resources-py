# ResourceMetricMetricType

How measurements should be treated as a time series.

**Source:** `waylay.services.resources.models.resource_metric_metric_type`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**MetricTypeRate**](MetricTypeRate.md) | -
[**MetricTypeCount**](MetricTypeCount.md) | -
[**MetricTypeGauge**](MetricTypeGauge.md) | -
[**MetricTypeCounter**](MetricTypeCounter.md) | -
[**MetricTypeTimestamp**](MetricTypeTimestamp.md) | -

## Example

```python
from waylay.services.resources.models.resource_metric_metric_type import (
    ResourceMetricMetricType,
)

# Use any of the accepted types (see table above)
my_resource_metric_metric_type: ResourceMetricMetricType = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


