# PagingCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of items in this result page. | [optional] 

## Example

```python
from waylay.services.resources.models.paging_count import PagingCount

# TODO update the JSON string below
json = "{}"
# create an instance of PagingCount from a JSON string
paging_count_instance = PagingCount.from_json(json)
# print the JSON string representation of the object
print PagingCount.to_json()

# convert the object into a dict
paging_count_dict = paging_count_instance.to_dict()
# create an instance of PagingCount from a dict
paging_count_form_dict = paging_count.from_dict(paging_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


