# Waylay Resources Service
This service manages 
[Waylay Resources](/#/features/resources/?id=resource) and related entities.

A _Waylay Resource_ models a real-world device or abstract entity of your IoT solution,
and provides a context when processing data in the Rule Engine.

You'll interact with the _Waylay Resources_ API to create this _Digital Twin_ model, 
a process that's also called _resource provisioning_.

This Python package is automatically generated based on the 
Waylay Resources OpenAPI specification (API version: 8.1.0)

It consists of two sub-packages that are both plugins for the  package.
- The `waylay-sdk-resources` sub-package contains the Resources api methods.
- The `waylay-sdk-resources-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-resources`.

## Requirements.
This package requires Python 3.11+.

## Installation
Typically this package is installed when installing the [waylay-sdk](https://github.com/waylayio/waylay-sdk-py) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-resources is included in:
- ```pip install waylay-sdk[resources]``` to install `waylay-sdk` along with only this service, or
- ```pip install waylay-sdk[services]``` to install `waylay-sdk` along with all services.
When the typed models are required, both waylay-sdk-resources and waylay-sdk-resources-types are included in:
- ```pip install waylay-sdk[resources,resources-types]``` to install `waylay-sdk` along with only this service including the typed models, or
- ```pip install waylay-sdk[resources]``` to install `waylay-sdk` along with all services along with the typed models.

## Usage


```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

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


## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BatchOperationsApi* | [**get**](docs/BatchOperationsApi.md#get) | **GET** /resources/v1/batch/{batchId} | Get Resource Batch Operation Status
*BatchOperationsApi* | [**start**](docs/BatchOperationsApi.md#start) | **POST** /resources/v1/batch | Bulk Delete
*MetadataEventsApi* | [**get_stream**](docs/MetadataEventsApi.md#get_stream) | **GET** /resources/v1/events | Events
*ResourceApi* | [**create**](docs/ResourceApi.md#create) | **POST** /resources/v1/resources | Create Resource
*ResourceApi* | [**delete**](docs/ResourceApi.md#delete) | **DELETE** /resources/v1/resources/{resourceId} | Remove Resource
*ResourceApi* | [**get**](docs/ResourceApi.md#get) | **GET** /resources/v1/resources/{resourceId} | Get Resource
*ResourceApi* | [**list_changes**](docs/ResourceApi.md#list_changes) | **GET** /resources/v1/resources/{resourceId}/changes | List Resource Changes
*ResourceApi* | [**list_children**](docs/ResourceApi.md#list_children) | **GET** /resources/v1/resources/{resourceId}/children | List Resource Children
*ResourceApi* | [**list_referrers**](docs/ResourceApi.md#list_referrers) | **GET** /resources/v1/resources/{resourceId}/referrers | List Referring Resources
*ResourceApi* | [**list**](docs/ResourceApi.md#list) | **GET** /resources/v1/resources | Query Resources
*ResourceApi* | [**patch**](docs/ResourceApi.md#patch) | **PATCH** /resources/v1/resources/{resourceId} | Create Or Update Resource Partially
*ResourceApi* | [**replace**](docs/ResourceApi.md#replace) | **PUT** /resources/v1/resources/{resourceId} | Update Resource
*ResourceConstraintApi* | [**create**](docs/ResourceConstraintApi.md#create) | **POST** /resources/v1/resourceconstraints | Create Resource Constraint
*ResourceConstraintApi* | [**delete**](docs/ResourceConstraintApi.md#delete) | **DELETE** /resources/v1/resourceconstraints/{resourceConstraintId} | Remove Resource Constraint
*ResourceConstraintApi* | [**get**](docs/ResourceConstraintApi.md#get) | **GET** /resources/v1/resourceconstraints/{resourceConstraintId} | Get Resource Constraint
*ResourceConstraintApi* | [**list**](docs/ResourceConstraintApi.md#list) | **GET** /resources/v1/resourceconstraints | List Resource Constraints
*ResourceConstraintApi* | [**replace**](docs/ResourceConstraintApi.md#replace) | **PUT** /resources/v1/resourceconstraints/{resourceConstraintId} | Update Resource Constraint
*ResourceTypeApi* | [**create**](docs/ResourceTypeApi.md#create) | **POST** /resources/v1/resourcetypes | Create Resource Type
*ResourceTypeApi* | [**delete**](docs/ResourceTypeApi.md#delete) | **DELETE** /resources/v1/resourcetypes/{resourceTypeId} | Remove Resource Type
*ResourceTypeApi* | [**get**](docs/ResourceTypeApi.md#get) | **GET** /resources/v1/resourcetypes/{resourceTypeId} | Get Resource Type
*ResourceTypeApi* | [**list_changes**](docs/ResourceTypeApi.md#list_changes) | **GET** /resources/v1/resourcetypes/{resourceTypeId}/changes | List Resource Type Changes
*ResourceTypeApi* | [**list_constraints**](docs/ResourceTypeApi.md#list_constraints) | **GET** /resources/v1/resourcetypes/{resourceTypeId}/constraints | Get Resource Type Constraints
*ResourceTypeApi* | [**list**](docs/ResourceTypeApi.md#list) | **GET** /resources/v1/resourcetypes | List Resource Types
*ResourceTypeApi* | [**patch**](docs/ResourceTypeApi.md#patch) | **PATCH** /resources/v1/resourcetypes/{resourceTypeId} | Create Or Update Resource Type
*ResourceTypeApi* | [**replace**](docs/ResourceTypeApi.md#replace) | **PUT** /resources/v1/resourcetypes/{resourceTypeId} | Update Resource Type
*ResourceTypeApi* | [**revalidate**](docs/ResourceTypeApi.md#revalidate) | **POST** /resources/v1/resourcetypes/{resourceTypeId}/revalidate | Revalidate Resource Type
*VersionApi* | [**get**](docs/VersionApi.md#get) | **GET** /resources/v1/ | Get Version


## Documentation For Models

 - [ArrayMustContainInner](docs/ArrayMustContainInner.md)
 - [ArrayValueConstraint](docs/ArrayValueConstraint.md)
 - [AttributeItem](docs/AttributeItem.md)
 - [BatchOperationEnqueued](docs/BatchOperationEnqueued.md)
 - [BatchOperationResult](docs/BatchOperationResult.md)
 - [BatchOperationStatusResponse](docs/BatchOperationStatusResponse.md)
 - [BatchResourceOperation](docs/BatchResourceOperation.md)
 - [BatchResourceOperationQuery](docs/BatchResourceOperationQuery.md)
 - [BatchResourceOperationQueryIdsInner](docs/BatchResourceOperationQueryIdsInner.md)
 - [BatchRunningResourceOperation](docs/BatchRunningResourceOperation.md)
 - [BatchRunningResourceOperationOperation](docs/BatchRunningResourceOperationOperation.md)
 - [BooleanValueConstraint](docs/BooleanValueConstraint.md)
 - [ChangedEvent](docs/ChangedEvent.md)
 - [CloudMetadataEvent](docs/CloudMetadataEvent.md)
 - [CloudMetadataEventData](docs/CloudMetadataEventData.md)
 - [Constraint](docs/Constraint.md)
 - [ConstraintError](docs/ConstraintError.md)
 - [ConstraintStatus](docs/ConstraintStatus.md)
 - [CreateDeleteEvent](docs/CreateDeleteEvent.md)
 - [DiscoveredEvent](docs/DiscoveredEvent.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [FailureOperationResultValue](docs/FailureOperationResultValue.md)
 - [GenericMetadataEvent](docs/GenericMetadataEvent.md)
 - [HALIdLink](docs/HALIdLink.md)
 - [HALLink](docs/HALLink.md)
 - [HALPageLinks](docs/HALPageLinks.md)
 - [HALResourceEntity](docs/HALResourceEntity.md)
 - [HALResourceEntityAllOfEmbedded](docs/HALResourceEntityAllOfEmbedded.md)
 - [HALResourceEntityAllOfLinks](docs/HALResourceEntityAllOfLinks.md)
 - [HALResourceEntityAllOfLinksChildren](docs/HALResourceEntityAllOfLinksChildren.md)
 - [HALResourceEntityAllOfLinksParent](docs/HALResourceEntityAllOfLinksParent.md)
 - [HALResourceEntityAllOfLinksResourceType](docs/HALResourceEntityAllOfLinksResourceType.md)
 - [HALResourceListing](docs/HALResourceListing.md)
 - [HALResourceListingAllOfEmbedded](docs/HALResourceListingAllOfEmbedded.md)
 - [HALResourceTypeEntity](docs/HALResourceTypeEntity.md)
 - [HALSelfLinks](docs/HALSelfLinks.md)
 - [HALSelfLinksLinks](docs/HALSelfLinksLinks.md)
 - [HALSelfLinksLinksSelf](docs/HALSelfLinksLinksSelf.md)
 - [HALSelfLinksLinksValue](docs/HALSelfLinksLinksValue.md)
 - [ListConstraints200Response](docs/ListConstraints200Response.md)
 - [MetadataEntity](docs/MetadataEntity.md)
 - [MetadataEntityLocation](docs/MetadataEntityLocation.md)
 - [MetadataEntityValue](docs/MetadataEntityValue.md)
 - [MetadataEvent](docs/MetadataEvent.md)
 - [NdJsonResponseStream](docs/NdJsonResponseStream.md)
 - [NumericEnumValueConstraint](docs/NumericEnumValueConstraint.md)
 - [NumericValueConstraint](docs/NumericValueConstraint.md)
 - [ObjectValueConstraint](docs/ObjectValueConstraint.md)
 - [OperationResultObject](docs/OperationResultObject.md)
 - [OperationResultObjectResults](docs/OperationResultObjectResults.md)
 - [PaginationLinks](docs/PaginationLinks.md)
 - [PaginationLinksNext](docs/PaginationLinksNext.md)
 - [PaginationLinksPrev](docs/PaginationLinksPrev.md)
 - [PaginationLinksSelf](docs/PaginationLinksSelf.md)
 - [PagingCount](docs/PagingCount.md)
 - [PagingResult](docs/PagingResult.md)
 - [PatchResourceEntity](docs/PatchResourceEntity.md)
 - [PatchResourceTypeEntity](docs/PatchResourceTypeEntity.md)
 - [ResourceChange](docs/ResourceChange.md)
 - [ResourceChangesPagedResponse](docs/ResourceChangesPagedResponse.md)
 - [ResourceConstraintCreationResponse](docs/ResourceConstraintCreationResponse.md)
 - [ResourceConstraintEntity](docs/ResourceConstraintEntity.md)
 - [ResourceConstraintWithIdEntity](docs/ResourceConstraintWithIdEntity.md)
 - [ResourceCreationResponse](docs/ResourceCreationResponse.md)
 - [ResourceEntity](docs/ResourceEntity.md)
 - [ResourceId](docs/ResourceId.md)
 - [ResourceListing](docs/ResourceListing.md)
 - [ResourceMetadataEvent](docs/ResourceMetadataEvent.md)
 - [ResourceMetric](docs/ResourceMetric.md)
 - [ResourceMetricMetricType](docs/ResourceMetricMetricType.md)
 - [ResourceParent](docs/ResourceParent.md)
 - [ResourceRefValueConstraint](docs/ResourceRefValueConstraint.md)
 - [ResourceReference](docs/ResourceReference.md)
 - [ResourceSensor](docs/ResourceSensor.md)
 - [ResourceSensorSensor](docs/ResourceSensorSensor.md)
 - [ResourceType](docs/ResourceType.md)
 - [ResourceTypeChange](docs/ResourceTypeChange.md)
 - [ResourceTypeCreationResponse](docs/ResourceTypeCreationResponse.md)
 - [ResourceTypeEntity](docs/ResourceTypeEntity.md)
 - [ResourceTypeId](docs/ResourceTypeId.md)
 - [ResourceTypeListing](docs/ResourceTypeListing.md)
 - [ResourceTypeWithConstraints](docs/ResourceTypeWithConstraints.md)
 - [ResourceTypeWithIdEntity](docs/ResourceTypeWithIdEntity.md)
 - [ResourceTypesChangesPagedResponse](docs/ResourceTypesChangesPagedResponse.md)
 - [ResourceWithIdEntity](docs/ResourceWithIdEntity.md)
 - [ResourcetypeMetadataEvent](docs/ResourcetypeMetadataEvent.md)
 - [SSEventStream](docs/SSEventStream.md)
 - [SchemaValidationError](docs/SchemaValidationError.md)
 - [StringEnumValueConstraint](docs/StringEnumValueConstraint.md)
 - [StringValueConstraint](docs/StringValueConstraint.md)
 - [SuccessOperationResultValue](docs/SuccessOperationResultValue.md)
 - [TaskConfiguration](docs/TaskConfiguration.md)
 - [ValidationFailure](docs/ValidationFailure.md)
 - [ValueConstraint](docs/ValueConstraint.md)
 - [VersionResponse](docs/VersionResponse.md)
