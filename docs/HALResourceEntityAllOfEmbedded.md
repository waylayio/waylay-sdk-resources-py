# HALResourceEntityAllOfEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**HALResourceTypeEntity**](HALResourceTypeEntity.md) |  | [optional] 

## Example

```python
from waylay.services.resources.models.hal_resource_entity_all_of_embedded import HALResourceEntityAllOfEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of HALResourceEntityAllOfEmbedded from a JSON string
hal_resource_entity_all_of_embedded_instance = HALResourceEntityAllOfEmbedded.from_json(json)
# print the JSON string representation of the object
print HALResourceEntityAllOfEmbedded.to_json()

# convert the object into a dict
hal_resource_entity_all_of_embedded_dict = hal_resource_entity_all_of_embedded_instance.to_dict()
# create an instance of HALResourceEntityAllOfEmbedded from a dict
hal_resource_entity_all_of_embedded_form_dict = hal_resource_entity_all_of_embedded.from_dict(hal_resource_entity_all_of_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


