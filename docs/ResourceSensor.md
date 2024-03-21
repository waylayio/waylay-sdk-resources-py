# ResourceSensor

Sensor associated with a _Resource_

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An alias name for the sensor in the context of this _Resource_. | 
**sensor** | [**ResourceSensorSensor**](ResourceSensorSensor.md) |  | 

## Example

```python
from waylay.services.resources.models.resource_sensor import ResourceSensor

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSensor from a JSON string
resource_sensor_instance = ResourceSensor.from_json(json)
# print the JSON string representation of the object
print ResourceSensor.to_json()

# convert the object into a dict
resource_sensor_dict = resource_sensor_instance.to_dict()
# create an instance of ResourceSensor from a dict
resource_sensor_form_dict = resource_sensor.from_dict(resource_sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


