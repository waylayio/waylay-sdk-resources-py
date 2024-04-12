# WithIdRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from waylay.services.resources.models.with_id_required import WithIdRequired

# TODO update the JSON string below
json = "{}"
# create an instance of WithIdRequired from a JSON string
with_id_required_instance = WithIdRequired.from_json(json)
# print the JSON string representation of the object
print WithIdRequired.to_json()

# convert the object into a dict
with_id_required_dict = with_id_required_instance.to_dict()
# create an instance of WithIdRequired from a dict
with_id_required_form_dict = with_id_required.from_dict(with_id_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


