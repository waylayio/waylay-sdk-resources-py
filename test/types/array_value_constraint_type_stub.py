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
    from waylay.services.resources.models.array_value_constraint_type import (
        ArrayValueConstraintType,
    )

    ArrayValueConstraintTypeAdapter = TypeAdapter(ArrayValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

array_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "ArrayValueConstraint_type",
  "type" : "string",
  "enum" : [ "array" ]
}
""",
    object_hook=with_example_provider,
)
array_value_constraint_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

array_value_constraint_type_faker = JSF(
    array_value_constraint_type_model_schema, allow_none_optionals=1
)


class ArrayValueConstraintTypeStub:
    """ArrayValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return array_value_constraint_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "ArrayValueConstraintType":
        """Create ArrayValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return ArrayValueConstraintTypeAdapter.validate_python(cls.create_json())
