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
    from waylay.services.resources.models.generic_metadata_event import (
        GenericMetadataEvent,
    )

    GenericMetadataEventAdapter = TypeAdapter(GenericMetadataEvent)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

generic_metadata_event_model_schema = json.loads(
    r"""{
  "required" : [ "objectType", "timestamp", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "type" : "string"
    },
    "objectType" : {
      "type" : "string"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    }
  }
}
""",
    object_hook=with_example_provider,
)
generic_metadata_event_model_schema.update({"definitions": MODEL_DEFINITIONS})

generic_metadata_event_faker = JSF(
    generic_metadata_event_model_schema, allow_none_optionals=1
)


class GenericMetadataEventStub:
    """GenericMetadataEvent unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return generic_metadata_event_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GenericMetadataEvent":
        """Create GenericMetadataEvent stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GenericMetadataEventAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GenericMetadataEventAdapter.validate_python(
            json, context={"skip_validation": True}
        )
