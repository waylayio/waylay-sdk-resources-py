# ResourceSensorSensor


**Source:** `waylay.services.resources.models.resource_sensor_sensor`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identifying name of the _Waylay Sensor_ | 
**version** | **str** | The sensor version | [optional] 
**properties** | **object** | Default sensor property configuration. | [optional] 


## Example

```python
from waylay.services.resources.models.resource_sensor_sensor import ResourceSensorSensor

resource_sensor_sensor = ResourceSensorSensor(name=..., version=..., properties=...)

# Create from JSON
resource_sensor_sensor = ResourceSensorSensor.from_json(
    '{ "name": ..., "version": ..., "properties": ... }'
)

# Export to dictionary
resource_sensor_sensor_dict = resource_sensor_sensor.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


