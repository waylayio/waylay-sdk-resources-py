# VersionResponse


**Source:** `waylay.services.resources.models.version_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | 


## Example

```python
from waylay.services.resources.models.version_response import VersionResponse

version_response = VersionResponse(name=..., version=...)

# Create from JSON
version_response = VersionResponse.from_json('{ "name": ..., "version": ... }')

# Export to dictionary
version_response_dict = version_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


