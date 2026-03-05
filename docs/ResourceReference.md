# ResourceReference

Represents a reference to a _Resource_

**Source:** `waylay.services.resources.models.resource_reference`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | A URI for the _Resource_, formatted as &#x60;/resources/{resourceId}&#x60; | 


## Example

```python
from waylay.services.resources.models.resource_reference import ResourceReference

resource_reference = ResourceReference(ref=...)

# Create from JSON
resource_reference = ResourceReference.from_json('{ "$ref": ... }')

# Export to dictionary
resource_reference_dict = resource_reference.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


