# ResourceMetric

Describes a value that is expected to be present in the events sent to Waylay on behalf of this _Resource (Type)_. By default, such values will end up in the time series database, where each time series is identified by the _resource id_ and the _metric name_.  > Note: The Waylay System does not enforce any of the statements made in a _Resource Metric_ when > processing or retrieving data. As long as a user does not explicitly use this metadata to configure > behaviour, a _Resource Metric_ is purely a documentation entity.

**Source:** `waylay.services.resources.models.resource_metric`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key under which values of this metric are present in the root of a Waylay Event. Also the _metric_ identifier in the timeseries database for these values when stored. | 
**value_type** | **str** | Type of the value | [optional] 
**value_choices** | **List[str]** | Enumeration of the possible values for a metric | [optional] 
**metric_type** | [**ResourceMetricMetricType**](ResourceMetricMetricType.md) |  | [optional] [default to 'gauge']
**unit** | **str** | Physical measurement unit, preferentially SI unit, for the numerical values of this metric | [optional] 
**maximum** | **float** | Expected maximum value for this metric. | [optional] 
**minimum** | **float** | Expected minimum value for this metric. | [optional] 
**precision** | **float** | The metric value precision. | [optional] 


## Example

```python
from waylay.services.resources.models.resource_metric import ResourceMetric

resource_metric = ResourceMetric(
    name=...,
    value_type=...,
    value_choices=...,
    metric_type=...,
    unit=...,
    maximum=...,
    minimum=...,
    precision=...,
)

# Create from JSON
resource_metric = ResourceMetric.from_json(
    '{ "name": ..., "valueType": ..., "valueChoices": ..., "metricType": ..., "unit": ..., "maximum": ..., "minimum": ..., "precision": ... }'
)

# Export to dictionary
resource_metric_dict = resource_metric.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


