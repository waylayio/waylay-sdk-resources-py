# ResourceSensorSensor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The identifying name of the _Waylay Sensor_ | 
**version** | **str** | The sensor version | [optional] 
**properties** | **object** | Default sensor property configuration. | [optional] 

## Example

```python
from waylay.services.resources.models.resource_sensor_sensor import ResourceSensorSensor

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSensorSensor from a JSON string
resource_sensor_sensor_instance = ResourceSensorSensor.from_json(json)
# print the JSON string representation of the object
print ResourceSensorSensor.to_json()

# convert the object into a dict
resource_sensor_sensor_dict = resource_sensor_sensor_instance.to_dict()
# create an instance of ResourceSensorSensor from a dict
resource_sensor_sensor_form_dict = resource_sensor_sensor.from_dict(resource_sensor_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


