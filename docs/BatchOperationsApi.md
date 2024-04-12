# waylay.services.resources.BatchOperationsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](BatchOperationsApi.md#get) | **GET** /resources/v1/batch/{batchId} | Get Resource Batch Operation Status
[**start**](BatchOperationsApi.md#start) | **POST** /resources/v1/batch | Bulk Delete

# **get**
> get(
> batch_id: str,
> headers
> ) -> BatchOperationStatusResponse

Get Resource Batch Operation Status

Get the results of the Resource Batch Operation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.batch_operation_status_response import BatchOperationStatusResponse
try:
    # Get Resource Batch Operation Status
    # calls `GET /resources/v1/batch/{batchId}`
    api_response = await waylay_client.resources.batch_operations.get(
        'batch_id_example', # batch_id | path param "batchId"
    )
    print("The response of resources.batch_operations.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.batch_operations.get: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/batch/{batchId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**batch_id** | **str** | path parameter `"batchId"` | Unique Batch Operation identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BatchOperationStatusResponse`** |  | [BatchOperationStatusResponse](BatchOperationStatusResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Batch Operation |  -  |
**404** | Batch Operation Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(
> headers
> ) -> BatchOperationEnqueued

Bulk Delete

Deletes multiple _Resources_ or _Resource Types_ in one batch.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.batch_operation_enqueued import BatchOperationEnqueued
from waylay.services.resources.models.batch_resource_operation import BatchResourceOperation
try:
    # Bulk Delete
    # calls `POST /resources/v1/batch`
    api_response = await waylay_client.resources.batch_operations.start(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.BatchResourceOperation() # BatchResourceOperation | Resource Batch Operation
    )
    print("The response of resources.batch_operations.start:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.batch_operations.start: %s\n" % e)
```

### Endpoint
```
POST /resources/v1/batch
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**BatchResourceOperation**](BatchResourceOperation.md) | json request body | Resource Batch Operation | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BatchOperationEnqueued`** |  | [BatchOperationEnqueued](BatchOperationEnqueued.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch Operation Started |  * Location - URI where the batch operation status can be followed <br>  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

