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
    from waylay.services.resources.models.metadata_entity_value import (
        MetadataEntityValue,
    )

    MetadataEntityValueAdapter = TypeAdapter(MetadataEntityValue)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

metadata_entity_value_model_schema = json.loads(
    r"""{
  "title" : "User Resource properties",
  "description" : "Other key-value properties provisioned by the user.",
  "nullable" : true,
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ResourceReference"
  } ]
}
""",
    object_hook=with_example_provider,
)
metadata_entity_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

metadata_entity_value_faker = JSF(
    metadata_entity_value_model_schema, allow_none_optionals=1
)


class MetadataEntityValueStub:
    """MetadataEntityValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return metadata_entity_value_faker.generate()

    @classmethod
    def create_instance(cls) -> "MetadataEntityValue":
        """Create MetadataEntityValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return MetadataEntityValueAdapter.validate_python(cls.create_json())
