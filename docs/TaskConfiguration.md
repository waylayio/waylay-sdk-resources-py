# TaskConfiguration

Specification of a template and task creation attributes for the task that gets instantiate when a _Resource_ created.

**Source:** `waylay.services.resources.models.task_configuration`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** |  | 
**type** | [**TaskConfigurationType**](TaskConfigurationType.md) |  | [optional] 
**diagnostic_template** | **bool** | flag indicating if template is diagnostic. No managed task will be created if that flag set to true. | [optional] [default to False]


## Example

```python
from waylay.services.resources.models.task_configuration import TaskConfiguration

task_configuration = TaskConfiguration(
    template_name=..., type=..., diagnostic_template=...
)

# Create from JSON
task_configuration = TaskConfiguration.from_json(
    '{ "templateName": ..., "type": ..., "diagnosticTemplate": ... }'
)

# Export to dictionary
task_configuration_dict = task_configuration.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


