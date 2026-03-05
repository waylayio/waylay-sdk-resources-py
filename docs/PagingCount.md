# PagingCount


**Source:** `waylay.services.resources.models.paging_count`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of items in this result page. | [optional] 


## Example

```python
from waylay.services.resources.models.paging_count import PagingCount

paging_count = PagingCount(count=...)

# Create from JSON
paging_count = PagingCount.from_json('{ "count": ... }')

# Export to dictionary
paging_count_dict = paging_count.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


