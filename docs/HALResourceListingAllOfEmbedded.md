# HALResourceListingAllOfEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[HALResourceEntity]**](HALResourceEntity.md) | _Resource_ entities in HAL format | 

## Example

```python
from waylay.services.resources.models.hal_resource_listing_all_of_embedded import HALResourceListingAllOfEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of HALResourceListingAllOfEmbedded from a JSON string
hal_resource_listing_all_of_embedded_instance = HALResourceListingAllOfEmbedded.from_json(json)
# print the JSON string representation of the object
print HALResourceListingAllOfEmbedded.to_json()

# convert the object into a dict
hal_resource_listing_all_of_embedded_dict = hal_resource_listing_all_of_embedded_instance.to_dict()
# create an instance of HALResourceListingAllOfEmbedded from a dict
hal_resource_listing_all_of_embedded_form_dict = hal_resource_listing_all_of_embedded.from_dict(hal_resource_listing_all_of_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


