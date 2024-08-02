# waylay.services.resources.ResourceTypeApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ResourceTypeApi.md#create) | **POST** /resources/v1/resourcetypes | Create Resource Type
[**delete**](ResourceTypeApi.md#delete) | **DELETE** /resources/v1/resourcetypes/{resourceTypeId} | Remove Resource Type
[**get**](ResourceTypeApi.md#get) | **GET** /resources/v1/resourcetypes/{resourceTypeId} | Get Resource Type
[**list_changes**](ResourceTypeApi.md#list_changes) | **GET** /resources/v1/resourcetypes/{resourceTypeId}/changes | List Resource Type Changes
[**list_constraints**](ResourceTypeApi.md#list_constraints) | **GET** /resources/v1/resourcetypes/{resourceTypeId}/constraints | Get Resource Type Constraints
[**list**](ResourceTypeApi.md#list) | **GET** /resources/v1/resourcetypes | List Resource Types
[**patch**](ResourceTypeApi.md#patch) | **PATCH** /resources/v1/resourcetypes/{resourceTypeId} | Create Or Update Resource Type
[**replace**](ResourceTypeApi.md#replace) | **PUT** /resources/v1/resourcetypes/{resourceTypeId} | Update Resource Type
[**revalidate**](ResourceTypeApi.md#revalidate) | **POST** /resources/v1/resourcetypes/{resourceTypeId}/revalidate | Revalidate Resource Type

# **create**
> create(
> headers
> ) -> ResourceTypeCreationResponse

Create Resource Type

Create a new _Resource Type_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_creation_response import ResourceTypeCreationResponse
from waylay.services.resources.models.resource_type_with_constraints import ResourceTypeWithConstraints
try:
    # Create Resource Type
    # calls `POST /resources/v1/resourcetypes`
    api_response = await waylay_client.resources.resource_type.create(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.ResourceTypeWithConstraints() # ResourceTypeWithConstraints | 
    )
    print("The response of resources.resource_type.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.create: %s\n" % e)
```

### Endpoint
```
POST /resources/v1/resourcetypes
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**ResourceTypeWithConstraints**](ResourceTypeWithConstraints.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeCreationResponse`** |  | [ResourceTypeCreationResponse](ResourceTypeCreationResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Type Created |  * Location - URI where the created _Resource Constraint_ can be fetched <br>  |
**400** | Bad Request |  -  |
**409** | Resource Type Already Exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> resource_type_id: ResourceTypeId,
> headers
> ) -> void (empty response body)

Remove Resource Type

Removes an existing _Resource Type_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
try:
    # Remove Resource Type
    # calls `DELETE /resources/v1/resourcetypes/{resourceTypeId}`
    await waylay_client.resources.resource_type.delete(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
    )
except ApiError as e:
    print("Exception when calling resources.resource_type.delete: %s\n" % e)
```

### Endpoint
```
DELETE /resources/v1/resourcetypes/{resourceTypeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
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
**204** | Resource Type Removed |  -  |
**400** | Resource Type Still In Use |  -  |
**404** | Resource Type Not Found |  -  |
**409** | Conflict: Resource Type Update Ongoing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> resource_type_id: ResourceTypeId,
> query: GetQuery,
> headers
> ) -> ResourceTypeWithIdEntity

Get Resource Type

Retrieves a representation of the _Resource Type_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_with_id_entity import ResourceTypeWithIdEntity
try:
    # Get Resource Type
    # calls `GET /resources/v1/resourcetypes/{resourceTypeId}`
    api_response = await waylay_client.resources.resource_type.get(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource_type.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.get: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourcetypes/{resourceTypeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['field']** (dict) <br> **query.var_field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeWithIdEntity`** |  | [ResourceTypeWithIdEntity](ResourceTypeWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Type Fetched |  -  |
**404** | Resource Type Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_changes**
> list_changes(
> resource_type_id: ResourceTypeId,
> query: ListChangesQuery,
> headers
> ) -> List[ResourceTypeChange]

List Resource Type Changes

Lists the change history of a _Resource Type_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_change import ResourceTypeChange
try:
    # List Resource Type Changes
    # calls `GET /resources/v1/resourcetypes/{resourceTypeId}/changes`
    api_response = await waylay_client.resources.resource_type.list_changes(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource_type.list_changes:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.list_changes: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourcetypes/{resourceTypeId}/changes
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[ResourceTypeChange]`** |  | [List[ResourceTypeChange]](ResourceTypeChange.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.waylay.paged+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Type Changes |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**404** | Resource Type Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_constraints**
> list_constraints(
> resource_type_id: ResourceTypeId,
> headers
> ) -> ResourceConstraintWithIdEntity

Get Resource Type Constraints

Retrieves the resource constraints that are applicable for the _Resource Type_.   This endpoint supports different representations of the constraints. * `application/json`: will give the reserved keywords for metadata expressed as _Resource Constraint_ merged with all user defined _Resource Constraints_ applied on the _Resource Type_. * `application/schema+json`: returns the (merged) constraints as a JSON Schema * `application/vnd.waylay.paged+json`: returns the constraints as a list of _Resource Constraints_ as defined by the user

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_constraint_with_id_entity import ResourceConstraintWithIdEntity
try:
    # Get Resource Type Constraints
    # calls `GET /resources/v1/resourcetypes/{resourceTypeId}/constraints`
    api_response = await waylay_client.resources.resource_type.list_constraints(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
    )
    print("The response of resources.resource_type.list_constraints:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.list_constraints: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourcetypes/{resourceTypeId}/constraints
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceConstraintWithIdEntity`** |  | [ResourceConstraintWithIdEntity](ResourceConstraintWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/schema+json, application/vnd.waylay.paged+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Type Constraints |  -  |
**404** | Resource Type Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> ResourceTypeListing

List Resource Types

List _Resource Types_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_id import ResourceTypeId
from waylay.services.resources.models.resource_type_listing import ResourceTypeListing
try:
    # List Resource Types
    # calls `GET /resources/v1/resourcetypes`
    api_response = await waylay_client.resources.resource_type.list(
        # query parameters:
        query = {
            'template': 'MonitoringTemplate_3443'
        },
    )
    print("The response of resources.resource_type.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.list: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resourcetypes
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**query['field']** (dict) <br> **query.var_field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**query['filter']** (dict) <br> **query.filter** (Query) | **str** | query parameter `"filter"` | (Filter) fuzzy search on multiple fields. | [optional] 
**query['query']** (dict) <br> **query.query** (Query) | **str** | query parameter `"query"` | Search string using a query language consisting of &gt; &#x60;&lt;metadata key&gt;:&lt;operation&gt;(&lt;arguments&gt;)&#x60;  Supported operations are - &#x60;eq&#x60;: equals - exact match - &#x60;in&#x60;: in - exact match - arguments are a (comma-separated) list of values - &#x60;lt&#x60;: smaller then - &#x60;lte&#x60;: smaller then or equal - &#x60;gt&#x60;: greater then - &#x60;gte&#x60;: greater then or equal - &#x60;ref&#x60;: references - argument should be uri /resources/&lt;resourceId&gt; - &#x60;exists&#x60;: check if the _Resource_ has the specified metadata key - no argument allowed - &#x60;like&#x60;: wildcard search - argument should contain * and/or ?  For more info see [Waylay Docs](/#/api/resources/?id&#x3D;metadata-query-language) | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | [**List[ResourceTypeId]**](ResourceTypeId.md) | query parameter `"id"` |  | [optional] 
**query['template']** (dict) <br> **query.template** (Query) | **str** | query parameter `"template"` | Return _Resource Types_ that are associated with the template. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeListing`** |  | [ResourceTypeListing](ResourceTypeListing.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Type Listing |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> patch(
> resource_type_id: ResourceTypeId,
> headers
> ) -> ResourceTypeCreationResponse \| ResourceTypeWithIdEntity

Create Or Update Resource Type

Add or modify attributes of an existing _Resource Type_. Remove attributes by including a `null`-valued property. Creates a new _Resource Type_ if it did not exist.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.patch_resource_type_entity import PatchResourceTypeEntity
from waylay.services.resources.models.resource_type_creation_response import ResourceTypeCreationResponse
try:
    # Create Or Update Resource Type
    # calls `PATCH /resources/v1/resourcetypes/{resourceTypeId}`
    api_response = await waylay_client.resources.resource_type.patch(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.PatchResourceTypeEntity() # PatchResourceTypeEntity | 
    )
    print("The response of resources.resource_type.patch:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.patch: %s\n" % e)
```

### Endpoint
```
PATCH /resources/v1/resourcetypes/{resourceTypeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**json** | [**PatchResourceTypeEntity**](PatchResourceTypeEntity.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeCreationResponse \| ResourceTypeWithIdEntity`** |  | [ResourceTypeCreationResponse](ResourceTypeCreationResponse.md) <br> [ResourceTypeWithIdEntity](ResourceTypeWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Type Created |  -  |
**202** | Resource Type Update Initiated |  -  |
**400** | Bad Request |  -  |
**409** | Conflict: Another Resource Type Update Ongoing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> resource_type_id: ResourceTypeId,
> headers
> ) -> ResourceTypeWithIdEntity

Update Resource Type

Replaces a _Resource Types_ with a new representation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_with_constraints import ResourceTypeWithConstraints
from waylay.services.resources.models.resource_type_with_id_entity import ResourceTypeWithIdEntity
try:
    # Update Resource Type
    # calls `PUT /resources/v1/resourcetypes/{resourceTypeId}`
    api_response = await waylay_client.resources.resource_type.replace(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.ResourceTypeWithConstraints() # ResourceTypeWithConstraints | 
    )
    print("The response of resources.resource_type.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.replace: %s\n" % e)
```

### Endpoint
```
PUT /resources/v1/resourcetypes/{resourceTypeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**json** | [**ResourceTypeWithConstraints**](ResourceTypeWithConstraints.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeWithIdEntity`** |  | [ResourceTypeWithIdEntity](ResourceTypeWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Resource Type Replacement Initiated |  -  |
**400** | Bad Request |  -  |
**404** | Resource Type Not Found |  -  |
**409** | Conflict: Another Resource Type Update Ongoing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revalidate**
> revalidate(
> resource_type_id: ResourceTypeId,
> headers
> ) -> ResourceTypeWithIdEntity

Revalidate Resource Type

Initiates revalidation of the _Resource Constraints_ of this _Resource Type_ on all its associated _Resources_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_type_with_id_entity import ResourceTypeWithIdEntity
try:
    # Revalidate Resource Type
    # calls `POST /resources/v1/resourcetypes/{resourceTypeId}/revalidate`
    api_response = await waylay_client.resources.resource_type.revalidate(
        waylay.services.resources.ResourceTypeId(), # resource_type_id | path param "resourceTypeId"
    )
    print("The response of resources.resource_type.revalidate:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource_type.revalidate: %s\n" % e)
```

### Endpoint
```
POST /resources/v1/resourcetypes/{resourceTypeId}/revalidate
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_type_id** | **ResourceTypeId** | path parameter `"resourceTypeId"` | _Resource Type_ id | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceTypeWithIdEntity`** |  | [ResourceTypeWithIdEntity](ResourceTypeWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Revalidation Initiated |  -  |
**409** | Conflict: Another Resource Type Update Ongoing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

