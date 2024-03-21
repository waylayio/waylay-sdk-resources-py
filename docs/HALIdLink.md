# HALIdLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | (Relative) URL of the entity. | 
**id** | **str** | Unique identifier of the linked item | 

## Example

```python
from waylay.services.resources.models.halid_link import HALIdLink

# TODO update the JSON string below
json = "{}"
# create an instance of HALIdLink from a JSON string
halid_link_instance = HALIdLink.from_json(json)
# print the JSON string representation of the object
print HALIdLink.to_json()

# convert the object into a dict
halid_link_dict = halid_link_instance.to_dict()
# create an instance of HALIdLink from a dict
halid_link_form_dict = halid_link.from_dict(halid_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


