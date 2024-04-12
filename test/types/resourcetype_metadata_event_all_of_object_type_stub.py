# coding: utf-8
"""Waylay Resources model tests.

This code was generated from the OpenAPI documentation of 'Waylay Resources'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.resources.models.resourcetype_metadata_event_all_of_object_type import (
        ResourcetypeMetadataEventAllOfObjectType,
    )

    ResourcetypeMetadataEventAllOfObjectTypeAdapter = TypeAdapter(
        ResourcetypeMetadataEventAllOfObjectType
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resourcetype_metadata_event_all_of_object_type_model_schema = json.loads(
    r"""{
  "title" : "ResourcetypeMetadataEvent_allOf_objectType",
  "type" : "string",
  "enum" : [ "resourcetype" ]
}
""",
    object_hook=with_example_provider,
)
resourcetype_metadata_event_all_of_object_type_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

resourcetype_metadata_event_all_of_object_type_faker = JSF(
    resourcetype_metadata_event_all_of_object_type_model_schema, allow_none_optionals=1
)


class ResourcetypeMetadataEventAllOfObjectTypeStub:
    """ResourcetypeMetadataEventAllOfObjectType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resourcetype_metadata_event_all_of_object_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "ResourcetypeMetadataEventAllOfObjectType":
        """Create ResourcetypeMetadataEventAllOfObjectType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ResourcetypeMetadataEventAllOfObjectTypeAdapter.validate_python(
            cls.create_json()
        )