# UserResourceProperties

Other key-value properties provisioned by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A URI for the _Resource_, formatted as &#x60;/resources/{resourceId}&#x60; | 

## Example

```python
from waylay.services.resources.models.user_resource_properties import UserResourceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourceProperties from a JSON string
user_resource_properties_instance = UserResourceProperties.from_json(json)
# print the JSON string representation of the object
print UserResourceProperties.to_json()

# convert the object into a dict
user_resource_properties_dict = user_resource_properties_instance.to_dict()
# create an instance of UserResourceProperties from a dict
user_resource_properties_form_dict = user_resource_properties.from_dict(user_resource_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


