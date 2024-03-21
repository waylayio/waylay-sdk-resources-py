# TaskConfiguration

Specification of a template and task creation attributes for the task that gets instantiate when a _Resource_ created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | 
**type** | **str** |  | [optional] 

## Example

```python
from waylay.services.resources.models.task_configuration import TaskConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TaskConfiguration from a JSON string
task_configuration_instance = TaskConfiguration.from_json(json)
# print the JSON string representation of the object
print TaskConfiguration.to_json()

# convert the object into a dict
task_configuration_dict = task_configuration_instance.to_dict()
# create an instance of TaskConfiguration from a dict
task_configuration_form_dict = task_configuration.from_dict(task_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


