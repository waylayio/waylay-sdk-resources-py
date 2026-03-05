# WithIdRequired


**Source:** `waylay.services.resources.models.with_id_required`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 


## Example

```python
from waylay.services.resources.models.with_id_required import WithIdRequired

with_id_required = WithIdRequired(id=...)

# Create from JSON
with_id_required = WithIdRequired.from_json('{ "id": ... }')

# Export to dictionary
with_id_required_dict = with_id_required.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


