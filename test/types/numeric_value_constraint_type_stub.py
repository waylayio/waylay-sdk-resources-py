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
    from waylay.services.resources.models.numeric_value_constraint_type import (
        NumericValueConstraintType,
    )

    NumericValueConstraintTypeAdapter = TypeAdapter(NumericValueConstraintType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

numeric_value_constraint_type_model_schema = json.loads(
    r"""{
  "title" : "NumericValueConstraint_type",
  "type" : "string",
  "enum" : [ "numeric" ]
}
""",
    object_hook=with_example_provider,
)
numeric_value_constraint_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

numeric_value_constraint_type_faker = JSF(
    numeric_value_constraint_type_model_schema, allow_none_optionals=1
)


class NumericValueConstraintTypeStub:
    """NumericValueConstraintType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return numeric_value_constraint_type_faker.generate()

    @classmethod
    def create_instance(cls) -> "NumericValueConstraintType":
        """Create NumericValueConstraintType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NumericValueConstraintTypeAdapter.validate_python(cls.create_json())
