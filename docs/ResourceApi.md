# waylay.services.resources.ResourceApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ResourceApi.md#create) | **POST** /resources/v1/resources | Create Resource
[**delete**](ResourceApi.md#delete) | **DELETE** /resources/v1/resources/{resourceId} | Remove Resource
[**get**](ResourceApi.md#get) | **GET** /resources/v1/resources/{resourceId} | Get Resource
[**list_changes**](ResourceApi.md#list_changes) | **GET** /resources/v1/resources/{resourceId}/changes | List Resource Changes
[**list_children**](ResourceApi.md#list_children) | **GET** /resources/v1/resources/{resourceId}/children | List Resource Children
[**list_referrers**](ResourceApi.md#list_referrers) | **GET** /resources/v1/resources/{resourceId}/referrers | List Referring Resources
[**list**](ResourceApi.md#list) | **GET** /resources/v1/resources | Query Resources
[**patch**](ResourceApi.md#patch) | **PATCH** /resources/v1/resources/{resourceId} | Create Or Update Resource Partially
[**replace**](ResourceApi.md#replace) | **PUT** /resources/v1/resources/{resourceId} | Update Resource

# **create**
> create(
> headers
> ) -> ResourceCreationResponse

Create Resource

Creates a new _Resource_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_creation_response import ResourceCreationResponse
from waylay.services.resources.models.resource_entity import ResourceEntity
try:
    # Create Resource
    # calls `POST /resources/v1/resources`
    api_response = await waylay_client.resources.resource.create(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.ResourceEntity() # ResourceEntity | 
    )
    print("The response of resources.resource.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.create: %s\n" % e)
```

### Endpoint
```
POST /resources/v1/resources
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**ResourceEntity**](ResourceEntity.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceCreationResponse`** |  | [ResourceCreationResponse](ResourceCreationResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource Created |  * Location - URI where the created _Resource Constraint_ can be fetched <br>  |
**400** | Validation Failure |  -  |
**409** | Resource Already Exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> resource_id: ResourceId,
> headers
> ) -> void (empty response body)

Remove Resource

Removes an existing _Resource_.

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
    # Remove Resource
    # calls `DELETE /resources/v1/resources/{resourceId}`
    await waylay_client.resources.resource.delete(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
    )
except ApiError as e:
    print("Exception when calling resources.resource.delete: %s\n" % e)
```

### Endpoint
```
DELETE /resources/v1/resources/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
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
**204** | Resource Removed |  -  |
**400** | Resource Still Referenced |  -  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> resource_id: ResourceId,
> query: GetQuery,
> headers
> ) -> ResourceWithIdEntity

Get Resource

Retrieves a representation of the _Resource_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_with_id_entity import ResourceWithIdEntity
try:
    # Get Resource
    # calls `GET /resources/v1/resources/{resourceId}`
    api_response = await waylay_client.resources.resource.get(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.get: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resources/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['denormalized']** (dict) <br> **query.denormalized** (Query) | **bool** | query parameter `"denormalized"` | Unless explicitly set to &#x60;false&#x60;, attributes inherited from a linked _Resource Type_ will be included in the representation. | [optional] [default True]
**query['field']** (dict) <br> **query.field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceWithIdEntity`** |  | [ResourceWithIdEntity](ResourceWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Fetched |  -  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_changes**
> list_changes(
> resource_id: ResourceId,
> query: ListChangesQuery,
> headers
> ) -> List[ResourceChange]

List Resource Changes

Lists the change history of a _Resource_.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_change import ResourceChange
try:
    # List Resource Changes
    # calls `GET /resources/v1/resources/{resourceId}/changes`
    api_response = await waylay_client.resources.resource.list_changes(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource.list_changes:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.list_changes: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resources/{resourceId}/changes
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[ResourceChange]`** |  | [List[ResourceChange]](ResourceChange.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.waylay.paged+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Changes |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_children**
> list_children(
> resource_id: ResourceId,
> query: ListChildrenQuery,
> headers
> ) -> ResourceListing

List Resource Children

Lists the children of a _Resource_, these are the _Resources_ that have the given _Resource_ referenced with the `parentId` attribute.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_listing import ResourceListing
try:
    # List Resource Children
    # calls `GET /resources/v1/resources/{resourceId}/children`
    api_response = await waylay_client.resources.resource.list_children(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource.list_children:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.list_children: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resources/{resourceId}/children
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['denormalized']** (dict) <br> **query.denormalized** (Query) | **bool** | query parameter `"denormalized"` | Unless explicitly set to &#x60;false&#x60;, attributes inherited from a linked _Resource Type_ will be included in the representation. | [optional] [default True]
**query['field']** (dict) <br> **query.field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceListing`** |  | [ResourceListing](ResourceListing.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Child Resources |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_referrers**
> list_referrers(
> resource_id: ResourceId,
> query: ListReferrersQuery,
> headers
> ) -> ResourceListing

List Referring Resources

List the _Resources_ that reference the given _Resource_.  #### visibility This definition has visibility status `beta`. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_listing import ResourceListing
try:
    # List Referring Resources
    # calls `GET /resources/v1/resources/{resourceId}/referrers`
    api_response = await waylay_client.resources.resource.list_referrers(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # query parameters:
        query = {
        },
    )
    print("The response of resources.resource.list_referrers:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.list_referrers: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resources/{resourceId}/referrers
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['field']** (dict) <br> **query.field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceListing`** |  | [ResourceListing](ResourceListing.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Referring Resources |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**404** | Resource Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> ResourceListing

Query Resources

Lists _Resources_ that satisfy the given filters.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_id import ResourceId
from waylay.services.resources.models.resource_listing import ResourceListing
try:
    # Query Resources
    # calls `GET /resources/v1/resources`
    api_response = await waylay_client.resources.resource.list(
        # query parameters:
        query = {
            'tag': ['']
            'provider': 'provider_example'
            'customer': 'customer_example'
            'resourceTypeId': '17b8b6ea-0573-4381-8088-8692f7938165'
            'lat': 3.4
            'lon': 3.4
            'distance': 'distance_example'
            'toplevelOnly': true
        },
    )
    print("The response of resources.resource.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.list: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/resources
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['skip']** (dict) <br> **query.skip** (Query) | **int** | query parameter `"skip"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['limit']** (dict) <br> **query.limit** (Query) | **int** | query parameter `"limit"` | (Paging) maximal number of items returned | [optional] [default 100]
**query['field']** (dict) <br> **query.field** (Query) | [**List[str]**](str.md) | query parameter `"field"` | Select which attributes to render for each matching _Resource_ (repeated). | [optional] 
**query['fields']** (dict) <br> **query.fields** (Query) | [**List[str]**](str.md) | query parameter `"fields"` | Select which attributes to render for each matching _Resource_ (comma-separated). | [optional] 
**query['filter']** (dict) <br> **query.filter** (Query) | **str** | query parameter `"filter"` | (Filter) fuzzy search on multiple fields. | [optional] 
**query['query']** (dict) <br> **query.query** (Query) | **str** | query parameter `"query"` | Search string using a query language consisting of &gt; &#x60;&lt;metadata key&gt;:&lt;operation&gt;(&lt;arguments&gt;)&#x60;  Supported operations are - &#x60;eq&#x60;: equals - exact match - &#x60;in&#x60;: in - exact match - arguments are a (comma-separated) list of values - &#x60;lt&#x60;: smaller then - &#x60;lte&#x60;: smaller then or equal - &#x60;gt&#x60;: greater then - &#x60;gte&#x60;: greater then or equal - &#x60;ref&#x60;: references - argument should be uri /resources/&lt;resourceId&gt; - &#x60;exists&#x60;: check if the _Resource_ has the specified metadata key - no argument allowed - &#x60;like&#x60;: wildcard search - argument should contain * and/or ?  For more info see [Waylay Docs](/#/api/resources/?id&#x3D;metadata-query-language) | [optional] 
**query['tag']** (dict) <br> **query.tag** (Query) | [**List[str]**](str.md) | query parameter `"tag"` |  | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | [**List[ResourceId]**](ResourceId.md) | query parameter `"id"` |  | [optional] 
**query['provider']** (dict) <br> **query.provider** (Query) | **str** | query parameter `"provider"` |  | [optional] 
**query['customer']** (dict) <br> **query.customer** (Query) | **str** | query parameter `"customer"` |  | [optional] 
**query['resourceTypeId']** (dict) <br> **query.resource_type_id** (Query) | **ResourceTypeId** | query parameter `"resourceTypeId"` |  | [optional] 
**query['lat']** (dict) <br> **query.lat** (Query) | **float** | query parameter `"lat"` |  | [optional] 
**query['lon']** (dict) <br> **query.lon** (Query) | **float** | query parameter `"lon"` |  | [optional] 
**query['distance']** (dict) <br> **query.distance** (Query) | **str** | query parameter `"distance"` |  | [optional] 
**query['toplevelOnly']** (dict) <br> **query.toplevel_only** (Query) | **bool** | query parameter `"toplevelOnly"` | If true, search only for _Resources_ without parent. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceListing`** |  | [ResourceListing](ResourceListing.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Listing |  * X-Count - Total number of resource constraints that fulfill the given criteria of which this is one page of results. <br>  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> patch(
> resource_id: ResourceId,
> headers
> ) -> ResourceWithIdEntity

Create Or Update Resource Partially

Updates some attributes of an existing _Resource_, or creates a new one.  When updating an existing _Resource_ you can remove keys by setting their value to `null` in the body

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.patch_resource_entity import PatchResourceEntity
from waylay.services.resources.models.resource_with_id_entity import ResourceWithIdEntity
try:
    # Create Or Update Resource Partially
    # calls `PATCH /resources/v1/resources/{resourceId}`
    api_response = await waylay_client.resources.resource.patch(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.PatchResourceEntity() # PatchResourceEntity | 
    )
    print("The response of resources.resource.patch:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.patch: %s\n" % e)
```

### Endpoint
```
PATCH /resources/v1/resources/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**json** | [**PatchResourceEntity**](PatchResourceEntity.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceWithIdEntity`** |  | [ResourceWithIdEntity](ResourceWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Created Or Updated |  -  |
**400** | Validation Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> resource_id: ResourceId,
> headers
> ) -> ResourceWithIdEntity

Update Resource

Replaces a _Resource_ with a new representation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.resource_entity import ResourceEntity
from waylay.services.resources.models.resource_with_id_entity import ResourceWithIdEntity
try:
    # Update Resource
    # calls `PUT /resources/v1/resources/{resourceId}`
    api_response = await waylay_client.resources.resource.replace(
        waylay.services.resources.ResourceId(), # resource_id | path param "resourceId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.resources.ResourceEntity() # ResourceEntity | 
    )
    print("The response of resources.resource.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.resource.replace: %s\n" % e)
```

### Endpoint
```
PUT /resources/v1/resources/{resourceId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**resource_id** | **ResourceId** | path parameter `"resourceId"` | _Resource_ id | 
**json** | [**ResourceEntity**](ResourceEntity.md) | json request body |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ResourceWithIdEntity`** |  | [ResourceWithIdEntity](ResourceWithIdEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/hal+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource Replaced |  -  |
**400** | Validation Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

