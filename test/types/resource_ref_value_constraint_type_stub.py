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
    from waylay.services.resources.models.resource_ref_value_constraint_type import (
        ResourceRefValueConstraintType,
    )

    ResourceRefValueConstraintTypeAdapter = TypeAdapter(ResourceRefValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

resource_ref_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ResourceRefValueConstraint_type",
  "type" : "string",
  "enum" : [ "resourceRef" ]
}
""",
    object_hook=with_example_provider,
)
resource_ref_value_constraint_type_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

resource_ref_value_constraint_type_faker = JSF(
    resource_ref_value_constraint_type_model_schema, allow_none_optionals=1
)


class ResourceRefValueConstraintTypeStub:
    """ResourceRefValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return resource_ref_value_constraint_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ResourceRefValueConstraintType":
        """Create ResourceRefValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ResourceRefValueConstraintTypeAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ResourceRefValueConstraintTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
