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
    from waylay.services.resources.models.object_value_constraint_type import (
        ObjectValueConstraintType,
    )

    ObjectValueConstraintTypeAdapter = TypeAdapter(ObjectValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

object_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ObjectValueConstraint_type",
  "type" : "string",
  "enum" : [ "object" ]
}
""",
    object_hook=with_example_provider,
)
object_value_constraint_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

object_value_constraint_type_faker = JSF(
    object_value_constraint_type_model_schema, allow_none_optionals=1
)


class ObjectValueConstraintTypeStub:
    """ObjectValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return object_value_constraint_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "ObjectValueConstraintType":
        """Create ObjectValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ObjectValueConstraintTypeAdapter.validate_python(cls.create_json())
