# coding: utf-8
"""Waylay Resources: REST Models.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

version: 8.1.0

This service manages  [Waylay Resources](/#/features/resources/?id=resource) and related entities.  A _Waylay Resource_ models a real-world device or abstract entity of your IoT solution, and provides a context when processing data in the Rule Engine.  You'll interact with the _Waylay Resources_ API to create this _Digital Twin_ model,  a process that's also called _resource provisioning_.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "8.1.0.20240415"

# import models into model package
from .array_must_contain_inner import ArrayMustContainInner
from .array_value_constraint import ArrayValueConstraint
from .array_value_constraint_type import ArrayValueConstraintType
from .attribute_item import AttributeItem
from .batch_operation_enqueued import BatchOperationEnqueued
from .batch_operation_result import BatchOperationResult
from .batch_operation_status_response import BatchOperationStatusResponse
from .batch_resource_operation import BatchResourceOperation
from .batch_resource_operation_action import BatchResourceOperationAction
from .batch_resource_operation_entity import BatchResourceOperationEntity
from .batch_resource_operation_query import BatchResourceOperationQuery
from .batch_resource_operation_query_ids_inner import (
    BatchResourceOperationQueryIdsInner,
)
from .batch_running_resource_operation import BatchRunningResourceOperation
from .batch_running_resource_operation_operation import (
    BatchRunningResourceOperationOperation,
)
from .batch_running_resource_operation_operation_entity import (
    BatchRunningResourceOperationOperationEntity,
)
from .boolean_value_constraint import BooleanValueConstraint
from .boolean_value_constraint_type import BooleanValueConstraintType
from .changed_event import ChangedEvent
from .changed_event_type import ChangedEventType
from .cloud_metadata_event import CloudMetadataEvent
from .cloud_metadata_event_data import CloudMetadataEventData
from .cloud_metadata_event_data_source import CloudMetadataEventDataSource
from .cloud_metadata_event_data_type import CloudMetadataEventDataType
from .constraint import Constraint
from .constraint_error import ConstraintError
from .constraint_status import ConstraintStatus
from .constraint_status_status import ConstraintStatusStatus
from .create_delete_event import CreateDeleteEvent
from .create_delete_event_type import CreateDeleteEventType
from .discovered_event import DiscoveredEvent
from .discovered_event_type import DiscoveredEventType
from .error_response import ErrorResponse
from .failure_operation_result_value import FailureOperationResultValue
from .generic_metadata_event import GenericMetadataEvent
from .get_stream_event_format_parameter import GetStreamEventFormatParameter
from .hal_link import HALLink
from .hal_page_links import HALPageLinks
from .hal_resource_entity import HALResourceEntity
from .hal_resource_entity_all_of_embedded import HALResourceEntityAllOfEmbedded
from .hal_resource_entity_all_of_links import HALResourceEntityAllOfLinks
from .hal_resource_entity_all_of_links_children import (
    HALResourceEntityAllOfLinksChildren,
)
from .hal_resource_entity_all_of_links_parent import HALResourceEntityAllOfLinksParent
from .hal_resource_entity_all_of_links_resource_type import (
    HALResourceEntityAllOfLinksResourceType,
)
from .hal_resource_listing import HALResourceListing
from .hal_resource_listing_all_of_embedded import HALResourceListingAllOfEmbedded
from .hal_resource_type_entity import HALResourceTypeEntity
from .hal_self_links import HALSelfLinks
from .hal_self_links_links import HALSelfLinksLinks
from .hal_self_links_links_self import HALSelfLinksLinksSelf
from .hal_self_links_links_value import HALSelfLinksLinksValue
from .halid_link import HALIdLink
from .list_constraints200_response import ListConstraints200Response
from .metadata_entity import MetadataEntity
from .metadata_entity_location import MetadataEntityLocation
from .metadata_entity_value import MetadataEntityValue
from .metadata_event import MetadataEvent
from .nd_json_response_stream import NdJsonResponseStream
from .numeric_enum_value_constraint import NumericEnumValueConstraint
from .numeric_enum_value_constraint_type import NumericEnumValueConstraintType
from .numeric_value_constraint import NumericValueConstraint
from .numeric_value_constraint_type import NumericValueConstraintType
from .object_value_constraint import ObjectValueConstraint
from .object_value_constraint_type import ObjectValueConstraintType
from .operation_result_object import OperationResultObject
from .operation_result_object_results import OperationResultObjectResults
from .pagination_links import PaginationLinks
from .pagination_links_next import PaginationLinksNext
from .pagination_links_prev import PaginationLinksPrev
from .pagination_links_self import PaginationLinksSelf
from .paging_count import PagingCount
from .paging_result import PagingResult
from .patch_resource_entity import PatchResourceEntity
from .patch_resource_type_entity import PatchResourceTypeEntity
from .resource_change import ResourceChange
from .resource_change_change import ResourceChangeChange
from .resource_changes_paged_response import ResourceChangesPagedResponse
from .resource_constraint_creation_response import ResourceConstraintCreationResponse
from .resource_constraint_entity import ResourceConstraintEntity
from .resource_constraint_with_id_entity import ResourceConstraintWithIdEntity
from .resource_creation_response import ResourceCreationResponse
from .resource_entity import ResourceEntity
from .resource_id import ResourceId
from .resource_listing import ResourceListing
from .resource_metadata_event import ResourceMetadataEvent
from .resource_metadata_event_all_of_object_type import (
    ResourceMetadataEventAllOfObjectType,
)
from .resource_metric import ResourceMetric
from .resource_metric_metric_type import ResourceMetricMetricType
from .resource_metric_metric_type_one_of import ResourceMetricMetricTypeOneOf
from .resource_metric_metric_type_one_of1 import ResourceMetricMetricTypeOneOf1
from .resource_metric_metric_type_one_of2 import ResourceMetricMetricTypeOneOf2
from .resource_metric_metric_type_one_of3 import ResourceMetricMetricTypeOneOf3
from .resource_metric_metric_type_one_of4 import ResourceMetricMetricTypeOneOf4
from .resource_parent import ResourceParent
from .resource_ref_value_constraint import ResourceRefValueConstraint
from .resource_ref_value_constraint_type import ResourceRefValueConstraintType
from .resource_reference import ResourceReference
from .resource_sensor import ResourceSensor
from .resource_sensor_sensor import ResourceSensorSensor
from .resource_type import ResourceType
from .resource_type_change import ResourceTypeChange
from .resource_type_creation_response import ResourceTypeCreationResponse
from .resource_type_entity import ResourceTypeEntity
from .resource_type_id import ResourceTypeId
from .resource_type_listing import ResourceTypeListing
from .resource_type_with_constraints import ResourceTypeWithConstraints
from .resource_type_with_id_entity import ResourceTypeWithIdEntity
from .resource_types_changes_paged_response import ResourceTypesChangesPagedResponse
from .resource_with_id_entity import ResourceWithIdEntity
from .resourcetype_metadata_event import ResourcetypeMetadataEvent
from .resourcetype_metadata_event_all_of_object_type import (
    ResourcetypeMetadataEventAllOfObjectType,
)
from .schema_validation_error import SchemaValidationError
from .ss_event_stream import SSEventStream
from .string_enum_value_constraint import StringEnumValueConstraint
from .string_value_constraint import StringValueConstraint
from .string_value_constraint_type import StringValueConstraintType
from .success_operation_result_value import SuccessOperationResultValue
from .task_configuration import TaskConfiguration
from .task_configuration_type import TaskConfigurationType
from .validation_failure import ValidationFailure
from .version_response import VersionResponse
from .with_id_required import WithIdRequired

__all__ = [
    "__version__",
    "ArrayMustContainInner",
    "ArrayValueConstraint",
    "ArrayValueConstraintType",
    "AttributeItem",
    "BatchOperationEnqueued",
    "BatchOperationResult",
    "BatchOperationStatusResponse",
    "BatchResourceOperation",
    "BatchResourceOperationAction",
    "BatchResourceOperationEntity",
    "BatchResourceOperationQuery",
    "BatchResourceOperationQueryIdsInner",
    "BatchRunningResourceOperation",
    "BatchRunningResourceOperationOperation",
    "BatchRunningResourceOperationOperationEntity",
    "BooleanValueConstraint",
    "BooleanValueConstraintType",
    "ChangedEvent",
    "ChangedEventType",
    "CloudMetadataEvent",
    "CloudMetadataEventData",
    "CloudMetadataEventDataSource",
    "CloudMetadataEventDataType",
    "Constraint",
    "ConstraintError",
    "ConstraintStatus",
    "ConstraintStatusStatus",
    "CreateDeleteEvent",
    "CreateDeleteEventType",
    "DiscoveredEvent",
    "DiscoveredEventType",
    "ErrorResponse",
    "FailureOperationResultValue",
    "GenericMetadataEvent",
    "GetStreamEventFormatParameter",
    "HALIdLink",
    "HALLink",
    "HALPageLinks",
    "HALResourceEntity",
    "HALResourceEntityAllOfEmbedded",
    "HALResourceEntityAllOfLinks",
    "HALResourceEntityAllOfLinksChildren",
    "HALResourceEntityAllOfLinksParent",
    "HALResourceEntityAllOfLinksResourceType",
    "HALResourceListing",
    "HALResourceListingAllOfEmbedded",
    "HALResourceTypeEntity",
    "HALSelfLinks",
    "HALSelfLinksLinks",
    "HALSelfLinksLinksSelf",
    "HALSelfLinksLinksValue",
    "ListConstraints200Response",
    "MetadataEntity",
    "MetadataEntityLocation",
    "MetadataEntityValue",
    "MetadataEvent",
    "NdJsonResponseStream",
    "NumericEnumValueConstraint",
    "NumericEnumValueConstraintType",
    "NumericValueConstraint",
    "NumericValueConstraintType",
    "ObjectValueConstraint",
    "ObjectValueConstraintType",
    "OperationResultObject",
    "OperationResultObjectResults",
    "PaginationLinks",
    "PaginationLinksNext",
    "PaginationLinksPrev",
    "PaginationLinksSelf",
    "PagingCount",
    "PagingResult",
    "PatchResourceEntity",
    "PatchResourceTypeEntity",
    "ResourceChange",
    "ResourceChangeChange",
    "ResourceChangesPagedResponse",
    "ResourceConstraintCreationResponse",
    "ResourceConstraintEntity",
    "ResourceConstraintWithIdEntity",
    "ResourceCreationResponse",
    "ResourceEntity",
    "ResourceId",
    "ResourceListing",
    "ResourceMetadataEvent",
    "ResourceMetadataEventAllOfObjectType",
    "ResourceMetric",
    "ResourceMetricMetricType",
    "ResourceMetricMetricTypeOneOf",
    "ResourceMetricMetricTypeOneOf1",
    "ResourceMetricMetricTypeOneOf2",
    "ResourceMetricMetricTypeOneOf3",
    "ResourceMetricMetricTypeOneOf4",
    "ResourceParent",
    "ResourceRefValueConstraint",
    "ResourceRefValueConstraintType",
    "ResourceReference",
    "ResourceSensor",
    "ResourceSensorSensor",
    "ResourceType",
    "ResourceTypeChange",
    "ResourceTypeCreationResponse",
    "ResourceTypeEntity",
    "ResourceTypeId",
    "ResourceTypeListing",
    "ResourceTypeWithConstraints",
    "ResourceTypeWithIdEntity",
    "ResourceTypesChangesPagedResponse",
    "ResourceWithIdEntity",
    "ResourcetypeMetadataEvent",
    "ResourcetypeMetadataEventAllOfObjectType",
    "SSEventStream",
    "SchemaValidationError",
    "StringEnumValueConstraint",
    "StringValueConstraint",
    "StringValueConstraintType",
    "SuccessOperationResultValue",
    "TaskConfiguration",
    "TaskConfigurationType",
    "ValidationFailure",
    "VersionResponse",
    "WithIdRequired",
]
