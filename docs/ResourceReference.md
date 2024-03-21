# ResourceReference

Represents a reference to a _Resource_

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A URI for the _Resource_, formatted as &#x60;/resources/{resourceId}&#x60; | 

## Example

```python
from waylay.services.resources.models.resource_reference import ResourceReference

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceReference from a JSON string
resource_reference_instance = ResourceReference.from_json(json)
# print the JSON string representation of the object
print ResourceReference.to_json()

# convert the object into a dict
resource_reference_dict = resource_reference_instance.to_dict()
# create an instance of ResourceReference from a dict
resource_reference_form_dict = resource_reference.from_dict(resource_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


