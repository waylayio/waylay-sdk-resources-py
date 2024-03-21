# waylay.services.resources.ResourceConstraintApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ResourceConstraintApi.md#create) | **POST** /resources/v1/resourceconstraints | Create Resource Constraint
[**delete**](ResourceConstraintApi.md#delete) | **DELETE** /resources/v1/resourceconstraints/{resourceConstraintId} | Remove Resource Constraint
[**get**](ResourceConstraintApi.md#get) | **GET** /resources/v1/resourceconstraints/{resourceConstraintId} | Get Resource Constraint
[**list**](ResourceConstraintApi.md#list) | **GET** /resources/v1/resourceconstraints | List Resource Constraints
[**replace**](ResourceConstraintApi.md#replace) | **PUT** /resources/v1/resourceconstraints/{resourceConstraintId} | Update Resource Constraint

# **create**
> create(
> headers
> ) -> ResourceConstraintCreationResponse

Create Resource Constraint

Creates a new _Resource Constraint_ from the given representation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.resources.models.constraint import Constraint
from waylay.services.resources.models.resource_constraint_creation_response import ResourceConstraintCreationResponse
try:
    # Create Resource Constraint
    # calls `POST /resources/v1/resourceconstraints`
    api_response = await waylay_client.resources.resource_constraint.create(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.Constraint() # Constraint | 
    )
    print("The response of resources.resource_constraint.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_constraint.create: %s\n" % e)
```

### Endpoint
```
POST /resources/v1/resourceconstraints
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**Constraint**](Constraint.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceConstraintCreationResponse`** |  | [ResourceConstraintCreationResponse](ResourceConstraintCreationResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Constraint Created |  * Location - URI where the created _Resource Constraint_ can be fetched <br>  |
**400** | Invalid Resource Constraint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> resource_constraint_id: str,
> headers
> ) -> void (empty response body)

Remove Resource Constraint

Removes a _Resource Constraint_. Fails if the _Resource Constraint_ is already applied to a _Resource Type_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

try:
    # Remove Resource Constraint
    # calls `DELETE /resources/v1/resourceconstraints/{resourceConstraintId}`
    await waylay_client.resources.resource_constraint.delete(
        'resource_constraint_id_example', # resource_constraint_id | path param "resourceConstraintId"
    )
except ApiError as e:
    print("Exception when calling resources.resource_constraint.delete: %s\n" % e)
```

### Endpoint
```
DELETE /resources/v1/resourceconstraints/{resourceConstraintId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_constraint_id** | **str** | path parameter `"resourceConstraintId"` | _Resource_ Constraint id | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | void (empty response body) |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource Constraint Removed |  -  |
**400** | Resource Constraint Still In Use |  -  |
**404** | Resource Constraint Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> resource_constraint_id: str,
> headers
> ) -> ResourceConstraintWithIdEntity

Get Resource Constraint

Gets the definition or _JSON Schema_ representation of a _Resource Constraint_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.resources.models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity
try:
    # Get Resource Constraint
    # calls `GET /resources/v1/resourceconstraints/{resourceConstraintId}`
    api_response = await waylay_client.resources.resource_constraint.get(
        'resource_constraint_id_example', # resource_constraint_id | path param "resourceConstraintId"
    )
    print("The response of resources.resource_constraint.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_constraint.get: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourceconstraints/{resourceConstraintId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_constraint_id** | **str** | path parameter `"resourceConstraintId"` | _Resource_ Constraint id | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceConstraintWithIdEntity`** |  | [ResourceConstraintWithIdEntity](ResourceConstraintWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/schema+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Constraint Fetched |  -  |
**404** | Resource Constraint Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> List[ResourceConstraintWithIdEntity]

List Resource Constraints

Lists _Resource Constraints_ that fulfill the given criteria.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.resources.models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity
try:
    # List Resource Constraints
    # calls `GET /resources/v1/resourceconstraints`
    api_response = await waylay_client.resources.resource_constraint.list(
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource_constraint.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_constraint.list: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourceconstraints
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**query['filter']** (dict) <br> **query.filter** (Query) | **str** | query parameter `"filter"` | (Filter) fuzzy search on multiple fields. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[ResourceConstraintWithIdEntity]`** |  | [List[ResourceConstraintWithIdEntity]](ResourceConstraintWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Constraints |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> resource_constraint_id: str,
> headers
> ) -> ResourceConstraintWithIdEntity

Update Resource Constraint

Replaces the full definition of a _Resource Constraint_. Fails if the _Resource Constraint_ is already applied to a _Resource Type_ that has _Resources_ assigned to it.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.resources.models.constraint import Constraint
from waylay.services.resources.models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity
try:
    # Update Resource Constraint
    # calls `PUT /resources/v1/resourceconstraints/{resourceConstraintId}`
    api_response = await waylay_client.resources.resource_constraint.replace(
        'resource_constraint_id_example', # resource_constraint_id | path param "resourceConstraintId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.Constraint() # Constraint | 
    )
    print("The response of resources.resource_constraint.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_constraint.replace: %s\n" % e)
```

### Endpoint
```
PUT /resources/v1/resourceconstraints/{resourceConstraintId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_constraint_id** | **str** | path parameter `"resourceConstraintId"` | _Resource_ Constraint id | 
**json** | [**Constraint**](Constraint.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceConstraintWithIdEntity`** |  | [ResourceConstraintWithIdEntity](ResourceConstraintWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Constraint Replaced |  -  |
**400** | Validation Failed |  -  |
**404** | Resource Constraint Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

