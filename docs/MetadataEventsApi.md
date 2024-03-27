# waylay.services.resources.MetadataEventsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stream**](MetadataEventsApi.md#get_stream) | **GET** /resources/v1/events | Events

# **get_stream**
> get_stream(
> query: GetStreamQuery,
> headers
> ) -> NdJsonResponseStream

Events

Opens a data stream for all Metadata events for this tenant.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-resources-types` is installed
from waylay.services.resources.models.get_stream_event_format_parameter import GetStreamEventFormatParameter
from waylay.services.resources.models.nd_json_response_stream import NdJsonResponseStream
try:
    # Events
    # calls `GET /resources/v1/events`
    api_response = await waylay_client.resources.metadata_events.get_stream(
        # query parameters:
        query = {
            'eventFormat': 'application/cloudevents+json'
        },
    )
    print("The response of resources.metadata_events.get_stream:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling resources.metadata_events.get_stream: %s\n" % e)
```

### Endpoint
```
GET /resources/v1/events
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['eventFormat']** (dict) <br> **query.event_format** (Query) | [**GetStreamEventFormatParameter**](.md) | query parameter `"eventFormat"` | The format of events in the stream.   If specified this must be &#x60;application/cloudevents+json&#x60; (make sure to correctly URL encode the &#x60;+&#x60; as &#x60;%2B&#x60;) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`NdJsonResponseStream`** |  | [NdJsonResponseStream](NdJsonResponseStream.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events Stream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

