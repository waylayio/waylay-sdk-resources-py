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
    from waylay.services.resources.models.resourcetype_metadata_event import (
        ResourcetypeMetadataEvent,
    )

    ResourcetypeMetadataEventAdapter = TypeAdapter(ResourcetypeMetadataEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resourcetype_metadata_event_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericMetadataEvent"
  }, {
    "oneOf" : [ {
      "$ref" : "#/components/schemas/CreateEvent"
    }, {
      "$ref" : "#/components/schemas/DeletedEvent"
    }, {
      "$ref" : "#/components/schemas/ChangedEvent"
    } ]
  }, {
    "required" : [ "resourcetype" ],
    "properties" : {
      "objectType" : {
        "$ref" : "#/components/schemas/ResourcetypeMetadataEvent_allOf_objectType"
      },
      "resourcetype" : {
        "$ref" : "#/components/schemas/ResourceTypeEntity"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
resourcetype_metadata_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

resourcetype_metadata_event_faker = JSF(
    resourcetype_metadata_event_model_schema, allow_none_optionals=1
)


class ResourcetypeMetadataEventStub:
    """ResourcetypeMetadataEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resourcetype_metadata_event_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourcetypeMetadataEvent":
        """Create ResourcetypeMetadataEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourcetypeMetadataEventAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourcetypeMetadataEventAdapter.validate_python(
            json, context={"skip_validation": True}
        )
