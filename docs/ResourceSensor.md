# ResourceSensor

Sensor associated with a _Resource_

**Source:** `waylay.services.resources.models.resource_sensor`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An alias name for the sensor in the context of this _Resource_. | 
**sensor** | [**ResourceSensorSensor**](ResourceSensorSensor.md) |  | 


## Example

```python
from waylay.services.resources.models.resource_sensor import ResourceSensor

resource_sensor = ResourceSensor(name=..., sensor=...)

# Create from JSON
resource_sensor = ResourceSensor.from_json('{ "name": ..., "sensor": ... }')

# Export to dictionary
resource_sensor_dict = resource_sensor.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


